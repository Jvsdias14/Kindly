from tkinter import *

class TelaInst11():
    def __init__(self):
        self.jan = Tk()
        self.jan.geometry("375x667+750+220")
        self.jan.title("Kindly")
        self.jan.resizable(False,False)
        
        self.imagens()
        self.labels()
        self.entries()
        self.botoes()
        self.lisboxes()
        
        self.ent1.bind("<1>",self.limpar1)
        self.lbl1.bind("<1>",self.voltatexto)
        
        self.jan.mainloop()
        
    def imagens(self):    
        self.img1 = PhotoImage(file = "C:\\Users\\Pichau\\OneDrive - Firjan\\Arquivos\\Kindly\\Doador12.png")
        self.img2 = PhotoImage(file = "C:\\Users\\Pichau\\OneDrive - Firjan\\Arquivos\\Kindly\\btnLupinha.PNG")
        self.img3 = PhotoImage(file = "C:\\Users\\Pichau\\OneDrive - Firjan\\Arquivos\\Kindly\\btnSetinha.PNG")
    
    def labels(self):
        self.lbl1 = Label(self.jan, image = self.img1)
        self.lbl1.place(relx = 0, rely = 0, relwidth =1, relheight = 1)
        
    def botoes(self):
       
        self.btn1 = Button(self.jan, bg = "#FEAD77",bd = 0, activebackground = "#FEAD77", image = self.img2 ,command = lambda: self.pesquisa())
        self.btn1.place(relx = 0.86, rely = 0.14, relwidth = 0.1, relheight = 0.075)
        
        self.btn2 = Button(self.jan, bg = "#131644",bd = 0, activebackground = "#131644", image = self.img3 ,command = lambda: self.teste())
        self.btn2.place(relx = 0.06, rely = 0.03, relwidth = 0.15, relheight = 0.06)
    
    def entries(self):
        global entrada1
        entrada1 = StringVar()
        self.ent1 = Entry(self.jan, bg = "#FEAD77", font = "Century\ Gothic 14",fg = "white", textvariable = entrada1, bd = 0)
        self.ent1.place(relx = 0.045, rely = 0.14, relwidth = 0.82, relheight = 0.075)
        entrada1.set("Digite aqui...")
    
    def lisboxes(self):
        self.listb1 = Listbox(self.jan, bg = "#131644",fg = "white", font = "Century\ Gothic 14", bd = 0, selectbackground = "#FEAD77")
        self.listb1.place(relx = 0.01, rely = 0.23, relwidth = 0.98, relheight = 0.41)
        
    def pesquisa(self):
        self.listb1.insert(END, "Nome do instituto")
        self.listb1.insert(END, "Nome do instituto")
        self.listb1.insert(END, "Nome do instituto")
        
    def limpar(self, entrada, text):
        x = entrada.get()
        if x == text:
            entrada.set("")
        elif x == "":
            entrada.set(text)
        else:
            entrada.set(x)
            
    def limpar1(self,evento=None):
        self.limpar(entrada1, "Digite aqui...")
    
    def voltatexto(self,vento=None):
        x = entrada1.get()
        if x == "":
            entrada1.set("Digite aqui...")
        
    def teste(self):
        print("sla")

TelaInst11()