from tkinter import *

class TelaInst1():
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
        self.ent2.bind("<1>",self.limpar2)
        self.lbl1.bind("<1>",self.voltatexto)
        
        self.jan.mainloop()
        
    def imagens(self):    
        self.img1 = PhotoImage(file = "C:\\Users\\Pichau\\OneDrive - Firjan\\Arquivos\\Kindly\\Doador1.png")
        self.img2 = PhotoImage(file = "C:\\Users\\Pichau\\OneDrive - Firjan\\Arquivos\\Kindly\\btnEntrar.PNG")
        self.img3 = PhotoImage(file = "C:\\Users\\Pichau\\OneDrive - Firjan\\Arquivos\\Kindly\\btnSetinha.PNG")
    
    def labels(self):
        self.lbl1 = Label(self.jan, image = self.img1)
        self.lbl1.place(relx = 0, rely = 0, relwidth =1, relheight = 1)
    
    def botoes(self):
        self.btn1 = Button(self.jan, bg = "#131644",bd = 0, activebackground = "#131644", image = self.img2 ,command = lambda: self.teste())
        self.btn1.place(relx = 0.29, rely = 0.6, relwidth = 0.42, relheight = 0.15)
        
        self.btn2 = Button(self.jan, bg = "#131644",bd = 0, activebackground = "#131644", image = self.img3 ,command = lambda: self.teste())
        self.btn2.place(relx = 0.03, rely = 0.055, relwidth = 0.15, relheight = 0.06)
        
        self.btn3 = Button(self.jan, text = "Crie agora", font = "Century\ Gothic 18",fg = "#FD824F", bg = "#131644",bd = 0, activebackground = "#131644",command = lambda: self.teste())
        self.btn3.place(relx = 0.33, rely = 0.84, relwidth = 0.33, relheight = 0.05)
        
        self.btn4 = Button(self.jan, text = "Esqueceu sua senha?", font = "Century\ Gothic 11",fg = "white", bg = "#131644",bd = 0, activebackground = "#131644",command = lambda: self.teste())
        self.btn4.place(relx = 0.17, rely = 0.54, relwidth = 0.42, relheight = 0.05)

    def entries(self):
        global entrada1
        entrada1 = StringVar()
        self.ent1 = Entry(self.jan, bg = "#131644", font = "Century\ Gothic 14",fg = "white",bd = 0, textvariable = entrada1,insertbackground='white')
        self.ent1.place(relx = 0.16, rely = 0.335, relwidth = 0.68, relheight = 0.06)
        entrada1.set("Digite seu e-mail")
        
        global entrada2
        entrada2 = StringVar()
        self.ent2 = Entry(self.jan, bg = "#131644", font = "Century\ Gothic 14",fg = "white",bd = 0, textvariable = entrada2,insertbackground='white')
        self.ent2.place(relx = 0.16, rely = 0.468, relwidth = 0.68, relheight = 0.06)
        entrada2.set("Digite seu código")

    def limpar1(self,evento=None):
        self.limpar(entrada1, "Digite seu e-mail")
    
    def limpar2(self,evento=None):
        self.limpar(entrada2, "Digite seu código")

    def limpar(self, entrada, text):
        x = entrada.get()
        if x == text:
            entrada.set("")
        elif x == "":
            entrada.set(text)
        else:
            entrada.set(x)
    
    def voltatexto(self,vento=None):
        x = entrada1.get()
        if x == "":
            entrada1.set("Digite seu e-mail") 
        y = entrada2.get()
        if y == "":
            entrada2.set("Digite seu código")
    
    def teste(self):
        print("sla")

TelaInst1()