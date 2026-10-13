import tkinter as tk
import os
from tkinter import ttk, messagebox, filedialog
from datetime import datetime
from generateur_pdf import GenerateurPDF
from etudiants import Eleve
from notes import Note
from infos_etudiant import InfoEtudiant


# ================== Palette ==================
COULEURS = {
    "bg": "#f8fafc",               
    "nav_bg": "#0f172a",           
    "nav_active": "#2563eb",       
    "nav_hover": "#1e293b",        
    "accent": "#2563eb",           
    "accent_hover": "#1d4ed8",     
    "accent_light": "#eff6ff",     
    "texte": "#1e293b",            
    "bordure": "#e2e8f0",          
    "succes": "#059669",           
    "succes_bg": "#ecfdf5",
    "erreur": "#dc2626",          
    "erreur_bg": "#fef2f2",
    "gris_clair": "#f1f5f9",
}

POLICE = "Segoe UI"


# ================== Widgets utilitaires ==================
class CarteOmbre(tk.Frame):
    """Conteneur effet carte moderne avec bordure fine et padding soigné."""
    def __init__(self, parent, **kwargs):
        super().__init__(parent, bg=COULEURS["bordure"])
        self.inner = tk.Frame(self, bg=COULEURS["blanc"])
        self.inner.pack(fill="both", expand=True, padx=1, pady=1)
        self.content_frame = tk.Frame(self.inner, bg=COULEURS["blanc"])
        self.content_frame.pack(fill="both", expand=True, padx=kwargs.get("padding", 24), pady=kwargs.get("padding", 24))

    def contenu(self):
        return self.content_frame


class ChampAvecLabel(tk.Frame):
    """Champ de saisie étiqueté avec gestion des erreurs intégrée."""
    def __init__(self, parent, label, variable, width=30, show=None):
        super().__init__(parent, bg=COULEURS["blanc"])
        lbl = tk.Label(self, text=label, bg=COULEURS["blanc"], fg=COULEURS["texte"], font=(POLICE, 10, "bold"))
        lbl.pack(anchor="w")
        self.entry = ttk.Entry(self, textvariable=variable, width=width, show=show, font=(POLICE, 11))
        self.entry.pack(fill="x", pady=(6, 2))
        self.erreur_lbl = tk.Label(self, text="", bg=COULEURS["blanc"], fg=COULEURS["erreur"], font=(POLICE, 9))
        self.erreur_lbl.pack(anchor="w")

    def erreur(self, message=""):
        self.erreur_lbl.config(text=message)

    def focus(self):
        self.entry.focus_set()


class Badge(tk.Label):
    """Pastille de statut élégante (succès, erreur, info)."""
    def __init__(self, parent, texte="", type_="info"):
        couleurs = {
            "succes": (COULEURS["succes_bg"], COULEURS["succes"]),
            "erreur": (COULEURS["erreur_bg"], COULEURS["erreur"]),
            "info": (COULEURS["accent_light"], COULEURS["accent"]),
        }
        bg, fg = couleurs.get(type_, couleurs["info"])
        super().__init__(parent, text=texte, bg=bg, fg=fg, font=(POLICE, 9, "bold"), padx=12, pady=6)

    def maj(self, texte, type_="info"):
        couleurs = {
            "succes": (COULEURS["succes_bg"], COULEURS["succes"]),
            "erreur": (COULEURS["erreur_bg"], COULEURS["erreur"]),
            "info": (COULEURS["accent_light"], COULEURS["accent"]),
        }
        bg, fg = couleurs.get(type_, couleurs["info"])
        self.config(text=texte, bg=bg, fg=fg)


# ================== Page de base & Helpers ==================
class Page(tk.Frame):
    """Classe de base pour toutes les vues de l'application."""
    def __init__(self, parent, titre, sous_titre=""):
        super().__init__(parent, bg=COULEURS["bg"])
        self.titre = titre
        self.sous_titre = sous_titre
        self._construire_ui()

    def _construire_ui(self):
        header = tk.Frame(self, bg=COULEURS["bg"])
        header.pack(fill='x', padx=35, pady=(20, 10))
        tk.Label(header, text=self.titre, bg=COULEURS["bg"], fg=COULEURS["texte"], font=(POLICE, 18, "bold")).pack(anchor="w", pady=(0, 2))
        if self.sous_titre:
            tk.Label(header, text=self.sous_titre, bg=COULEURS["bg"], fg=COULEURS["texte_muet"], font=(POLICE, 10)).pack(anchor="w")
        
        sep = tk.Frame(self, bg=COULEURS["bordure"], height=1)
        sep.pack(fill="x", padx=35, pady=(10, 5))


class BarreRecherche(tk.Frame):
    def __init__(self, parent, on_search):
        super().__init__(parent, bg=COULEURS["blanc"])
        self.on_search = on_search
        self.var_nom = tk.StringVar()
        self.var_prenom = tk.StringVar()

        tk.Label(self, text="🔎  Recherche d'étudiant", bg=COULEURS["blanc"], fg=COULEURS["texte"],
                 font=(POLICE, 12, "bold")).grid(row=0, column=0, columnspan=3, sticky="w", pady=(0, 15))
        
        tk.Label(self, text="Nom", bg=COULEURS["blanc"], fg=COULEURS["texte_muet"], font=(POLICE, 10)).grid(row=1, column=0, sticky="w", padx=(0, 10))
        tk.Label(self, text="Prénom", bg=COULEURS["blanc"], fg=COULEURS["texte_muet"], font=(POLICE, 10)).grid(row=1, column=1, sticky="w", padx=(0, 10))
        
        e1 = ttk.Entry(self, textvariable=self.var_nom, width=22, font=(POLICE, 10))
        e2 = ttk.Entry(self, textvariable=self.var_prenom, width=22, font=(POLICE, 10))
        e1.grid(row=2, column=0, padx=(0, 10), pady=(4, 0), sticky="ew")
        e2.grid(row=2, column=1, padx=(0, 10), pady=(4, 0), sticky="ew")
        
        ttk.Button(self, text="Rechercher", style="Accent.TButton",
                   command=self._rechercher).grid(row=2, column=2, pady=(4, 0))
        
        for w in (e1, e2):
            w.bind("<Return>", lambda e: self._rechercher())
        self.columnconfigure((0, 1), weight=1)

    def _rechercher(self):
        nom = self.var_nom.get().strip()
        prenom = self.var_prenom.get().strip()
        if not nom and not prenom:
            messagebox.showwarning("Champs vides", "Veuillez entrer un nom ou un prénom pour lancer la recherche.")
            return
        self.on_search(nom, prenom)


def creer_treeview_etudiants(parent):
    frame = tk.Frame(parent, bg=COULEURS["bg"])
    tree = ttk.Treeview(frame, columns=("num", "nom", "prenom", "classe"), show="headings", height=5)
    entetes = {"num": "N°", "nom": "Nom", "prenom": "Prénom", "classe": "Classe"}
    largeurs = {"num": 60, "nom": 150, "prenom": 150, "classe": 100}
    for col, texte in entetes.items():
        tree.heading(col, text=texte)
        tree.column(col, width=largeurs[col], anchor="center" if col in ("num", "classe") else "w")
    tree.pack(side="left", fill="both", expand=True)
    scroll = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
    tree.configure(yscrollcommand=scroll.set)
    scroll.pack(side="right", fill="y")
    return frame, tree


class PageAvecScroll(Page):
    """Page avec gestion robuste et fluide du défilement et adaptation plein écran."""
    def __init__(self, parent, titre, sous_titre=""):
        super().__init__(parent, titre, sous_titre)
        self._construire_scroll()

    def _construire_scroll(self):
        conteneur = tk.Frame(self, bg=COULEURS["bg"])
        conteneur.pack(fill="both", expand=True)

        self.canvas = tk.Canvas(conteneur, background=COULEURS["bg"], highlightthickness=0)
        scrollbar = ttk.Scrollbar(conteneur, orient="vertical", command=self.canvas.yview)

        self.scrollable = tk.Frame(self.canvas, bg=COULEURS["bg"])
        
        self.window_id = self.canvas.create_window((0, 0), window=self.scrollable, anchor="nw")

        self.canvas.bind("<Configure>", lambda e: self.canvas.itemconfig(self.window_id, width=e.width))
        self.scrollable.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))

        self.canvas.configure(yscrollcommand=scrollbar.set)
        self.canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        self.canvas.bind("<Enter>", lambda e: self.canvas.bind_all("<MouseWheel>", self._sur_molette))
        self.canvas.bind("<Leave>", lambda e: self.canvas.unbind_all("<MouseWheel>"))

    def _sur_molette(self, event):
        self.canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")


# ================== Page Accueil ==================
class AccueilPage(Page):
    def __init__(self, parent, controleur):
        super().__init__(parent, "Tableau de bord", "Bienvenue sur votre plateforme de gestion académique.")
        self.controleur = controleur
        self._construire_contenu()

    def _construire_contenu(self):
        wrapper = tk.Frame(self, bg=COULEURS["bg"])
        wrapper.pack(expand=True, fill='both', padx=35, pady=25)

        tk.Label(wrapper, text="Accès rapide aux fonctionnalités :",
                 bg=COULEURS["bg"], fg=COULEURS["texte"], font=(POLICE, 12, "bold")).pack(anchor="w", pady=(0, 20))

        grille = tk.Frame(wrapper, bg=COULEURS["bg"])
        grille.pack(fill="x")
        grille.columnconfigure((0, 1, 2, 3), weight=1, uniform="col")

        actions = [
            ("➕", "Inscription", "Nouveau dossier étudiant", "inscription"),
            ("📝", "Notes", "Saisie des notes par matière", "notes"),
            ("🔎", "Recherche", "Dossier et notes détaillées", "recherche"),
            ("📇", "Coordonnées", "Adresses & contacts parents", "infos"),
        ]
        for i, (icone, titre, desc, page_key) in enumerate(actions):
            self._creer_carte_action(grille, icone, titre, desc, page_key).grid(
                row=0, column=i, padx=10, sticky="nsew")

    def _creer_carte_action(self, parent, icone, titre, desc, page_key):
        carte = CarteOmbre(parent, padding=20)
        c = carte.contenu()
        tk.Label(c, text=icone, bg=COULEURS["blanc"], fg=COULEURS["accent"], font=(POLICE, 26)).pack(anchor="w")
        tk.Label(c, text=titre, bg=COULEURS["blanc"], fg=COULEURS["texte"], font=(POLICE, 12, "bold")).pack(anchor="w", pady=(10, 4))
        tk.Label(c, text=desc, bg=COULEURS["blanc"], fg=COULEURS["texte_muet"], font=(POLICE, 9),
                 wraplength=160, justify="left").pack(anchor="w", pady=(0, 15))
        ttk.Button(c, text="Ouvrir →", style="Accent.TButton",
                   command=lambda: self.controleur.afficher_page(page_key)).pack(anchor="w")
        return carte


# ================== Page Inscription ==================
class InscriptionPage(Page):
    def __init__(self, parent, controleur):
        super().__init__(parent, "Inscription d'un étudiant", "Enregistrez un nouvel élève dans le système.")
        self.controleur = controleur
        self.var_nom = tk.StringVar()
        self.var_prenom = tk.StringVar()
        self.var_classe = tk.StringVar()
        self._construire_contenu()

    def _construire_contenu(self):
        carte = CarteOmbre(self, padding=30)
        carte.pack(pady=25, padx=35, fill='x')
        c = carte.contenu()
        c.columnconfigure((0, 1), weight=1)

        self.champ_nom = ChampAvecLabel(c, "Nom", self.var_nom, width=32)
        self.champ_nom.grid(row=0, column=0, padx=(0, 15), pady=10, sticky="ew")
        self.champ_prenom = ChampAvecLabel(c, "Prénom", self.var_prenom, width=32)
        self.champ_prenom.grid(row=0, column=1, padx=(15, 0), pady=10, sticky="ew")

        tk.Label(c, text="Classe", bg=COULEURS["blanc"], fg=COULEURS["texte"], font=(POLICE, 10, "bold")).grid(row=1, column=0, sticky='w', pady=(15, 6))
        self.combo_classe = ttk.Combobox(c, textvariable=self.var_classe,
                                         values=Eleve.obtenir_classes_existantes(),
                                         state="normal", font=(POLICE, 11),
                                         postcommand=self._maj_classes)
        self.combo_classe.grid(row=2, column=0, columnspan=2, sticky="ew", pady=(0, 15))

        boutons = tk.Frame(c, bg=COULEURS["blanc"])
        boutons.grid(row=3, column=0, columnspan=2, pady=(15, 5), sticky="w")
        ttk.Button(boutons, text="✔ Inscrire l'étudiant", style="Accent.TButton",
                   command=self._inscrire).pack(side="left")
        ttk.Button(boutons, text="Réinitialiser", style="Secondary.TButton",
                   command=self._reinitialiser).pack(side="left", padx=(12, 0))

        self.badge = Badge(c)
        self.badge.grid(row=4, column=0, columnspan=2, pady=(20, 0), sticky="w")
        self.badge.grid_remove()

        for widget in (self.champ_nom.entry, self.champ_prenom.entry, self.combo_classe):
            widget.bind("<Return>", lambda e: self._inscrire())
        self.champ_nom.focus()

    def _maj_classes(self):
        self.combo_classe['values'] = Eleve.obtenir_classes_existantes()

    def _reinitialiser(self):
        self.var_nom.set("")
        self.var_prenom.set("")
        self.var_classe.set("")
        self.champ_nom.erreur()
        self.champ_prenom.erreur()
        self.badge.grid_remove()
        self.champ_nom.focus()

    def _inscrire(self):
        nom = self.var_nom.get().strip()
        prenom = self.var_prenom.get().strip()
        classe = self.var_classe.get().strip()

        valide = True
        self.champ_nom.erreur()
        self.champ_prenom.erreur()
        if not nom:
            self.champ_nom.erreur("Champ requis")
            valide = False
        if not prenom:
            self.champ_prenom.erreur("Champ requis")
            valide = False
        if not classe:
            messagebox.showerror("Erreur", "La classe est obligatoire.")
            valide = False
        if not valide:
            return

        try:
            nouvel = Eleve(nom, prenom, classe)
            nouvel.inscription()
            self.badge.maj(f"✔ Succès : {prenom} {nom} a bien été inscrit(e).", "succes")
            self.badge.grid()
            self._reinitialiser()
            self.badge.grid()
        except Exception as e:
            self.badge.maj(f"✘ Erreur : {e}", "erreur")
            self.badge.grid()


# ================== Page Notes ==================
class NotesPage(PageAvecScroll):
    MATIERES = ["Math", "PC", "HG", "Malagasy", "Français", "Philo"]

    def __init__(self, parent, controleur):
        super().__init__(parent, "Gestion des notes", "Sélectionnez un étudiant puis saisissez ses notes sur /20.")
        self.controleur = controleur
        self.numero_courant = None
        self.entries_notes = []
        self._construire_contenu()

    def _construire_contenu(self):
        carte_recherche = CarteOmbre(self.scrollable, padding=20)
        carte_recherche.pack(pady=20, padx=35, fill='x')
        self.recherche = BarreRecherche(carte_recherche.contenu(), self._rechercher)
        self.recherche.pack(fill="x")

        frame_res, self.tree_etudiants = creer_treeview_etudiants(self.scrollable)
        frame_res.pack(pady=(5, 12), padx=35, fill='x')
        self.tree_etudiants.bind("<Double-1>", lambda e: self._selectionner())

        actions_res = tk.Frame(self.scrollable, bg=COULEURS["bg"])
        actions_res.pack(padx=35, fill="x")
        ttk.Button(actions_res, text="Sélectionner l'étudiant →", style="Accent.TButton",
                   command=self._selectionner).pack(anchor="e", pady=(0, 15))

        carte_notes = CarteOmbre(self.scrollable, padding=25)
        carte_notes.pack(pady=(0, 30), padx=35, fill='both', expand=True)
        c = carte_notes.contenu()

        self.label_selection = tk.Label(c, text="📌 Aucun étudiant sélectionné",
                                        bg=COULEURS["blanc"], fg=COULEURS["texte"], font=(POLICE, 11, "bold"))
        self.label_selection.grid(row=0, column=0, columnspan=4, pady=(0, 18), sticky='w')

        self.vars_notes = [tk.StringVar() for _ in range(6)]
        vcmd = (self.register(self._valider_note), "%P")
        for i, (mat, var) in enumerate(zip(self.MATIERES, self.vars_notes)):
            row, col = divmod(i, 2)
            bloc = tk.Frame(c, bg=COULEURS["blanc"])
            bloc.grid(row=row + 1, column=col, padx=12, pady=10, sticky="ew")
            tk.Label(bloc, text=mat, bg=COULEURS["blanc"], fg=COULEURS["texte"], font=(POLICE, 10, "bold")).pack(anchor="w")
            entry = ttk.Entry(bloc, textvariable=var, width=14, state='disabled',
                              font=(POLICE, 11), validate="key", validatecommand=vcmd)
            entry.pack(fill="x", pady=(4, 0))
            self.entries_notes.append(entry)
        c.columnconfigure((0, 1), weight=1)

        boutons = tk.Frame(c, bg=COULEURS["blanc"])
        boutons.grid(row=5, column=0, columnspan=4, pady=(20, 5), sticky="w")
        self.btn_ajouter = ttk.Button(boutons, text="💾 Enregistrer les notes", style="Accent.TButton",
                                      state='disabled', command=self._ajouter)
        self.btn_ajouter.pack(side="left")

        self.badge = Badge(c)
        self.badge.grid(row=6, column=0, columnspan=4, pady=(15, 0), sticky="w")
        self.badge.grid_remove()

    @staticmethod
    def _valider_note(texte_propose):
        if texte_propose == "":
            return True
        try:
            valeur = float(texte_propose)
            return 0 <= valeur <= 20 or texte_propose.endswith(".")
        except ValueError:
            return False

    def _rechercher(self, nom, prenom):
        for item in self.tree_etudiants.get_children():
            self.tree_etudiants.delete(item)
        resultats = Eleve.rechercher_par_nom_prenom(nom, prenom)
        if not resultats:
            messagebox.showinfo("Aucun résultat", "Aucun étudiant ne correspond à cette recherche.")
            return
        for num, n, p, cl in resultats:
            self.tree_etudiants.insert("", tk.END, values=(num, n, p, cl))

    def _selectionner(self):
        sel = self.tree_etudiants.selection()
        if not sel:
            messagebox.showwarning("Sélection", "Veuillez sélectionner un étudiant dans la liste.")
            return
        num, nom, prenom, classe = self.tree_etudiants.item(sel[0])['values']
        self.numero_courant = int(num)
        self.label_selection.config(text=f"📌 Étudiant : {prenom} {nom} | Classe : {classe} (N°{num})")
        for entry in self.entries_notes:
            entry.config(state='normal')
        self.btn_ajouter.config(state='normal')
        self.entries_notes[0].focus_set()

    def _ajouter(self):
        if self.numero_courant is None:
            return
        notes = []
        for i, var in enumerate(self.vars_notes):
            try:
                note = float(var.get().strip())
                if not (0 <= note <= 20):
                    raise ValueError
                notes.append(note)
            except ValueError:
                messagebox.showerror("Erreur", f"Note invalide pour '{self.MATIERES[i]}' (Valeur attendue : entre 0 et 20).")
                self.entries_notes[i].focus_set()
                return
        etudiant = Eleve.etudiant(self.numero_courant)
        nouvelle = Note(self.numero_courant, etudiant.nom, etudiant.prenom, *notes)
        try:
            nouvelle.ajout_de_note()
            self.badge.maj("✔ Notes enregistrées avec succès.", "succes")
            self.badge.grid()
            for var in self.vars_notes:
                var.set("")
            for entry in self.entries_notes:
                entry.config(state='disabled')
            self.btn_ajouter.config(state='disabled')
            self.label_selection.config(text="📌 Aucun étudiant sélectionné")
            self.numero_courant = None
        except Exception as e:
            self.badge.maj(f"✘ Erreur : {e}", "erreur")
            self.badge.grid()


# ================== Page Recherche & Dossier ==================
class RecherchePage(PageAvecScroll):
    def __init__(self, parent, controleur):
        super().__init__(parent, "Dossier étudiant", "Consultez les notes et informations complètes d'un élève.")
        self.controleur = controleur
        self._construire_contenu()

    def _construire_contenu(self):
        carte_recherche = CarteOmbre(self.scrollable, padding=20)
        carte_recherche.pack(pady=20, padx=35, fill='x')
        self.recherche = BarreRecherche(carte_recherche.contenu(), self._rechercher)
        self.recherche.pack(fill="x")

        frame_res, self.tree_etudiants = creer_treeview_etudiants(self.scrollable)
        frame_res.pack(pady=(5, 12), padx=35, fill='x')
        self.tree_etudiants.bind("<Double-1>", lambda e: self._selectionner())

        actions_res = tk.Frame(self.scrollable, bg=COULEURS["bg"])
        actions_res.pack(padx=35, fill="x")
        ttk.Button(actions_res, text="Afficher le dossier →", style="Accent.TButton",
                   command=self._selectionner).pack(anchor="e", pady=(0, 15))

        carte_details = CarteOmbre(self.scrollable, padding=25)
        carte_details.pack(pady=(0, 30), padx=35, fill='both', expand=True)
        c = carte_details.contenu()

        self.label_etudiant = tk.Label(c, text="👤 Aucun étudiant sélectionné",
                                        bg=COULEURS["blanc"], fg=COULEURS["texte"], font=(POLICE, 11, "bold"))
        self.label_etudiant.pack(anchor='w', pady=(0, 18))

        deux_colonnes = tk.Frame(c, bg=COULEURS["blanc"])
        deux_colonnes.pack(fill="both", expand=True)
        deux_colonnes.columnconfigure((0, 1), weight=1)

        bloc_notes = tk.Frame(deux_colonnes, bg=COULEURS["blanc"])
        bloc_notes.grid(row=0, column=0, sticky="nsew", padx=(0, 15))
        tk.Label(bloc_notes, text="📊 Notes obtenues", bg=COULEURS["blanc"], fg=COULEURS["texte"], font=(POLICE, 11, "bold")).pack(anchor="w", pady=(0, 8))
        self.tree_notes = ttk.Treeview(bloc_notes, columns=("matiere", "note"), show="headings", height=6)
        self.tree_notes.heading("matiere", text="Matière")
        self.tree_notes.heading("note", text="Note /20")
        self.tree_notes.column("matiere", width=150, anchor='w')
        self.tree_notes.column("note", width=90, anchor='center')
        self.tree_notes.pack(fill="both", expand=True)

        bloc_infos = tk.Frame(deux_colonnes, bg=COULEURS["blanc"])
        bloc_infos.grid(row=0, column=1, sticky="nsew", padx=(15, 0))
        tk.Label(bloc_infos, text="ℹ️ Coordonnées", bg=COULEURS["blanc"], fg=COULEURS["texte"], font=(POLICE, 11, "bold")).pack(anchor="w", pady=(0, 8))
        self.label_infos = tk.Label(bloc_infos, text="Sélectionnez un étudiant pour afficher ses informations.", bg=COULEURS["blanc"], fg=COULEURS["texte_muet"], justify="left")
        self.label_infos.pack(anchor='w')

    def _rechercher(self, nom, prenom):
        for item in self.tree_etudiants.get_children():
            self.tree_etudiants.delete(item)
        resultats = Eleve.rechercher_par_nom_prenom(nom, prenom)
        if not resultats:
            messagebox.showinfo("Aucun résultat", "Aucun étudiant trouvé.")
            return
        for num, n, p, cl in resultats:
            self.tree_etudiants.insert("", tk.END, values=(num, n, p, cl))

    def _selectionner(self):
        sel = self.tree_etudiants.selection()
        if not sel:
            messagebox.showwarning("Sélection", "Veuillez sélectionner un étudiant.")
            return
        num, nom, prenom, classe = self.tree_etudiants.item(sel[0])['values']
        self.label_etudiant.config(text=f"👤 Dossier de {prenom} {nom}  •  Classe : {classe}  •  N°{num}")

        for row in self.tree_notes.get_children():
            self.tree_notes.delete(row)
        etudiant = Eleve.etudiant(int(num))
        note_obj = Note.afficher_les_notes_d_un_etudiant(int(num), etudiant)
        if note_obj:
            notes_data = [
                ("Mathématiques", note_obj.note_math), ("Physique-Chimie", note_obj.note_pc),
                ("Histoire-Géo", note_obj.note_hg), ("Malagasy", note_obj.note_malagasy),
                ("Français", note_obj.note_francais), ("Philosophie", note_obj.note_philo),
            ]
            for matiere, note in notes_data:
                self.tree_notes.insert("", tk.END, values=(matiere, note))
        else:
            self.tree_notes.insert("", tk.END, values=("Aucune note enregistrée", "—"))

        infos = InfoEtudiant.charger_infos(int(num))
        if infos:
            self.label_infos.config(
                text=f"📍 Adresse :\n{infos.adresse}\n\n📞 Contact personnel :\n{infos.contact}\n\n👨‍👩‍👧 Contact parents :\n{infos.contact_parents}")
        else:
            self.label_infos.config(text="Aucune information complémentaire enregistrée pour cet élève.")


# ================== Page Infos Étudiant ==================
class InfosPage(PageAvecScroll):
    def __init__(self, parent, controleur):
        super().__init__(parent, "Coordonnées & Adresses", "Mettez à jour les informations de contact et d'adresse.")
        self.controleur = controleur
        self.numero_courant = None
        self._construire_contenu()

    def _construire_contenu(self):
        carte_recherche = CarteOmbre(self.scrollable, padding=20)
        carte_recherche.pack(pady=20, padx=35, fill='x')
        self.recherche = BarreRecherche(carte_recherche.contenu(), self._rechercher)
        self.recherche.pack(fill="x")

        frame_res, self.tree_etudiants = creer_treeview_etudiants(self.scrollable)
        frame_res.pack(pady=(5, 12), padx=35, fill='x')
        self.tree_etudiants.bind("<Double-1>", lambda e: self._selectionner())

        actions_res = tk.Frame(self.scrollable, bg=COULEURS["bg"])
        actions_res.pack(padx=35, fill="x")
        ttk.Button(actions_res, text="Modifier les infos →", style="Accent.TButton",
                   command=self._selectionner).pack(anchor="e", pady=(0, 15))

        carte_infos = CarteOmbre(self.scrollable, padding=25)
        carte_infos.pack(pady=(0, 30), padx=35, fill='both', expand=True)
        c = carte_infos.contenu()
        c.columnconfigure(0, weight=1)

        self.label_etudiant = tk.Label(c, text="👤 Aucun étudiant sélectionné",
                                        bg=COULEURS["blanc"], fg=COULEURS["texte"], font=(POLICE, 11, "bold"))
        self.label_etudiant.grid(row=0, column=0, pady=(0, 18), sticky='w')

        self.var_adresse = tk.StringVar()
        self.var_contact = tk.StringVar()
        self.var_contact_parents = tk.StringVar()
        
        self.champ_adresse = ChampAvecLabel(c, "Adresse complète", self.var_adresse, width=50)
        self.champ_adresse.grid(row=1, column=0, sticky="ew", pady=8)
        self.champ_contact = ChampAvecLabel(c, "Contact personnel", self.var_contact, width=50)
        self.champ_contact.grid(row=2, column=0, sticky="ew", pady=8)
        self.champ_parents = ChampAvecLabel(c, "Contact des parents", self.var_contact_parents, width=50)
        self.champ_parents.grid(row=3, column=0, sticky="ew", pady=8)

        self.btn_enregistrer = ttk.Button(c, text="💾 Enregistrer les modifications", style="Accent.TButton",
                                          state='disabled', command=self._enregistrer)
        self.btn_enregistrer.grid(row=4, column=0, pady=(20, 5), sticky="w")

        self.badge = Badge(c)
        self.badge.grid(row=5, column=0, pady=(15, 0), sticky="w")
        self.badge.grid_remove()

    def _rechercher(self, nom, prenom):
        for item in self.tree_etudiants.get_children():
            self.tree_etudiants.delete(item)
        resultats = Eleve.rechercher_par_nom_prenom(nom, prenom)
        if not resultats:
            messagebox.showinfo("Aucun résultat", "Aucun étudiant trouvé.")
            return
        for num, n, p, cl in resultats:
            self.tree_etudiants.insert("", tk.END, values=(num, n, p, cl))

    def _selectionner(self):
        sel = self.tree_etudiants.selection()
        if not sel:
            messagebox.showwarning("Sélection", "Veuillez sélectionner un étudiant.")
            return
        num, nom, prenom, classe = self.tree_etudiants.item(sel[0])['values']
        self.numero_courant = int(num)
        self.label_etudiant.config(text=f"👤 Modification pour : {prenom} {nom}  •  Classe : {classe}  •  N°{num}")
        infos = InfoEtudiant.charger_infos(int(num))
        self.var_adresse.set(infos.adresse if infos else "")
        self.var_contact.set(infos.contact if infos else "")
        self.var_contact_parents.set(infos.contact_parents if infos else "")
        self.btn_enregistrer.config(state='normal')
        self.badge.grid_remove()
        self.champ_adresse.focus()

    def _enregistrer(self):
        if self.numero_courant is None:
            return
        etudiant = Eleve.etudiant(self.numero_courant)
        info = InfoEtudiant(etudiant.nom, etudiant.prenom, etudiant.classe,
                            adresse=self.var_adresse.get().strip(),
                            contact=self.var_contact.get().strip(),
                            contact_parents=self.var_contact_parents.get().strip())
        try:
            info.enregistrer_infos(self.numero_courant)
            self.badge.maj("✔ Coordonnées mises à jour avec succès.", "succes")
            self.badge.grid()
            self.btn_enregistrer.config(state='disabled')
            self.numero_courant = None
        except Exception as e:
            self.badge.maj(f"✘ Erreur : {e}", "erreur")
            self.badge.grid()


# ================== Page Export PDF  ==================
class PdfPage(Page):
    def __init__(self, parent, controleur):
        super().__init__(parent, "Exportation PDF", "Générez la liste officielle des étudiants par classe.")
        self.controleur = controleur
        self._construire_contenu()

    def _construire_contenu(self):
        carte = CarteOmbre(self, padding=25)
        carte.pack(pady=20, padx=35, fill='x')
        c = carte.contenu()
        c.columnconfigure(0, weight=1)

        tk.Label(c, text="Sélectionner une classe", bg=COULEURS["blanc"], fg=COULEURS["texte"], font=(POLICE, 10, "bold")).grid(row=0, column=0, sticky='w', pady=(0, 6))
        self.var_classe = tk.StringVar()
        self.combo_classe = ttk.Combobox(
            c,
            textvariable=self.var_classe,
            values=Eleve.obtenir_classes_existantes(),
            state="readonly",
            font=(POLICE, 11),
            postcommand=self._maj_classes
        )
        self.combo_classe.grid(row=1, column=0, sticky='ew', pady=(0, 18))
        self.combo_classe.bind("<<ComboboxSelected>>", self._afficher_apercu)

        self.btn_generer = ttk.Button(c, text="📄 Générer et enregistrer le PDF", style="Accent.TButton",
                                      command=self._generer_pdf, state='disabled')
        self.btn_generer.grid(row=2, column=0, sticky='w', pady=(5, 5))

        self.badge = Badge(c)
        self.badge.grid(row=3, column=0, pady=(15, 0), sticky="w")
        self.badge.grid_remove()

        tk.Label(self, text="Aperçu des élèves inclus", bg=COULEURS["bg"], fg=COULEURS["texte"],
                 font=(POLICE, 12, 'bold')).pack(padx=35, anchor='w', pady=(10, 8))
        self.frame_apercu, self.tree_apercu = creer_treeview_etudiants(self)
        self.frame_apercu.pack(padx=35, fill='both', expand=True, pady=(0, 25))

        self._maj_classes()

    def _maj_classes(self):
        self.combo_classe['values'] = Eleve.obtenir_classes_existantes()

    def _afficher_apercu(self, event=None):
        classe = self.var_classe.get().strip()
        if not classe:
            self.btn_generer.config(state='disabled')
            return
        for item in self.tree_apercu.get_children():
            self.tree_apercu.delete(item)
        etudiants = Eleve.obtenir_etudiants_par_classe(classe)
        for num, nom, prenom, cl in etudiants:
            self.tree_apercu.insert("", tk.END, values=(num, nom, prenom, cl))
        self.btn_generer.config(state='normal' if etudiants else 'disabled')
        if not etudiants:
            self.badge.maj("Aucun étudiant inscrit dans cette classe.", "erreur")
            self.badge.grid()
        else:
            self.badge.grid_remove()

    def _generer_pdf(self):
        classe = self.var_classe.get().strip()
        if not classe:
            messagebox.showwarning("Classe", "Veuillez sélectionner une classe.")
            return

        etudiants = Eleve.obtenir_etudiants_par_classe(classe)
        if not etudiants:
            messagebox.showinfo("Aucun étudiant", "Aucun étudiant trouvé pour cette classe.")
            return

        chemin = filedialog.asksaveasfilename(
            title="Enregistrer le document PDF",
            defaultextension=".pdf",
            initialfile=f"liste_{classe.replace(' ', '_')}.pdf",
            filetypes=[("Fichier PDF", "*.pdf")]
        )
        if not chemin:
            return

        try:
            GenerateurPDF.generer_liste_classe(classe, etudiants, chemin)
            self.badge.maj(f"✔ PDF généré avec succès : {os.path.basename(chemin)}", "succes")
            self.badge.grid()
        except Exception as e:
            self.badge.maj(f"✘ Erreur lors de la génération : {e}", "erreur")
            self.badge.grid()


# ================== Contrôleur Principal & Lancement ==================
class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Gestion Académique")
        self.geometry("1100x700")
        self.minsize(900, 600)
        self.configure(bg=COULEURS["bg"])

        # Configuration des styles globaux TTK
        self._configurer_styles()

        # Structure principale (Navbar en haut + Contenu en bas)
        self.rowconfigure(1, weight=1)
        self.columnconfigure(0, weight=1)

        self._creer_navbar()

        # Dictionnaire des pages
        self.pages = {}
        self._initialiser_pages()

        # Afficher la page d'accueil par défaut
        self.afficher_page("accueil")

    def _configurer_styles(self):
        style = ttk.Style()
        style.theme_use("clam")

        # Boutons
        style.configure("Accent.TButton", font=(POLICE, 10, "bold"), background=COULEURS["accent"], foreground=COULEURS["blanc"], borderwidth=0, focusthickness=0)
        style.map("Accent.TButton", background=[('active', COULEURS["accent_hover"])])

        style.configure("Secondary.TButton", font=(POLICE, 10), background=COULEURS["gris_clair"], foreground=COULEURS["texte"], borderwidth=0)

    def _creer_navbar(self):
        self.navbar = tk.Frame(self, bg=COULEURS["nav_bg"], height=60)
        self.navbar.grid(row=0, column=0, sticky="ew")
        self.navbar.grid_propagate(False)

        # Logo / Titre à gauche dans la navbar
        logo_lbl = tk.Label(self.navbar, text="🎓 GESTION ÉTUDIANTS", bg=COULEURS["nav_bg"], fg=COULEURS["blanc"], font=(POLICE, 12, "bold"))
        logo_lbl.pack(side="left", padx=25)

        # Cadre pour les boutons de navigation à droite
        nav_buttons_frame = tk.Frame(self.navbar, bg=COULEURS["nav_bg"])
        nav_buttons_frame.pack(side="right", padx=15)

        nav_items = [
            ("🏠", "Accueil", "accueil"),
            ("➕", "Inscription", "inscription"),
            ("📝", "Notes", "notes"),
            ("🔎", "Recherche", "recherche"),
            ("📇", "Coordonnées", "infos"),
            ("📥", "Export PDF", "pdf"),
        ]

        self.boutons_nav = {}
        for icone, texte, key in nav_items:
            btn = tk.Button(
                nav_buttons_frame,
                text=f"{icone}  {texte}",
                bg=COULEURS["nav_bg"],
                fg=COULEURS["blanc"],
                activebackground=COULEURS["nav_hover"],
                activeforeground=COULEURS["blanc"],
                bd=0,
                padx=12,
                pady=8,
                font=(POLICE, 10, "bold"),
                cursor="hand2",
                command=lambda k=key: self.afficher_page(k)
            )
            btn.pack(side="left", padx=3)
            self.boutons_nav[key] = btn

    def _initialiser_pages(self):
        self.container_pages = tk.Frame(self, bg=COULEURS["bg"])
        self.container_pages.grid(row=1, column=0, sticky="nsew")
        self.container_pages.rowconfigure(0, weight=1)
        self.container_pages.columnconfigure(0, weight=1)

        # Instanciation de toutes les pages
        self.pages["accueil"] = AccueilPage(self.container_pages, self)
        self.pages["inscription"] = InscriptionPage(self.container_pages, self)
        self.pages["notes"] = NotesPage(self.container_pages, self)
        self.pages["recherche"] = RecherchePage(self.container_pages, self)
        self.pages["infos"] = InfosPage(self.container_pages, self)
        self.pages["pdf"] = PdfPage(self.container_pages, self)

        for page in self.pages.values():
            page.grid(row=0, column=0, sticky="nsew")

    def afficher_page(self, page_key):
        # Mettre en avant la page sélectionnée
        page = self.pages[page_key]
        page.tkraise()

        # Mettre à jour les couleurs des boutons de la navbar
        for key, btn in self.boutons_nav.items():
            if key == page_key:
                btn.config(bg=COULEURS["nav_active"])
            else:
                btn.config(bg=COULEURS["nav_bg"])


if __name__ == "__main__":
    app = Application()
    app.mainloop()