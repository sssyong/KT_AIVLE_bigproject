import jinja2, pdfkit, os, copy
from datetime import datetime
from main import local_settings
from .models import Document

def makedocument(sender, recipient, context, documentSub, documentMain, userId):
    template_loader = jinja2.FileSystemLoader(local_settings.DocumentForm)
    template_env = jinja2.Environment(loader=template_loader)
    
    sub_name = documentSub.replace(' ', '_')
    template_pwd = f'/{documentMain}/{sub_name}.html'
    context_copy = copy.deepcopy(context)
    template = template_env.get_template(template_pwd)
    
    context['sender_name'] = sender.sender_name
    context['sender_address'] = sender.sender_address
    context['sender_phone'] = sender.sender_phone
    
    context['recipient_name'] = recipient.recipient_name
    context['recipient_address'] = recipient.recipient_address
    context['recipient_phone'] = recipient.recipient_phone
    
    now = datetime.now()
    today = now.strftime('%Y년 %m월 %d일')
    
    context['today'] = today
    
    options = {
    'page-size': 'A4',
    'margin-top': '0.40in',
    'margin-bottom': '0.0in',
    'margin-right': '0.5in',
    'margin-left': '0.5in',
    'encoding': "UTF-8",
    'no-outline': None}
    
    pdfpath = local_settings.PdfFileSave + str(userId) + '/'
    if not os.path.exists(pdfpath):
        os.makedirs(pdfpath)
    
    pdffilter = f'{sub_name}'
    document_data = Document.objects.filter(user = userId, file_path__contains = pdffilter)
    number = len(document_data) + 1
    title = f'{sub_name}{number}'
    pdfsave = pdfpath + f'{title}.pdf'
    output_text = template.render(context)
    
    if os.path.exists(pdfsave):
        os.remove(pdfsave)
        
    config = pdfkit.configuration(wkhtmltopdf=local_settings.wkhtmltopdfLocation)
    pdfkit.from_string(output_text, pdfsave, configuration=config, options=options)
    return context_copy, pdfsave, title

def patchDocument(sender, recipient, context, documentSub, documentMain, userId, documentId, title):
    template_loader = jinja2.FileSystemLoader(local_settings.DocumentForm)
    template_env = jinja2.Environment(loader=template_loader)
    
    sub_name = documentSub.replace(' ', '_')
    template_pwd = f'/{documentMain}/{sub_name}.html'
    context_copy = copy.deepcopy(context)
    template = template_env.get_template(template_pwd)
    
    context['sender_name'] = sender.sender_name
    context['sender_address'] = sender.sender_address
    context['sender_phone'] = sender.sender_phone
    
    context['recipient_name'] = recipient.recipient_name
    context['recipient_address'] = recipient.recipient_address
    context['recipient_phone'] = recipient.recipient_phone
    
    now = datetime.now()
    today = now.strftime('%Y년 %m월 %d일')
    
    context['today'] = today
    
    options = {
    'page-size': 'A4',
    'margin-top': '0.40in',
    'margin-bottom': '0.0in',
    'margin-right': '0.5in',
    'margin-left': '0.5in',
    'encoding': "UTF-8",
    'no-outline': None}
    
    pdfpath = local_settings.PdfFileSave + str(userId) + '/'
    if not os.path.exists(pdfpath):
        os.makedirs(pdfpath)
    
    pdffilter = f'{sub_name}'
    document_data = Document.objects.get(user = userId, id=documentId)
    title_temp = document_data.title
    pdfsave = pdfpath + f'{title}.pdf'
    pdfdele = pdfpath + f'{title_temp}.pdf'
    output_text = template.render(context)
    
    if os.path.exists(pdfdele):
        os.remove(pdfdele)
        
    config = pdfkit.configuration(wkhtmltopdf=local_settings.wkhtmltopdfLocation)
    pdfkit.from_string(output_text, pdfsave, configuration=config, options=options)
    return context_copy, pdfsave, title