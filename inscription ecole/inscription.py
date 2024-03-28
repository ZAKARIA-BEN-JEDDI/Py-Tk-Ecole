from tkinter import *
import tkinter.messagebox
class Inscription:
    nom = ["a", "b", "c"]
    prenom = ["a", "b", "c"]
    email1 = ["a", "b", "c"]
    mdp1 = ["a", "b", "c"]
    def variable(self,l1,l2,l3,l4,l5,r1,r2,r3,r4,r5,text1,text2,text3,text4,b1,b2,f1):
        self.l1=l1
        self.l2=l2
        self.l3=l3
        self.l4=l4
        self.l5=l5
        self.r1=r1
        self.r2=r2
        self.r3=r3
        self.r4=r4
        self.r5=r5
        self.text1=text1
        self.text2=text2
        self.text3=text3
        self.text1=text4
        self.b1=b1
        self.b2=b2
        self.f1=f1
    def inscrire(self):
        self.f1 = Tk()
        self.f1.geometry("450x600")
        self.f1.title("inscrire")

        self.l1 = Label(self.f1, text="Nom ")
        self.l1.config(bg="yellow", fg="black")
        self.l1.pack(pady=10)
        self.text1 = Entry(self.f1)
        self.text1.pack()

        self.l2 = Label(self.f1, text="Prenom ")
        self.l2.config(bg="yellow", fg="black")

        self.l2.pack(pady=10)
        self.text2 = Entry(self.f1)
        self.text2.pack()

        choix = ["Marrakech", "Casa", "Rabat", "Tanger"]
        imp = StringVar(value="Ville",name="Ville")
        option = OptionMenu(self.f1,imp, *choix)
        option.pack(pady=10)

        self.l3 = Label(self.f1,text="Gender")
        self.l3.config(bg="yellow", fg="black")
        self.l3.pack(pady=10)

        variable1 = IntVar()
        self.r1 = Radiobutton(self.f1, text="F", variable=variable1, value=1)
        self.r1.pack()

        self.r2 = Radiobutton(self.f1, text="H", variable=variable1, value=2)
        self.r2.pack()

        self.l4 = Label(self.f1,text="Filiere")
        self.l4.config(bg="yellow", fg="black")
        self.l4.pack(pady=5)

        variable2 = IntVar()
        self.r3 = Radiobutton(self.f1,text="Developpement",variable=variable2,value=1)
        self.r3.pack()

        self.r4 = Radiobutton(self.f1,text="Gestion",variable=variable2,value=2)
        self.r4.pack()

        self.r5 = Radiobutton(self.f1,text="Infrastructure",variable=variable2,value=3)
        self.r5.pack()
        if variable2.get()==1:
            self.r3.config(bg="yellow", fg="black")
            self.r3.pack()

        self.l3 = Label(self.f1,text="Email ")
        self.l3.config(bg="yellow", fg="black")
        self.l3.pack(pady=10)

        self.text3 = Entry(self.f1)
        self.text3.pack()

        self.l5 = Label(self.f1,text="Mot De Passe")
        self.l5.config(bg="yellow", fg="black")
        self.l5.pack(pady=10)

        self.text4 = Entry(self.f1,show="*")
        self.text4.pack()

        self.b1 = Button(self.f1,text="S'inscrire",command=self.verifier_inscrire)
        self.b1.config(bg="yellow", fg="black")
        self.b1.pack(side=LEFT)

        self.b2 = Button(self.f1,text="Se Connecter",command=self.se_connecter)
        # self.b2.bind('<Button-1>',self.se_connecter())
        self.b2.config(bg="yellow", fg="black")
        self.b2.pack(side=RIGHT)


        self.f1.mainloop()
    def verifier_inscrire(self):

        index = 0

        for i in range(len(self.email1)):
            if self.text3.get() == self.email1[i]:
                index = i
        if (self.text1.get() in self.nom) and (self.text2.get() in self.prenom) and self.text4.get() == self.mdp1[index]:
            from bienvenue import Afficher
            self.f1.destroy()
            window = Afficher()
            window.create_window()
        else:
            tkinter.messagebox.showinfo("OFPPT", "Information Incorecte")

    def se_connecter(self):
        from seconecter import Se_Connecter
        self.f1.destroy()
        f2 = Se_Connecter()
        f2.se_consecter()

ob = Inscription()
ob.inscrire()