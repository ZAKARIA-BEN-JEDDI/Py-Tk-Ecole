import tkinter as tk
from tkinter import ttk

# Fonction pour créer la fenêtre
class Afficher:
    def create_window(self):
        # Créer une instance de la classe Tk
        window = tk.Tk()
        window.title("Bienvenue dans 'OFPPT'")

        # Configuration de la taille de la fenêtre
        window.geometry("600x400")  # Taille arbitraire

        # Création d'un canevas avec un arrière-plan bleu ciel
        canvas = tk.Canvas(window, bg="#87CEEB")
        canvas.pack(fill="both", expand=True)

        label = tk.Label(canvas, text="Bienvenue dans 'OFPPT'", fg="white", font=("Arial", 20))
        label.pack(pady=20)

        timetable = ttk.Treeview(canvas, columns=("Jour", "Matière"), show="headings")
        timetable.heading("Jour", text="Jour")
        timetable.heading("Matière", text="Matière")
        timetable.insert("", "end", values=("Lundi", "Algorithmique"))
        timetable.insert("", "end", values=("Mardi", "Base de données"))
        timetable.insert("", "end", values=("Mercredi", "Langage de programmation"))
        timetable.insert("", "end", values=("Jeudi", "Sécurité informatique"))
        timetable.insert("", "end", values=("Vendredi", "Réseaux informatiques"))

        style = ttk.Style()
        style.configure("Treeview", background="white", foreground="black")

        timetable.pack(pady=10)

        window.mainloop()
