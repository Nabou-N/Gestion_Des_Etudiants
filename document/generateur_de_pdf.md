## Fiche explicative : Générateur de PDF avec ReportLab

### 1. Qu’est-ce que ce code fait ?

La classe `GenerateurPDF` permet de créer un fichier PDF contenant un tableau listant les étudiants d’une classe donnée. Elle utilise la bibliothèque **ReportLab**, spécialisée dans la génération de documents PDF en Python.

---

### 2. Les imports essentiels

| Import | Rôle |
|--------|------|
| `from reportlab.lib.pagesizes import A4` | Définit le format de page (A4). |
| `from reportlab.lib import colors` | Fournit des couleurs prédéfinies ou la possibilité d’utiliser des couleurs hexadécimales. |
| `from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle` | Récupère les styles par défaut et permet d’en créer de personnalisés. |
| `from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer` | Importe les éléments de base pour construire le document. |
| `from datetime import datetime` | Pour afficher la date et l’heure de génération. |
| `import os` | Pour gérer les dossiers (créer le dossier de destination si nécessaire). |

---

### 3. La classe et sa méthode statique

- La classe `GenerateurPDF` ne possède qu’une **méthode statique** : `generer_liste_classe`.  
- Elle prend trois paramètres :
  - `classe` : nom de la classe (exemple `"L1"`).
  - `etudiants` : liste de tuples `(numéro, nom, prénom, classe)`.
  - `chemin_sortie` : emplacement où enregistrer le PDF.

- **Pourquoi `@staticmethod` ?**  
  Parce que la méthode n’a pas besoin d’un objet `GenerateurPDF` ; elle peut être appelée directement via `GenerateurPDF.generer_liste_classe(...)`.

---

### 4. Étapes de la génération du PDF

#### a) Vérification des données

```python
if not etudiants:
    raise ValueError("Aucun étudiant trouvé pour cette classe.")
```

Si la liste est vide, on lève une erreur : le PDF ne serait pas utile.

#### b) Création du dossier parent

```python
dossier = os.path.dirname(chemin_sortie)
if dossier and not os.path.exists(dossier):
    os.makedirs(dossier)
```

- `os.path.dirname()` extrait le chemin du dossier à partir du chemin complet.  
- `os.path.exists()` vérifie s’il existe déjà.  
- `os.makedirs()` crée le dossier (et les sous-dossiers) s’il n’existe pas.

#### c) Initialisation du document

```python
doc = SimpleDocTemplate(
    chemin_sortie,
    pagesize=A4,
    rightMargin=50,
    leftMargin=50,
    topMargin=50,
    bottomMargin=50
)
```

- On crée un **modèle de document** au format A4 avec des marges de 50 points (~1,8 cm).  
- Ce n’est pas encore le PDF final ; c’est un conteneur qui recevra les éléments.

#### d) Définition des styles

```python
styles = getSampleStyleSheet()   # styles de base
style_titre = ParagraphStyle('Titre', parent=styles['Title'], fontSize=18, textColor=colors.HexColor('#1e2430'), spaceAfter=6)
style_sous_titre = ParagraphStyle('SousTitre', parent=styles['Normal'], fontSize=11, textColor=colors.HexColor('#6b7280'), spaceAfter=20)
```

- On récupère les styles prédéfinis (Title, Normal, etc.) et on crée des **styles personnalisés** :
  - `style_titre` : grande police (18), couleur foncée.
  - `style_sous_titre` : police 11, couleur grise, espace après le paragraphe.

#### e) Construction de la liste des éléments

```python
elements = []
elements.append(Paragraph(f"Liste des étudiants – Classe {classe}", style_titre))
elements.append(Paragraph(f"Généré le {datetime.now().strftime('%d/%m/%Y à %H:%M:%S')}", style_sous_titre))
elements.append(Spacer(1, 20))
```

- Un `Paragraph` est un bloc de texte avec un style.  
- `Spacer` crée un espace vertical (ici 20 points) pour aérer la mise en page.

#### f) Préparation des données du tableau

```python
data = [["N°", "Nom", "Prénom", "Classe"]]
for numero, nom, prenom, classe_etudiant in etudiants:
    data.append([str(numero), nom, prenom, classe_etudiant])
```

- On construit une **liste de listes** : la première ligne est l’en-tête, les suivantes sont les étudiants.

#### g) Création et stylage du tableau

```python
table = Table(data, colWidths=[50, 180, 180, 80])
table.setStyle(TableStyle([...]))
```

- `Table` crée le tableau avec des largeurs de colonnes fixes (en points).  
- `TableStyle` applique un ensemble de règles de formatage. Les plus utilisées :

| Commande | Description |
|----------|-------------|
| `('BACKGROUND', (col1, lig1), (col2, lig2), couleur)` | Colore l’arrière-plan d’une zone. |
| `('TEXTCOLOR', (col1, lig1), (col2, lig2), couleur)` | Définit la couleur du texte. |
| `('ALIGN', (col1, lig1), (col2, lig2), alignement)` | Alignement (`'CENTER'`, `'LEFT'`, etc.). |
| `('FONTNAME', ..., police)` | Police : `'Helvetica'`, `'Helvetica-Bold'`, etc. |
| `('FONTSIZE', ..., taille)` | Taille de la police. |
| `('BOTTOMPADDING', ..., valeur)` | Espace sous le texte dans la cellule. |
| `('TOPPADDING', ..., valeur)` | Espace au-dessus du texte. |
| `('GRID', ..., épaisseur, couleur)` | Affiche les bordures du tableau. |
| `('ROWBACKGROUNDS', (col1, lig1), (col2, lig2), [couleur1, couleur2])` | Alterne les couleurs de fond des lignes. |

- Les coordonnées sont `(colonne, ligne)`, sachant que `(0, 0)` est la première cellule, et `(-1, -1)` représente la dernière cellule (donc toute la zone).

Exemple : `('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#151a2d'))` colore toute la première ligne (en-tête) en bleu nuit.

#### h) Génération du fichier PDF

```python
elements.append(table)
doc.build(elements)
```

- On ajoute le tableau à la liste `elements`.  
- `doc.build(elements)` assemble tout et crée le fichier PDF à l’emplacement indiqué.

---

### 5. Résumé du flux

1. Vérifier la liste d’étudiants.
2. Créer le dossier de sortie avec `os`.
3. Configurer `SimpleDocTemplate` (format A4, marges).
4. Définir les styles avec `ParagraphStyle`.
5. Remplir une liste `elements` avec titre, sous-titre, espace, tableau.
6. Construire le tableau avec `Table` et le styler avec `TableStyle`.
7. Appeler `doc.build(elements)` pour générer le PDF.

---

### 6. Utilisation dans l’application

Dans `PdfPage`, on appelle :

```python
GenerateurPDF.generer_liste_classe(classe, etudiants, chemin)
```

Où `chemin` provient de la boîte de dialogue d’enregistrement (`filedialog.asksaveasfilename`).

---

Cette fiche vous donne une compréhension de base du générateur. N’hésitez pas à modifier les couleurs, largeurs ou styles pour personnaliser le document.