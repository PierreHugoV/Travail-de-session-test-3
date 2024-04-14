import os
import pandas as pd
import json

# Le but de la phase 1 est de s'assurer que notre code prend bien en compte tout les fichier de data que nous avons en notre possesion

# On commence donc par implémenter le chemins vers lequel toute notre data est présente
data_dir = '../../../Travail-de-session-test-3/data/final'

# Ensuite on vient vérifier si tout nos fichiers son bien présent
def read_data_files(directory):
    print("Commencer à lire les fichiers ...")
    data_files = {}
    for root, dirs, files in os.walk(directory):
        print(f"Recherche dans le directory: {root}")  # Affiche le répertoire actuel
        for file in files:
            print(f"Fichier trouvé: {file}")  # Affiche chaque fichier trouvé
            file_path = os.path.join(root, file)
            if file.endswith('.csv'):
                data_files[file] = pd.read_csv(file_path)
            elif file.endswith('.json'):
                with open(file_path, 'r') as f:
                    data_content = json.load(f)
                    # La même logique pour JSON s'applique ici
                    if isinstance(data_content, list):
                        data_files[file] = pd.DataFrame(data_content)
                    else:
                        data_files[file] = pd.DataFrame([data_content])
            elif file.endswith('.xlsx'):
                data_files[file] = pd.read_excel(file_path)
    print("Fin de la lecture des fichiers.")
    return data_files

# Exécutez la fonction avec le bon chemin
data_contents = read_data_files(data_dir)

# Au final, l'output que l'on obtien avec le code de cette phase 1 nous montre belle et bien que nous avons tout nos fichier, sous différents format et que si jamais nous rajoutons un fichier sous un de ces 3 formats, on peu run de nouveau le code et le fichier devrait apparaitre.

# Pour les besoins du travail, le code de cette phase 1 va aussi nous montrer chaque fichier python (Phase 1 à 4) que nous utilisons pour le travail de session