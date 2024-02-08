Voici un exemple de fichier `readme.md` pour documenter votre script Python :

```markdown
# Description

Ce script Python permet de gérer des données de véhicules et d'utilisateurs à partir de fichiers CSV contenant des informations sur les véhicules et les utilisateurs associés.

## Fonctionnalités

- Afficher la liste des véhicules.
- Afficher la liste des utilisateurs.
- Afficher la liste complète des véhicules avec les utilisateurs associés.

## Utilisation

Assurez-vous d'avoir installé Python sur votre système. Ce script utilise Python 3.

1. Clonez ou téléchargez ce dépôt sur votre machine.
2. Placez vos fichiers CSV contenant les données des véhicules et des utilisateurs dans le même répertoire que le script.
3. Exécutez le script en utilisant la commande suivante :

```bash
python nom_du_script.py
```

## Exemple de Structure de Fichiers

Assurez-vous que vos fichiers CSV ont la structure suivante :

- `vehicules.csv` : contient les données des véhicules avec les colonnes suivantes : `id`, `marque`, `modele`, `immatriculation_id`, etc.
- `utilisateurs.csv` : contient les données des utilisateurs avec les colonnes suivantes : `id`, `nom`, `prenom`, `vehicule_id`, etc.

## Exemple d'Utilisation du Script

```python
import os
import csv

# Fonctions pour afficher les données des véhicules et des utilisateurs
...

# Lancement du script
if __name__ == "__main__":
    file_path = os.path.realpath(__file__)
    work_dir = os.path.dirname(file_path)
    csv_vehicule_file_path = f"{work_dir}/vehicules.csv"
    csv_utilisateur_file_path = f"{work_dir}/utilisateurs.csv"
    fn_display_veh_and_user(csv_vehicule_file_path, csv_utilisateur_file_path)
```

## Remarques

- Ce script utilise le module `csv` de Python pour lire les données à partir des fichiers CSV.
- Assurez-vous que les fichiers CSV sont correctement formatés et qu'ils sont accessibles depuis le répertoire où se trouve le script.

N'hésitez pas à contribuer ou à signaler des problèmes en créant une issue ou une pull request.
```

N'oubliez pas de personnaliser ce fichier en fonction de vos besoins spécifiques et de votre projet.