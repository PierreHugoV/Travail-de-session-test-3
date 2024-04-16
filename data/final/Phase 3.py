import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

#GRAPHIQUE 1
# Charger les données à partir du fichier Excel
excel_path = '../../../Travail-de-session-test-3/data/final/output_combiné.xlsx'
conseillers_df = pd.read_excel(excel_path, sheet_name='conseillers_cleaned')
clients_df = pd.read_excel(excel_path, sheet_name='clients_cleaned')

# Simuler le nombre de clients pour chaque conseiller (remplacez cette partie par les vraies données une fois que celle-ci seront disponibles)
np.random.seed(42)  # pour la reproductibilité
conseillers_df['nombre_clients'] = np.random.randint(20, 100, size=len(conseillers_df))

# Créer un graphique en barres
plt.figure(figsize=(10, 6))
plt.bar(conseillers_df['prenom'], conseillers_df['nombre_clients'], color='skyblue')
plt.xlabel('Conseiller')
plt.ylabel('Nombre de Clients')
plt.title('Nombre de Clients par Conseiller')
plt.xticks(rotation=45)  # Rotation des étiquettes pour une meilleure lisibilité
plt.tight_layout()  # Ajuste automatiquement les sous-tracés pour donner un peu de padding entre les bords
plt.savefig('graphique1.png')
plt.show()



#GRAPHIQUE 2
# Suppose que 'conseillers_df' est votre DataFrame contenant les informations des conseillers financiers
# Générer des valeurs simulées pour la valeur totale des portefeuilles pour chaque conseiller financier
np.random.seed(42)
mean_portfolio_value = 500000  # Valeur moyenne supposée pour un portefeuille
std_dev_portfolio_value = 100000  # Écart-type supposé pour la valeur du portefeuille

# Simuler la valeur totale du portefeuille d'investissement pour chaque conseiller financier
conseillers_df['valeur_portefeuille'] = np.random.normal(mean_portfolio_value, std_dev_portfolio_value, len(conseillers_df))

# Créer un graphique en barres horizontales de la valeur totale du portefeuille par conseiller financier
plt.figure(figsize=(10, 6))
plt.barh(range(len(conseillers_df)), conseillers_df['valeur_portefeuille'], color='green', edgecolor='black')
plt.ylabel('Conseiller Financier')
plt.xlabel('Valeur du Portefeuille (en dollars)')
plt.title('Valeur Totale du Portefeuille par Conseiller Financier')
plt.yticks(range(len(conseillers_df)), conseillers_df['prenom'])  # Utiliser le prénom du conseiller pour l'étiquette
plt.grid(True)
plt.tight_layout()
plt.savefig('graphique2.png')
plt.show()

#GRAPHIQUE 3
# Suppose que 'conseillers_df' est votre DataFrame contenant les informations des conseillers financiers
# Générer des valeurs simulées séparément pour la valeur totale des portefeuilles des clients féminins et masculins pour chaque conseiller financier
np.random.seed(42)
mean_portfolio_value = 500000  # Valeur moyenne supposée pour un portefeuille
std_dev_portfolio_value = 100000  # Écart-type supposé pour la valeur du portefeuille

# Simuler la valeur totale du portefeuille pour des clients féminins et masculins
conseillers_df['valeur_portefeuille_femmes'] = np.random.normal(mean_portfolio_value, std_dev_portfolio_value, len(conseillers_df))
conseillers_df['valeur_portefeuille_hommes'] = np.random.normal(mean_portfolio_value, std_dev_portfolio_value, len(conseillers_df))

# Créer un histogramme comparatif pour les valeurs de portefeuille par genre
labels = conseillers_df['prenom']
x = np.arange(len(labels))  # the label locations
width = 0.35  # the width of the bars

fig, ax = plt.subplots(figsize=(14, 7))
rects1 = ax.bar(x - width/2, conseillers_df['valeur_portefeuille_femmes'], width, label='Femmes', color='pink')
rects2 = ax.bar(x + width/2, conseillers_df['valeur_portefeuille_hommes'], width, label='Hommes', color='blue')

# Ajouter des textes pour les labels, titre et axes ticks personnalisés
ax.set_xlabel('Conseillers Financiers')
ax.set_ylabel('Valeur du Portefeuille (en dollars)')
ax.set_title('Valeur du Portefeuille par Genre et par Conseiller Financier')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()

ax.bar_label(rects1, padding=3)
ax.bar_label(rects2, padding=3)

fig.tight_layout()
plt.savefig('graphique3.png')
plt.show()

#GRAPHIQUE 4
# Chargement de la feuille des clients
df_clients = pd.read_excel(excel_path, sheet_name='clients_cleaned')

# Assurons-nous que la colonne contenant les âges est nommée 'Age'
# Si ce n'est pas le cas, ajustez 'Age' à la colonne appropriée

# Création de l'histogramme pour l'âge des clients
def plot_age_distribution():
    plt.figure(figsize=(12, 6))
    sns.histplot(df_clients['age'], bins=20, color='skyblue', kde=True)
    plt.title('Distribution des Âges des Clients')
    plt.xlabel('Âge')
    plt.ylabel('Nombre de Clients')
    plt.grid(True)  # Ajoute un grille pour une meilleure lisibilité
    plt.savefig('graphique4.png')
    plt.show()

# Appeler la fonction pour afficher l'histogramme
plot_age_distribution()


#GRAPHIQUE 5
# Chemin d'accès au fichier Excel combiné (assurez-vous que le chemin est correct)
file_path = '../../../Travail-de-session-test-3/data/final/output_combiné.xlsx'

# Chargement de la feuille des clients
df_clients = pd.read_excel(file_path, sheet_name='clients_cleaned')

# Assurons-nous que la colonne contenant les revenus annuels est nommée 'AnnualIncome'
# Si ce n'est pas le cas, ajustez 'AnnualIncome' à la colonne appropriée

# Création de l'histogramme pour le revenu annuel des clients
def plot_income_distribution():
    plt.figure(figsize=(12, 6))
    sns.histplot(df_clients['revenu_annuel'], bins=20, color='skyblue', kde=True)
    plt.title('Distribution des Revenus Annuels des Clients')
    plt.xlabel('Revenu Annuel ($)')
    plt.ylabel('Nombre de Clients')
    plt.grid(True)  # Ajoute une grille pour une meilleure lisibilité
    plt.savefig('graphique5.png')
    plt.show()

# Appeler la fonction pour afficher l'histogramme
plot_income_distribution()

#GRAPHIQUE 6
# Charger les données de revenu annuel des clients
clients_revenu_df = pd.read_excel(excel_path, sheet_name='clients_cleaned')

# Simuler la valeur du portefeuille pour chaque client
np.random.seed(42)
clients_revenu_df['valeur_portefeuille'] = np.random.normal(100000, 50000, len(clients_revenu_df))

# Créer un graphique à points de la valeur actuelle du portefeuille par rapport au revenu des clients
plt.figure(figsize=(12, 8))
plt.scatter(clients_revenu_df['revenu_annuel'], clients_revenu_df['valeur_portefeuille'], alpha=0.5)
plt.title('Valeur Actuelle du Portefeuille par Rapport au Revenu des Clients')
plt.xlabel('Revenu Annuel des Clients (en dollars)')
plt.ylabel('Valeur Simulée Actuelle du Portefeuille (en dollars)')
plt.grid(True)
plt.savefig('graphique6.png')
plt.show()

#GRAPHIQUE 7
# Supposons que titres_df est déjà chargé avec des informations sur les titres et les industries
# Simuler des valeurs pour chaque titre
# Chargement des données des titres
titres_df = pd.read_excel('../../../Travail-de-session-test-3/data/final/output_combiné.xlsx', sheet_name='titres_tsx_sp_cleaned')

np.random.seed(42)
titres_df['valeur'] = np.random.normal(100, 20, len(titres_df))

# Calculer la valeur totale des titres sous gestion par industrie
valeur_par_industrie = titres_df.groupby('industry')['valeur'].sum()

# Créer un graphique à pointes pour la valeur totale des titres par industrie
plt.figure(figsize=(12, 8))
valeur_par_industrie.plot(kind='bar', color='skyblue')
plt.title('Valeur Totale des Titres Sous Gestion par Industrie')
plt.xlabel('Industrie')
plt.ylabel('Valeur Totale (en dollars)')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.savefig('graphique7.png')
plt.show()

#GRAPHIQUE 8
# Charger les données de la profession des clients et simuler les valeurs des portefeuilles
clients_revenu_df = pd.read_excel(excel_path, sheet_name='clients_cleaned')
np.random.seed(42)
clients_revenu_df['valeur_portefeuille'] = np.random.normal(100000, 50000, len(clients_revenu_df))

# Calculer la valeur totale du portefeuille par profession
valeur_par_profession = clients_revenu_df.groupby('profession')['valeur_portefeuille'].sum()

# Créer un graphique à barres de la valeur totale du portefeuille par profession
plt.figure(figsize=(14, 8))
valeur_par_profession.sort_values().plot(kind='barh', color='purple')
plt.title('Valeur Totale du Portefeuille par Profession')
plt.xlabel('Valeur Totale du Portefeuille (en dollars)')
plt.ylabel('Profession')
plt.grid(True)
plt.tight_layout()
plt.savefig('graphique8.png')
plt.show()

#GRAPIQUE 9
# Chargement des données des produits financiers
produits_df = pd.read_excel(excel_path, sheet_name='produits_transformed')

# Utilisation de la colonne 'Pourcentage Stock (%)' comme un indicateur de popularité des produits
# et simulation du nombre de clients pour chaque produit financier
np.random.seed(42)
produits_popularite = produits_df.groupby('Produit')['Pourcentage Stock (%)'].sum()

# Création d'un graphique à barres horizontales pour le nombre estimé de clients par produit financier
plt.figure(figsize=(14, 10))
produits_popularite.sort_values().plot(kind='barh', color='teal')
plt.title('Nombre Estimé de Clients par Produit Financier')
plt.ylabel('Produit Financier')
plt.xlabel('Nombre Estimé de Clients (proportionnel)')
plt.grid(True)
plt.tight_layout()
plt.savefig('graphique9.png')
plt.show()

#GRAPHIQUE 10
# Charger les données des titres et simuler la valeur de marché pour chaque titre
titres_df = pd.read_excel(excel_path, sheet_name='titres_tsx_sp_cleaned')
np.random.seed(42)
titres_df['valeur_marche'] = np.random.normal(100, 20, len(titres_df))

# Calculer la valeur totale des titres sous gestion par industrie
valeur_totale_par_industrie = titres_df.groupby('industry')['valeur_marche'].sum()

# Convertir les totaux en pourcentages de la valeur totale
valeur_totale = valeur_totale_par_industrie.sum()
pourcentages_par_industrie = (valeur_totale_par_industrie / valeur_totale) * 100

# Créer un graphique à pointes pour les pourcentages de la valeur totale sous gestion par industrie
plt.figure(figsize=(14, 8))
pourcentages_par_industrie.plot(kind='bar', color='orange')
plt.title('Pourcentages de la Valeur Totale Sous Gestion par Industrie')
plt.xlabel('Industrie')
plt.ylabel('Pourcentage de la Valeur Totale Sous Gestion (%)')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.savefig('graphique10.png')
plt.show()

#GRAPHIQUE 11
# Chargement de la feuille des portefeuilles du premier client
df_portfolios = pd.read_excel(file_path, sheet_name='portfolios_premier_client')

# Calcul des titres les plus populaires
# Groupement des données par 'TitreAction' et somme des 'NombreActions' pour chaque titre
title_popularity = df_portfolios.groupby('TitreAction')['NombreActions'].sum().nlargest(10)

# Création du DataFrame pour le tracé
data = pd.DataFrame({
    'Titre': title_popularity.index,
    'Nombre d\'Actions': title_popularity.values
})

# Fonction pour créer l'histogramme
def plot_top_titles():
    plt.figure(figsize=(14, 7))
    barplot = sns.barplot(x='Titre', y='Nombre d\'Actions', hue='Titre', data=data, palette='coolwarm')
    plt.title('Top 10 des Titres les Plus Populaires par Nombre d\'Actions')
    plt.xlabel('Titre de l\'Action')
    plt.ylabel('Nombre Total d\'Actions')
    plt.xticks(rotation=45)  # Rotation pour une meilleure lisibilité
    barplot.legend().set_visible(False)  # Cacher la légende si elle n'est pas nécessaire
    plt.savefig('graphique11.png')
    plt.show()

# Appeler la fonction pour afficher l'histogramme
plot_top_titles()
