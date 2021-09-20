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
        
        self.jan.mainloop()
        
    def imagens(self):    
        self.img1 = PhotoImage(file = "C:\\Users\\Pichau\\OneDrive - Firjan\\Arquivos\\Kindly\\Inst2.png")
        self.img2 = PhotoImage(file = "C:\\Users\\Pichau\\OneDrive - Firjan\\Arquivos\\Kindly\\btnCadastrar.PNG")
        self.img3 = PhotoImage(file = "C:\\Users\\Pichau\\OneDrive - Firjan\\Arquivos\\Kindly\\btnSetinha.PNG")
    
    def labels(self):
        self.lbl1 = Label(self.jan, image = self.img1)
        self.lbl1.place(relx = 0, rely = 0, relwidth =1, relheight = 1)
    
    def botoes(self):
        self.btn1 = Button(self.jan, bg = "#131644",bd = 0, activebackground = "#131644", image = self.img2 ,command = lambda: self.validar())
        self.btn1.place(relx = 0.29, rely = 0.62, relwidth = 0.42, relheight = 0.15)
        
        self.btn2 = Button(self.jan, bg = "#131644",bd = 0, activebackground = "#131644", image = self.img3 ,command = lambda: self.teste())
        self.btn2.place(relx = 0.03, rely = 0.055, relwidth = 0.15, relheight = 0.06)
        
        self.btn3 = Button(self.jan, text = "clique aqui", font = "Century\ Gothic 18",fg = "#FD824F", bg = "#131644",bd = 0, activebackground = "#131644",command = lambda: self.teste())
        self.btn3.place(relx = 0.32, rely = 0.9, relwidth = 0.37, relheight = 0.05)

    def entries(self):
        global entrada1
        entrada1 = StringVar()
        self.ent1 = Entry(self.jan, bg = "#131644", font = "Century\ Gothic 14",fg = "white",bd = 0, textvariable = entrada1)
        self.ent1.place(relx = 0.155, rely = 0.332, relwidth = 0.69, relheight = 0.055)
        entrada1.set("Digite o nome da instituição")
        
        global entrada2
        entrada2 = StringVar()
        self.ent2 = Entry(self.jan, bg = "#131644", font = "Century\ Gothic 14",fg = "white",bd = 0, textvariable = entrada2)
        self.ent2.place(relx = 0.155, rely = 0.426, relwidth = 0.68, relheight = 0.055)
        entrada2.set("Digite seu e-mail")
        
        global entrada3
        entrada3 = StringVar()
        self.ent3 = Entry(self.jan, bg = "#131644", font = "Century\ Gothic 14",fg = "white",bd = 0, textvariable = entrada3)
        self.ent3.place(relx = 0.155, rely = 0.522, relwidth = 0.68, relheight = 0.055)
        entrada3.set("Digite seu código")
    
    def teste(self):
        print("sla")

    def validar(self):
        lbl = Label(self.jan, text = "Código inválido", font = "Century\ Gothic 14",fg = "#FE4A49",bd = 0, bg = "#131644")
        lbl.place(relx = 0.155, rely = 0.59, relwidth = 0.4, relheight = 0.05)

    def limpar1(self,evento=None):
        self.limpar(entrada1, "Digite o nome da instituição")
    
    def limpar2(self,evento=None):
        self.limpar(entrada2, "Digite seu e-mail")
            
    def limpar3(self,evento=None):
        self.limpar(entrada3, "Digite seu código")
            
    def limpar(self, entrada, text):
        x = entrada.get()
        if x == text:
            entrada.set("")
        elif x == "":
            entrada.set(text)
        else:
            entrada.set(x)       
            
TelaInst2e3()