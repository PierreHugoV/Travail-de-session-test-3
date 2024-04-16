# Rapport d'Analyse des Données de Summit Investment

## Contexte et Objectifs du Projet
Dans un monde financier de plus en plus complexe et diversifié, les institutions financières et bancaires sont sans cesse à l'affut d’opportunités pour développer et améliorer les services offerts à leur clientèle et de personnaliser leurs offres. Summit Investment cherche à optimiser ses stratégies en analysant la performance des conseillers, des portefeuilles clients et des produits financiers à partir de données diversifiées provenant de plusieurs systèmes internes. Ce projet vise à intégrer ces données et à fournir des analyses permettant de mieux comprendre les tendances et performances. 

## Démarche du projet/ Manipulation
### Extraction des données:
Tout d’abord, nous avons procédé à l’extraction des données clients de l’agence financière ce qui a servi de base pour l’analyse. Les données utilisées proviennent des fichiers clients, conseillers, produits, titres financiers et portefeuilles d'investissement. Ces données sont extraites de fichiers JSON, CSV et XLSX. Nous avons commencé par analyser le format de ces fichiers pour nous assurer que nous allions être en mesure de les analyser et puis nous nous sommes assurer que chacun de ces fichiers contenait de la data pour nos futures analyses.

### Nettoyage des données:
Par la suite, nous avons procédé au nettoyage des données:
- Supprimer les colonnes qui sont complètement vides.
- Remplacer les valeurs manquantes par “N/A” ou une autre valeur indicative de données manquantes qui convenait mieux à l’analyse 
- Normaliser les formats dates, des nombres et d’autres types de données spécifiques comme les identifiants de produits ou les codes de titres financiers. 
- Vérifier et éliminer les éventuelles données dupliquées pour éviter les biais pour l' analyse ultérieure. 

Pour terminer, nous avons généré un fichier Excel qui reflète toutes les transformations effectuées pour une révision visuelle du code utilisé et pour nous aider dans les phases ultérieures du projet. Dans ce fichier Excel (qui pourrait être sur n’importe quel autre format, seulement en Excel il est plus facile de visualiser que nos données ont bien été traité, nettoyer et autre), nous retrouvons chacune des sections des documents fournis par le client, soit: clients, conseillers, produits, titres financiers et portefeuilles d'investissement. Ces sections sont divisées pour chacune dans une table différentes, avec des titres de colonnes nous permettant de bien retrouver l’information utile pour nos prochaines étapes ainsi que la data nettoyé et normalisé entre les différentes tables. 

### Segmentation:
Ces données nous ont permis d'établir une segmentation de la clientèle afin d’identifier des groupes avec des besoins similaires. Grâce à la segmentation les conseillers financiers pourront offrir des services répondent mieux aux besoins des segments de clientèles dont ils sont chargés. Les données recueillies nous ont également permis d’établir des modèles prédictifs afin d’anticiper les besoins financiers des clients basés sur leurs historiques financiers. Ces analyses permettront de cibler plus précisément les offres et services, d'optimiser les stratégies de marketing, et d'améliorer la gestion des relations clients. 

### Hypothèses:
Nous avons produit certains graphiques avec des données aléatoires puisqu’il nous manquait certaines données pour arriver à certaines représentations. Lorsque les différentes informations manquantes seront rendues disponibles par la firme financière, seule une partie minime du code devrait être modifiée afin d’arriver aux représentations graphiques exactes de la situation de l’entreprise. 

## Graphiques:
### Histogramme du nombre de clients par conseiller financier:
Le graphique suivant représente une situation possible de la répartition des clients entre les trois conseillers financiers de la firme permettant un service client optimal. 

<img src="../../../Travail-de-session-test-3/data/final/graphique1.png" alt="Graphique 1" width="600" />

(si l'image des différents graphiques ne s'ouvre pas sur GitHub, veillez ouvrir le code sur PyCharm et voir le fichier python phase 4 qui est en format markdown, et à partir de ce fichier vous pouvez visualier le tout correctement)

### Histogramme de la valeur totale du portefeuille d'investissement par conseiller financier en date d'aujourd'hui:
Ce graphique permet d'analyser la performance des différents conseillers afin d’identifier les points forts et les points faibles de chacun, permettant d’identifier des pistes d’améliorations.

<img src="../../../Travail-de-session-test-3/data/final/graphique2.png" alt="Graphique 2" width="600" />

### Histogramme comparatif de la valeur totale du portefeuille d'investissement détenu par une femme ou un homme pour chaque conseiller financier:
Ce graphique permettra à l’entreprise de mieux comprendre leur clientèle afin de mieux orienter leurs différentes stratégies de placement ainsi que leurs stratégie marketing.

<img src="../../../Travail-de-session-test-3/data/final/graphique3.png" alt="Graphique 3" width="600" />

### Histogramme de l'âge des clients:
Cette représentation graphique permet d’identifier les différents segments de clientèles permettant de cibler d'éventuelles campagnes marketing.

<img src="../../../Travail-de-session-test-3/data/final/graphique4.png" alt="Graphique 4" width="600" />

### Histogramme du revenu annuel des clients
Ce graphique permet d’identifier le potentiel de revenu des clients pour d’éventuel campagne marketing

<img src="../../../Travail-de-session-test-3/data/final/graphique5.png" alt="Graphique 5" width="600" />

### Graphique à points de la valeur actuelle du portefeuille par rapport au revenu des clients
Ce graphique permettra à l’organisation financière d’identifier les clients à fort potentiel de développement afin de leurs offrir une offre de services de meilleurs qualités et des titres correspondant à leurs besoins et leurs objectifs respectifs. 

<img src="../../../Travail-de-session-test-3/data/final/graphique6.png" alt="Graphique 6" width="600" />

### Graphique à pointes de la valeur totale des titres sous gestion par industrie
Ce graphique permettra de produire des rapports de performance de l'investissement par industrie et afin de proposer des ajustements de portefeuille.

<img src="../../../Travail-de-session-test-3/data/final/graphique7.png" alt="Graphique 7" width="600" />

### Graphique à barres de la valeur totale du portefeuille d'investissement par profession 
Ce graphique permettra aux analystes financiers d’établir des modèles des placements par profession, ce qui leur permettra de présenter des options de titres financiers que les clients sont plus susceptibles d’aimer.

<img src="../../../Travail-de-session-test-3/data/final/graphique8.png" alt="Graphique 8" width="600" />

### Graphique à pointes du nombre de clients par produit financiers
Ce graphique permettra d’évaluer la popularité des produits financiers. Grâce à cette analyse les conseillers financiers seront en mesure d’ajuster les stratégies de placement de marketing pour leurs clients.

<img src="../../../Travail-de-session-test-3/data/final/graphique9.png" alt="Graphique 9" width="600" />

### Graphique à pointe montrant les pourcentages de la valeur totale sous gestion par industrie
Ce graphique permettra d’évaluer la performance des produits financiers dans les différents secteurs d’industrie permettant au conseiller financier d’être au courant de l’évolution des marchés et de pouvoir orienter leurs clients dans la meilleure directions selon leurs besoins. 

<img src="../../../Travail-de-session-test-3/data/final/graphique10.png" alt="Graphique 10" width="600" />

### Histogramme des 10 titres les plus populaires
Ce graphique permettra d’évaluer la popularité des titres. De cette façon, il sera possible pour les conseiller financer d’être au courant des tendances afin de pouvoir mieux conseiller leurs clients.  

<img src="../../../Travail-de-session-test-3/data/final/graphique11.png" alt="Graphique 11" width="600" />

## Quelques statistiques:
#### Statistiques descriptives :
- Revenu annuel : Moyenne de 185,747 $ avec un écart type de 65,710 $, indiquant une variation significative dans les revenus des clients.
- Passif et Dettes : Moyenne de passif est de 46,246 $ et de dettes est de 143,447 $.
- Actif : Moyenne d'environ 580,242 $, suggérant que beaucoup de clients ont des actifs substantiels.
- Épargne : Moyenne d'épargne à 288,795 $, avec certains clients ayant jusqu'à 658,853 $ en épargne.
#### Professions les plus courantes :
- Ingénieur : 16
- Pharmacien et Comptable : 11 chacun
- Avocat, Infirmière  et Entrepreneur : 9 chacun

Ces informations montrent une diversité dans les professions des clients, avec une concentration notable dans des secteurs technologiques et médicaux.

##### ** Ces informations on été tirée du documents excel obtenu à la phase deux

## Résultats:
 Les analyses réalisées montrent une concentration des investissements dans certaines industries. Cette analyse pourrait démontrer une stratégie d'investissement de façon excessivement ciblée pouvant mener à certains risques comme une exposition sectorielle. La popularité des titres spécifiques peut également indiquer les tendances du marché ou les préférences des investisseurs.
 
## Recommendations:
Notre première recommandation serait d’opter pour une plus grande diversification de la stratégie d'investissement afin d’offrir aux clients des options de portefeuilles plus diversifiés à l’abri des risques sectoriels. Deuxièmement, l’utilisation de techniques de segmentation avancée pourrait permettre à l’entreprise de mieux comprendre les divers groupes de clients et leurs préférences en matière d’investissement. De cette façon, il serait possible pour Summit Investment d’offrir des services beaucoup plus personnalisés comportant des stratégies d’approche et des offres de produits différentes pour chaque segments de clientèle. Cela permettrait d’augmenter de manière significative la satisfaction client. Pour terminer, la mise en œuvre de modèles prédictifs pourrait être une valeur ajoutée intéressante pour l’entreprise. La création de modèles prédictifs pourrait permettre d’identifier les tendances des performances des titres financiers et d’ajuster les portefeuilles en conséquence.  Cela peut inclure des modèles de régression pour prévoir les rendements futurs ou des modèles de classification pour déterminer les niveaux de risque des divers actifs.

## Conclusion:
 Ce projet a permis de mettre en lumière des aspects clés de la gestion des portefeuilles et des stratégies d'investissement chez Summit Investment. Les analyses effectuées offrent des pistes pour améliorer les décisions d'investissement et la gestion des risques afin d’offrir une meilleure offre de services à leurs clients.
