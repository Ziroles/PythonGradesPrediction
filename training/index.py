import json

fileName = "ForTrainCleanedraw_image_review_all.json"
negative_avis = []
postive_avis = []
with open("../data/"+fileName) as fichier:
    data = json.load(fichier)

    for nomDataSet in data:
        
        updated_data = []  
        for objet in data[nomDataSet]:
            rating = objet.get('label')
            if rating == 'negatif':
                negative_avis.append(objet)
            else:
                postive_avis.append(objet)

with open("../data/DataPosAndNegSep.json", 'w') as fichier_json:
        json.dump({"pos":postive_avis,"neg":negative_avis}, fichier_json, indent=4)

