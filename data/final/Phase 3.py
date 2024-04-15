import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pandas import to_datetime

# Chemins d'accès aux fichiers
path_portfolios = '../../../Travail-de-session-test-3/data/final/portfolios_premier_client.xlsx'
path_products = '../../../Travail-de-session-test-3/data/final/produits_transformed.xlsx'
path_titles = '../../../Travail-de-session-test-3/data/final/titres_tsx_sp_cleaned.xlsx'
path_clients = '../../../Travail-de-session-test-3/data/final/clients_cleaned.xlsx'
path_advisors = '../../../Travail-de-session-test-3/data/final/conseillers_cleaned.xlsx'

# Chargement des données
df_portfolios = pd.read_excel(path_portfolios)
df_products = pd.read_excel(path_products)
df_titles = pd.read_excel(path_titles)
df_clients = pd.read_excel(path_clients)
df_advisors = pd.read_excel(path_advisors)

# Conversion des colonnes de date en UTC
def convert_to_utc(df, time_col):
    df[time_col] = pd.to_datetime(df[time_col], utc=True)
    return df

df_clients = convert_to_utc(df_clients, 'maj')

# Identification de la colonne de l'ID du conseiller
advisor_id_col = 'uid' if 'uid' in df_advisors.columns else df_advisors.columns[0]
print(f"Using column '{advisor_id_col}' as AdvisorID.")

# ---- Section 1 : Graphiques sur les Conseillers Financiers ----
# Graphique : Nombre de clients par conseiller financier

# Comptage du nombre de clients par conseiller
client_counts = df_clients['AdvisorID'].value_counts().reindex([1, 2, 3], fill_value=0)
def clients_per_advisor():
    plt.figure(figsize=(8, 6))
    sns.barplot(x=client_counts.index, y=client_counts.values, palette='coolwarm')
    plt.title('Nombre de Clients par Conseiller Financier')
    plt.xlabel('ID du Conseiller')
    plt.ylabel('Nombre de Clients')
    plt.xticks(range(len(client_counts.index)),['Conseiller 1', 'Conseiller 2', 'Conseiller 3'])  # Nommer les ticks pour clarté
    plt.show()

# Graphique : Valeur totale du portefeuille par conseiller financier
def portfolio_value_per_advisor():
    plt.figure(figsize=(10, 6))
    total_values = df_portfolios.groupby(advisor_id_col)['PortfolioValue'].sum()
    sns.barplot(x=total_values.index, y=total_values.values, palette='viridis')
    plt.title('Valeur Totale du Portefeuille par Conseiller Financier')
    plt.xlabel('ID du Conseiller')
    plt.ylabel('Valeur Totale du Portefeuille ($)')
    plt.xticks(rotation=45)
    plt.show()

# Graphique : Comparaison de la valeur du portefeuille par genre
def comparative_gender_portfolio_value():
    plt.figure(figsize=(10, 6))
    sns.histplot(data=df_portfolios, x='PortfolioValue', hue='Gender', multiple='stack', palette='pastel')
    plt.title('Valeur du Portefeuille par Genre pour Chaque Conseiller')
    plt.xlabel('Valeur Totale du Portefeuille ($)')
    plt.ylabel('Nombre')
    plt.show()

# ---- Section 2 : Graphiques sur les Clients et leurs Portefeuilles ----
# Graphique : Distribution des âges des clients
def age_distribution_of_clients():
    plt.figure(figsize=(10, 6))
    sns.histplot(df_clients['Age'], bins=30, kde=False)
    plt.title('Distribution des Âges des Clients')
    plt.xlabel('Âge')
    plt.ylabel('Nombre de Clients')
    plt.show()

# Graphique : Distribution des revenus annuels des clients
def income_distribution_of_clients():
    plt.figure(figsize=(10, 6))
    sns.histplot(df_clients['AnnualIncome'], bins=30, kde=False)
    plt.title('Distribution des Revenus Annuels des Clients')
    plt.xlabel('Revenu Annuel ($)')
    plt.ylabel('Nombre de Clients')
    plt.show()

# Graphique : Corrélation entre la valeur du portefeuille et le revenu annuel
def portfolio_vs_income_scatter():
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='AnnualIncome', y='PortfolioValue', data=df_clients, hue='RiskPreference', style='Gender')
    plt.title('Corrélation entre Valeur du Portefeuille et Revenu Annuel des Clients')
    plt.xlabel('Revenu Annuel ($)')
    plt.ylabel('Valeur du Portefeuille ($)')
    plt.legend(title='Préférence de Risque')
    plt.show()

# Graphique : Valeur totale des titres sous gestion par industrie
def total_securities_by_industry():
    plt.figure(figsize=(10, 6))
    industry_values = df_portfolios.groupby('Industry')['PortfolioValue'].sum().sort_values(ascending=False)
    sns.barplot(x=industry_values.values, y=industry_values.index, palette='rocket')
    plt.title('Valeur Totale des Titres sous Gestion par Industrie')
    plt.xlabel('Valeur Totale ($)')
    plt.ylabel('Industrie')
    plt.show()

# ---- Section 3 : Graphiques sur les Produits Financiers ----
# Graphique : Nombre de clients par produit financier
def clients_per_financial_product():
    plt.figure(figsize=(10, 6))
    product_counts = df_products['ProductName'].value_counts()
    sns.barplot(x=product_counts.values, y=product_counts.index, palette='coolwarm')
    plt.title('Nombre de Clients par Produit Financier')
    plt.xlabel('Nombre de Clients')
    plt.ylabel('Produit Financier')
    plt.show()

# Graphique : Pourcentages de la valeur totale sous gestion par industrie
def portfolio_distribution_by_industry():
    plt.figure(figsize=(10, 6))
    industry_portfolio = df_portfolios.groupby('Industry')['PortfolioValue'].sum()
    industry_portfolio.plot(kind='pie', autopct='%1.1f%%', startangle=90, colors=sns.color_palette('viridis', len(industry_portfolio)))
    plt.title('Pourcentages de la Valeur Totale sous Gestion par Industrie')
    plt.ylabel('')  # Enlever le label de l'axe y
    plt.show()

# Exécution des fonctions de visualisation
clients_per_advisor()
portfolio_value_per_advisor()
comparative_gender_portfolio_value()
age_distribution_of_clients()
income_distribution_of_clients()
portfolio_vs_income_scatter()
total_securities_by_industry()
clients_per_financial_product()
portfolio_distribution_by_industry()