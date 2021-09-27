from tkinter import *

class TelaInst2e3():
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
        self.ent3.bind("<1>",self.limpar3)
        self.ent4.bind("<1>",self.limpar4)
        self.lbl1.bind("<1>",self.voltatexto)
        
        self.jan.mainloop()
        
    def imagens(self):    
        self.img1 = PhotoImage(file = "C:\\Users\\Pichau\\OneDrive - Firjan\\Arquivos\\Kindly\\Doador6.png")
        self.img2 = PhotoImage(file = "C:\\Users\\Pichau\\OneDrive - Firjan\\Arquivos\\Kindly\\btnCadastrar.PNG")
        self.img3 = PhotoImage(file = "C:\\Users\\Pichau\\OneDrive - Firjan\\Arquivos\\Kindly\\btnSetinha.PNG")
    
    def labels(self):
        self.lbl1 = Label(self.jan, image = self.img1)
        self.lbl1.place(relx = 0, rely = 0, relwidth =1, relheight = 1)
    
    def botoes(self):
        self.btn1 = Button(self.jan, bg = "#131644",bd = 0, activebackground = "#131644", image = self.img2 ,command = lambda: self.teste())
        self.btn1.place(relx = 0.29, rely = 0.8, relwidth = 0.42, relheight = 0.15)
        
        self.btn2 = Button(self.jan, bg = "#131644",bd = 0, activebackground = "#131644", image = self.img3 ,command = lambda: self.teste())
        self.btn2.place(relx = 0.03, rely = 0.055, relwidth = 0.15, relheight = 0.06)
        

    def entries(self):
        global entrada1
        entrada1 = StringVar()
        self.ent1 = Entry(self.jan, bg = "#131644", font = "Century\ Gothic 14",fg = "white",bd = 0, textvariable = entrada1,insertbackground='white')
        self.ent1.place(relx = 0.155, rely = 0.305, relwidth = 0.69, relheight = 0.055)
        entrada1.set("Digite seu nome de usuário")
        
        global entrada2
        entrada2 = StringVar()
        self.ent2 = Entry(self.jan, bg = "#131644", font = "Century\ Gothic 14",fg = "white",bd = 0, textvariable = entrada2,insertbackground='white')
        self.ent2.place(relx = 0.155, rely = 0.435, relwidth = 0.68, relheight = 0.055)
        entrada2.set("Digite seu e-mail")
        
        global entrada3
        entrada3 = StringVar()
        self.ent3 = Entry(self.jan, bg = "#131644", font = "Century\ Gothic 14",fg = "white",bd = 0, textvariable = entrada3,insertbackground='white')
        self.ent3.place(relx = 0.155, rely = 0.57, relwidth = 0.68, relheight = 0.055)
        entrada3.set("Digite sua senha")
        
        global entrada4
        entrada4 = StringVar()
        self.ent4 = Entry(self.jan, bg = "#131644", font = "Century\ Gothic 14",fg = "white",bd = 0, textvariable = entrada4,insertbackground='white')
        self.ent4.place(relx = 0.155, rely = 0.695, relwidth = 0.68, relheight = 0.055)
        entrada4.set("Confirme sua senha")
    
    def teste(self):
        print("sla")

    def limpar1(self,evento=None):
        self.limpar(entrada1, "Digite seu nome de usuário")
    
    def limpar2(self,evento=None):
        self.limpar(entrada2, "Digite seu e-mail")
            
    def limpar3(self,evento=None):
        self.limpar(entrada3, "Digite sua senha")
    
    def limpar4(self,evento=None):
        self.limpar(entrada4, "Confirme sua senha")
            
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
            entrada1.set("Digite seu nome de usuário") 
        y = entrada2.get()
        if y == "":
            entrada2.set("Digite seu e-mail")
        z = entrada3.get()
        if z == "":
            entrada3.set("Digite seu nome de usuário") 
        a = entrada4.get()
        if a == "":
            entrada4.set("Digite seu e-mail")
            
TelaInst2e3()