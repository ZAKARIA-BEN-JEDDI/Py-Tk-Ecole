from tkinter import *
import tkinter.messagebox

class Motdepass:
    def var(self,f4,l1,l2,l3,text1,text2,text3,b1):
        self.f4=f4
        self.l1=l1
        self.l2=l2
        self.l3=l3
        self.text1=text1
        self.text2=text2
        self.text3=text3
        self.b1=b1

    def mdp(self):
        self.f4 = Tk()
        self.f4.title("Reinitialiser Mdp")
        self.f4.geometry("300x300")

        self.l1 = Label(self.f4,text="Email")
        self.l1.config(bg="yellow", fg="black")
        self.l1.pack(pady=10)

        self.text1 = Entry(self.f4)
        self.text1.pack()

        self.l2 = Label(self.f4,text="Mot De Pass")
        self.l2.config(bg="yellow", fg="black")
        self.l2.pack(pady=10)

        self.text2 = Entry(self.f4)
        self.text2.pack()

        self.l3 = Label(self.f4,text="Rentrer Mot De Pass")
        self.l3.config(bg="yellow", fg="black")
        self.l3.pack(pady=10)

        self.text3 = Entry(self.f4)
        self.text3.pack()

        self.b1 = Button(self.f4,text="Valider",command=self.verifier_mdp)
        self.b1.config(bg="yellow", fg="black")
        self.b1.pack(pady=15)

        self.f4.mainloop()
    def verifier_mdp(self):
        email3 = ["a","b","c","d",]
        boolean = False
        if self.text1.get().isdigit() == False or self.text2.get().isdigit() == False or self.text3.get().isdigit() == False:
            tkinter.messagebox.showinfo("OFPPT","Champ Vide !")
        for i in email3:
            if self.text1.get()== i:
                boolean =True
            else:
                tkinter.messagebox.showinfo("OFPPT", "Information Incorecte !")
        if boolean == True:
            if self.text2.get() == self.text3.get():
                from seconecter import Se_Connecter
                self.f4.destroy()
                f2 = Se_Connecter()
                f2.se_consecter()
        else:
            if boolean == True:
                if self.text2.get() != self.text3.get():
                    tkinter.messagebox.showinfo("OFPPT","Mot de pass Incorecte !")
