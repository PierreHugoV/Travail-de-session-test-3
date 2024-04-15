import pandas as pd
import json

# Chemin vers les fichiers de données des clients
client_files = {
    'clients.xlsx': '../../../Travail-de-session-test-3/data/final/clients/clients.xlsx',
    'clients001.json': '../../../Travail-de-session-test-3/data/final/clients/clients001.json',
    'clients002.csv': '../../../Travail-de-session-test-3/data/final/clients/clients002.csv',
    'clients003.csv': '../../../Travail-de-session-test-3/data/final/clients/clients003.csv',
    'clients004.json': '../../../Travail-de-session-test-3/data/final/clients/clients004.json',
    'clients005.json': '../../../Travail-de-session-test-3/data/final/clients/clients005.json',
    'clients006.csv': '../../../Travail-de-session-test-3/data/final/clients/clients006.csv'
}

# Chemin vers les fichiers de données des conseillers
conseillers_file_path = '../../../Travail-de-session-test-3/data/final/conseillers/conseillers.json'

# Chemin vers le fichier de données des portfolios
chemin_fichier_portfolios = '../../../Travail-de-session-test-3/data/final/portfolios/portfolios.json'

# Chemin vers le fichier de données des produits
produits_json_path = '../../../Travail-de-session-test-3/data/final/produits/produits.json'

# Chemin vers le fichier de données des titres
titres_csv_path = '../../../Travail-de-session-test-3/data/final/titres/titres_tsx_sp.csv'

# Fonction pour charger les données en fonction de l'extension du fichier
def load_data(file_path):
    if file_path.endswith('.xlsx'):
        return pd.read_excel(file_path)
    elif file_path.endswith('.csv'):
        return pd.read_csv(file_path)
    elif file_path.endswith('.json'):
        return pd.read_json(file_path)

# Fonction pour nettoyer les données des clients
def clean_client_data(df):
    # Retirer les colonnes entièrement vides
    df.dropna(axis=1, how='all', inplace=True)

    # Remplacer les valeurs manquantes pour 'gendre', 'age', 'langue' avec "N/A"
    # Seulement si la colonne existe dans le DataFrame
    for col in ['gendre', 'age', 'langue', 'pays']:
        if col in df.columns:
            df[col] = df[col].fillna("N/A")

    # Convertir 'maj' en format datetime si elle existe
    if 'maj' in df.columns:
        df['maj'] = pd.to_datetime(df['maj'])

    return df


# Fonction pour nettoyer les données des conseillers
def clean_conseillers_data(df):
    # Retirer les colonnes entièrement vides, s'il y en a
    df.dropna(axis=1, how='all', inplace=True)
    # Remplacer les valeurs manquantes par "N/A" dans les colonnes où cela est pertinent
    for col in ['genre', 'langues']:
        df[col] = df[col].fillna("N/A")
    # Normaliser les formats de listes pour 'formation', 'specialite', et 'langues'
    list_columns = ['formation', 'specialite', 'langues']
    for col in list_columns:
        df[col] = df[col].apply(lambda x: x if isinstance(x, list) else [x])
    return df

# Charger les données des portfolios
with open(chemin_fichier_portfolios, 'r') as f:
    donnees_portfolios = json.load(f)

# Extraire les données du premier client
premier_client = donnees_portfolios[0]  # On suppose que le fichier JSON est une liste

# Créer une liste pour stocker les données aplaties
donnees_aplaties = []

# Obtenir l'identifiant du client et du conseiller
identifiant_client = premier_client['client']
identifiant_conseiller = premier_client['adviser']

# Itérer sur chaque portefeuille du premier client
for portefeuille in premier_client['packages']:
    nom_portefeuille = portefeuille['nom']  # Nom du portfolio
    # Itérer sur chaque titre dans le contenu du portefeuille
    for titre in portefeuille['contenu']:
        nom_titre = titre['titre']  # Nom du titre
        nombre_titres = titre['nb_titres']  # Nombre de titres
        # Ajouter les informations dans la liste des données aplaties
        donnees_aplaties.append({
            'Client': identifiant_client,
            'Conseiller': identifiant_conseiller,
            'NomPortefeuille': nom_portefeuille,
            'TitreAction': nom_titre,
            'NombreActions': nombre_titres
        })

# Convertir les données aplaties en DataFrame
df_portfolios = pd.DataFrame(donnees_aplaties)

# Charger les données JSON
with open(produits_json_path, 'r', encoding='utf-8') as file:
    produits_data = json.load(file)

# Fonction pour transformer les données JSON en DataFrame structuré
def transform_products_data(data):
    structured_data = []
    for product in data:
        product_name = product['produit']
        categories = product['content']
        for category_name, category_info in categories.items():
            category_weight = category_info['weight']
            for stock in category_info['stocks']:
                stock_symbol = stock[0]
                stock_percentage = stock[1]
                structured_data.append({
                    "Produit": product_name,
                    "Catégorie": category_name,
                    "Poids de Catégorie (%)": category_weight,
                    "Symbole Stock": stock_symbol,
                    "Pourcentage Stock (%)": stock_percentage
                })
    return pd.DataFrame(structured_data)

# Transformer les données JSON
products_df = transform_products_data(produits_data)

# Vérifier les valeurs manquantes
if products_df.isnull().any().any():
    products_df.fillna('N/A', inplace=True)

# Charger le fichier CSV avec un séparateur de tabulation
titres_df = pd.read_csv(titres_csv_path, sep='\t')

# Nettoyer la colonne 'symbol' pour extraire uniquement le symbole de l'action
titres_df['symbol'] = titres_df['symbol'].str.extract(r'q\?s=(\w+\.\w+)$')

# Supprimer les espaces inutiles autour des noms de compagnies
titres_df['cie'] = titres_df['cie'].str.strip()

# Remplacer les valeurs manquantes par 'N/A'
titres_df.fillna('N/A', inplace=True)


# Assurez-vous que toutes les transformations sont appliquées aux clients
def final_transformations_clients(df):
    # Remplacer les valeurs manquantes pour 'gendre', 'age', 'langue' avec "N/A"
    for col in ['gendre', 'age', 'langue']:
        df[col] = df[col].fillna("N/A")
    # Remplacer les valeurs manquantes pour 'actif', 'passif', 'dettes', 'epargne' avec 0
    for col in ['actif', 'passif', 'dettes', 'epargne']:
        df[col] = df[col].fillna(0)
    # Remplacer les valeurs manquantes dans 'pays' par "Canada" si la 'province' est "Quebec" ou "Ontario"
    df['pays'] = df.apply(lambda row: "Canada" if pd.isna(row['pays']) and row['province'] in ["Quebec", "ON", "Ontario"] else row['pays'], axis=1)
    return df

# Traiter chaque fichier de clients, les nettoyer et les combiner
cleaned_client_dfs = []
for file, path in client_files.items():
    df = load_data(path)
    cleaned_df = clean_client_data(df)
    cleaned_client_dfs.append(cleaned_df)

# Combiner toutes les données des clients en un seul DataFrame
all_clients_data = pd.concat(cleaned_client_dfs, ignore_index=True)

# Appliquer les transformations finales aux clients
all_clients_data = final_transformations_clients(all_clients_data)

# Exporter les données des clients finales vers Excel
output_file_path_clients = '../../../Travail-de-session-test-3/data/final/clients_cleaned.xlsx'
all_clients_data.to_excel(output_file_path_clients, index=False)
print(f"Les données des clients ont été exportées avec succès vers {output_file_path_clients}")

# Charger les données des conseillers
conseillers_data = load_data(conseillers_file_path)

# Nettoyer les données des conseillers
cleaned_conseillers_data = clean_conseillers_data(conseillers_data)

# Exporter les données des conseillers nettoyées vers Excel
output_file_path_conseillers = '../../../Travail-de-session-test-3/data/final/conseillers_cleaned.xlsx'
cleaned_conseillers_data.to_excel(output_file_path_conseillers, index=False)
print(f"Les données des conseillers ont été exportées avec succès vers {output_file_path_conseillers}")

# Exporter le DataFrame dans un fichier Excel
chemin_fichier_excel = '../../../Travail-de-session-test-3/data/final/portfolios_premier_client.xlsx'
df_portfolios.to_excel(chemin_fichier_excel, index=False)

print(f"Le portfolio du premier client a été exporté avec succès vers {chemin_fichier_excel}")

# Chemin pour sauvegarder le fichier Excel transformé
output_excel_path = '../../../Travail-de-session-test-3/data/final/produits_transformed.xlsx'

# Exporter le DataFrame en fichier Excel
products_df.to_excel(output_excel_path, index=False)

print(f"Le fichier Excel a été sauvegardé à : {output_excel_path}")

# Chemin pour sauvegarder le fichier CSV nettoyé
output_csv_path = '../../../Travail-de-session-test-3/data/final/titres_tsx_sp_cleaned.csv'

# Exporter le DataFrame nettoyé en fichier CSV
titres_df.to_csv(output_csv_path, index=False)

# Chemin pour sauvegarder le fichier Excel
output_excel_path = '../../../Travail-de-session-test-3/data/final/titres_tsx_sp_cleaned.xlsx'

# Exporter le DataFrame nettoyé en fichier Excel
titres_df.to_excel(output_excel_path, index=False)

print(f"CSV file saved to: {output_csv_path}")
print(f"Excel file saved to: {output_excel_path}")

