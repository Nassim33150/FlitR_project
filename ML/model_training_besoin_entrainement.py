# -*- coding: utf-8 -*-
"""Untitled7.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1c8bFWz2FbOeRGhncc20fCHQYOEzP9o0I
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import OneHotEncoder, MinMaxScaler
from sklearn.impute import KNNImputer
import seaborn as sns
import pickle
import os

df = pd.read_csv("/content/df_encoded.csv")
df

df.info()

df = df.rename(columns={'4. Quel est ton âge ? ': 'Âge'})

df = df.rename(columns={"a. L'amélioration de ton confort?": 'Objectif_Améliorer_Confort'})

df = df.rename(columns={"Amélioration des performances": 'Objectif_Améliorer_Performances'})

df = df.rename(columns={"Changement de protections plus d'une fois toutes les deux heures": 'Changement de protection'})

df = df.rename(columns={"Contraintes de pauses pendant entraînement": 'Contraintes de pauses'})

df['Changement de protections plus d\'une fois toutes les deux heures'].value_counts()

# Sélection des caractéristiques (features)
# Sélection des caractéristiques (features)
X = df[['Âge', 'Sport pratiqué_autre', 'Sport pratiqué_course sur route', 'Sport pratiqué_cyclisme ', 'Sport pratiqué_triathlon', 'Durée moyenne des règles', 'Prise en compte du cycle menstruel dans le plan d’entraînement', 
        'Crainte de tâcher sous-vêtements', 'Contraception ?', "Programme d'entrainement"]]
# Définir la variable abondance_des_regles (ici, on utilise 'Durée moyenne des règles')
df['abondance_des_regles'] = df['Durée moyenne des règles']

# Définir la variable cible (besoin d'un plan d'entraînement)
def determine_besoin_plan_entrainement(row):
    # Exemple simplifié: besoin d'un plan si l'abondance est élevée
    if row['abondance_des_regles'] > 5:
        return 1
    else:
        return 0

df['besoin_d_entrainement'] = df.apply(determine_besoin_plan_entrainement, axis=1)

df['Durée moyenne des règles'].value_counts()



# Vérifier les nouvelles colonnes
print(df[['abondance_des_regles', 'besoin_d_entrainement']])

df['ne_suit_pas_programme'] = df["Programme d'entrainement"].apply(lambda x: 1 if x == 0 else 0)

print(df[['Programme d\'entrainement', 'ne_suit_pas_programme']].head())

# Définir la variable cible (besoin d'un plan d'entraînement)
def determine_besoin_plan_entrainement(row):
    # Exemple simplifié: besoin d'un plan si l'abondance est élevée et ne suit pas déjà un programme
    if row['abondance_des_regles'] > 5 and row['ne_suit_pas_programme'] == 1:
        return 1
    else:
        return 0

df['besoin_d_entrainement'] = df.apply(determine_besoin_plan_entrainement, axis=1)

# Vérification des nouvelles colonnes
print(df[['abondance_des_regles', 'ne_suit_pas_programme', 'besoin_d_entrainement']].head())

# Mise à jour de la sélection des caractéristiques (features)
# Sélection des caractéristiques (features)
X = df[['Âge', 'Sport pratiqué_autre', 'Sport pratiqué_course sur route', 'Sport pratiqué_cyclisme ', 'Sport pratiqué_triathlon', 'Durée moyenne des règles', 'Prise en compte du cycle menstruel dans le plan d’entraînement', 
        'Crainte de tâcher sous-vêtements', 'Contraception ?', "Programme d'entrainement"]]

y = df['besoin_d_entrainement']

# Diviser les données en ensembles d'entraînement et de test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Entraîner le modèle de régression linéaire
model = LinearRegression()
model.fit(X_train, y_train)

# Faire des prédictions
y_pred = model.predict(X_test)

# Binariser les prédictions (0 ou 1) car c'est un problème de classification binaire
y_pred_binary = [1 if pred >= 0.5 else 0 for pred in y_pred]
