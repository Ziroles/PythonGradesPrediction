import json

def LabelCreation(fileName):

    
    with open("../data/"+fileName) as fichier:
        data = json.load(fichier)

    for nomDataSet in data:
        updated_data = []  
        for objet in data[nomDataSet]:
            rating = objet.get('rating')
            if rating < 3:
                objet['label'] = 'negatif'
            else:
                objet['label'] = 'positif'
            

            objet['id'] = objet.get('user_id') + "_" + objet.get('business_id')
            objet['business_id'] = objet.get('business_id')
            objet['user_id'] = objet.get('user_id')
            objet['review_text'] = objet.get('review_text')

            updated_data.append(objet)  

        data[nomDataSet] = updated_data  



    with open("../data/ForTrain"+fileName, 'w') as fichier_json:
        json.dump(data, fichier_json, indent=4)


LabelCreation("Cleanedraw_image_review_all.json")
