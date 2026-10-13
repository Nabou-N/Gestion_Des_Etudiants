# Cours complet : pandas + openpyxl avec un fichier Excel de gestion de stock

**Base de travail :** `stock_boutique_simule.xlsx`  
**Public :** étudiants ayant déjà des bases en Python  
**Objectif général :** maîtriser pandas pour lire, nettoyer, analyser, transformer et exporter des données Excel ; utiliser openpyxl pour mettre en forme et automatiser des classeurs Excel.

---
# Table des matières détaillée – Cours pandas + openpyxl

0. **Structure du fichier utilisé**

1. **Installation et environnement**
   - 1.1 Créer un environnement Python
   - 1.2 Import standard

2. **Lecture du fichier Excel avec pandas**
   - 2.1 Définir le chemin du fichier
   - 2.2 Lire la liste des feuilles
   - 2.3 Lire une feuille
   - 2.4 Lire plusieurs feuilles en une seule instruction

3. **Comprendre les objets pandas**
   - 3.1 Series
   - 3.2 DataFrame
   - 3.3 Méthodes d’inspection essentielles

4. **Types de colonnes : quantitatif, qualitatif, datetime**
   - 4.1 Types statistiques
   - 4.2 Vérifier les types pandas
   - 4.3 Nettoyer les noms de colonnes
   - 4.4 Convertir les dates
   - 4.5 Convertir les colonnes qualitatives en catégories
   - 4.6 Convertir proprement en numérique

5. **Sélection de données : colonnes, lignes, `loc`, `iloc`**
   - 5.1 Sélectionner une colonne
   - 5.2 Sélectionner plusieurs colonnes
   - 5.3 Sélection par position avec `iloc`
   - 5.4 Sélection par étiquette avec `loc`
   - 5.5 Filtrage avec masque booléen
   - 5.6 Plusieurs conditions
   - 5.7 Modification propre avec `loc`

6. **Trier les données**
   - 6.1 Trier par prix
   - 6.2 Trier par catégorie puis prix
   - 6.3 Réinitialiser l’index

7. **Valeurs manquantes et doublons**
   - 7.1 Repérer les valeurs manquantes
   - 7.2 Voir les lignes incomplètes
   - 7.3 Supprimer les lignes incomplètes
   - 7.4 Remplacer les valeurs manquantes
   - 7.5 Doublons

8. **Statistiques descriptives**
   - 8.1 `describe`
   - 8.2 Moyenne, médiane, variance, écart-type
   - 8.3 Quartiles et intervalle interquartile
   - 8.4 Détection simple des valeurs atypiques par IQR

9. **Créer et modifier des colonnes**
   - 9.1 Calculer une colonne
   - 9.2 Vérifier l’écart entre une colonne existante et une colonne recalculée
   - 9.3 Créer une colonne conditionnelle avec `np.where`
   - 9.4 Plusieurs conditions avec `np.select`

10. **Regroupements avec `groupby` et `agg`**
    - 10.1 Quantité totale entrée par catégorie
    - 10.2 Sorties par catégorie
    - 10.3 Agrégation par référence
    - 10.4 Plusieurs statistiques sur une même colonne

11. **Fusionner des tables avec `merge`**
    - 11.1 Principe
    - 11.2 Fusionner les entrées et sorties par référence
    - 11.3 Fusionner avec la liste des marchandises
    - 11.4 Recalculer le stock final
    - 11.5 Utiliser `indicator=True`

12. **Concaténer proprement avec `pd.concat`**
    - 12.1 Concaténer entrées et sorties
    - 12.2 Éviter les avertissements liés aux DataFrames vides ou colonnes entièrement NA

13. **Tableaux croisés et pivot**
    - 13.1 Chiffre d’affaires par mois et catégorie
    - 13.2 Quantités mensuelles vendues
    - 13.3 Transformer un tableau large en tableau long avec `melt`

14. **Manipulation des dates**
    - 14.1 Extraire année, mois, jour
    - 14.2 Grouper par mois
    - 14.3 Fenêtre glissante

15. **Exporter vers Excel avec pandas**
    - 15.1 Export simple
    - 15.2 Exporter plusieurs feuilles
    - 15.3 Exporter sans index

16. **Visualisation rapide avec pandas / matplotlib**
    - 16.1 Barres : chiffre d’affaires par catégorie
    - 16.2 Courbe temporelle

17. **OpenPyXL : manipulation directe d’un fichier Excel**
    - 17.1 Quand utiliser pandas et quand utiliser openpyxl ?
    - 17.2 Lire un classeur
    - 17.3 Sélectionner une feuille
    - 17.4 Lire et écrire une cellule
    - 17.5 Parcourir des lignes
    - 17.6 Sauvegarder

18. **Mise en forme Excel avec openpyxl**
    - 18.1 Styles de base
    - 18.2 Ajuster les largeurs de colonnes
    - 18.3 Figer la première ligne
    - 18.4 Ajouter un filtre automatique
    - 18.5 Format monétaire

19. **Formules Excel avec openpyxl**
    - 19.1 Ajouter une feuille de synthèse

20. **Graphique Excel avec openpyxl**
    - *(aucun sous‑titre)*

21. **Validation de données avec openpyxl**
    - *(aucun sous‑titre)*

22. **Mini-projet complet : générer un rapport de stock**
    - Objectif et script complet intégré

23. **Bonnes pratiques pandas modernes**
    - 23.1 Éviter `inplace=True`
    - 23.2 Éviter les modifications chaînées
    - 23.3 Éviter `append`
    - 23.4 Utiliser des arguments nommés
    - 23.5 Toujours contrôler le résultat d’un `merge`

24. **Exercices progressifs**
    - Exercice 1 — Lecture et inspection
    - Exercice 2 — Nettoyage
    - Exercice 3 — Filtrage
    - Exercice 4 — Statistiques
    - Exercice 5 — GroupBy
    - Exercice 6 — Merge
    - Exercice 7 — Pivot table
    - Exercice 8 — Rapport Excel

25. **Projet final noté**
    - Sujet
    - Travail demandé
    - Barème sur 20

26. **Résumé des syntaxes essentielles**
    - *(bloc de code récapitulatif)*
---

## 0. Structure du fichier utilisé

Le fichier contient quatre feuilles :

| Feuille | Nombre de lignes | Colonnes principales | Rôle pédagogique |
|---|---:|---|---|
| `Liste des marchandises` | 500 | `Reference`, `Designation`, `Categorie`, `Seuil d'alerte`, `Unite`, `Stock initial`, `Prix Unitaire`, `Total` | Table de référence des produits |
| `Entrees` | 800 | `Date`, `Reference`, `Designation`, `Categorie`, `Prix Unitaire`, `Quantite`, `Total`, `Type` | Mouvements d'entrée en stock |
| `Sorties` | 900 | mêmes colonnes que `Entrees` | Mouvements de sortie / ventes |
| `Inventaire` | 500 | `reference`, `designation`, `categorie`, `seuil d'alerte`, `stock initial`, `entrees`, `sorties`, `stock final`, `valeur`, `statut` | État calculé du stock |

Dans ce cours, on va apprendre à :

- lire un fichier Excel complet ;
- inspecter les feuilles et les colonnes ;
- corriger les types de données ;
- sélectionner avec `loc`, `iloc`, `at`, `iat` ;
- filtrer, trier, nettoyer ;
- calculer des statistiques descriptives ;
- grouper avec `groupby` et `agg` ;
- fusionner des tables avec `merge` ;
- concaténer proprement avec `pd.concat` ;
- créer des tableaux croisés avec `pivot_table` ;
- manipuler les dates ;
- exporter vers Excel ;
- améliorer le fichier Excel avec openpyxl : styles, largeurs, filtres, formules, graphiques, validation de données.

Références principales utilisées pour garder les syntaxes à jour : documentation officielle pandas 3.0.x et openpyxl 3.1.x :

- https://pandas.pydata.org/docs/
- https://pandas.pydata.org/docs/whatsnew/v3.0.0.html
- https://openpyxl.readthedocs.io/en/3.1/

---

## 1. Installation et environnement

### 1.1 Créer un environnement Python

```bash
python -m venv .venv
```

Sous Windows :

```bash
.venv\Scripts\activate
```

Sous Linux / macOS :

```bash
source .venv/bin/activate
```

Installer les bibliothèques :

```bash
python -m pip install --upgrade pip
python -m pip install pandas openpyxl matplotlib numpy
```

### 1.2 Import standard

```python
from pathlib import Path

import numpy as np
import pandas as pd
```

Convention :

```python
pd.set_option("display.max_columns", None)
pd.set_option("display.width", 120)
```

`pandas` sert à manipuler les données sous forme de tableaux. `openpyxl` sert à manipuler directement les fichiers Excel `.xlsx` : cellules, styles, feuilles, formules, graphiques.

---

## 2. Lecture du fichier Excel avec pandas

### 2.1 Définir le chemin du fichier

```python
FICHIER = Path("stock_boutique_simule(1).xlsx")
```

### 2.2 Lire la liste des feuilles

```python
xls = pd.ExcelFile(FICHIER, engine="openpyxl")
print(xls.sheet_names)
```

Résultat attendu :

```python
['Liste des marchandises', 'Entrees', 'Sorties', 'Inventaire']
```

### 2.3 Lire une feuille

```python
marchandises = pd.read_excel(
    FICHIER,
    sheet_name="Liste des marchandises",
    engine="openpyxl",
)

print(marchandises.head())
```

### 2.4 Lire plusieurs feuilles en une seule instruction

```python
feuilles = pd.read_excel(
    FICHIER,
    sheet_name=None,
    engine="openpyxl",
)

marchandises = feuilles["Liste des marchandises"]
entrees = feuilles["Entrees"]
sorties = feuilles["Sorties"]
inventaire = feuilles["Inventaire"]
```

`sheet_name=None` renvoie un dictionnaire : les clés sont les noms des feuilles, les valeurs sont les DataFrames.

---

## 3. Comprendre les objets pandas

### 3.1 Series

Une `Series` est une colonne pandas : une suite de valeurs avec un index.

```python
prix = marchandises["Prix Unitaire"]
print(type(prix))
print(prix.head())
```

### 3.2 DataFrame

Un `DataFrame` est un tableau à deux dimensions : lignes + colonnes.

```python
print(type(marchandises))
print(marchandises.shape)
print(marchandises.columns)
print(marchandises.index)
```

### 3.3 Méthodes d’inspection essentielles

```python
marchandises.head()       # premières lignes
marchandises.tail()       # dernières lignes
marchandises.sample(5)    # 5 lignes au hasard
marchandises.info()       # colonnes, types, valeurs manquantes
marchandises.describe()   # statistiques des colonnes numériques
```

Pour inclure aussi les colonnes qualitatives :

```python
marchandises.describe(include="all")
```

---

## 4. Types de colonnes : quantitatif, qualitatif, datetime

### 4.1 Types statistiques

Dans le fichier :

| Type statistique | Exemple | Interprétation |
|---|---|---|
| Quantitative discrète | `Stock initial`, `Quantite`, `stock final` | nombre entier comptable |
| Quantitative continue | `Prix Unitaire`, `Total`, `valeur` | valeur numérique mesurable |
| Qualitative nominale | `Reference`, `Designation`, `Categorie`, `statut` | texte ou catégorie sans ordre naturel |
| Date / temps | `Date` | variable temporelle |

### 4.2 Vérifier les types pandas

```python
print(entrees.dtypes)
```

Dans le fichier fourni, les dates sont souvent lues comme texte. Il faut donc les convertir.

### 4.3 Nettoyer les noms de colonnes

Il est fréquent que les fichiers Excel contiennent des espaces, accents ou casses différentes. Pour unifier :

```python
def nettoyer_colonnes(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_", regex=False)
        .str.replace("'", "", regex=False)
    )
    return df

marchandises_clean = nettoyer_colonnes(marchandises)
print(marchandises_clean.columns)
```

Exemple : `Prix Unitaire` devient `prix_unitaire`, `Seuil d'alerte` devient `seuil_dalerte`.

### 4.4 Convertir les dates

```python
entrees["Date"] = pd.to_datetime(
    entrees["Date"],
    format="%Y-%m-%d",
    errors="coerce",
)

sorties["Date"] = pd.to_datetime(
    sorties["Date"],
    format="%Y-%m-%d",
    errors="coerce",
)
```

`errors="coerce"` transforme les dates invalides en `NaT`, l’équivalent temporel de `NaN`.

### 4.5 Convertir les colonnes qualitatives en catégories

```python
for df in [marchandises, entrees, sorties]:
    df["Categorie"] = df["Categorie"].astype("category")
```

Avantages :

- mémoire réduite ;
- catégories contrôlées ;
- regroupements plus propres.

### 4.6 Convertir proprement en numérique

```python
entrees["Quantite"] = pd.to_numeric(entrees["Quantite"], errors="coerce")
entrees["Prix Unitaire"] = pd.to_numeric(entrees["Prix Unitaire"], errors="coerce")
entrees["Total"] = pd.to_numeric(entrees["Total"], errors="coerce")
```

---

## 5. Sélection de données : colonnes, lignes, `loc`, `iloc`

### 5.1 Sélectionner une colonne

```python
marchandises["Reference"]
```

### 5.2 Sélectionner plusieurs colonnes

```python
marchandises[["Reference", "Designation", "Categorie", "Prix Unitaire"]]
```

### 5.3 Sélection par position avec `iloc`

`iloc` sélectionne par position entière : ligne 0, ligne 1, colonne 0, etc.

```python
marchandises.iloc[0]          # première ligne
marchandises.iloc[0:5]        # cinq premières lignes
marchandises.iloc[0:5, 0:3]   # 5 premières lignes, 3 premières colonnes
marchandises.iloc[:, [0, 2, 6]]
```

À retenir : avec `iloc`, la borne de fin est exclue, comme dans les slices Python.

### 5.4 Sélection par étiquette avec `loc`

`loc` sélectionne par nom d’index ou par nom de colonne.

```python
marchandises.loc[0, "Reference"]
marchandises.loc[0:4, ["Reference", "Categorie", "Prix Unitaire"]]
```

À retenir : avec `loc`, quand l’index est numérique, `0:4` inclut la ligne d’index 4.

### 5.5 Filtrage avec masque booléen

```python
smartphones = marchandises.loc[marchandises["Categorie"] == "Smartphone"]
```

Autres exemples :

```python
produits_chers = marchandises.loc[marchandises["Prix Unitaire"] >= 1_000_000]

stock_faible = inventaire.loc[inventaire["statut"] == "stock faible"]

sorties_grandes_quantites = sorties.loc[sorties["Quantite"] >= 100]
```

### 5.6 Plusieurs conditions

```python
condition = (
    (marchandises["Categorie"] == "Smartphone")
    & (marchandises["Prix Unitaire"] >= 1_000_000)
)

smartphones_chers = marchandises.loc[condition]
```

Avec `|` pour OU :

```python
condition = (
    (marchandises["Categorie"] == "Smartphone")
    | (marchandises["Categorie"] == "Electromenager")
)
selection = marchandises.loc[condition]
```

Toujours mettre chaque condition entre parenthèses.

### 5.7 Modification propre avec `loc`

À éviter :

```python
# À éviter : risque de SettingWithCopyWarning
inventaire[inventaire["stock final"] < 0]["statut"] = "anomalie"
```

À faire :

```python
inventaire.loc[inventaire["stock final"] < 0, "statut"] = "anomalie"
```

---

## 6. Trier les données

### 6.1 Trier par prix

```python
marchandises.sort_values(
    by="Prix Unitaire",
    ascending=False,
).head(10)
```

### 6.2 Trier par catégorie puis prix

```python
marchandises.sort_values(
    by=["Categorie", "Prix Unitaire"],
    ascending=[True, False],
)
```

### 6.3 Réinitialiser l’index

```python
classement = marchandises.sort_values("Prix Unitaire", ascending=False).reset_index(drop=True)
```

---

## 7. Valeurs manquantes et doublons

### 7.1 Repérer les valeurs manquantes

```python
marchandises.isna().sum()
```

### 7.2 Voir les lignes incomplètes

```python
lignes_incompletes = marchandises.loc[marchandises.isna().any(axis=1)]
```

### 7.3 Supprimer les lignes incomplètes

```python
marchandises_sans_na = marchandises.dropna()
```

### 7.4 Remplacer les valeurs manquantes

```python
marchandises["Prix Unitaire"] = marchandises["Prix Unitaire"].fillna(0)
```

Pour une variable qualitative :

```python
marchandises["Categorie"] = marchandises["Categorie"].fillna("Non classé")
```

### 7.5 Doublons

```python
marchandises.duplicated().sum()
marchandises.duplicated(subset=["Reference"]).sum()
```

Supprimer les doublons :

```python
marchandises_uniques = marchandises.drop_duplicates(subset=["Reference"], keep="first")
```

---

## 8. Statistiques descriptives

### 8.1 `describe`

```python
inventaire[["stock final", "valeur"]].describe()
```

Les indicateurs usuels :

| Indicateur | Signification |
|---|---|
| `count` | nombre de valeurs non manquantes |
| `mean` | moyenne arithmétique |
| `std` | écart-type, dispersion autour de la moyenne |
| `min` | minimum |
| `25%` | premier quartile Q1 |
| `50%` | médiane Q2 |
| `75%` | troisième quartile Q3 |
| `max` | maximum |

### 8.2 Moyenne, médiane, variance, écart-type

```python
stock = inventaire["stock final"]

moyenne = stock.mean()
mediane = stock.median()
variance = stock.var()
ecart_type = stock.std()
minimum = stock.min()
maximum = stock.max()
```

Définitions rapides :

- **Moyenne** : somme des valeurs divisée par le nombre de valeurs.
- **Médiane** : valeur centrale lorsque les données sont triées. Elle sépare la série en deux parties de même effectif.
- **Variance** : moyenne des carrés des écarts à la moyenne. Elle mesure la dispersion.
- **Écart-type** : racine carrée de la variance. Il s’exprime dans la même unité que les données.

### 8.3 Quartiles et intervalle interquartile

```python
q1 = stock.quantile(0.25)
q2 = stock.quantile(0.50)
q3 = stock.quantile(0.75)
iqr = q3 - q1
```

Définition :

- Q1 : 25 % des valeurs sont inférieures ou égales à Q1.
- Q2 : médiane.
- Q3 : 75 % des valeurs sont inférieures ou égales à Q3.
- **IQR** ou intervalle interquartile : `Q3 - Q1`. Il mesure la dispersion de la moitié centrale des données.

### 8.4 Détection simple des valeurs atypiques par IQR

```python
borne_basse = q1 - 1.5 * iqr
borne_haute = q3 + 1.5 * iqr

valeurs_atypiques = inventaire.loc[
    (inventaire["stock final"] < borne_basse)
    | (inventaire["stock final"] > borne_haute)
]
```

---

## 9. Créer et modifier des colonnes

### 9.1 Calculer une colonne

```python
marchandises["Total_recalcule"] = (
    marchandises["Stock initial"] * marchandises["Prix Unitaire"]
)
```

### 9.2 Vérifier l’écart entre une colonne existante et une colonne recalculée

```python
marchandises["Ecart_total"] = marchandises["Total"] - marchandises["Total_recalcule"]
```

### 9.3 Créer une colonne conditionnelle avec `np.where`

```python
inventaire["alerte"] = np.where(
    inventaire["stock final"] <= inventaire["seuil d'alerte"],
    "Alerte",
    "OK",
)
```

### 9.4 Plusieurs conditions avec `np.select`

```python
conditions = [
    inventaire["stock final"] < 0,
    inventaire["stock final"] <= inventaire["seuil d'alerte"],
    inventaire["stock final"] > inventaire["seuil d'alerte"],
]
choix = ["stock négatif", "stock faible", "stock normal"]

inventaire["statut_recalcule"] = np.select(
    conditions,
    choix,
    default="non défini",
)
```

---

## 10. Regroupements avec `groupby` et `agg`

### 10.1 Quantité totale entrée par catégorie

```python
entrees_par_categorie = entrees.groupby(
    "Categorie",
    as_index=False,
    observed=True,
).agg(
    quantite_entree=("Quantite", "sum"),
    valeur_entree=("Total", "sum"),
    prix_moyen=("Prix Unitaire", "mean"),
    nombre_operations=("Reference", "count"),
)
```

`as_index=False` donne un résultat lisible comme en SQL. `observed=True` est recommandé lorsqu’on travaille avec des colonnes catégorielles.

### 10.2 Sorties par catégorie

```python
sorties_par_categorie = sorties.groupby(
    "Categorie",
    as_index=False,
    observed=True,
).agg(
    quantite_sortie=("Quantite", "sum"),
    chiffre_affaires=("Total", "sum"),
    nombre_ventes=("Reference", "count"),
)
```

### 10.3 Agrégation par référence

```python
entrees_ref = entrees.groupby(
    "Reference",
    as_index=False,
).agg(
    entrees=("Quantite", "sum"),
    valeur_entrees=("Total", "sum"),
)

sorties_ref = sorties.groupby(
    "Reference",
    as_index=False,
).agg(
    sorties=("Quantite", "sum"),
    valeur_sorties=("Total", "sum"),
)
```

### 10.4 Plusieurs statistiques sur une même colonne

```python
stats_stock_categorie = inventaire.groupby(
    "categorie",
    as_index=False,
).agg(
    stock_min=("stock final", "min"),
    stock_moyen=("stock final", "mean"),
    stock_median=("stock final", "median"),
    stock_max=("stock final", "max"),
    valeur_totale=("valeur", "sum"),
)
```

---

## 11. Fusionner des tables avec `merge`

### 11.1 Principe

`merge` permet de joindre deux DataFrames comme dans une base de données SQL.

Types de jointure :

| Type | Code | Sens |
|---|---|---|
| interne | `how="inner"` | garder seulement les clés présentes dans les deux tables |
| gauche | `how="left"` | garder toutes les lignes de gauche |
| droite | `how="right"` | garder toutes les lignes de droite |
| externe | `how="outer"` | garder toutes les clés des deux tables |

### 11.2 Fusionner les entrées et sorties par référence

```python
mouvements_ref = pd.merge(
    entrees_ref,
    sorties_ref,
    on="Reference",
    how="outer",
    validate="one_to_one",
)

mouvements_ref[["entrees", "sorties", "valeur_entrees", "valeur_sorties"]] = (
    mouvements_ref[["entrees", "sorties", "valeur_entrees", "valeur_sorties"]]
    .fillna(0)
)
```

`validate="one_to_one"` vérifie qu’il n’y a qu’une ligne par référence dans chaque table agrégée. C’est une bonne pratique pour éviter des erreurs silencieuses.

### 11.3 Fusionner avec la liste des marchandises

```python
base_stock = pd.merge(
    marchandises,
    mouvements_ref,
    on="Reference",
    how="left",
    validate="one_to_one",
)

base_stock[["entrees", "sorties"]] = base_stock[["entrees", "sorties"]].fillna(0)
```

### 11.4 Recalculer le stock final

```python
base_stock["stock_final_recalcule"] = (
    base_stock["Stock initial"]
    + base_stock["entrees"]
    - base_stock["sorties"]
)
```

### 11.5 Utiliser `indicator=True`

```python
controle = pd.merge(
    marchandises[["Reference"]],
    mouvements_ref[["Reference"]],
    on="Reference",
    how="outer",
    indicator=True,
)

controle["_merge"].value_counts()
```

`_merge` indique si la référence vient de la table gauche, droite ou des deux.

---

## 12. Concaténer proprement avec `pd.concat`

### 12.1 Concaténer entrées et sorties

On veut créer une seule table des mouvements.

```python
colonnes_mouvements = [
    "Date", "Reference", "Designation", "Categorie",
    "Prix Unitaire", "Quantite", "Total", "Type",
]

frames = [
    entrees.loc[:, colonnes_mouvements],
    sorties.loc[:, colonnes_mouvements],
]

mouvements = pd.concat(
    frames,
    axis=0,
    ignore_index=True,
    sort=False,
)
```

### 12.2 Éviter les avertissements liés aux DataFrames vides ou colonnes entièrement NA

Dans pandas 3.0, `concat()` ne traite plus les objets vides ou entièrement NA comme certaines anciennes versions. Bonne pratique : filtrer avant de concaténer.

```python
def dataframe_utilisable(df: pd.DataFrame) -> bool:
    return not df.empty and not df.dropna(axis=1, how="all").empty

frames_valides = [
    df.dropna(axis=1, how="all")
    for df in frames
    if dataframe_utilisable(df)
]

if frames_valides:
    mouvements = pd.concat(
        frames_valides,
        axis=0,
        ignore_index=True,
        sort=False,
    )
else:
    mouvements = pd.DataFrame(columns=colonnes_mouvements)
```

À éviter :

```python
# Mauvaise pratique : concaténer ligne par ligne dans une boucle
resultat = pd.DataFrame()
for ligne in liste_lignes:
    resultat = pd.concat([resultat, pd.DataFrame([ligne])])
```

À faire :

```python
resultat = pd.DataFrame(liste_lignes)
```

ou :

```python
frames = []
for bloc in blocs:
    frames.append(bloc)

resultat = pd.concat(frames, ignore_index=True) if frames else pd.DataFrame()
```

---

## 13. Tableaux croisés et pivot

### 13.1 Chiffre d’affaires par mois et catégorie

```python
mouvements["Date"] = pd.to_datetime(mouvements["Date"], errors="coerce")

sorties_only = mouvements.loc[mouvements["Type"] == "Sortie"].copy()
sorties_only["mois"] = sorties_only["Date"].dt.to_period("M").astype(str)

ca_mensuel = pd.pivot_table(
    sorties_only,
    index="mois",
    columns="Categorie",
    values="Total",
    aggfunc="sum",
    fill_value=0,
    observed=True,
)
```

### 13.2 Quantités mensuelles vendues

```python
qte_mensuelle = pd.pivot_table(
    sorties_only,
    index="mois",
    columns="Categorie",
    values="Quantite",
    aggfunc="sum",
    fill_value=0,
    observed=True,
)
```

### 13.3 Transformer un tableau large en tableau long avec `melt`

```python
ca_mensuel_long = ca_mensuel.reset_index().melt(
    id_vars="mois",
    var_name="Categorie",
    value_name="Chiffre_affaires",
)
```

---

## 14. Manipulation des dates

### 14.1 Extraire année, mois, jour

```python
entrees["Date"] = pd.to_datetime(entrees["Date"], errors="coerce")

entrees["annee"] = entrees["Date"].dt.year
entrees["mois"] = entrees["Date"].dt.month
entrees["jour"] = entrees["Date"].dt.day
entrees["nom_jour"] = entrees["Date"].dt.day_name()
```

### 14.2 Grouper par mois

```python
entrees_mois = entrees.groupby(
    pd.Grouper(key="Date", freq="ME"),
    as_index=True,
).agg(
    quantite_entree=("Quantite", "sum"),
    valeur_entree=("Total", "sum"),
)
```

Remarque importante : dans pandas 3.0, plusieurs anciens alias de fréquence ont été remplacés. Pour fin de mois, utiliser `ME` plutôt que l’ancien alias `M`.

### 14.3 Fenêtre glissante

```python
sorties_jour = sorties.groupby("Date", as_index=False).agg(
    chiffre_affaires=("Total", "sum")
).sort_values("Date")

sorties_jour["ca_mobile_7j"] = (
    sorties_jour["chiffre_affaires"]
    .rolling(window=7, min_periods=1)
    .mean()
)
```

---

## 15. Exporter vers Excel avec pandas

### 15.1 Export simple

```python
sorties_par_categorie.to_excel(
    "sorties_par_categorie.xlsx",
    index=False,
    engine="openpyxl",
)
```

### 15.2 Exporter plusieurs feuilles

```python
with pd.ExcelWriter("rapport_stock.xlsx", engine="openpyxl") as writer:
    marchandises.to_excel(writer, sheet_name="Marchandises", index=False)
    mouvements.to_excel(writer, sheet_name="Mouvements", index=False)
    sorties_par_categorie.to_excel(writer, sheet_name="Sorties categorie", index=False)
    ca_mensuel.to_excel(writer, sheet_name="CA mensuel")
```

Bonne pratique pandas 3 : utiliser des arguments nommés, par exemple `sheet_name=...`, `index=False`, `engine=...`.

### 15.3 Exporter sans index

```python
df.to_excel("fichier.xlsx", index=False)
```

La plupart du temps, pour des tableaux destinés à Excel, on met `index=False`, sauf si l’index a un sens métier.

---

## 16. Visualisation rapide avec pandas / matplotlib

### 16.1 Barres : chiffre d’affaires par catégorie

```python
import matplotlib.pyplot as plt

ax = sorties_par_categorie.plot.bar(
    x="Categorie",
    y="chiffre_affaires",
    legend=False,
    title="Chiffre d'affaires par catégorie",
)
ax.set_xlabel("Catégorie")
ax.set_ylabel("Chiffre d'affaires")
plt.tight_layout()
plt.show()
```

### 16.2 Courbe temporelle

```python
ax = sorties_jour.plot.line(
    x="Date",
    y="chiffre_affaires",
    title="Chiffre d'affaires journalier",
)
ax.set_xlabel("Date")
ax.set_ylabel("Chiffre d'affaires")
plt.tight_layout()
plt.show()
```

---

## 17. OpenPyXL : manipulation directe d’un fichier Excel

### 17.1 Quand utiliser pandas et quand utiliser openpyxl ?

| Besoin | Outil recommandé |
|---|---|
| Lire des données, filtrer, grouper, fusionner | pandas |
| Faire des statistiques et analyses | pandas |
| Exporter rapidement un tableau | pandas |
| Formater précisément un fichier Excel | openpyxl |
| Ajouter styles, couleurs, filtres, largeurs, formules, graphiques | openpyxl |
| Modifier une cellule précise dans un classeur existant | openpyxl |

### 17.2 Lire un classeur

```python
from openpyxl import load_workbook

wb = load_workbook("rapport_stock.xlsx")
print(wb.sheetnames)
```

### 17.3 Sélectionner une feuille

```python
ws = wb["Sorties categorie"]
```

### 17.4 Lire et écrire une cellule

```python
print(ws["A1"].value)
ws["A1"] = "Catégorie"
```

Autre syntaxe :

```python
ws.cell(row=1, column=1, value="Catégorie")
```

### 17.5 Parcourir des lignes

```python
for row in ws.iter_rows(min_row=1, max_row=5, values_only=True):
    print(row)
```

### 17.6 Sauvegarder

```python
wb.save("rapport_stock_formate.xlsx")
```

---

## 18. Mise en forme Excel avec openpyxl

### 18.1 Styles de base

```python
from openpyxl.styles import Font, PatternFill, Border, Side, Alignment

header_fill = PatternFill(fill_type="solid", fgColor="1F4E78")
header_font = Font(color="FFFFFF", bold=True)
thin_side = Side(style="thin", color="D9E2F3")
thin_border = Border(left=thin_side, right=thin_side, top=thin_side, bottom=thin_side)

for cell in ws[1]:
    cell.fill = header_fill
    cell.font = header_font
    cell.alignment = Alignment(horizontal="center")
    cell.border = thin_border
```

### 18.2 Ajuster les largeurs de colonnes

```python
for column_cells in ws.columns:
    max_length = 0
    column_letter = column_cells[0].column_letter

    for cell in column_cells:
        value = "" if cell.value is None else str(cell.value)
        max_length = max(max_length, len(value))

    ws.column_dimensions[column_letter].width = min(max_length + 2, 35)
```

### 18.3 Figer la première ligne

```python
ws.freeze_panes = "A2"
```

### 18.4 Ajouter un filtre automatique

```python
ws.auto_filter.ref = ws.dimensions
```

### 18.5 Format monétaire

```python
for row in ws.iter_rows(min_row=2):
    for cell in row:
        if cell.column_letter in ["B", "C"]:
            cell.number_format = '#,##0'
```

---

## 19. Formules Excel avec openpyxl

### 19.1 Ajouter une feuille de synthèse

```python
ws_resume = wb.create_sheet("Résumé")
ws_resume["A1"] = "Indicateur"
ws_resume["B1"] = "Valeur"

ws_resume["A2"] = "Nombre de catégories"
ws_resume["B2"] = "=COUNTA('Sorties categorie'!A2:A100)"

ws_resume["A3"] = "Chiffre d'affaires total"
ws_resume["B3"] = "=SUM('Sorties categorie'!B2:B100)"
```

openpyxl écrit la formule dans le fichier. Le calcul final est généralement fait par Excel ou LibreOffice à l’ouverture du fichier.

---

## 20. Graphique Excel avec openpyxl

```python
from openpyxl.chart import BarChart, Reference

ws = wb["Sorties categorie"]

chart = BarChart()
chart.title = "Chiffre d'affaires par catégorie"
chart.x_axis.title = "Catégorie"
chart.y_axis.title = "Chiffre d'affaires"

data = Reference(ws, min_col=2, min_row=1, max_row=ws.max_row)
cats = Reference(ws, min_col=1, min_row=2, max_row=ws.max_row)

chart.add_data(data, titles_from_data=True)
chart.set_categories(cats)
chart.height = 8
chart.width = 16

ws.add_chart(chart, "E2")
```

---

## 21. Validation de données avec openpyxl

Exemple : créer une liste déroulante de statuts.

```python
from openpyxl.worksheet.datavalidation import DataValidation

ws = wb["Résumé"]

validation = DataValidation(
    type="list",
    formula1='"OK,Alerte,Anomalie"',
    allow_blank=False,
)

ws.add_data_validation(validation)
validation.add(ws["D2"])
ws["D1"] = "Statut choisi"
```

---

## 22. Mini-projet complet : générer un rapport de stock

### Objectif

À partir du fichier initial, produire un fichier `rapport_stock_final.xlsx` contenant :

1. une feuille `Marchandises` ;
2. une feuille `Mouvements` combinant entrées et sorties ;
3. une feuille `Synthèse catégorie` ;
4. une feuille `Inventaire recalculé` ;
5. une mise en forme professionnelle ;
6. un graphique du chiffre d’affaires par catégorie.

### Script complet

```python
from pathlib import Path

import numpy as np
import pandas as pd
from openpyxl import load_workbook
from openpyxl.chart import BarChart, Reference
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side

FICHIER_SOURCE = Path("stock_boutique_simule(1).xlsx")
FICHIER_SORTIE = Path("rapport_stock_final.xlsx")

# 1. Lecture
feuilles = pd.read_excel(FICHIER_SOURCE, sheet_name=None, engine="openpyxl")
marchandises = feuilles["Liste des marchandises"].copy()
entrees = feuilles["Entrees"].copy()
sorties = feuilles["Sorties"].copy()

# 2. Conversion des dates
for df in [entrees, sorties]:
    df["Date"] = pd.to_datetime(df["Date"], format="%Y-%m-%d", errors="coerce")
    df["Categorie"] = df["Categorie"].astype("category")

# 3. Table mouvements
colonnes_mouvements = [
    "Date", "Reference", "Designation", "Categorie",
    "Prix Unitaire", "Quantite", "Total", "Type",
]

frames = [
    entrees.loc[:, colonnes_mouvements],
    sorties.loc[:, colonnes_mouvements],
]

frames_valides = [
    df.dropna(axis=1, how="all")
    for df in frames
    if not df.empty and not df.dropna(axis=1, how="all").empty
]

mouvements = pd.concat(
    frames_valides,
    axis=0,
    ignore_index=True,
    sort=False,
) if frames_valides else pd.DataFrame(columns=colonnes_mouvements)

# 4. Synthèse catégorie
sorties_only = mouvements.loc[mouvements["Type"] == "Sortie"].copy()

synthese_categorie = sorties_only.groupby(
    "Categorie",
    as_index=False,
    observed=True,
).agg(
    quantite_sortie=("Quantite", "sum"),
    chiffre_affaires=("Total", "sum"),
    nombre_ventes=("Reference", "count"),
)

# 5. Stock recalculé par référence
entrees_ref = entrees.groupby("Reference", as_index=False).agg(
    entrees=("Quantite", "sum"),
)

sorties_ref = sorties.groupby("Reference", as_index=False).agg(
    sorties=("Quantite", "sum"),
)

mouvements_ref = pd.merge(
    entrees_ref,
    sorties_ref,
    on="Reference",
    how="outer",
    validate="one_to_one",
)

mouvements_ref[["entrees", "sorties"]] = mouvements_ref[["entrees", "sorties"]].fillna(0)

inventaire_recalcule = pd.merge(
    marchandises,
    mouvements_ref,
    on="Reference",
    how="left",
    validate="one_to_one",
)

inventaire_recalcule[["entrees", "sorties"]] = inventaire_recalcule[["entrees", "sorties"]].fillna(0)

inventaire_recalcule["stock_final"] = (
    inventaire_recalcule["Stock initial"]
    + inventaire_recalcule["entrees"]
    - inventaire_recalcule["sorties"]
)

inventaire_recalcule["valeur_stock"] = (
    inventaire_recalcule["stock_final"]
    * inventaire_recalcule["Prix Unitaire"]
)

inventaire_recalcule["statut"] = np.select(
    [
        inventaire_recalcule["stock_final"] < 0,
        inventaire_recalcule["stock_final"] <= inventaire_recalcule["Seuil d'alerte"],
    ],
    ["stock négatif", "stock faible"],
    default="stock normal",
)

# 6. Export pandas
with pd.ExcelWriter(FICHIER_SORTIE, engine="openpyxl") as writer:
    marchandises.to_excel(writer, sheet_name="Marchandises", index=False)
    mouvements.to_excel(writer, sheet_name="Mouvements", index=False)
    synthese_categorie.to_excel(writer, sheet_name="Synthèse catégorie", index=False)
    inventaire_recalcule.to_excel(writer, sheet_name="Inventaire recalculé", index=False)

# 7. Mise en forme openpyxl
wb = load_workbook(FICHIER_SORTIE)

header_fill = PatternFill(fill_type="solid", fgColor="1F4E78")
header_font = Font(color="FFFFFF", bold=True)
thin_side = Side(style="thin", color="D9E2F3")
thin_border = Border(left=thin_side, right=thin_side, top=thin_side, bottom=thin_side)

for ws in wb.worksheets:
    ws.freeze_panes = "A2"
    ws.auto_filter.ref = ws.dimensions

    for cell in ws[1]:
        cell.fill = header_fill
        cell.font = header_font
        cell.alignment = Alignment(horizontal="center", vertical="center")
        cell.border = thin_border

    for row in ws.iter_rows(min_row=2):
        for cell in row:
            cell.border = thin_border

    for column_cells in ws.columns:
        max_length = 0
        column_letter = column_cells[0].column_letter
        for cell in column_cells:
            value = "" if cell.value is None else str(cell.value)
            max_length = max(max_length, len(value))
        ws.column_dimensions[column_letter].width = min(max_length + 2, 35)

# Formats numériques sur la synthèse
ws = wb["Synthèse catégorie"]
for cell in ws["C"][1:]:
    cell.number_format = '#,##0'

# Graphique
chart = BarChart()
chart.title = "Chiffre d'affaires par catégorie"
chart.x_axis.title = "Catégorie"
chart.y_axis.title = "Chiffre d'affaires"

data = Reference(ws, min_col=3, min_row=1, max_row=ws.max_row)
cats = Reference(ws, min_col=1, min_row=2, max_row=ws.max_row)
chart.add_data(data, titles_from_data=True)
chart.set_categories(cats)
chart.height = 8
chart.width = 16
ws.add_chart(chart, "F2")

wb.save(FICHIER_SORTIE)
print(f"Rapport généré : {FICHIER_SORTIE}")
```

---

## 23. Bonnes pratiques pandas modernes

### 23.1 Éviter `inplace=True`

Préférer :

```python
df = df.drop(columns=["colonne_inutile"])
```

plutôt que :

```python
df.drop(columns=["colonne_inutile"], inplace=True)
```

Cela rend le code plus clair et plus compatible avec les évolutions de pandas.

### 23.2 Éviter les modifications chaînées

À éviter :

```python
df[df["stock final"] < 0]["statut"] = "anomalie"
```

À faire :

```python
df.loc[df["stock final"] < 0, "statut"] = "anomalie"
```

### 23.3 Éviter `append`

`DataFrame.append()` ne doit plus être utilisé. Utiliser `pd.concat` ou créer directement une liste de dictionnaires.

```python
lignes = [
    {"Reference": "SMP-9999", "Quantite": 10},
    {"Reference": "ELM-9999", "Quantite": 5},
]

df = pd.DataFrame(lignes)
```

### 23.4 Utiliser des arguments nommés

Préférer :

```python
df.to_excel("rapport.xlsx", sheet_name="Rapport", index=False, engine="openpyxl")
```

### 23.5 Toujours contrôler le résultat d’un `merge`

```python
resultat = pd.merge(
    gauche,
    droite,
    on="Reference",
    how="left",
    validate="one_to_one",
    indicator=True,
)

print(resultat["_merge"].value_counts())
```

---

## 24. Exercices progressifs

### Exercice 1 — Lecture et inspection

1. Lire toutes les feuilles du fichier Excel.
2. Afficher les 5 premières lignes de chaque feuille.
3. Afficher les types de colonnes.
4. Identifier les colonnes quantitatives, qualitatives et datetime.

### Exercice 2 — Nettoyage

1. Convertir les colonnes `Date` des feuilles `Entrees` et `Sorties` en datetime.
2. Convertir `Categorie` en type category.
3. Vérifier qu’il n’y a pas de valeurs manquantes.
4. Vérifier s’il existe des doublons sur `Reference` dans `Liste des marchandises`.

### Exercice 3 — Filtrage

1. Extraire tous les smartphones.
2. Extraire les produits dont le prix unitaire dépasse 1 000 000.
3. Extraire les mouvements dont la quantité dépasse 100.
4. Extraire les stocks faibles dans l’inventaire.

### Exercice 4 — Statistiques

1. Calculer moyenne, médiane, variance, écart-type du stock final.
2. Calculer Q1, Q3 et IQR.
3. Détecter les produits à stock final atypique.
4. Interpréter les résultats en 5 phrases.

### Exercice 5 — GroupBy

1. Calculer les quantités entrées par catégorie.
2. Calculer les quantités sorties par catégorie.
3. Calculer le chiffre d’affaires par catégorie.
4. Trouver la catégorie qui génère le plus de chiffre d’affaires.

### Exercice 6 — Merge

1. Agréger les entrées par référence.
2. Agréger les sorties par référence.
3. Fusionner avec la liste des marchandises.
4. Recalculer le stock final.
5. Comparer avec la feuille `Inventaire`.

### Exercice 7 — Pivot table

1. Créer un tableau croisé du chiffre d’affaires mensuel par catégorie.
2. Créer un tableau croisé des quantités vendues mensuelles par catégorie.
3. Exporter ces deux tableaux dans un fichier Excel.

### Exercice 8 — Rapport Excel

Créer un fichier `rapport_etudiant.xlsx` contenant :

- `Mouvements` ;
- `Synthèse catégorie` ;
- `Inventaire recalculé` ;
- `CA mensuel` ;
- un graphique Excel ;
- des en-têtes colorés ;
- des filtres automatiques ;
- la première ligne figée.

---

## 25. Projet final noté

### Sujet

Vous êtes chargé d’automatiser l’analyse d’un fichier de stock pour une boutique. À partir du fichier fourni, vous devez produire un rapport Excel propre et exploitable par un responsable de magasin.

### Travail demandé

1. Lire les quatre feuilles du classeur.
2. Nettoyer les types de colonnes.
3. Recalculer les entrées et sorties par référence.
4. Recalculer le stock final.
5. Identifier les anomalies : stock négatif, stock faible, valeur de stock négative.
6. Calculer les KPI suivants :
   - nombre total de produits ;
   - nombre de produits en stock faible ;
   - nombre de produits en stock négatif ;
   - valeur totale du stock ;
   - chiffre d’affaires total des sorties ;
   - catégorie la plus rentable.
7. Créer des synthèses par catégorie et par mois.
8. Exporter le rapport final dans Excel avec mise en forme openpyxl.
9. Ajouter au moins un graphique.
10. Rédiger une courte interprétation des résultats.

### Barème sur 20

| Critère | Points |
|---|---:|
| Lecture correcte du fichier | 2 |
| Nettoyage des types | 3 |
| Utilisation correcte de `loc`, filtres, tris | 2 |
| Statistiques descriptives | 2 |
| `groupby` / `agg` | 3 |
| `merge` et recalcul du stock | 3 |
| Export Excel multi-feuilles | 2 |
| Mise en forme openpyxl | 2 |
| Interprétation claire | 1 |

---

## 26. Résumé des syntaxes essentielles

```python
# Lecture
pd.read_excel("fichier.xlsx", sheet_name="Feuille", engine="openpyxl")
pd.read_excel("fichier.xlsx", sheet_name=None, engine="openpyxl")

# Inspection
df.head()
df.info()
df.describe()
df.dtypes
df.shape
df.columns

# Sélection
df["colonne"]
df[["col1", "col2"]]
df.loc[condition, ["col1", "col2"]]
df.iloc[0:5, 0:3]

# Nettoyage
df.isna().sum()
df.dropna()
df.fillna(0)
df.drop_duplicates(subset=["Reference"])
pd.to_datetime(df["Date"], errors="coerce")
pd.to_numeric(df["Prix"], errors="coerce")

# Statistiques
df.describe()
df["x"].mean()
df["x"].median()
df["x"].var()
df["x"].std()
df["x"].quantile(0.25)

# Groupement
df.groupby("Categorie", as_index=False).agg(total=("Total", "sum"))

# Fusion
pd.merge(df1, df2, on="Reference", how="left", validate="one_to_one")

# Concaténation
pd.concat([df1, df2], ignore_index=True, sort=False)

# Pivot
pd.pivot_table(df, index="mois", columns="Categorie", values="Total", aggfunc="sum", fill_value=0)

# Export
with pd.ExcelWriter("rapport.xlsx", engine="openpyxl") as writer:
    df.to_excel(writer, sheet_name="Données", index=False)
```

---

## Conclusion pédagogique

Ce cours doit être enseigné de manière progressive :

1. commencer par lire et comprendre le fichier ;
2. montrer que pandas n’est pas seulement une bibliothèque, mais une manière de raisonner en tableaux ;
3. faire beaucoup pratiquer `loc`, `iloc`, `groupby`, `merge` ;
4. finir avec un mini-projet de rapport automatisé ;
5. utiliser openpyxl seulement après que les calculs pandas sont corrects.

La règle principale pour les étudiants : **pandas sert à produire les données correctes ; openpyxl sert à produire un fichier Excel présentable.**
