# from bitsandbytes.cextension import CUDASetup
# import torch

# print(torch.cuda.is_available())
# lib = CUDASetup.get_instance().lib


from flask import Flask, jsonify, request
from flask_restx import Api, Resource, fields, reqparse

from peft import PeftModel, PeftConfig
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig

from peft import PeftModel, PeftConfig

access_token = "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"
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
model = PeftModel.from_pretrained(model, peft_model_id)
tokenizer = AutoTokenizer.from_pretrained(config.base_model_name_or_path)
device = "cuda:0" if torch.cuda.is_available() else "cpu"

input_ids = tokenizer( f"### 질문: 부동산 등기가 뭐야?\n\n### 답변:", return_tensors="pt", return_token_type_ids=False).to(device)
print(1)