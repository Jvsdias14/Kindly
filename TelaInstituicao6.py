from tkinter import *
from tkinter import filedialog

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
        self.img1 = PhotoImage(file = "C:\\Users\\Pichau\\OneDrive - Firjan\\Arquivos\\Kindly\\Inst6.png")
        self.img2 = PhotoImage(file = "C:\\Users\\Pichau\\OneDrive - Firjan\\Arquivos\\Kindly\\btnPostar.PNG")
        self.img3 = PhotoImage(file = "C:\\Users\\Pichau\\OneDrive - Firjan\\Arquivos\\Kindly\\btnCamera.PNG")
        self.img4 = PhotoImage(file = "C:\\Users\\Pichau\\OneDrive - Firjan\\Arquivos\\Kindly\\btnSetinha.PNG")
    def labels(self):
        self.lbl1 = Label(self.jan, image = self.img1)
        self.lbl1.place(relx = 0, rely = 0, relwidth =1, relheight = 1)
    
    def botoes(self):
        self.btn1 = Button(self.jan, bg = "#131644",bd = 0, activebackground = "#131644", image = self.img2 ,command = lambda: self.teste())
        self.btn1.place(relx = 0.4, rely = 0.33, relwidth = 0.42, relheight = 0.1)
        
        self.btn2 = Button(self.jan, bg = "#131644",bd = 0, activebackground = "#131644", image = self.img3 ,command = lambda: self.selecionar())
        self.btn2.place(relx = 0.14, rely = 0.33, relwidth = 0.2, relheight = 0.1)
        
        self.btn3 = Button(self.jan, bg = "#131644",bd = 0, activebackground = "#131644", image = self.img4 ,command = lambda: self.teste())
        self.btn3.place(relx = 0.07, rely = 0.03, relwidth = 0.15, relheight = 0.06)
    
    def entries(self):
        global entrada1
        entrada1 = StringVar()
        self.ent1 = Entry(self.jan, bg = "#131644", font = "Century\ Gothic 14",fg = "white",bd = 0, textvariable = entrada1)
        self.ent1.place(relx = 0.155, rely = 0.23, relwidth = 0.69, relheight = 0.055)
        entrada1.set("Digite aqui...")

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
        self.limpar(entrada1, "Digite aqui...")
    
    def voltatexto(self,vento=None):
        x = entrada1.get()
        if x == "":
            entrada1.set("Digite aqui...")
    
    def selecionar(self):
        self.nomearq = filedialog.askopenfilename(initialdir ="C:/", title = "Escolher Arquivo")

TelaInst6()
        