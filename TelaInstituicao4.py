from tkinter import *

class TelaIsnt4():
    def __init__(self):
        self.jan = Tk()
        self.jan.geometry("375x667+750+220")
        self.jan.title("Kindly")
        self.jan.config(bg = "white")
        self.jan.resizable(False,False)
        self.imagens()
        self.labels()
        self.botoes()
        self.jan.mainloop()
        
    def imagens(self):    
        self.img1 = PhotoImage(file = "C:\\Users\\Pichau\\OneDrive - Firjan\\Arquivos\\Kindly\\Inst4.png")
        self.img2 = PhotoImage(file = "C:\\Users\\Pichau\\OneDrive - Firjan\\Arquivos\\Kindly\\btnSeta.PNG")
    
    def labels(self):
        self.lbl1 = Label(self.jan, image = self.img1)
        self.lbl1.place(relx = 0, rely = 0, relwidth =1, relheight = 1)
    
    def botoes(self):
        self.btn1 = Button(self.jan, bg = "#131644",bd = 0, activebackground = "#131644", image = self.img2 ,command = lambda: self.teste())
        self.btn1.place(relx = 0.13, rely = 0.75, relwidth = 0.74, relheight = 0.15)

    def teste(self):
        print("sla")

TelaIsnt4()
        