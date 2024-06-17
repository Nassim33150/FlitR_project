-- Insertion d'un nouvel utilisateur
USE SystemeRecommandation

INSERT INTO Users (Username, Email, HashedPassword, Nom, Prénom, Age, Sport_Pratiqué, Durée_Moyenne_Cycle, Crainte_Tâcher)
VALUES ('john_doe', 'john.doe@example.com', 'hashed_password', 'Doe', 'John', 30, 'Course à pied', '28 jours', 1);

-- Sélection de tous les utilisateurs
SELECT * FROM Users;

-- Mise à jour de l'âge d'un utilisateur spécifique
UPDATE Users SET Age = 31 WHERE Username = 'john_doe';

-- Suppression d'un utilisateur spécifique
DELETE FROM Users WHERE Username = 'john_doe';
