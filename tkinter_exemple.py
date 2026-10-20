import tkinter as tk

fenetre = tk.Tk()            # Instance de la classe Tk (la fenêtre principale)
bouton = tk.Button(fenetre, text="Cliquez-moi")  # Instance de Button
bouton.pack()                # Méthode pour afficher le bouton
fenetre.mainloop()           # Méthode pour lancer la boucle d'événements
