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
        self.ent1.bind("<KeyRelease>",self.maiusculo)
        self.ent2.bind("<1>",self.limpar2)
        self.ent3.bind("<1>",self.limpar3)
        self.ent4.bind("<1>",self.limpar4)
        self.ent5.bind("<1>",self.limpar5)
        self.ent6.bind("<1>",self.limpar6)
        self.lbl1.bind("<1>",self.voltatexto)
        
        self.jan.mainloop()
        
    def imagens(self):    
        self.img1 = PhotoImage(file = "C:\\Users\\Pichau\\OneDrive - Firjan\\Arquivos\\Kindly\\Doador11.png")
        self.img2 = PhotoImage(file = "C:\\Users\\Pichau\\OneDrive - Firjan\\Arquivos\\Kindly\\btnCadastrar.PNG")
        self.img3 = PhotoImage(file = "C:\\Users\\Pichau\\OneDrive - Firjan\\Arquivos\\Kindly\\btnSetinha.PNG")
    
    def labels(self):
        self.lbl1 = Label(self.jan, image = self.img1)
        self.lbl1.place(relx = 0, rely = 0, relwidth =1, relheight = 1)
    
    def botoes(self):
        self.btn1 = Button(self.jan, bg = "#131644",bd = 0, activebackground = "#131644", image = self.img2 ,command = lambda: self.teste())
        self.btn1.place(relx = 0.29, rely = 0.8, relwidth = 0.42, relheight = 0.15)
        
        self.btn2 = Button(self.jan, bg = "#131644",bd = 0, activebackground = "#131644", image = self.img3 ,command = lambda: self.teste())
        self.btn2.place(relx = 0.055, rely = 0.025, relwidth = 0.15, relheight = 0.06)
        

    def entries(self):
        global entrada1
        entrada1 = StringVar()
        self.ent1 = Entry(self.jan, bg = "#131644", font = "Century\ Gothic 14",fg = "white",bd = 0, textvariable = entrada1,insertbackground='white')
        self.ent1.place(relx = 0.155, rely = 0.25, relwidth = 0.69, relheight = 0.055)
        entrada1.set("Nome do cartão")
        
        global entrada2
        entrada2 = StringVar()
        self.ent2 = Entry(self.jan, bg = "#131644", font = "Century\ Gothic 14",fg = "white",bd = 0, textvariable = entrada2,insertbackground='white')
        self.ent2.place(relx = 0.155, rely = 0.35, relwidth = 0.68, relheight = 0.055)
        entrada2.set("CPF/CNPJ")
        
        global entrada3
        entrada3 = StringVar()
        self.ent3 = Entry(self.jan, bg = "#131644", font = "Century\ Gothic 14",fg = "white",bd = 0, textvariable = entrada3,insertbackground='white')
        self.ent3.place(relx = 0.155, rely = 0.447, relwidth = 0.68, relheight = 0.055)
        entrada3.set("Número do cartão")
        
        global entrada4
        entrada4 = StringVar()
        self.ent4 = Entry(self.jan, bg = "#131644", font = "Century\ Gothic 14",fg = "white",bd = 0, textvariable = entrada4,insertbackground='white')
        self.ent4.place(relx = 0.155, rely = 0.545, relwidth = 0.68, relheight = 0.055)
        entrada4.set("CVC")
        
        global entrada5
        entrada5 = StringVar()
        self.ent5 = Entry(self.jan, bg = "#131644", font = "Century\ Gothic 14",fg = "white",bd = 0, textvariable = entrada5,insertbackground='white')
        self.ent5.place(relx = 0.155, rely = 0.64, relwidth = 0.68, relheight = 0.055)
        entrada5.set("Vencimento")
        
        global entrada6
        entrada6 = StringVar()
        self.ent6 = Entry(self.jan, bg = "#131644", font = "Century\ Gothic 14",fg = "white",bd = 0, textvariable = entrada6,insertbackground='white')
        self.ent6.place(relx = 0.155, rely = 0.73, relwidth = 0.68, relheight = 0.055)
        entrada6.set("Bandeira")
    
    def teste(self):
        print("sla")

    def limpar1(self,evento=None):
        self.limpar(entrada1, "Nome do cartão")
    
    def limpar2(self,evento=None):
        self.limpar(entrada2, "CPF/CNPJ")
            
    def limpar3(self,evento=None):
        self.limpar(entrada3, "Número do cartão")
    
    def limpar4(self,evento=None):
        self.limpar(entrada4, "CVC")
        
    def limpar5(self,evento=None):
        self.limpar(entrada5, "Vencimento")
    
    def limpar6(self,evento=None):
        self.limpar(entrada6, "Bandeira")
            
    def limpar(self, entrada, text):
        x = entrada.get()
        if x == text:
            entrada.set("")
        elif x == "":
            entrada.set(text)
        else:
            entrada.set(x)       
    
    def voltatexto(self,evento=None):
        x = entrada1.get()
        if x == "":
            entrada1.set("Nome do cartão") 
        y = entrada2.get()
        if y == "":
            entrada2.set("CPF/CNPJ")
        z = entrada3.get()
        if z == "":
            entrada3.set("Número do cartão") 
        a = entrada4.get()
        if a == "":
            entrada4.set("CVC")
        b = entrada5.get()
        if b == "":
            entrada5.set("Vencimento") 
        c = entrada6.get()
        if c == "":
            entrada6.set("Bandeira")
    
    def maiusculo(self,evento=None):
        x = entrada1.get()        
        x = x.upper()
        entrada1.set(x)
            
TelaInst2e3()