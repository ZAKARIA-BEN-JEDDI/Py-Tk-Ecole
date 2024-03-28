from tkinter import *
import tkinter.messagebox
class Se_Connecter:
    def variable(self,f2,l1,l2,text1,text2,b1,b2):
        self.f2=f2
        self.l1=l1
        self.l2=l2
        self.text1=text1
        self.text2=text2
        self.b1=b1
        self.b2=b2

    def se_consecter(self):
        self.f2 = Tk()
        self.f2.geometry("300x300")
        self.f2.title("Se Connecter")

        self.l1 = Label(self.f2,text="Email")
        self.l1.config(bg="yellow", fg="black")
        self.l1.pack()
        self.text1 = Entry(self.f2)
        self.text1.pack()

        self.l2 = Label(self.f2,text="Mot De Pass",)
        self.l2.config(bg="yellow", fg="black")
        self.l2.pack()
        self.text2 = Entry(self.f2,show="*")
        self.text2.pack()

        self.b1 = Button(self.f2,text="Se connecter",command=self.verifier_se_connecter)
        self.b1.config(bg="yellow", fg="black")
        self.b1.pack(side=LEFT)

        self.b2 = Button(self.f2,text="Mot De Pass\n  Oublier",command=self.mot_de_pass_oblier)
        self.b2.config(bg="yellow", fg="black")
        self.b2.pack(side=RIGHT)
    def verifier_se_connecter(self):
        from bienvenue import Afficher
        email2 = ["a","b","c","d",]
        mdp2=["a","b","c","d",]
        index2 = 0
        # if self.text1.get().isdigit() == False or self.text2.get().isdigit() == False:
        #     tkinter.messagebox.showinfo("OFPPT","Champ Vide !")
        for i in range(len(email2)):
            if self.text1.get() == email2[i]:
                index2 = i
        if  mdp2[index2] == self.text2.get():
            from bienvenue import Afficher
            self.f2.destroy()
            window = Afficher()
            window.create_window()
        else:
            tkinter.messagebox.showinfo("OFPPT","Email ou Mot de pass Incorecte !")
        self.f2.mainloop()
    def mot_de_pass_oblier(self):
        from oublier import Motdepass
        self.f2.destroy()
        newFenetre = Motdepass()
        newFenetre.mdp()