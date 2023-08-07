from flask import Flask, jsonify, request
from flask_restx import Api, Resource, fields, reqparse

from peft import PeftModel, PeftConfig
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig

from peft import PeftModel, PeftConfig
from local_settings import ACCESS_TOKEN

access_token = ACCESS_TOKEN
peft_model_id = "aivleschool25/koalp"
config = PeftConfig.from_pretrained(peft_model_id)
print(config)
bnb_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_use_double_quant=True,
    bnb_4bit_quant_type="nf4",
    bnb_4bit_compute_dtype=torch.bfloat16
)
model = AutoModelForCausalLM.from_pretrained(config.base_model_name_or_path, quantization_config=bnb_config, device_map= "auto")
model = PeftModel.from_pretrained(model, peft_model_id, )
tokenizer = AutoTokenizer.from_pretrained(config.base_model_name_or_path)
device = "cuda:0" if torch.cuda.is_available() else "cpu"
model.eval()

app = Flask(__name__)
api = Api(
    app,
    title='LLM API Server')

def gen(x):
    gened = model.generate(
        **tokenizer(
            f"### 질문: {x}\n\n### 답변:",
            return_tensors='pt',
            return_token_type_ids=False
        ).to(device),
        max_new_tokens=50,
        early_stopping=True,
        do_sample=True,
        eos_token_id=2,
    ).to('cuda')
    decoded=tokenizer.decode(gened[0])
    answer=decoded.split("### 답변:")[1].strip()
    return answer

input_model = api.model('Input', {'text': fields.String(required=True, description='text_input')})
output_model = api.model('Output', {'answer': fields.String })

@api.route('/llmtest')
class LLMtest(Resource):
    @api.expect(input_model)
    @api.marshal_with(output_model)
    def post(self):
        text = request.json.get('text')
        new_sentence = text
        answer = gen(new_sentence)
        response = {'answer': answer }
        return response

if __name__ == '__main__':
    app.run()