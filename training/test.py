import spacy
import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report
import numpy as np
import random

# Charger le modèle de langue en anglais
nlp = spacy.load("en_core_web_sm")

# Charger les données
with open('datafrotrain.json') as fichier:
    data = json.load(fichier)

avis_negatifs = []
avis_positifs = []
for dicName in data:
    avis_negatifs.extend(obj for obj in data[dicName] if obj.get('label') == 'negatif')
    avis_positifs.extend(obj for obj in data[dicName] if obj.get('label') == 'positif')
avis = avis_negatifs + avis_positifs

# Créer la liste de tuples (id, review_text, label)
tab = [(obj['id'], obj['review_text'], obj['label']) for obj in avis]
tab = tab[:10000]

# Mélanger les données
random.shuffle(tab)

# Diviser les données en ensemble d'entraînement et ensemble de test
id, reviews, labels = zip(*tab)
processed_reviews = [str(doc).lower() for doc in nlp.pipe(reviews)]
train_reviews, test_reviews, train_labels, test_labels = train_test_split(processed_reviews, labels, test_size=0.2, random_state=42)

# Extraction des caractéristiques avec TF-IDF
vectorizer = TfidfVectorizer()
X_train = vectorizer.fit_transform(train_reviews)
X_test = vectorizer.transform(test_reviews)

# Construction et entraînement du modèle SVM
svm_model = SVC(kernel='linear', C=1.0) 
svm_model.fit(X_train, train_labels)

# Prédiction sur l'ensemble de test
predictions = svm_model.predict(X_test)

# Évaluation du modèle
accuracy = accuracy_score(test_labels, predictions)
print("Précision du modèle :", accuracy)

# Afficher le rapport de classification pour une analyse plus détaillée
print("Rapport de Classification :\n", classification_report(test_labels, predictions))

# Examinez les exemples mal classés pour comprendre les erreurs
misclassified_examples = [example for example, true_label, pred_label in zip(test_reviews, test_labels, predictions) if true_label != pred_label]
print("Exemples mal classés :\n", misclassified_examples[:5])  # Affichez les premiers 5 exemples mal classés

print(svm_model.predict(vectorizer.transform(["The food was so bad"])))
print(svm_model.predict(vectorizer.transform(["The food was discusting"])))

test = svm_model.predict(vectorizer.transform(["I love this place!"]))
test1 = svm_model.predict(vectorizer.transform(["I hate this place"]))
test3 = svm_model.predict(vectorizer.transform(["The place is known for quantity and not quality for the veg Biryani I was served."]))

print(test,test1,test3)