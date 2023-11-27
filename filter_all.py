import json
"""with open("data/filter_all_t.json") as f:
    data = json.load(f)
"""
#print(len(data))
#print(data.head())
#print(json.dumps(data, indent=4))
#Si jamais le dataset est trop grand ou pas vraiment modifiale KAGGLE
# Charger le fichier JSON
with open('data/filter_all_t.json') as fichier:
    data = json.load(fichier)

print(data.keys())

date_train = data['train']
date_val = data['val']
date_test = data['test'] 

print(len(date_train))#87013
print(len(date_val))#10860
print(len(date_test))#11015

print(date_train[0].keys())
print(date_train[0])
print(json.dumps(date_train[0], indent=4))

with open("data_train.json", 'w') as fichier_json:
    json.dump(data['train'], fichier_json)
