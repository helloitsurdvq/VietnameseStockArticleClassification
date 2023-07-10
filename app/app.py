import re
import string
from flask import Flask, render_template, request
from transformers import XLMRobertaTokenizer, XLMRobertaForSequenceClassification
import torchtext
from torchtext.models import RobertaClassificationHead, XLMR_BASE_ENCODER
import torch
from torch.nn import functional as f
import matplotlib.pyplot as plt
import requests
from bs4 import BeautifulSoup
from pyvi import ViTokenizer
from collections import Counter
from nltk.stem import WordNetLemmatizer

app = Flask(__name__, template_folder='template')

DEVICE = torch.device("cuda") if torch.cuda.is_available() else torch.device("cpu")
label_map = {
    0: 'negative',
    1: 'neutral',
    2: 'postive'
}

def articleCrawler(url):
    if 'vneconomy.vn' in url:
        div_class = 'detail__content'
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        content_div = soup.find("div", class_=div_class) 
        if content_div:
            content = content_div.find_all('p')
            content_texts = ' '.join([c.get_text() for c in content])
            return content_texts
        
    elif 'vnexpress.net' in url:
        div_class = 'fck_detail'
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        content_div = soup.find("article", class_=div_class) 
        if content_div:
            content = content_div.find_all('p')
            content_texts = ' '.join([c.get_text() for c in content])
            return content_texts
        
    elif 'cafef.vn' in url:
        div_class = 'contentdetail'
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        content_div = soup.find("div", class_=div_class) 
        if content_div:
            content = content_div.find_all('p')
            content_texts = ' '.join([c.get_text() for c in content])
            return content_texts
        
    else:
        return
    
def get_stopwords_list(stop_file_path):
    """load stop words """

    with open(stop_file_path, 'r', encoding="utf-8") as f:
        stopwords = f.readlines()
        stop_set = set(m.strip() for m in stopwords)
        return list(frozenset(stop_set))
    
stopwords_path = 'source/data/vietnamese_stopwords.txt'
sw = get_stopwords_list(stopwords_path)
lemmatizer = WordNetLemmatizer()

def clean_text(text):
    text = text.lower()
    text = re.sub(r"[^a-zA-Z?.!,¿0-9]+", " ", text)
    punctuations = '@#!?+&*[]-%.:/();$=><|{}^,_' + "'`"
    for p in punctuations:
        text = text.replace(p,'')
    text = [word.lower() for word in text.split() if word.lower() not in sw]
    text = [lemmatizer.lemmatize(word) for word in text]
    text = " ".join(text)
    return text

def prepare_model():
    num_classes = 3
    input_dim = 768

    classifier_head = RobertaClassificationHead(num_classes=num_classes, input_dim=input_dim)
    model = XLMR_BASE_ENCODER.get_model(head=classifier_head)
    
    DEMO_MODEL_PATH = './source/output/trained_XLMRoBERTa/model_max_weighted_f1.pth'
    model.load_state_dict(torch.load(DEMO_MODEL_PATH))
    model.to(DEVICE)
    
    return model

def prepare_text_transform():
    text_transform = torchtext.models.XLMR_LARGE_ENCODER.transform()
    return text_transform

def predict_xlmRoberta(sentence, model, text_transform, label_map):
    transformed_text = text_transform(sentence)
    out = model(torch.tensor([transformed_text]).to(DEVICE))
    probabilities = torch.softmax(out, dim=1).squeeze().detach().cpu().numpy()
    predicted_label = label_map[torch.argmax(out).item()]
    return probabilities, predicted_label

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def display():
    input_text = request.form['input-text']
    
    model = prepare_model()
    text_transform = prepare_text_transform()
    
    result = predict_xlmRoberta(input_text, model, text_transform, label_map)
    zipped_result = zip(range(len(result[0])), result[0])
    return render_template('index.html', 
                           input_text=input_text, 
                           result=result, 
                           zipped_result=zipped_result, 
                           label_map=label_map
                           )

@app.route('/predictUrl', methods=['POST'])
def show():
    input_url = request.form['input-url']
    
    model = prepare_model()
    text_transform = prepare_text_transform()
    
    result_Url = predict_xlmRoberta(articleCrawler(input_url), model, text_transform, label_map)
    zipped_result_Url = zip(range(len(result_Url[0])), result_Url[0])
    return render_template('index.html', 
                           input_url=input_url, 
                           result_content=articleCrawler(input_url), 
                           result_Url=result_Url, 
                           zipped_result_Url=zipped_result_Url,
                           label_map=label_map
                           )

if __name__ == '__main__':
    app.run(debug=True)