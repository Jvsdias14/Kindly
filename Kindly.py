from tkinter import *
from threading import Timer
from tkinter import filedialog

class Kindly():
    def __init__(self):
        self.jan = Tk()
        self.jan.geometry("375x667+750+220")
        self.jan.title("Kindly")
        self.jan.config(bg = "white")
        self.jan.resizable(False,False)
        
        self.imagens()
        self.labels()
        
        t = Timer(2, self.Padrao2)
        t.start()
        
        self.jan.mainloop()
        
    def teste(self):
        print("sla")
    
    def selecionar(self):
        self.nomearq = filedialog.askopenfilename(initialdir ="C:/", title = "Escolher Arquivo")
    
    def imagens(self):    
        self.img1 = PhotoImage(file = "C:\\Users\\Pichau\\OneDrive - Firjan\\Arquivos\\Kindly\\Padrao1.png")
    
    def labels(self):
        self.lbl1 = Label(self.jan, image = self.img1)
        self.lbl1.place(relx = 0, rely = 0, relwidth =1, relheight = 1)
    
    def Padrao2(self):
        self.img1 = PhotoImage(file = "C:\\Users\\Pichau\\OneDrive - Firjan\\Arquivos\\Kindly\\Padrao2.png")
        self.img2 = PhotoImage(file = "C:\\Users\\Pichau\\OneDrive - Firjan\\Arquivos\\Kindly\\btn1 TelaPadrao2.PNG")
        self.img3 = PhotoImage(file = "C:\\Users\\Pichau\\OneDrive - Firjan\\Arquivos\\Kindly\\btn2 TelaPadrao2.PNG")
    
        self.lbl1 = Label(self.jan, image = self.img1)
        self.lbl1.place(relx = 0, rely = 0, relwidth =1, relheight = 1)
    
        self.btn1 = Button(self.jan, bg = "#131644",bd = 0, activebackground = "#131644", image = self.img2 ,command = lambda: self.telainst1())
        self.btn1.place(relx = 0.13, rely = 0.42, relwidth = 0.74, relheight = 0.15)
        self.btn2 = Button(self.jan, bg = "#131644",bd = 0, activebackground = "#131644", image = self.img3 ,command = lambda: self.teste())
        self.btn2.place(relx = 0.13, rely = 0.58, relwidth = 0.74, relheight = 0.15)

    
    def telainst1(self):

        self.img1 = PhotoImage(file = "C:\\Users\\Pichau\\OneDrive - Firjan\\Arquivos\\Kindly\\Inst1.png")
        self.img2 = PhotoImage(file = "C:\\Users\\Pichau\\OneDrive - Firjan\\Arquivos\\Kindly\\btnEntrar.PNG")
        self.img3 = PhotoImage(file = "C:\\Users\\Pichau\\OneDrive - Firjan\\Arquivos\\Kindly\\btnSetinha.PNG")


        self.lbl1 = Label(self.jan, image = self.img1)
        self.lbl1.place(relx = 0, rely = 0, relwidth =1, relheight = 1)


        self.btn1 = Button(self.jan, bg = "#131644",bd = 0, activebackground = "#131644", image = self.img2 ,command = lambda: self.telainst5())
        self.btn1.place(relx = 0.29, rely = 0.565, relwidth = 0.42, relheight = 0.15)
        
        self.btn2 = Button(self.jan, bg = "#131644",bd = 0, activebackground = "#131644", image = self.img3 ,command = lambda: self.Padrao2())
        self.btn2.place(relx = 0.03, rely = 0.055, relwidth = 0.15, relheight = 0.06)
        
        self.btn3 = Button(self.jan, text = "Crie agora", font = "Century\ Gothic 18",fg = "#FD824F", bg = "#131644",bd = 0, activebackground = "#131644",command = lambda: self.telainst2e3())
        self.btn3.place(relx = 0.33, rely = 0.84, relwidth = 0.33, relheight = 0.05)


        global entrada1
        entrada1 = StringVar()
        self.ent1 = Entry(self.jan, bg = "#131644", font = "Century\ Gothic 14",fg = "white",bd = 0, textvariable = entrada1)
        self.ent1.place(relx = 0.16, rely = 0.335, relwidth = 0.68, relheight = 0.06)
        entrada1.set("Digite seu e-mail")
        
        global entrada2
        entrada2 = StringVar()
        self.ent2 = Entry(self.jan, bg = "#131644", font = "Century\ Gothic 14",fg = "white",bd = 0, textvariable = entrada2)
        self.ent2.place(relx = 0.16, rely = 0.468, relwidth = 0.68, relheight = 0.06)
        entrada2.set("Digite seu código")
        
        self.ent1.bind("<1>",self.limpart11)
        self.ent2.bind("<1>",self.limpart12)

    def limpart11(self,evento=None):
        self.limpar(entrada1, "Digite seu e-mail")
    
    def limpart12(self,evento=None):
        self.limpar(entrada2, "Digite seu código")

    def limpar(self, entrada, text):
        x = entrada.get()
        if x == text:
            entrada.set("")
        elif x == "":
            entrada.set(text)
        else:
            entrada.set(x)      
    
    
    def telainst2e3(self):
        self.img1 = PhotoImage(file = "C:\\Users\\Pichau\\OneDrive - Firjan\\Arquivos\\Kindly\\Inst2.png")
        self.img2 = PhotoImage(file = "C:\\Users\\Pichau\\OneDrive - Firjan\\Arquivos\\Kindly\\btnCadastrar.PNG")
        self.img3 = PhotoImage(file = "C:\\Users\\Pichau\\OneDrive - Firjan\\Arquivos\\Kindly\\btnSetinha.PNG")
    
        
        self.lbl1 = Label(self.jan, image = self.img1)
        self.lbl1.place(relx = 0, rely = 0, relwidth =1, relheight = 1)
    
        
        self.btn1 = Button(self.jan, bg = "#131644",bd = 0, activebackground = "#131644", image = self.img2 ,command = lambda: self.validar())
        self.btn1.place(relx = 0.29, rely = 0.62, relwidth = 0.42, relheight = 0.15)
        
        self.btn2 = Button(self.jan, bg = "#131644",bd = 0, activebackground = "#131644", image = self.img3 ,command = lambda: self.telainst1())
        self.btn2.place(relx = 0.03, rely = 0.055, relwidth = 0.15, relheight = 0.06)
        
        self.btn3 = Button(self.jan, text = "clique aqui", font = "Century\ Gothic 18",fg = "#FD824F", bg = "#131644",bd = 0, activebackground = "#131644",command = lambda: self.telainst4())
        self.btn3.place(relx = 0.32, rely = 0.9, relwidth = 0.37, relheight = 0.05)


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
        
        self.ent1.bind("<1>",self.limpar21)
        self.ent2.bind("<1>",self.limpar22)
        self.ent3.bind("<1>",self.limpar23)

    def validar(self):
        lbl = Label(self.jan, text = "Código inválido", font = "Century\ Gothic 14",fg = "#FE4A49",bd = 0, bg = "#131644")
        lbl.place(relx = 0.155, rely = 0.59, relwidth = 0.4, relheight = 0.05)

    def limpar21(self,evento=None):
        self.limpar(entrada1, "Digite o nome da instituição")
    
    def limpar22(self,evento=None):
        self.limpar(entrada2, "Digite seu e-mail")
            
    def limpar23(self,evento=None):
        self.limpar(entrada3, "Digite seu código")
    

    def telainst4(self):
           
        self.img1 = PhotoImage(file = "C:\\Users\\Pichau\\OneDrive - Firjan\\Arquivos\\Kindly\\Inst4.png")
        self.img2 = PhotoImage(file = "C:\\Users\\Pichau\\OneDrive - Firjan\\Arquivos\\Kindly\\btnSeta.PNG")
    
        self.lbl1 = Label(self.jan, image = self.img1)
        self.lbl1.place(relx = 0, rely = 0, relwidth =1, relheight = 1)

        self.btn1 = Button(self.jan, bg = "#131644",bd = 0, activebackground = "#131644", image = self.img2 ,command = lambda: self.telainst2e3())
        self.btn1.place(relx = 0.13, rely = 0.75, relwidth = 0.74, relheight = 0.15)

    def telainst5(self):
           
        self.img1 = PhotoImage(file = "C:\\Users\\Pichau\\OneDrive - Firjan\\Arquivos\\Kindly\\Inst5.png")
        self.img2 = PhotoImage(file = "C:\\Users\\Pichau\\OneDrive - Firjan\\Arquivos\\Kindly\\btnPerfil.PNG")
        self.img3 = PhotoImage(file = "C:\\Users\\Pichau\\OneDrive - Firjan\\Arquivos\\Kindly\\btnChat.PNG")
        self.img4 = PhotoImage(file = "C:\\Users\\Pichau\\OneDrive - Firjan\\Arquivos\\Kindly\\btnLupa.PNG")
        self.img5 = PhotoImage(file = "C:\\Users\\Pichau\\OneDrive - Firjan\\Arquivos\\Kindly\\btnPerfilmaior.PNG")
        self.img6 = PhotoImage(file = "C:\\Users\\Pichau\\OneDrive - Firjan\\Arquivos\\Kindly\\btn+.PNG")
    
    
        self.lbl1 = Label(self.jan, image = self.img1)
        self.lbl1.place(relx = 0, rely = 0, relwidth =1, relheight = 1)
        
        self.lbl2 = Label(self.jan, bg = "#BDAB9F", fg = "black", text = "Nome da instituição", font = " Century\ Gothic 14")
        self.lbl2.place(relx = 0.18, rely = 0.145, relwidth =0.62, relheight = 0.04)
        
        self.lbl3 = Label(self.jan, bg = "#BDAB9F", fg = "black", text = "Nome da instituição", font = " Century\ Gothic 14")
        self.lbl3.place(relx = 0.18, rely = 0.695, relwidth =0.62, relheight = 0.04)
        

        self.btn1 = Button(self.jan, bg = "#131644",bd = 0, activebackground = "#131644", image = self.img2 ,command = lambda: self.telainst7())
        self.btn1.place(relx = 0.035, rely = 0.009, relwidth = 0.12, relheight = 0.08)
       
        self.btn2 = Button(self.jan, bg = "#131644",bd = 0, activebackground = "#131644", image = self.img3 ,command = lambda: self.telainst10())
        self.btn2.place(relx = 0.64, rely = 0.009, relwidth = 0.15, relheight = 0.08)
        
        self.btn3 = Button(self.jan, bg = "#131644",bd = 0, activebackground = "#131644", image = self.img4 ,command = lambda: self.telainst13())
        self.btn3.place(relx = 0.83, rely = 0.009, relwidth = 0.15, relheight = 0.08)
        
        self.btn4 = Button(self.jan, bg = "#131644",bd = 0, activebackground = "#131644", image = self.img5 ,command = lambda: self.telainst9())
        self.btn4.place(relx = 0.02, rely = 0.1, relwidth = 0.17, relheight = 0.12)
        
        self.btn5 = Button(self.jan, bg = "#131644",bd = 0, activebackground = "#131644", image = self.img5 ,command = lambda: self.telainst9())
        self.btn5.place(relx = 0.02, rely = 0.65, relwidth = 0.17, relheight = 0.12)
        
        self.btn6 = Button(self.jan, bd = 0, image = self.img6 ,command = lambda: self.telainst6())
        self.btn6.place(relx = 0.8, rely = 0.75, relwidth = 0.17, relheight = 0.09)
        
    def telainst6(self):
         
        self.img1 = PhotoImage(file = "C:\\Users\\Pichau\\OneDrive - Firjan\\Arquivos\\Kindly\\Inst6.png")
        self.img2 = PhotoImage(file = "C:\\Users\\Pichau\\OneDrive - Firjan\\Arquivos\\Kindly\\btnPostar.PNG")
        self.img3 = PhotoImage(file = "C:\\Users\\Pichau\\OneDrive - Firjan\\Arquivos\\Kindly\\btnCamera.PNG")
        self.img4 = PhotoImage(file = "C:\\Users\\Pichau\\OneDrive - Firjan\\Arquivos\\Kindly\\btnSetinha.PNG")
    
        self.lbl1 = Label(self.jan, image = self.img1)
        self.lbl1.place(relx = 0, rely = 0, relwidth =1, relheight = 1)
    
    
        self.btn1 = Button(self.jan, bg = "#131644",bd = 0, activebackground = "#131644", image = self.img2 ,command = lambda: self.telainst5())
        self.btn1.place(relx = 0.4, rely = 0.33, relwidth = 0.42, relheight = 0.1)
        
        self.btn2 = Button(self.jan, bg = "#131644",bd = 0, activebackground = "#131644", image = self.img3 ,command = lambda: self.selecionar())
        self.btn2.place(relx = 0.14, rely = 0.33, relwidth = 0.2, relheight = 0.1)
        
        self.btn3 = Button(self.jan, bg = "#131644",bd = 0, activebackground = "#131644", image = self.img4 ,command = lambda: self.telainst5())
        self.btn3.place(relx = 0.07, rely = 0.03, relwidth = 0.15, relheight = 0.06)
    
    
        global entrada1
        entrada1 = StringVar()
        self.ent1 = Entry(self.jan, bg = "#131644", font = "Century\ Gothic 14",fg = "white",bd = 0, textvariable = entrada1)
        self.ent1.place(relx = 0.155, rely = 0.23, relwidth = 0.69, relheight = 0.055)
        entrada1.set("Digite aqui...")
        
        self.ent1.bind("<1>",self.limpar61)
        self.lbl1.bind("<1>",self.voltatexto)
            
    def limpar61(self,evento=None):
        self.limpar(entrada1, "Digite aqui...")
    
    def voltatexto(self,evento=None):
        x = entrada1.get()
        if x == "":
            entrada1.set("Digite aqui...")
        
    def telainst7(self):
          
        self.img1 = PhotoImage(file = "C:\\Users\\Pichau\\OneDrive - Firjan\\Arquivos\\Kindly\\Inst7.png")
        self.img2 = PhotoImage(file = "C:\\Users\\Pichau\\OneDrive - Firjan\\Arquivos\\Kindly\\btnPerfilgg.PNG")
        self.img3 = PhotoImage(file = "C:\\Users\\Pichau\\OneDrive - Firjan\\Arquivos\\Kindly\\btnDinheiro.PNG")
        self.img4 = PhotoImage(file = "C:\\Users\\Pichau\\OneDrive - Firjan\\Arquivos\\Kindly\\btnSetinha.PNG")
        self.img5 = PhotoImage(file = "C:\\Users\\Pichau\\OneDrive - Firjan\\Arquivos\\Kindly\\btnCamerabranca.PNG")
    
    
        self.lbl1 = Label(self.jan, image = self.img1)
        self.lbl1.place(relx = 0, rely = 0, relwidth =1, relheight = 1)
        
        self.lbl2 = Label(self.jan, bg = "#BDAB9F", fg = "black", text = "Nome da instituição", font = " Century\ Gothic 14")
        self.lbl2.place(relx = 0.32, rely = 0.165, relwidth =0.62, relheight = 0.04)
        

        self.btn1 = Button(self.jan, bg = "#131644",bd = 0, activebackground = "#131644", image = self.img2 ,command = lambda: self.teste())
        self.btn1.place(relx = 0.05, rely = 0.123, relwidth = 0.22, relheight = 0.14)
       
        self.btn2 = Button(self.jan, bg = "#131644",bd = 0, activebackground = "#131644", image = self.img3 ,command = lambda: self.telainst8())
        self.btn2.place(relx = 0.76, rely = 0.01, relwidth = 0.15, relheight = 0.08)
        
        self.btn3 = Button(self.jan, bg = "#131644",bd = 0, activebackground = "#131644", image = self.img4 ,command = lambda: self.telainst5())
        self.btn3.place(relx = 0.07, rely = 0.03, relwidth = 0.15, relheight = 0.06)
        
        self.btn4 = Button(self.jan, bg = "white",bd = 0, activebackground = "white", image = self.img5 ,command = lambda: self.selecionar())
        self.btn4.place(relx = 0.16, rely = 0.56, relwidth = 0.16, relheight = 0.1)
        
    def telainst8(self):
        self.img1 = PhotoImage(file = "C:\\Users\\Pichau\\OneDrive - Firjan\\Arquivos\\Kindly\\Inst8.png")
        self.img2 = PhotoImage(file = "C:\\Users\\Pichau\\OneDrive - Firjan\\Arquivos\\Kindly\\btnPerfilmaior.PNG")
        self.img3 = PhotoImage(file = "C:\\Users\\Pichau\\OneDrive - Firjan\\Arquivos\\Kindly\\btnSetinha.PNG")
    
        
        self.lbl1 = Label(self.jan, image = self.img1)
        self.lbl1.place(relx = 0, rely = 0, relwidth =1, relheight = 1)
    
        self.btn1 = Button(self.jan, bg = "#131644",bd = 0, activebackground = "gray",command = lambda: self.teste())
        self.btn1.place(relx = 0, rely = 0.235, relwidth = 1, relheight = 0.11)
       
        self.btn2 = Button(self.jan, bg = "#131644",bd = 0, activebackground = "#131644", image = self.img2 ,command = lambda: self.teste())
        self.btn2.place(relx = 0.05, rely = 0.235, relwidth = 0.17, relheight = 0.11)
        
        self.btn1 = Button(self.jan, bg = "#131644",bd = 0, activebackground = "gray",command = lambda: self.teste())
        self.btn1.place(relx = 0, rely = 0.345, relwidth = 1, relheight = 0.11)
       
        self.btn2 = Button(self.jan, bg = "#131644",bd = 0, activebackground = "#131644", image = self.img2 ,command = lambda: self.teste())
        self.btn2.place(relx = 0.05, rely = 0.345, relwidth = 0.17, relheight = 0.11)
        
        self.btn1 = Button(self.jan, bg = "#131644",bd = 0, activebackground = "gray",command = lambda: self.teste())
        self.btn1.place(relx = 0, rely = 0.455, relwidth = 1, relheight = 0.11)
       
        self.btn2 = Button(self.jan, bg = "#131644",bd = 0, activebackground = "#131644", image = self.img2 ,command = lambda: self.teste())
        self.btn2.place(relx = 0.05, rely = 0.455, relwidth = 0.17, relheight = 0.11)
        
        self.btn1 = Button(self.jan, bg = "#131644",bd = 0, activebackground = "gray",command = lambda: self.teste())
        self.btn1.place(relx = 0, rely = 0.565, relwidth = 1, relheight = 0.11)
       
        self.btn2 = Button(self.jan, bg = "#131644",bd = 0, activebackground = "#131644", image = self.img2 ,command = lambda: self.teste())
        self.btn2.place(relx = 0.05, rely = 0.565, relwidth = 0.17, relheight = 0.11)
        
        self.btn1 = Button(self.jan, bg = "#131644",bd = 0, activebackground = "gray",command = lambda: self.teste())
        self.btn1.place(relx = 0, rely = 0.675, relwidth = 1, relheight = 0.11)
       
        self.btn2 = Button(self.jan, bg = "#131644",bd = 0, activebackground = "#131644", image = self.img2 ,command = lambda: self.teste())
        self.btn2.place(relx = 0.05, rely = 0.675, relwidth = 0.17, relheight = 0.11)
        
        self.btn1 = Button(self.jan, bg = "#131644",bd = 0, activebackground = "gray",command = lambda: self.teste())
        self.btn1.place(relx = 0, rely = 0.785, relwidth = 1, relheight = 0.11)
       
        self.btn2 = Button(self.jan, bg = "#131644",bd = 0, activebackground = "#131644", image = self.img2 ,command = lambda: self.teste())
        self.btn2.place(relx = 0.05, rely = 0.785, relwidth = 0.17, relheight = 0.11)
        
        self.btn1 = Button(self.jan, bg = "#131644",bd = 0, activebackground = "gray",command = lambda: self.teste())
        self.btn1.place(relx = 0, rely = 0.895, relwidth = 1, relheight = 0.11)
       
        self.btn2 = Button(self.jan, bg = "#131644",bd = 0, activebackground = "#131644", image = self.img2 ,command = lambda: self.teste())
        self.btn2.place(relx = 0.05, rely = 0.895, relwidth = 0.17, relheight = 0.11)
        
        self.btn3 = Button(self.jan, bg = "#131644",bd = 0, activebackground = "#131644", image = self.img3 ,command = lambda: self.telainst7())
        self.btn3.place(relx = 0.07, rely = 0.03, relwidth = 0.15, relheight = 0.06)


        self.lbl2 = Label(self.jan, bg = "#131644", fg = "white", text = "Nome do doador", font = " Century\ Gothic 14",anchor = "w")
        self.lbl2.place(relx = 0.26, rely = 0.25, relwidth =0.55, relheight = 0.04)
        
        self.lbl3 = Label(self.jan, bg = "#131644", fg = "white", text = "Doou R$...", font = " Century\ Gothic 10",anchor= "w")
        self.lbl3.place(relx = 0.26, rely = 0.29, relwidth =0.55, relheight = 0.03)
        
        self.lbl2 = Label(self.jan, bg = "#131644", fg = "white", text = "Nome do doador", font = " Century\ Gothic 14",anchor = "w")
        self.lbl2.place(relx = 0.26, rely = 0.365, relwidth =0.55, relheight = 0.04)
        
        self.lbl3 = Label(self.jan, bg = "#131644", fg = "white", text = "Doou R$...", font = " Century\ Gothic 10",anchor= "w")
        self.lbl3.place(relx = 0.26, rely = 0.405, relwidth =0.55, relheight = 0.03)
        
        self.lbl2 = Label(self.jan, bg = "#131644", fg = "white", text = "Nome do doador", font = " Century\ Gothic 14",anchor = "w")
        self.lbl2.place(relx = 0.26, rely = 0.475, relwidth =0.55, relheight = 0.04)
        
        self.lbl3 = Label(self.jan, bg = "#131644", fg = "white", text = "Doou R$...", font = " Century\ Gothic 10",anchor= "w")
        self.lbl3.place(relx = 0.26, rely = 0.515, relwidth =0.55, relheight = 0.03)
        
        self.lbl2 = Label(self.jan, bg = "#131644", fg = "white", text = "Nome do doador", font = " Century\ Gothic 14",anchor = "w")
        self.lbl2.place(relx = 0.26, rely = 0.585, relwidth =0.55, relheight = 0.04)
        
        self.lbl3 = Label(self.jan, bg = "#131644", fg = "white", text = "Doou R$...", font = " Century\ Gothic 10",anchor= "w")
        self.lbl3.place(relx = 0.26, rely = 0.625, relwidth =0.55, relheight = 0.03)
        
        self.lbl2 = Label(self.jan, bg = "#131644", fg = "white", text = "Nome do doador", font = " Century\ Gothic 14",anchor = "w")
        self.lbl2.place(relx = 0.26, rely = 0.695, relwidth =0.55, relheight = 0.04)
        
        self.lbl3 = Label(self.jan, bg = "#131644", fg = "white", text = "Doou R$...", font = " Century\ Gothic 10",anchor= "w")
        self.lbl3.place(relx = 0.26, rely = 0.735, relwidth =0.55, relheight = 0.03)
        
        self.lbl2 = Label(self.jan, bg = "#131644", fg = "white", text = "Nome do doador", font = " Century\ Gothic 14",anchor = "w")
        self.lbl2.place(relx = 0.26, rely = 0.805, relwidth =0.55, relheight = 0.04)
        
        self.lbl3 = Label(self.jan, bg = "#131644", fg = "white", text = "Doou R$...", font = " Century\ Gothic 10",anchor= "w")
        self.lbl3.place(relx = 0.26, rely = 0.845, relwidth =0.55, relheight = 0.03)
        
        self.lbl2 = Label(self.jan, bg = "#131644", fg = "white", text = "Nome do doador", font = " Century\ Gothic 14",anchor = "w")
        self.lbl2.place(relx = 0.26, rely = 0.915, relwidth =0.55, relheight = 0.04)
        
        self.lbl3 = Label(self.jan, bg = "#131644", fg = "white", text = "Doou R$...", font = " Century\ Gothic 10",anchor= "w")
        self.lbl3.place(relx = 0.26, rely = 0.955, relwidth =0.55, relheight = 0.03)
        
    def telainst9(self):
       
        self.img1 = PhotoImage(file = "C:\\Users\\Pichau\\OneDrive - Firjan\\Arquivos\\Kindly\\Inst9.png")
        self.img2 = PhotoImage(file = "C:\\Users\\Pichau\\OneDrive - Firjan\\Arquivos\\Kindly\\btnPerfilgg.PNG")
        self.img3 = PhotoImage(file = "C:\\Users\\Pichau\\OneDrive - Firjan\\Arquivos\\Kindly\\btnSetinha.PNG")
    
        
        self.lbl1 = Label(self.jan, image = self.img1)
        self.lbl1.place(relx = 0, rely = 0, relwidth =1, relheight = 1)
        
        self.lbl2 = Label(self.jan, bg = "#BDAB9F", fg = "black", text = "Nome da instituição", font = " Century\ Gothic 14")
        self.lbl2.place(relx = 0.32, rely = 0.165, relwidth =0.62, relheight = 0.04)
        
   
        self.btn1 = Button(self.jan, bg = "#131644",bd = 0, activebackground = "#131644", image = self.img2 ,command = lambda: self.teste())
        self.btn1.place(relx = 0.05, rely = 0.123, relwidth = 0.22, relheight = 0.14)
        
        self.btn2 = Button(self.jan, bg = "#131644",bd = 0, activebackground = "#131644", image = self.img3 ,command = lambda: self.telainst5())
        self.btn2.place(relx = 0.07, rely = 0.03, relwidth = 0.15, relheight = 0.06)
    
    def telainst10(self):  
        self.img1 = PhotoImage(file = "C:\\Users\\Pichau\\OneDrive - Firjan\\Arquivos\\Kindly\\Inst10.png")
        self.img2 = PhotoImage(file = "C:\\Users\\Pichau\\OneDrive - Firjan\\Arquivos\\Kindly\\btnPerfilmaior.PNG")
        self.img3 = PhotoImage(file = "C:\\Users\\Pichau\\OneDrive - Firjan\\Arquivos\\Kindly\\btnSetinha.PNG")
    

        self.lbl1 = Label(self.jan, image = self.img1)
        self.lbl1.place(relx = 0, rely = 0, relwidth =1, relheight = 1)
    
        self.btn1 = Button(self.jan, bg = "#131644",bd = 0, activebackground = "gray",command = lambda: self.telainst11())
        self.btn1.place(relx = 0, rely = 0.125, relwidth = 1, relheight = 0.11)
       
        self.btn2 = Button(self.jan, bg = "#131644",bd = 0, activebackground = "#131644", image = self.img2 ,command = lambda: self.telainst12())
        self.btn2.place(relx = 0.05, rely = 0.125, relwidth = 0.17, relheight = 0.11)
        
        self.btn1 = Button(self.jan, bg = "#131644",bd = 0, activebackground = "gray",command = lambda: self.telainst11())
        self.btn1.place(relx = 0, rely = 0.235, relwidth = 1, relheight = 0.11)
       
        self.btn2 = Button(self.jan, bg = "#131644",bd = 0, activebackground = "#131644", image = self.img2 ,command = lambda: self.telainst12())
        self.btn2.place(relx = 0.05, rely = 0.235, relwidth = 0.17, relheight = 0.11)
        
        self.btn1 = Button(self.jan, bg = "#131644",bd = 0, activebackground = "gray",command = lambda: self.telainst11())
        self.btn1.place(relx = 0, rely = 0.345, relwidth = 1, relheight = 0.11)
       
        self.btn2 = Button(self.jan, bg = "#131644",bd = 0, activebackground = "#131644", image = self.img2 ,command = lambda: self.telainst12())
        self.btn2.place(relx = 0.05, rely = 0.345, relwidth = 0.17, relheight = 0.11)
        
        self.btn1 = Button(self.jan, bg = "#131644",bd = 0, activebackground = "gray",command = lambda: self.telainst11())
        self.btn1.place(relx = 0, rely = 0.455, relwidth = 1, relheight = 0.11)
       
        self.btn2 = Button(self.jan, bg = "#131644",bd = 0, activebackground = "#131644", image = self.img2 ,command = lambda: self.telainst12())
        self.btn2.place(relx = 0.05, rely = 0.455, relwidth = 0.17, relheight = 0.11)
        
        self.btn1 = Button(self.jan, bg = "#131644",bd = 0, activebackground = "gray",command = lambda: self.telainst11())
        self.btn1.place(relx = 0, rely = 0.565, relwidth = 1, relheight = 0.11)
       
        self.btn2 = Button(self.jan, bg = "#131644",bd = 0, activebackground = "#131644", image = self.img2 ,command = lambda: self.telainst12())
        self.btn2.place(relx = 0.05, rely = 0.565, relwidth = 0.17, relheight = 0.11)
        
        self.btn1 = Button(self.jan, bg = "#131644",bd = 0, activebackground = "gray",command = lambda: self.telainst11())
        self.btn1.place(relx = 0, rely = 0.675, relwidth = 1, relheight = 0.11)
       
        self.btn2 = Button(self.jan, bg = "#131644",bd = 0, activebackground = "#131644", image = self.img2 ,command = lambda: self.telainst12())
        self.btn2.place(relx = 0.05, rely = 0.675, relwidth = 0.17, relheight = 0.11)
        
        self.btn1 = Button(self.jan, bg = "#131644",bd = 0, activebackground = "gray",command = lambda: self.telainst11())
        self.btn1.place(relx = 0, rely = 0.785, relwidth = 1, relheight = 0.11)
       
        self.btn2 = Button(self.jan, bg = "#131644",bd = 0, activebackground = "#131644", image = self.img2 ,command = lambda: self.telainst12())
        self.btn2.place(relx = 0.05, rely = 0.785, relwidth = 0.17, relheight = 0.11)
        
        self.btn1 = Button(self.jan, bg = "#131644",bd = 0, activebackground = "gray",command = lambda: self.telainst11())
        self.btn1.place(relx = 0, rely = 0.895, relwidth = 1, relheight = 0.11)
       
        self.btn2 = Button(self.jan, bg = "#131644",bd = 0, activebackground = "#131644", image = self.img2 ,command = lambda: self.telainst12())
        self.btn2.place(relx = 0.05, rely = 0.895, relwidth = 0.17, relheight = 0.11)
        
        self.btn3 = Button(self.jan, bg = "#131644",bd = 0, activebackground = "#131644", image = self.img3 ,command = lambda: self.telainst5())
        self.btn3.place(relx = 0.07, rely = 0.03, relwidth = 0.15, relheight = 0.06)
        
        
        self.lbl2 = Label(self.jan, bg = "#131644", fg = "white", text = "Nome do doador", font = " Century\ Gothic 14",anchor = "w")
        self.lbl2.place(relx = 0.26, rely = 0.145, relwidth =0.55, relheight = 0.04)
        
        self.lbl3 = Label(self.jan, bg = "#131644", fg = "white", text = "Msg...", font = " Century\ Gothic 10",anchor= "w")
        self.lbl3.place(relx = 0.26, rely = 0.185, relwidth =0.55, relheight = 0.03)
        
        self.lbl2 = Label(self.jan, bg = "#131644", fg = "white", text = "Nome do doador", font = " Century\ Gothic 14",anchor = "w")
        self.lbl2.place(relx = 0.26, rely = 0.255, relwidth =0.55, relheight = 0.04)
        
        self.lbl3 = Label(self.jan, bg = "#131644", fg = "white", text = "Msg...", font = " Century\ Gothic 10",anchor= "w")
        self.lbl3.place(relx = 0.26, rely = 0.295, relwidth =0.55, relheight = 0.03)
        
        self.lbl2 = Label(self.jan, bg = "#131644", fg = "white", text = "Nome do doador", font = " Century\ Gothic 14",anchor = "w")
        self.lbl2.place(relx = 0.26, rely = 0.365, relwidth =0.55, relheight = 0.04)
        
        self.lbl3 = Label(self.jan, bg = "#131644", fg = "white", text = "Msg...", font = " Century\ Gothic 10",anchor= "w")
        self.lbl3.place(relx = 0.26, rely = 0.405, relwidth =0.55, relheight = 0.03)
        
        self.lbl2 = Label(self.jan, bg = "#131644", fg = "white", text = "Nome do doador", font = " Century\ Gothic 14",anchor = "w")
        self.lbl2.place(relx = 0.26, rely = 0.475, relwidth =0.55, relheight = 0.04)
        
        self.lbl3 = Label(self.jan, bg = "#131644", fg = "white", text = "Msg...", font = " Century\ Gothic 10",anchor= "w")
        self.lbl3.place(relx = 0.26, rely = 0.515, relwidth =0.55, relheight = 0.03)
        
        self.lbl2 = Label(self.jan, bg = "#131644", fg = "white", text = "Nome do doador", font = " Century\ Gothic 14",anchor = "w")
        self.lbl2.place(relx = 0.26, rely = 0.585, relwidth =0.55, relheight = 0.04)
        
        self.lbl3 = Label(self.jan, bg = "#131644", fg = "white", text = "Msg...", font = " Century\ Gothic 10",anchor= "w")
        self.lbl3.place(relx = 0.26, rely = 0.625, relwidth =0.55, relheight = 0.03)
        
        self.lbl2 = Label(self.jan, bg = "#131644", fg = "white", text = "Nome do doador", font = " Century\ Gothic 14",anchor = "w")
        self.lbl2.place(relx = 0.26, rely = 0.695, relwidth =0.55, relheight = 0.04)
        
        self.lbl3 = Label(self.jan, bg = "#131644", fg = "white", text = "Msg...", font = " Century\ Gothic 10",anchor= "w")
        self.lbl3.place(relx = 0.26, rely = 0.735, relwidth =0.55, relheight = 0.03)
        
        self.lbl2 = Label(self.jan, bg = "#131644", fg = "white", text = "Nome do doador", font = " Century\ Gothic 14",anchor = "w")
        self.lbl2.place(relx = 0.26, rely = 0.805, relwidth =0.55, relheight = 0.04)
        
        self.lbl3 = Label(self.jan, bg = "#131644", fg = "white", text = "Msg...", font = " Century\ Gothic 10",anchor= "w")
        self.lbl3.place(relx = 0.26, rely = 0.845, relwidth =0.55, relheight = 0.03)
        
        self.lbl2 = Label(self.jan, bg = "#131644", fg = "white", text = "Nome do doador", font = " Century\ Gothic 14",anchor = "w")
        self.lbl2.place(relx = 0.26, rely = 0.915, relwidth =0.55, relheight = 0.04)
        
        self.lbl3 = Label(self.jan, bg = "#131644", fg = "white", text = "Msg...", font = " Century\ Gothic 10",anchor= "w")
        self.lbl3.place(relx = 0.26, rely = 0.955, relwidth =0.55, relheight = 0.03)
        
    def telainst11(self):
        
        self.img1 = PhotoImage(file = "C:\\Users\\Pichau\\OneDrive - Firjan\\Arquivos\\Kindly\\Inst11.png")
        self.img2 = PhotoImage(file = "C:\\Users\\Pichau\\OneDrive - Firjan\\Arquivos\\Kindly\\btnPerfilmaior.PNG")
        self.img3 = PhotoImage(file = "C:\\Users\\Pichau\\OneDrive - Firjan\\Arquivos\\Kindly\\btnSetinha.PNG")
    

        self.lbl1 = Label(self.jan, image = self.img1)
        self.lbl1.place(relx = 0, rely = 0, relwidth =1, relheight = 1)
        
    
        self.btn1 = Button(self.jan,text = "Nome do doador", font = "Century\ Gothic 14",fg = "white", bg = "#131644",bd = 0, activebackground = "gray",command = lambda: self.telainst12())
        self.btn1.place(relx = 0.23, rely = 0.01, relwidth = 0.78, relheight = 0.09)
       
        self.btn2 = Button(self.jan, bg = "#131644",bd = 0, activebackground = "#131644", image = self.img2 ,command = lambda: self.telainst12())
        self.btn2.place(relx = 0.21, rely = 0.01, relwidth = 0.17, relheight = 0.08)
        
        self.btn3 = Button(self.jan, bg = "#131644",bd = 0, activebackground = "#131644", image = self.img3 ,command = lambda: self.telainst10())
        self.btn3.place(relx = 0.03, rely = 0.025, relwidth = 0.15, relheight = 0.06)
    
    
        global entrada1
        entrada1 = StringVar()
        self.ent1 = Entry(self.jan, bg = "#131644", font = "Century\ Gothic 14",fg = "white",bd = 3, textvariable = entrada1)
        self.ent1.place(relx = 0.01, rely = 0.565, relwidth = 0.98, relheight = 0.08)
        entrada1.set("Digite aqui...")
        
        self.ent1.bind("<1>",self.limpar111)
        self.lbl1.bind("<1>",self.voltatexto)
        
    def limpar111(self,evento=None):
        self.limpar(entrada1, "Digite aqui...")
    
    def telainst12(self):   
        self.img1 = PhotoImage(file = "C:\\Users\\Pichau\\OneDrive - Firjan\\Arquivos\\Kindly\\Inst12.png")
        self.img2 = PhotoImage(file = "C:\\Users\\Pichau\\OneDrive - Firjan\\Arquivos\\Kindly\\btnPerfilgg.PNG")
        self.img3 = PhotoImage(file = "C:\\Users\\Pichau\\OneDrive - Firjan\\Arquivos\\Kindly\\btnSetinha.PNG")
    
        
        self.lbl1 = Label(self.jan, image = self.img1)
        self.lbl1.place(relx = 0, rely = 0, relwidth =1, relheight = 1)
        
        self.lbl2 = Label(self.jan, bg = "#BDAB9F", fg = "black", text = "Nome do doador", font = " Century\ Gothic 14")
        self.lbl2.place(relx = 0.31, rely = 0.165, relwidth =0.62, relheight = 0.04)
        
        
        self.btn1 = Button(self.jan, bg = "#131644",bd = 0, activebackground = "#131644", image = self.img2 ,command = lambda: self.teste())
        self.btn1.place(relx = 0.05, rely = 0.123, relwidth = 0.22, relheight = 0.14)
        
        self.btn2 = Button(self.jan, bg = "#131644",bd = 0, activebackground = "#131644", image = self.img3 ,command = lambda: self.telainst10())
        self.btn2.place(relx = 0.04, rely = 0.025, relwidth = 0.15, relheight = 0.06)
    
    def telainst13(self):   
        self.img1 = PhotoImage(file = "C:\\Users\\Pichau\\OneDrive - Firjan\\Arquivos\\Kindly\\Doador12.png")
        self.img2 = PhotoImage(file = "C:\\Users\\Pichau\\OneDrive - Firjan\\Arquivos\\Kindly\\btnLupinha.PNG")
        self.img3 = PhotoImage(file = "C:\\Users\\Pichau\\OneDrive - Firjan\\Arquivos\\Kindly\\btnSetinha.PNG")
    

        self.lbl1 = Label(self.jan, image = self.img1)
        self.lbl1.place(relx = 0, rely = 0, relwidth =1, relheight = 1)
        
       
        self.btn1 = Button(self.jan, bg = "#FEAD77",bd = 0, activebackground = "#FEAD77", image = self.img2 ,command = lambda: self.pesquisa())
        self.btn1.place(relx = 0.86, rely = 0.14, relwidth = 0.1, relheight = 0.075)
        
        self.btn2 = Button(self.jan, bg = "#131644",bd = 0, activebackground = "#131644", image = self.img3 ,command = lambda: self.telainst5())
        self.btn2.place(relx = 0.06, rely = 0.03, relwidth = 0.15, relheight = 0.06)
    

        global entrada1
        entrada1 = StringVar()
        self.ent1 = Entry(self.jan, bg = "#FEAD77", font = "Century\ Gothic 14",fg = "white", textvariable = entrada1, bd = 0)
        self.ent1.place(relx = 0.045, rely = 0.14, relwidth = 0.82, relheight = 0.075)
        entrada1.set("Digite aqui...")
        
        self.ent1.bind("<1>",self.limpar131)
        self.lbl1.bind("<1>",self.voltatexto)
 
        self.listb1 = Listbox(self.jan, bg = "#131644",fg = "white", font = "Century\ Gothic 14", bd = 0, selectbackground = "#FEAD77")
        self.listb1.place(relx = 0.01, rely = 0.23, relwidth = 0.98, relheight = 0.41)
        
    def pesquisa(self):
        self.listb1.insert(END, "Nome do instituto")
        self.listb1.insert(END, "Nome do instituto")
        self.listb1.insert(END, "Nome do instituto")
        
            
    def limpar131(self,evento=None):
        self.limpar(entrada1, "Digite aqui...")
    
    def voltatexto(self,vento=None):
        x = entrada1.get()
        if x == "":
            entrada1.set("Digite aqui...")

Kindly()