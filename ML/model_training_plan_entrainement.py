# Filtrer les données pour ne garder que les personnes ayant besoin d'un entraînement
df_besoin_entrainement = df[df['besoin_d_entrainement'] == 1]

# Sélection des caractéristiques (features)
features = df[['Âge', 'Sport pratiqué_autre', 'Sport pratiqué_course sur route', 'Sport pratiqué_cyclisme ', 'Sport pratiqué_triathlon', 'Durée moyenne des règles', 'Prise en compte du cycle menstruel dans le plan d’entraînement', 
        'Crainte de tâcher sous-vêtements', 'Contraception ?', "Programme d'entrainement"]]

# Création de X en ajoutant une colonne à la fois
X = pd.DataFrame()
for feature in [
    'Âge', 'Sport pratiqué_autre', 'Sport pratiqué_course sur route',
    'Sport pratiqué_cyclisme ', 'Sport pratiqué_triathlon',
    'Durée moyenne des règles', 'Prise en compte du cycle menstruel dans le plan d’entraînement',
    'Crainte de tâcher sous-vêtements', 'Contraception ?', 'Programme d\'entrainement'
]:
    try:
        X[feature] = df_besoin_entrainement[feature]
        print(f"Ajout réussi pour la colonne : {feature}")
    except Exception as e:
        print(f"Erreur lors de l'ajout de la colonne : {feature}")
        print(e)

# Sélection des caractéristiques pour X
X = df_besoin_entrainement[['Âge', 'Sport pratiqué_autre', 'Sport pratiqué_course sur route',
                            'Sport pratiqué_cyclisme ', 'Sport pratiqué_triathlon',
                            'Durée moyenne des règles', 'Prise en compte du cycle menstruel dans le plan d’entraînement', 
                            'Crainte de tâcher sous-vêtements', 'Contraception ?']]

# Sélection des cibles pour targets
targets = df_besoin_entrainement[[
    "Nombre d'entrainements par semaine_2 à 4 entrainements/semaine",
    "Nombre d'entrainements par semaine_4 à 6 entrainements/semaine",
    "Nombre d'entrainements par semaine_<2 entrainements/semaine",
    "Nombre d'entrainements par semaine_>6 entrainements/semaine",
    "Changement de protection",
    "Contraintes port de double protection",
    "Objectif_Améliorer_Performances",
    "Objectif_Améliorer_Confort",
    "Contraintes de pauses"
]]

# Séparation des données en ensemble d'entraînement et de test
X_train, X_test, y_train, y_test = train_test_split(X, targets, test_size=0.2, random_state=42)

# Définir le modèle de régression linéaire
lr = LinearRegression()

# Entraînement du modèle
lr.fit(X, targets)

# Prédictions
y_pred = lr.predict(X)
