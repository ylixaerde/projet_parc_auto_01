import os
import csv

# afficher la liste des vehicules
def fn_display_vehicule(csv_file_path):
    # Lecture du fichier CSV
    with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
        vehicule_reader = csv.DictReader(csvfile, delimiter=',')
        for item in vehicule_reader:
            print(f"Marque : {item["marque"]}, Modèle : {item["modele"]}, Plaque d'immatriculation : {item["immatriculation_id"]}, ID utilisateur : {item["utilisateur_id"]}")

# afficher la liste des utilisateurs
def fn_display_utilisateur(csv_file_path):
    # Lecture du fichier CSV
    with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
        utilisateur_reader = csv.DictReader(csvfile, delimiter=',')
        for item in utilisateur_reader:
            print(f"Nom : {item["nom"]}, Prénom : {item["prenom"]}, ID véhicule : {item["vehicule_id"]}")

# afficher la liste complète véhicule avec utilisateur
def fn_display_veh_and_user(csv_vehicule_file_path, csv_utilisateur_file_path):
    vehicules = {}

    # Lecture du fichier CSV des véhicules
    with open(csv_vehicule_file_path, newline='', encoding='utf-8') as csvfile:
        vehicule_reader = csv.DictReader(csvfile, delimiter=',')
        for item in vehicule_reader:
            vehicules[item['id']] = item

    # Lecture du fichier CSV des utilisateurs
    with open(csv_utilisateur_file_path, newline='', encoding='utf-8') as csvfile:
        utilisateur_reader = csv.DictReader(csvfile, delimiter=',')
        for item in utilisateur_reader:
            vehicule_id = item['vehicule_id']
            if vehicule_id in vehicules:
                vehicule_info = vehicules[vehicule_id]
                print(f"Véhicule - Marque : {vehicule_info['marque']}, Modèle : {vehicule_info['modele']}, Plaque d'immatriculation : {vehicule_info['immatriculation_id']}, Nom utilisateur : {item['nom']}, Prénom utilisateur : {item['prenom']}")   

    
# Lancement du script
if __name__ == "__main__":
    file_path = os.path.realpath(__file__)
    work_dir = os.path.dirname(file_path)
    csv_vehicule_file_path = f"{work_dir}/vehicules.csv"
    csv_utilisateur_file_path = f"{work_dir}/utilisateurs.csv"
    # fn_display_vehicule(csv_vehicule_file_path)
    # fn_display_utilisateur(csv_utilisateur_file_path)
    fn_display_veh_and_user(csv_vehicule_file_path, csv_utilisateur_file_path)
