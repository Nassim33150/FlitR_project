# Calcul des métriques de performance
mse = mean_squared_error(targets, y_pred)
r2 = r2_score(targets, y_pred)

# Effectuer une validation croisée
scores = cross_val_score(lr, X_train, y_train, cv=5, scoring='r2')

# Créer un pipeline qui normalise les données puis applique une régression Ridge
ridge_pipeline = make_pipeline(StandardScaler(), Ridge(alpha=1.0))

# Effectuer une validation croisée avec le pipeline Ridge
ridge_scores = cross_val_score(ridge_pipeline, X_train, y_train, cv=5, scoring='r2')

# Initialiser le modèle Random Forest
rf_model = RandomForestRegressor(n_estimators=100, random_state=42)

# Sélection des caractéristiques pour X
X = df_besoin_entrainement[['Âge', 'Sport pratiqué_autre', 'Sport pratiqué_course sur route',
                            'Sport pratiqué_cyclisme ', 'Sport pratiqué_triathlon',
                            'Durée moyenne des règles', 'Prise en compte du cycle menstruel dans le plan d’entraînement', 
                            'Crainte de tâcher sous-vêtements', 'Contraception ?']] 

# Sélection des cibles pour y
y = df_besoin_entrainement[[
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

# Réinitialiser les index de X et y
X = X.reset_index(drop=True)
y = y.reset_index(drop=True)

# Initialisation du modèle Random Forest
rf_model = RandomForestRegressor(n_estimators=100, random_state=42)
# Effectuer une validation croisée avec le modèle Random Forest
rf_scores = cross_val_score(rf_model, X, y, cv=5, scoring='r2')
