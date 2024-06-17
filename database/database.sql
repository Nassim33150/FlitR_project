-- Utilisation de la base de données SystemeRecommandation
USE SystemeRecommandation;

-- Création de la table Users si elle n'existe pas
CREATE TABLE IF NOT EXISTS Users (
    ID INT PRIMARY KEY AUTO_INCREMENT,
    Username VARCHAR(100) NOT NULL UNIQUE,
    Email VARCHAR(255) NOT NULL UNIQUE,
    HashedPassword VARCHAR(255) NOT NULL,
    Nom VARCHAR(100),
    Prénom VARCHAR(100),
    Age INT,
    Sport_Pratiqué VARCHAR(255),
    Durée_Moyenne_Cycle VARCHAR(255),
    Crainte_Tâcher BOOLEAN
);

-- Suppression et création de la table Entrainement
DROP TABLE IF EXISTS Entrainement;
CREATE TABLE Entrainement (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    Utilisateur_ID INT,
    Fréquence_Entraînement VARCHAR(500),
    Changement_Protection BOOLEAN,
    Recommandations_Pauses TEXT,
    Objectif_Améliorer_Confort INT,
    Objectif_Améliorer_Performances INT,
    FOREIGN KEY (Utilisateur_ID) REFERENCES Users(ID)
);

-- Suppression et création de la table Sessions
DROP TABLE IF EXISTS Sessions;
CREATE TABLE Sessions (
    SessionID INT PRIMARY KEY AUTO_INCREMENT,
    UserID INT,
    SessionToken VARCHAR(255) UNIQUE,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    ExpiresAt TIMESTAMP,
    FOREIGN KEY (UserID) REFERENCES Users(ID)
);

