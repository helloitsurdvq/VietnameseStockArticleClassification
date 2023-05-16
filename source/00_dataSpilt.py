import json
import os
from glob import glob
from copy import deepcopy

#run this file only once
process_path = "C:/Users/DELL/Programming/python/StockReview.IntroAI.20222/data/modelling"
data_labels = ['positive', 'negative', 'neutral']
concat_dict = []
samples_num = {'train': 0.6, 'test' : 0.4, 'dev':0}
dict_num = []
sum_count = 0

data_labels = []
for filename in glob(f"{process_path}/*.json"):
    label = os.path.basename(filename)[:-5]
    data_labels.append(label)  
    samples_num[label] = (len(json.load(open(filename, 'r'))))
    
    for f in json.load(open(filename, 'r')):
        if f not in concat_dict:
            concat_dict.append(f)
            
sum_count = sum([samples_num[label] for label in samples_num if label not in ['train', 'test', 'dev']])
samples_num = dict([(key, value) if key  in ['train', 'dev', 'test'] else (key, value/sum_count) for key, value in samples_num.items()])

data_stat = dict([(mode, dict([(label, len(concat_dict) * samples_num[mode] * samples_num[label]) for label in data_labels])) for mode in ['train', 'dev', 'test']])
print(data_stat)

for mode in data_stat.keys():
    temp_dict = deepcopy(concat_dict)
    data = []
    
    for file in temp_dict:
        if data_stat[mode][file['label']] > 0:
            data.append(file)
            concat_dict.remove(file)
            data_stat[mode][file['label']] -= 1
            
    if mode == 'test':
        for f in concat_dict:
            if f not in data:
                data.append(f)
    json.dump(data, open(f'{process_path}/stock_{mode}.json', 'w'), indent=3)
print("AFTER", data_stat)