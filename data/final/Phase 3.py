import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pandas import to_datetime

# Charger le fichier Excel
xls = pd.ExcelFile('../../../Travail-de-session-test-3/data/final/output_combiné.xlsx')
# Lire les données des onglets spécifiques
df_clients = pd.read_excel(xls, 'clients_cleaned')
df_conseillers = pd.read_excel(xls, 'conseillers_cleaned')
df_portfolios = pd.read_excel(xls, 'portfolios_premier_client')
df_produits = pd.read_excel(xls, 'produits_transformed')
df_titres = pd.read_excel(xls, 'titres_tsx_sp_cleaned')

# ---- Section 1 : Graphiques sur les Conseillers Financiers ----
### - Graphique : Nombre de clients par conseiller financier
# Calculer le nombre moyen de clients par conseiller
average_clients_per_advisor = len(df_clients) / len(df_conseillers)
# Fonction pour créer le graphique
def clients_per_advisor():
    plt.figure(figsize=(8, 6))
    # Ici, on crée un DataFrame pour simplifier le tracé avec seaborn
    data = pd.DataFrame({
        'Conseiller': ['Conseiller 1', 'Conseiller 2', 'Conseiller 3'],
        'Moyenne de Clients': [average_clients_per_advisor] * 3
    })
    sns.barplot(x='Conseiller', y='Moyenne de Clients', data=data, color='steelblue')
    plt.title('Moyenne du Nombre de Clients par Conseiller Financier')
    plt.ylabel('Moyenne de Clients')
    plt.show()
# Appeler la fonction pour afficher le graphique
clients_per_advisor()

### - Graphique : Valeur totale du portefeuille d'investissement par conseiller financier
# Calcul de la valeur totale du portefeuille par conseiller
# Supposons que 'epargne' est une colonne dans df_clients qui représente la valeur du portefeuille
total_portfolio_value_clients = df_clients['epargne'].sum()
# Supposons qu'il y ait exactement trois conseillers pour une distribution égale
total_portfolio_value_per_advisor = total_portfolio_value_clients / 3
# Création du DataFrame pour le tracé
data = pd.DataFrame({
    'Conseiller': ['Conseiller 1', 'Conseiller 2', 'Conseiller 3'],
    'Valeur totale du portefeuille': [total_portfolio_value_per_advisor] * 3
})
# Fonction pour créer l'histogramme
def portfolio_value_per_advisor():
    plt.figure(figsize=(10, 6))
    sns.barplot(x='Conseiller', y='Valeur totale du portefeuille', data=data, color='steelblue')
    plt.title('Valeur Totale du Portefeuille par Conseiller Financier')
    plt.xlabel('Conseiller')
    plt.ylabel('Valeur Totale du Portefeuille ($)')
    plt.xticks(rotation=45)  # Rotation pour une meilleure lisibilité
    plt.show()
# Appeler la fonction pour afficher le graphique
portfolio_value_per_advisor()
