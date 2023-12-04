import json
def Datacleaner (nameFile = 'raw_filter_all_t.json', DefaultImport = True ):

   
    with open("../data/"+nameFile) as fichier:
        if DefaultImport:
            data = json.load(fichier)
            dic = {"train": [], "val": [], "test": []}

            for nomDataSet in data:
                for objet in data[nomDataSet]:
                    dic[nomDataSet].append({
                        "id": objet.get('user_id')+"_"+objet.get('business_id'),
                        "business_id": objet.get('business_id'),
                        "user_id": objet.get('user_id'),
                        "rating": objet.get('rating'),
                        "review_text": objet.get('review_text'),
                    })
        else:
            dic = {"Val":[]}
            for line in fichier:
                dataTempo = json.loads(line)
                
                dic["Val"].append({
                        "id": dataTempo.get('user_id')+"_"+dataTempo.get('business_id'),
                        "business_id": dataTempo.get('business_id'),
                        "user_id": dataTempo.get('user_id'),
                        "rating": dataTempo.get('rating'),
                        "review_text": dataTempo.get('review_text'),
                    })
            



    

    with open("../data/Cleaned"+nameFile, 'w') as fichier_json:
        json.dump(dic, fichier_json, indent=4)

Datacleaner("raw_image_review_all.json",False)