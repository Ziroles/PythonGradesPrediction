import json

with open('data/image_review_all.json') as fichier:
    # Read each line as a separate JSON object
    for line in fichier:
        data = json.loads(line)
print(data.keys())
