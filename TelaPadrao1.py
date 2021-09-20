from tkinter import *

class Padrao1():
    def __init__(self):
        self.jan = Tk()
        self.jan.geometry("375x667+750+220")
        self.jan.title("Kindly")
        self.jan.config(bg = "white")
        self.jan.resizable(False,False)
        self.imagens()
        self.labels()
        self.jan.mainloop()
        
    def imagens(self):    
        self.img1 = PhotoImage(file = "C:\\Users\\Pichau\\OneDrive - Firjan\\Arquivos\\Kindly\\Padrao1.png")
    
    def labels(self):
        self.lbl1 = Label(self.jan, image = self.img1)
        self.lbl1.place(relx = 0, rely = 0, relwidth =1, relheight = 1)
        
Padrao1()
        