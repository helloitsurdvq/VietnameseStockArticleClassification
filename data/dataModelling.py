import json
import os

input_files = ["C:\\Users\\DELL\\Programming\\python\\StockReview.IntroAI.20222\\data\\labelling\\positive.txt",
               "C:\\Users\\DELL\\Programming\\python\\StockReview.IntroAI.20222\\data\\labelling\\negative.txt",
               "C:\\Users\\DELL\\Programming\\python\\StockReview.IntroAI.20222\\data\\labelling\\neutral.txt"]

output_files = ["C:\\Users\\DELL\\Programming\\python\\StockReview.IntroAI.20222\\data\\modelling\\positive.json",
                "C:\\Users\\DELL\\Programming\\python\\StockReview.IntroAI.20222\\data\\modelling\\negative.json",
                "C:\\Users\\DELL\\Programming\\python\\StockReview.IntroAI.20222\\data\\modelling\\neutral.json"]

label_map = {"positive.txt": 'positive', "negative.txt": 'negative', "neutral.txt": 'neutral'}
for i, input_file in enumerate(input_files):
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    data = {'data': []}
    for line in lines:
        line = line.strip()
        if line:
            data['data'].append({'text': line, 'label': label_map[os.path.basename(input_file)]})

    with open(output_files[i], 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
