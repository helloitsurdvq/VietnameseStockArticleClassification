import json

input_file = "C:\\Users\\DELL\\Programming\\python\\StockReview.IntroAI.20222\\data\\labelling\\negative.txt"
output_file = "C:\\Users\\DELL\\Programming\\python\\StockReview.IntroAI.20222\\data\\modelling\\negative.json"

with open(input_file, 'r', encoding='utf-8') as f:
    lines = f.readlines()
    
data = {'data': []}
for line in lines:
    line = line.strip()
    if line:
        data['data'].append({'text': line, 'label': 1}) # 0 = positive, 1 = negative, 2 = neutral

with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)