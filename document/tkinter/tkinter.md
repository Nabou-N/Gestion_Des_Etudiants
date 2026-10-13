## Leçon : Tkinter et les bases des interfaces graphiques en POO

### 1. Qu’est-ce que Tkinter ?

**Tkinter** est une bibliothèque incluse avec Python qui permet de créer des **interfaces graphiques** (GUI – Graphical User Interface). Elle donne accès à des **widgets** : fenêtres, boutons, zones de texte, menus, etc.

**Pourquoi c’est orienté objet ?**  
Chaque élément graphique (un bouton, une fenêtre, une étiquette) est représenté par une **classe** dans Tkinter. Quand vous écrivez `tk.Button(...)`, vous créez une **instance** de la classe `Button`. Toutes les notions que nous avons vues (attributs, méthodes, héritage) s’appliquent directement.

---

### 2. Votre première fenêtre

Commençons par le strict minimum : une fenêtre vide.

```python
import tkinter as tk

fenetre = tk.Tk()          # Instance de la classe Tk : la fenêtre principale
fenetre.title("Ma première fenêtre")
fenetre.geometry("400x300")  # largeur x hauteur en pixels

fenetre.mainloop()        # Démarre la boucle d’événements : la fenêtre reste ouverte
```

**Explications :**
- `tk.Tk()` crée l’objet fenêtre principale.
- `title()` et `geometry()` sont des **méthodes** de la classe `Tk`.
- `mainloop()` est essentielle : elle écoute les événements (clics, frappe clavier) et garde la fenêtre affichée. Sans elle, la fenêtre s’ouvre et se ferme immédiatement.

---

### 3. Les widgets de base

Un **widget** est un composant graphique. Les plus courants :

| Widget | Classe Tkinter | Description |
|--------|----------------|-------------|
| Étiquette | `Label` | Affiche du texte ou une image |
| Bouton | `Button` | Déclenche une action au clic |
| Champ de saisie | `Entry` | Permet de saisir une ligne de texte |
| Zone de texte | `Text` | Texte multi-lignes |
| Cadre | `Frame` | Conteneur pour organiser d’autres widgets |

Chaque widget a un **parent** (le conteneur dans lequel il est placé). La fenêtre principale est souvent le parent initial.

**Exemple avec un Label :**

```python
import tkinter as tk

fenetre = tk.Tk()
fenetre.title("Widgets")

# Création d'un label dont le parent est 'fenetre'
label = tk.Label(fenetre, text="Bonjour, POO !")
label.pack()  # Méthode de placement simple (empile les widgets)

fenetre.mainloop()
```

**Placement des widgets** : il existe trois méthodes principales :
- `pack()` : empile les widgets les uns sous les autres (ou côte à côte avec `side`).
- `grid(row, column)` : placement en grille.
- `place(x, y)` : position absolue en pixels.

Nous utiliserons surtout `pack` et `grid`.

---

### 4. Lier un bouton à une méthode

Un bouton doit réagir au clic. On utilise le paramètre `command` pour associer une **fonction ou méthode** à l’événement.

```python
import tkinter as tk

def dire_bonjour():
    print("Bonjour !")

fenetre = tk.Tk()
bouton = tk.Button(fenetre, text="Cliquez-moi", command=dire_bonjour)
bouton.pack()

fenetre.mainloop()
```

Chaque clic sur le bouton déclenche l’appel de `dire_bonjour`.

---

### 5. Tkinter et POO : créer sa propre classe d’application

Pour structurer une application un peu plus grande, on préfère encapsuler les widgets dans une **classe**. On peut hériter de `tk.Tk` (la fenêtre) ou de `tk.Frame` (un conteneur).

**Exemple : une classe `Application` qui hérite de `tk.Tk`**

```python
import tkinter as tk

class Application(tk.Tk):
    def __init__(self):
        super().__init__()          # Appel du constructeur de tk.Tk
        self.title("Mon application")
        self.geometry("300x200")

        # Créer les widgets
        self.label = tk.Label(self, text="Entrez votre nom :")
        self.label.pack()

        self.entry = tk.Entry(self)
        self.entry.pack()

        self.bouton = tk.Button(self, text="Valider", command=self.afficher_nom)
        self.bouton.pack()

    def afficher_nom(self):
        nom = self.entry.get()      # Récupère le texte saisi
        self.label.config(text=f"Bonjour, {nom} !")

if __name__ == "__main__":
    app = Application()
    app.mainloop()
```

**Analyse :**
- `Application` hérite de `tk.Tk` : c’est une fenêtre à part entière.
- `super().__init__()` initialise la partie fenêtre.
- Les widgets sont des **attributs** de l’instance (`self.label`, `self.entry`, `self.bouton`).
- La méthode `afficher_nom` est associée au bouton via `command`.
- `self.entry.get()` lit le contenu du champ.
- `self.label.config(text=...)` modifie le texte du label.

**Avantage de la POO** : tout est regroupé dans une seule classe, facile à maintenir et à réutiliser.

---

### 6. Les événements et `bind`

En plus de `command`, on peut lier des événements plus précis (appui d’une touche, survol de souris) avec la méthode `bind`.

```python
self.entry.bind("<Return>", lambda event: self.afficher_nom())
```

Ici, appuyer sur Entrée dans le champ déclenche la même méthode.

---

### 7. Petit exercice pour pratiquer

**Objectif :** Créer une petite calculatrice de conversion de kilomètres en miles.

1. Créez une classe `Convertisseur` héritant de `tk.Tk`.
2. Dans le constructeur :
   - Titre : "Convertisseur km -> miles".
   - Un `Entry` pour saisir les kilomètres.
   - Un `Button` "Convertir".
   - Un `Label` pour afficher le résultat.
3. La méthode `convertir` doit :
   - Lire la valeur de l’`Entry` (un float, attention aux erreurs de saisie).
   - Calculer : miles = km * 0.621371.
   - Afficher le résultat dans le `Label`.
4. Bonus : gérez le cas où l’utilisateur entre un texte non numérique en affichant un message d’erreur.

**Aide :** Utilisez `try/except` pour la conversion.

---

### Résumé des points importants

- Tkinter est la bibliothèque graphique standard de Python, basée sur la POO.
- Chaque widget est une instance d’une classe (`tk.Tk`, `tk.Label`, `tk.Button`, etc.).
- La fenêtre principale est créée par `tk.Tk()` et la boucle d’événements est lancée avec `mainloop()`.
- On peut organiser l’application dans une classe qui hérite de `tk.Tk` ou `tk.Frame`.
- Les actions des widgets sont liées à des méthodes via `command` ou `bind`.