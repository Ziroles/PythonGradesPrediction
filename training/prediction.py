import spacy
import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
import numpy as np
import random
# Charger le modèle de langue en anglais
nlp = spacy.load("en_core_web_sm")
tab = []
# Exemple de données (remplacez cela par vos propres données)
with open('datafrotrain.json') as fichier:
    data = json.load(fichier)


taille_finale = 10000
avis_negatifs = []
avis_positifs = []
for dicName in data:
    avis_negatifs.extend(obj for obj in data[dicName] if obj.get('label') == 'negatif')
    avis_positifs.extend(obj for obj in data[dicName] if obj.get('label') == 'positif')
avis = avis_negatifs + avis_positifs
# Créer la liste de tuples (id, review_text, label)



tab.extend((obj['id'], obj['review_text'], obj['label']) for obj in avis)
tab = tab[:10000]
random.shuffle(tab)
print("on train sur", len(tab))
id , reviews, labels = zip(*tab)

processed_reviews = [str(doc).lower() for doc in nlp.pipe(reviews)]

print("nb positif label",labels.count('positif'),"nb négatif label",labels.count('negatif'))
train_reviews, test_reviews, train_labels, test_labels = train_test_split(processed_reviews, labels, test_size=0.2, random_state=42)


vectorizer = TfidfVectorizer()
X_train = vectorizer.fit_transform(train_reviews)
X_test = vectorizer.transform(test_reviews)


svm_model = SVC(kernel='linear')

svm_model.fit(X_train, train_labels)
predictions = svm_model.predict(X_test)
unique_classes, counts = np.unique(predictions, return_counts=True)
class_counts = dict(zip(unique_classes, counts))
print("Nombre d'occurrences de chaque classe dans les prédictions :", class_counts)

accuracy = accuracy_score(test_labels, predictions)
print("Précision du modèle :", accuracy)


test = svm_model.predict(vectorizer.transform(["I love this place!"]))
test1 = svm_model.predict(vectorizer.transform(["I hate this place"]))
test3 = svm_model.predict(vectorizer.transform(["The place is known for quantity and not quality for the veg Biryani I was served."]))

print(test, test1, test3)
