from tkinter import *
import random
import string

class TelaInst6():
    def __init__(self):
        self.jan = Tk()
        self.jan.geometry("375x667+750+220")
        self.jan.title("Kindly")
        self.jan.config(bg = "white")
        self.jan.resizable(False,False)
        
        self.imagens()
        self.labels()
        self.botoes()
        self.entries()
        
        self.ent1.bind("<1>",self.limpar1)
        self.lbl1.bind("<1>",self.voltatexto)
        
        self.jan.mainloop()
        
    def imagens(self):    
        self.img1 = PhotoImage(file = "C:\\Users\\Pichau\\OneDrive - Firjan\\Arquivos\\Kindly\\Doador4.png")
        self.img2 = PhotoImage(file = "C:\\Users\\Pichau\\OneDrive - Firjan\\Arquivos\\Kindly\\btnVerificar.PNG")
        self.img3 = PhotoImage(file = "C:\\Users\\Pichau\\OneDrive - Firjan\\Arquivos\\Kindly\\btnReenviar.PNG")
        self.img4 = PhotoImage(file = "C:\\Users\\Pichau\\OneDrive - Firjan\\Arquivos\\Kindly\\btnSetinha.PNG")
    
    def labels(self):
        self.lbl1 = Label(self.jan, image = self.img1)
        self.lbl1.place(relx = 0, rely = 0, relwidth =1, relheight = 1)
    
    def botoes(self):
        self.btn1 = Button(self.jan, bg = "#131644",bd = 0, activebackground = "#131644", image = self.img2 ,command = lambda: self.teste())
        self.btn1.place(relx = 0.29, rely = 0.59, relwidth = 0.42, relheight = 0.14)
        
        self.btn2 = Button(self.jan, bg = "#131644",bd = 0, activebackground = "#131644", image = self.img3 ,command = lambda: self.createcodigo())
        self.btn2.place(relx = 0.1, rely = 0.47, relwidth = 0.8, relheight = 0.14)
        
        self.btn3 = Button(self.jan, bg = "#131644",bd = 0, activebackground = "#131644", image = self.img4 ,command = lambda: self.teste())
        self.btn3.place(relx = 0.03, rely = 0.06, relwidth = 0.15, relheight = 0.06)

    
    def entries(self):
        global entrada1
        entrada1 = StringVar()
        self.ent1 = Entry(self.jan, bg = "#131644", font = "Century\ Gothic 14",fg = "white",bd = 0, textvariable = entrada1,insertbackground='white')
        self.ent1.place(relx = 0.155, rely = 0.335, relwidth = 0.69, relheight = 0.055)
        entrada1.set("Insira o c??digo")

    def teste(self):
        print("sla")
    
    def limpar(self, entrada, text):
        x = entrada.get()
        if x == text:
            entrada.set("")
        elif x == "":
            entrada.set(text)
        else:
            entrada.set(x)
            
    def limpar1(self,evento=None):
        self.limpar(entrada1, "Insira o c??digo")
    
    def voltatexto(self,vento=None):
        x = entrada1.get()
        if x == "":
            entrada1.set("Insira o c??digo")
    
    def createcodigo(self):
        possibilidades = string.ascii_uppercase + string.digits
        result_str = ''.join(random.choice(possibilidades) for i in range(6))
        print(result_str)
    
TelaInst6()