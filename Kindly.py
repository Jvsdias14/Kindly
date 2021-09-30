from tkinter import *
from threading import Timer
from tkinter import filedialog
import random
import string
from PIL import Image, ImageTk
import mysql.connector 

try:
    global conexao
    conexao = mysql.connector.connect(user = "root",host = "127.0.0.1")
    bdOK = True
except:
	print("Não foi possível conectar ao SGBD. \nVerifique o XAMPP/WAMP ou os dados de conexão.")
	bdOK = False

if bdOK:
    global cursor
    cursor = conexao.cursor()
# ---------- Cria e Conecta no Banco de Dados ---------- #	
    try:
	    cursor.execute("USE kindly;")
	    print("kindly selecionado!!")
    except:
	    cursor.execute("USE kindly;")
	    print("kindly selecionado!")


class Kindly():
    def __init__(self):
        self.jan = Tk()
        self.jan.geometry("375x667+750+220")
        self.jan.title("Kindly")
        self.jan.config(bg = "white")
        self.jan.resizable(False,False)
        self.jan.iconbitmap("C:\\Users\\res0130160\\OneDrive - Firjan\\Arquivos\\Kindly\\logoKindly.ico")
        self.imagens()
        self.labels()
        
        self.listad1_1 = []
        self.listad1_2 = []
        
        t = Timer(2, self.Padrao2)
        t.start()
        
        self.jan.mainloop()
        
    def teste(self):
        print("sla")
    
    def selecionar(self):
        self.nomearq = filedialog.askopenfilename(initialdir ="C:/", title = "Escolher Arquivo")
    
    def imagens(self):    
        self.img1 = PhotoImage(file = "C:\\Users\\res0130160\\OneDrive - Firjan\\Arquivos\\Kindly\\Padrao1.png")
    
    def labels(self):
        self.lbl1 = Label(self.jan, image = self.img1)
        self.lbl1.place(relx = 0, rely = 0, relwidth =1, relheight = 1)
    
    def Padrao2(self):
        self.img1 = PhotoImage(file = "C:\\Users\\res0130160\\OneDrive - Firjan\\Arquivos\\Kindly\\Padrao2.png")
        self.img2 = PhotoImage(file = "C:\\Users\\res0130160\\OneDrive - Firjan\\Arquivos\\Kindly\\btn1 TelaPadrao2.PNG")
        self.img3 = PhotoImage(file = "C:\\Users\\res0130160\\OneDrive - Firjan\\Arquivos\\Kindly\\btn2 TelaPadrao2.PNG")
    
        self.lbl1 = Label(self.jan, image = self.img1)
        self.lbl1.place(relx = 0, rely = 0, relwidth =1, relheight = 1)
    
        self.btn1 = Button(self.jan, bg = "#131644",bd = 0, activebackground = "#131644", image = self.img2 ,command = lambda: self.telainst1())
        self.btn1.place(relx = 0.13, rely = 0.42, relwidth = 0.74, relheight = 0.15)
        self.btn2 = Button(self.jan, bg = "#131644",bd = 0, activebackground = "#131644", image = self.img3 ,command = lambda: self.teladoador1())
        self.btn2.place(relx = 0.13, rely = 0.58, relwidth = 0.74, relheight = 0.15)

    
    def telainst1(self):

        self.img1 = PhotoImage(file = "C:\\Users\\res0130160\\OneDrive - Firjan\\Arquivos\\Kindly\\Inst1.png")
        self.img2 = PhotoImage(file = "C:\\Users\\res0130160\\OneDrive - Firjan\\Arquivos\\Kindly\\btnEntrar.PNG")
        self.img3 = PhotoImage(file = "C:\\Users\\res0130160\\OneDrive - Firjan\\Arquivos\\Kindly\\btnSetinha.PNG")


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
        self.ent1 = Entry(self.jan, bg = "#131644", font = "Century\ Gothic 14",fg = "white",bd = 0, textvariable = entrada1,insertbackground='white')
        self.ent1.place(relx = 0.16, rely = 0.335, relwidth = 0.68, relheight = 0.06)
        entrada1.set("Digite seu e-mail")
        
        global entrada2
        entrada2 = StringVar()
        self.ent2 = Entry(self.jan, bg = "#131644", font = "Century\ Gothic 14",fg = "white",bd = 0, textvariable = entrada2,insertbackground='white')
        self.ent2.place(relx = 0.16, rely = 0.468, relwidth = 0.68, relheight = 0.06)
        entrada2.set("Digite seu código")
        
        self.ent1.bind("<1>",self.limpart11)
        self.ent2.bind("<1>",self.limpart12)
        self.lbl1.bind("<1>",self.voltatextoI1)

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
    
    def voltatextoI1(self,vento=None):
        x = entrada1.get()
        if x == "":
            entrada1.set("Digite seu e-mail") 
        y = entrada2.get()
        if y == "":
            entrada2.set("Digite seu código")
    
    
    def telainst2e3(self):
        self.img1 = PhotoImage(file = "C:\\Users\\res0130160\\OneDrive - Firjan\\Arquivos\\Kindly\\Inst2.png")
        self.img2 = PhotoImage(file = "C:\\Users\\res0130160\\OneDrive - Firjan\\Arquivos\\Kindly\\btnCadastrar.PNG")
        self.img3 = PhotoImage(file = "C:\\Users\\res0130160\\OneDrive - Firjan\\Arquivos\\Kindly\\btnSetinha.PNG")
    
        
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
        self.ent1 = Entry(self.jan, bg = "#131644", font = "Century\ Gothic 14",fg = "white",bd = 0, textvariable = entrada1,insertbackground='white')
        self.ent1.place(relx = 0.155, rely = 0.332, relwidth = 0.69, relheight = 0.055)
        entrada1.set("Digite o nome da instituição")
        
        global entrada2
        entrada2 = StringVar()
        self.ent2 = Entry(self.jan, bg = "#131644", font = "Century\ Gothic 14",fg = "white",bd = 0, textvariable = entrada2,insertbackground='white')
        self.ent2.place(relx = 0.155, rely = 0.426, relwidth = 0.68, relheight = 0.055)
        entrada2.set("Digite seu e-mail")
        
        global entrada3
        entrada3 = StringVar()
        self.ent3 = Entry(self.jan, bg = "#131644", font = "Century\ Gothic 14",fg = "white",bd = 0, textvariable = entrada3,insertbackground='white')
        self.ent3.place(relx = 0.155, rely = 0.522, relwidth = 0.68, relheight = 0.055)
        entrada3.set("Digite seu código")
        
        self.ent1.bind("<1>",self.limpar21)
        self.ent2.bind("<1>",self.limpar22)
        self.ent3.bind("<1>",self.limpar23)
        self.lbl1.bind("<1>",self.voltatextoI2e3)

    def validar(self):
        lbl = Label(self.jan, text = "Código inválido", font = "Century\ Gothic 14",fg = "#FE4A49",bd = 0, bg = "#131644")
        lbl.place(relx = 0.155, rely = 0.59, relwidth = 0.4, relheight = 0.05)

    def limpar21(self,evento=None):
        self.limpar(entrada1, "Digite o nome da instituição")
    
    def limpar22(self,evento=None):
        self.limpar(entrada2, "Digite seu e-mail")
            
    def limpar23(self,evento=None):
        self.limpar(entrada3, "Digite seu código")
    
    def voltatextoI2e3(self,vento=None):
        x = entrada1.get()
        if x == "":
            entrada1.set("Digite o nome da instituição")
        y = entrada2.get()
        if y == "":
            entrada2.set("Digite seu e-mail")
        z = entrada3.get()
        if z == "":
            entrada3.set("Digite seu código")
    

    def telainst4(self):
           
        self.img1 = PhotoImage(file = "C:\\Users\\res0130160\\OneDrive - Firjan\\Arquivos\\Kindly\\Inst4.png")
        self.img2 = PhotoImage(file = "C:\\Users\\res0130160\\OneDrive - Firjan\\Arquivos\\Kindly\\btnSetaL.PNG")
    
        self.lbl1 = Label(self.jan, image = self.img1)
        self.lbl1.place(relx = 0, rely = 0, relwidth =1, relheight = 1)

        self.btn1 = Button(self.jan, bg = "#131644",bd = 0, activebackground = "#131644", image = self.img2 ,command = lambda: self.telainst2e3())
        self.btn1.place(relx = 0.13, rely = 0.75, relwidth = 0.74, relheight = 0.15)

    def telainst5(self):
           
        self.img1 = PhotoImage(file = "C:\\Users\\res0130160\\OneDrive - Firjan\\Arquivos\\Kindly\\Inst5.png")
        self.img2 = PhotoImage(file = "C:\\Users\\res0130160\\OneDrive - Firjan\\Arquivos\\Kindly\\btnPerfil.PNG")
        self.img3 = PhotoImage(file = "C:\\Users\\res0130160\\OneDrive - Firjan\\Arquivos\\Kindly\\btnChat.PNG")
        self.img4 = PhotoImage(file = "C:\\Users\\res0130160\\OneDrive - Firjan\\Arquivos\\Kindly\\btnLupa.PNG")
        self.img5 = PhotoImage(file = "C:\\Users\\res0130160\\OneDrive - Firjan\\Arquivos\\Kindly\\btnPerfilmaior.PNG")
        self.img6 = PhotoImage(file = 'C:\\Users\\res0130160\\OneDrive - Firjan\\Arquivos\\Kindly\\btn+.PNG')
    
    
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
        
        self.btn6 = Button(self.jan, bd = 2 ,bg = "#131644", image = self.img6, command = lambda: self.telainst6())
        self.btn6.place(relx = 0.8, rely = 0.85, relwidth = 0.14, relheight = 0.082)
        
    def telainst6(self):
         
        self.img1 = PhotoImage(file = "C:\\Users\\res0130160\\OneDrive - Firjan\\Arquivos\\Kindly\\Inst6.png")
        self.img2 = PhotoImage(file = "C:\\Users\\res0130160\\OneDrive - Firjan\\Arquivos\\Kindly\\btnPostar.PNG")
        self.img3 = PhotoImage(file = "C:\\Users\\res0130160\\OneDrive - Firjan\\Arquivos\\Kindly\\btnCamera.PNG")
        self.img4 = PhotoImage(file = "C:\\Users\\res0130160\\OneDrive - Firjan\\Arquivos\\Kindly\\btnSetinha.PNG")
    
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
        self.ent1 = Entry(self.jan, bg = "#131644", font = "Century\ Gothic 14",fg = "white",bd = 0, textvariable = entrada1,insertbackground='white')
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
          
        self.img1 = PhotoImage(file = "C:\\Users\\res0130160\\OneDrive - Firjan\\Arquivos\\Kindly\\Inst7.png")
        self.img2 = PhotoImage(file = "C:\\Users\\res0130160\\OneDrive - Firjan\\Arquivos\\Kindly\\btnPerfilgg.PNG")
        self.img3 = PhotoImage(file = "C:\\Users\\res0130160\\OneDrive - Firjan\\Arquivos\\Kindly\\btnDinheiro.PNG")
        self.img4 = PhotoImage(file = "C:\\Users\\res0130160\\OneDrive - Firjan\\Arquivos\\Kindly\\btnSetinha.PNG")
        self.img5 = PhotoImage(file = "C:\\Users\\res0130160\\OneDrive - Firjan\\Arquivos\\Kindly\\btnCamerabranca.PNG")
    
    
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
        self.img1 = PhotoImage(file = "C:\\Users\\res0130160\\OneDrive - Firjan\\Arquivos\\Kindly\\Inst8.png")
        self.img2 = PhotoImage(file = "C:\\Users\\res0130160\\OneDrive - Firjan\\Arquivos\\Kindly\\btnPerfilmaior.PNG")
        self.img3 = PhotoImage(file = "C:\\Users\\res0130160\\OneDrive - Firjan\\Arquivos\\Kindly\\btnSetinha.PNG")
    
        
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
       
        self.img1 = PhotoImage(file = "C:\\Users\\res0130160\\OneDrive - Firjan\\Arquivos\\Kindly\\Inst9.png")
        self.img2 = PhotoImage(file = "C:\\Users\\res0130160\\OneDrive - Firjan\\Arquivos\\Kindly\\btnPerfilgg.PNG")
        self.img3 = PhotoImage(file = "C:\\Users\\res0130160\\OneDrive - Firjan\\Arquivos\\Kindly\\btnSetinha.PNG")
    
        
        self.lbl1 = Label(self.jan, image = self.img1)
        self.lbl1.place(relx = 0, rely = 0, relwidth =1, relheight = 1)
        
        self.lbl2 = Label(self.jan, bg = "#BDAB9F", fg = "black", text = "Nome da instituição", font = " Century\ Gothic 14")
        self.lbl2.place(relx = 0.32, rely = 0.165, relwidth =0.62, relheight = 0.04)
        
   
        self.btn1 = Button(self.jan, bg = "#131644",bd = 0, activebackground = "#131644", image = self.img2 ,command = lambda: self.teste())
        self.btn1.place(relx = 0.05, rely = 0.123, relwidth = 0.22, relheight = 0.14)
        
        self.btn2 = Button(self.jan, bg = "#131644",bd = 0, activebackground = "#131644", image = self.img3 ,command = lambda: self.telainst5())
        self.btn2.place(relx = 0.07, rely = 0.03, relwidth = 0.15, relheight = 0.06)
    
    def telainst10(self):  
        self.img1 = PhotoImage(file = "C:\\Users\\res0130160\\OneDrive - Firjan\\Arquivos\\Kindly\\Inst10.png")
        self.img2 = PhotoImage(file = "C:\\Users\\res0130160\\OneDrive - Firjan\\Arquivos\\Kindly\\btnPerfilmaior.PNG")
        self.img3 = PhotoImage(file = "C:\\Users\\res0130160\\OneDrive - Firjan\\Arquivos\\Kindly\\btnSetinha.PNG")
    

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
        
        self.img1 = PhotoImage(file = "C:\\Users\\res0130160\\OneDrive - Firjan\\Arquivos\\Kindly\\Inst11.png")
        self.img2 = PhotoImage(file = "C:\\Users\\res0130160\\OneDrive - Firjan\\Arquivos\\Kindly\\btnPerfilmaior.PNG")
        self.img3 = PhotoImage(file = "C:\\Users\\res0130160\\OneDrive - Firjan\\Arquivos\\Kindly\\btnSetinha.PNG")
    

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
        self.ent1 = Entry(self.jan, bg = "#131644", font = "Century\ Gothic 14",fg = "white",bd = 3, textvariable = entrada1,insertbackground='white')
        self.ent1.place(relx = 0.01, rely = 0.565, relwidth = 0.98, relheight = 0.08)
        entrada1.set("Digite aqui...")
        
        self.ent1.bind("<1>",self.limpar111)
        self.lbl1.bind("<1>",self.voltatexto)
        
    def limpar111(self,evento=None):
        self.limpar(entrada1, "Digite aqui...")
    
    def telainst12(self):   
        self.img1 = PhotoImage(file = "C:\\Users\\res0130160\\OneDrive - Firjan\\Arquivos\\Kindly\\Inst12.png")
        self.img2 = PhotoImage(file = "C:\\Users\\res0130160\\OneDrive - Firjan\\Arquivos\\Kindly\\btnPerfilgg.PNG")
        self.img3 = PhotoImage(file = "C:\\Users\\res0130160\\OneDrive - Firjan\\Arquivos\\Kindly\\btnSetinha.PNG")
    
        
        self.lbl1 = Label(self.jan, image = self.img1)
        self.lbl1.place(relx = 0, rely = 0, relwidth =1, relheight = 1)
        
        self.lbl2 = Label(self.jan, bg = "#BDAB9F", fg = "black", text = "Nome do doador", font = " Century\ Gothic 14")
        self.lbl2.place(relx = 0.31, rely = 0.165, relwidth =0.62, relheight = 0.04)
        
        
        self.btn1 = Button(self.jan, bg = "#131644",bd = 0, activebackground = "#131644", image = self.img2 ,command = lambda: self.teste())
        self.btn1.place(relx = 0.05, rely = 0.123, relwidth = 0.22, relheight = 0.14)
        
        self.btn2 = Button(self.jan, bg = "#131644",bd = 0, activebackground = "#131644", image = self.img3 ,command = lambda: self.telainst10())
        self.btn2.place(relx = 0.04, rely = 0.025, relwidth = 0.15, relheight = 0.06)
    
    def telainst13(self):   
        self.img1 = PhotoImage(file = "C:\\Users\\res0130160\\OneDrive - Firjan\\Arquivos\\Kindly\\Doador12.png")
        self.img2 = PhotoImage(file = "C:\\Users\\res0130160\\OneDrive - Firjan\\Arquivos\\Kindly\\btnLupinha.PNG")
        self.img3 = PhotoImage(file = "C:\\Users\\res0130160\\OneDrive - Firjan\\Arquivos\\Kindly\\btnSetinha.PNG")
    

        self.lbl1 = Label(self.jan, image = self.img1)
        self.lbl1.place(relx = 0, rely = 0, relwidth =1, relheight = 1)
        
       
        self.btn1 = Button(self.jan, bg = "#FEAD77",bd = 0, activebackground = "#FEAD77", image = self.img2 ,command = lambda: self.pesquisa())
        self.btn1.place(relx = 0.86, rely = 0.14, relwidth = 0.1, relheight = 0.075)
        
        self.btn2 = Button(self.jan, bg = "#131644",bd = 0, activebackground = "#131644", image = self.img3 ,command = lambda: self.telainst5())
        self.btn2.place(relx = 0.06, rely = 0.03, relwidth = 0.15, relheight = 0.06)
    

        global entrada1
        entrada1 = StringVar()
        self.ent1 = Entry(self.jan, bg = "#FEAD77", font = "Century\ Gothic 14",fg = "white", textvariable = entrada1, bd = 0,insertbackground='white')
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

    def teladoador1(self):    
        self.img1 = PhotoImage(file = "C:\\Users\\res0130160\\OneDrive - Firjan\\Arquivos\\Kindly\\Doador1.png")
        self.img2 = PhotoImage(file = "C:\\Users\\res0130160\\OneDrive - Firjan\\Arquivos\\Kindly\\btnEntrar.PNG")
        self.img3 = PhotoImage(file = "C:\\Users\\res0130160\\OneDrive - Firjan\\Arquivos\\Kindly\\btnSetinha.PNG")
    

        self.lbl1 = Label(self.jan, image = self.img1)
        self.lbl1.place(relx = 0, rely = 0, relwidth =1, relheight = 1)
    

        self.btn1 = Button(self.jan, bg = "#131644",bd = 0, activebackground = "#131644", image = self.img2 ,command = lambda: self.conexãod1())
        self.btn1.place(relx = 0.29, rely = 0.6, relwidth = 0.42, relheight = 0.15)
        
        self.btn2 = Button(self.jan, bg = "#131644",bd = 0, activebackground = "#131644", image = self.img3 ,command = lambda: self.Padrao2())
        self.btn2.place(relx = 0.03, rely = 0.055, relwidth = 0.15, relheight = 0.06)
        
        self.btn3 = Button(self.jan, text = "Crie agora", font = "Century\ Gothic 18",fg = "#FD824F", bg = "#131644",bd = 0, activebackground = "#131644",command = lambda: self.teladoador6())
        self.btn3.place(relx = 0.33, rely = 0.84, relwidth = 0.33, relheight = 0.05)
        
        self.btn4 = Button(self.jan, text = "Esqueceu sua senha?", font = "Century\ Gothic 11",fg = "white", bg = "#131644",bd = 0, activebackground = "#131644",command = lambda: self.teladoador2())
        self.btn4.place(relx = 0.17, rely = 0.54, relwidth = 0.42, relheight = 0.05)

        global entrada1
        entrada1 = StringVar()
        self.ent1 = Entry(self.jan, bg = "#131644", font = "Century\ Gothic 14",fg = "white",bd = 0, textvariable = entrada1,insertbackground='white')
        self.ent1.place(relx = 0.16, rely = 0.36, relwidth = 0.68, relheight = 0.06)
        entrada1.set("Digite seu e-mail")
        
        global entrada2
        entrada2 = StringVar()
        self.ent2 = Entry(self.jan, bg = "#131644", font = "Century\ Gothic 14",fg = "white",bd = 0, textvariable = entrada2,insertbackground='white')
        self.ent2.place(relx = 0.16, rely = 0.468, relwidth = 0.68, relheight = 0.06)
        entrada2.set("Digite sua senha")

        self.ent1.bind("<1>",self.limpard11)
        self.ent2.bind("<1>",self.limpard12)
        self.lbl1.bind("<1>",self.voltatexto)
        
    def limpard11(self,evento=None):
        self.limpar(entrada1, "Digite seu e-mail")
    
    def limpard12(self,evento=None):
        self.limpar(entrada2, "Digite sua senha")
    
    def voltatexto(self,vento=None):
        x = entrada1.get()
        if x == "":
            entrada1.set("Digite seu e-mail") 
        y = entrada2.get()
        if y == "":
            entrada2.set("Digite sua senha")

    def conexãod1(self):
        self.emailescrito = entrada1.get()
        self.senhaescrita = entrada2.get()
 
        try:
            cursor.execute("SELECT email FROM doadores WHERE email = '{}'".format(self.emailescrito))
            for i in cursor:
                for x in i:
                    self.listad1_1.append(x)
            self.emaildoador = self.listad1_1[0]
            if self.emaildoador == self.emailescrito:
                self.x = True
            else:
                self.lbl2 = Label(self.jan, text = "E-mail e/ou senha inválidos", font = "Century\ Gothic 14", fg = "#FE4A49", bg = "#131644")
                self.lbl2.place(relx = 0.16, rely = 0.29, relwidth = 0.68, relheight = 0.06)
            
            cursor.execute("SELECT senha FROM doadores WHERE senha = '{}'".format(self.senhaescrita))
            for i in cursor:
                for x in i:
                    self.listad1_2.append(x)
            self.senhadoador = self.listad1_2[0]
            if self.senhadoador == self.senhaescrita:
                self.x = True
            else:
                self.x = False
                self.lbl2 = Label(self.jan, text = "E-mail e/ou senha inválidos", font = "Century\ Gothic 14", fg = "#FE4A49", bg = "#131644")
                self.lbl2.place(relx = 0.16, rely = 0.29, relwidth = 0.68, relheight = 0.05)
        except Exception as e: 
            print(e)
            self.lbl2 = Label(self.jan, text = "E-mail e/ou senha inválidos", font = "Century\ Gothic 14", fg = "#FE4A49", bg = "#131644")
            self.lbl2.place(relx = 0.16, rely = 0.29, relwidth = 0.68, relheight = 0.05)
        
        if self.x == True:
            self.teladoador7()
        
            
    def teladoador2(self):
        self.img1 = PhotoImage(file = "C:\\Users\\res0130160\\OneDrive - Firjan\\Arquivos\\Kindly\\Doador2.png")
        self.img2 = PhotoImage(file = "C:\\Users\\res0130160\\OneDrive - Firjan\\Arquivos\\Kindly\\btnSetaR.PNG")
        self.img3 = PhotoImage(file = "C:\\Users\\res0130160\\OneDrive - Firjan\\Arquivos\\Kindly\\btnSetinha.PNG")
    
 
        self.lbl1 = Label(self.jan, image = self.img1)
        self.lbl1.place(relx = 0, rely = 0, relwidth =1, relheight = 1)

        self.btn1 = Button(self.jan, bg = "#131644",bd = 0, activebackground = "#131644", image = self.img2 ,command = lambda: self.teladoador3())
        self.btn1.place(relx = 0.29, rely = 0.65, relwidth = 0.42, relheight = 0.14)
        
        self.btn2 = Button(self.jan, bg = "#131644",bd = 0, activebackground = "#131644", image = self.img3 ,command = lambda: self.teladoador1())
        self.btn2.place(relx = 0.03, rely = 0.06, relwidth = 0.15, relheight = 0.06)
    

        global entrada1
        entrada1 = StringVar()
        self.ent1 = Entry(self.jan, bg = "#131644", font = "Century\ Gothic 14",fg = "white",bd = 0, textvariable = entrada1,insertbackground='white')
        self.ent1.place(relx = 0.155, rely = 0.545, relwidth = 0.69, relheight = 0.055)
        entrada1.set("Digite seu e-mail")
        
        self.ent1.bind("<1>",self.limpard21)
        self.lbl1.bind("<1>",self.voltatexto)
            
    def limpard21(self,evento=None):
        self.limpar(entrada1, "Digite seu e-mail")
    
    def voltatexto(self,vento=None):
        x = entrada1.get()
        if x == "":
            entrada1.set("Digite seu e-mail")
    
    def createcodigo(self):
        possibilidades = string.ascii_uppercase + string.digits
        result_str = ''.join(random.choice(possibilidades) for i in range(6))
        print(result_str)
            
            
    def teladoador3(self):
        self.createcodigo()
        
        self.img1 = PhotoImage(file = "C:\\Users\\res0130160\\OneDrive - Firjan\\Arquivos\\Kindly\\Doador3.png")
        self.img2 = PhotoImage(file = "C:\\Users\\res0130160\\OneDrive - Firjan\\Arquivos\\Kindly\\btnVerificar.PNG")
        self.img3 = PhotoImage(file = "C:\\Users\\res0130160\\OneDrive - Firjan\\Arquivos\\Kindly\\btnSetinha.PNG")

        self.lbl1 = Label(self.jan, image = self.img1)
        self.lbl1.place(relx = 0, rely = 0, relwidth =1, relheight = 1)
    

        self.btn1 = Button(self.jan, bg = "#131644",bd = 0, activebackground = "#131644", image = self.img2 ,command = lambda: self.teladoador4())
        self.btn1.place(relx = 0.29, rely = 0.55, relwidth = 0.42, relheight = 0.14)
        
        self.btn2 = Button(self.jan, bg = "#131644",bd = 0, activebackground = "#131644", image = self.img3 ,command = lambda: self.teladoador2())
        self.btn2.place(relx = 0.03, rely = 0.06, relwidth = 0.15, relheight = 0.06)
    

        global entrada1
        entrada1 = StringVar()
        self.ent1 = Entry(self.jan, bg = "#131644", font = "Century\ Gothic 14",fg = "white",bd = 0, textvariable = entrada1,insertbackground='white')
        self.ent1.place(relx = 0.155, rely = 0.46, relwidth = 0.69, relheight = 0.055)
        entrada1.set("Insira o código")
        
        self.ent1.bind("<1>",self.limpard31)
        self.lbl1.bind("<1>",self.voltatexto)

            
    def limpard31(self,evento=None):
        self.limpar(entrada1, "Insira o código")
    
    def voltatexto(self,vento=None):
        x = entrada1.get()
        if x == "":
            entrada1.set("Insira o código")
            
    def teladoador4(self):
         
        self.img1 = PhotoImage(file = "C:\\Users\\res0130160\\OneDrive - Firjan\\Arquivos\\Kindly\\Doador4.png")
        self.img2 = PhotoImage(file = "C:\\Users\\res0130160\\OneDrive - Firjan\\Arquivos\\Kindly\\btnVerificar.PNG")
        self.img3 = PhotoImage(file = "C:\\Users\\res0130160\\OneDrive - Firjan\\Arquivos\\Kindly\\btnReenviar.PNG")
        self.img4 = PhotoImage(file = "C:\\Users\\res0130160\\OneDrive - Firjan\\Arquivos\\Kindly\\btnSetinha.PNG")
    
 
        self.lbl1 = Label(self.jan, image = self.img1)
        self.lbl1.place(relx = 0, rely = 0, relwidth =1, relheight = 1)
    

        self.btn1 = Button(self.jan, bg = "#131644",bd = 0, activebackground = "#131644", image = self.img2 ,command = lambda: self.teladoador5())
        self.btn1.place(relx = 0.29, rely = 0.59, relwidth = 0.42, relheight = 0.14)
        
        self.btn2 = Button(self.jan, bg = "#131644",bd = 0, activebackground = "#131644", image = self.img3 ,command = lambda: self.createcodigo())
        self.btn2.place(relx = 0.1, rely = 0.47, relwidth = 0.8, relheight = 0.14)
        
        self.btn3 = Button(self.jan, bg = "#131644",bd = 0, activebackground = "#131644", image = self.img4 ,command = lambda: self.teladoador2())
        self.btn3.place(relx = 0.03, rely = 0.06, relwidth = 0.15, relheight = 0.06)

    
        global entrada1
        entrada1 = StringVar()
        self.ent1 = Entry(self.jan, bg = "#131644", font = "Century\ Gothic 14",fg = "white",bd = 0, textvariable = entrada1,insertbackground='white')
        self.ent1.place(relx = 0.155, rely = 0.335, relwidth = 0.69, relheight = 0.055)
        entrada1.set("Insira o código")
        
        self.ent1.bind("<1>",self.limpard41)
        self.lbl1.bind("<1>",self.voltatexto)
            
    def limpard41(self,evento=None):
        self.limpar(entrada1, "Insira o código")
    
    def voltatexto(self,vento=None):
        x = entrada1.get()
        if x == "":
            entrada1.set("Insira o código")
            
    def teladoador5(self):
  
        self.img1 = PhotoImage(file = "C:\\Users\\res0130160\\OneDrive - Firjan\\Arquivos\\Kindly\\Doador5.png")
        self.img2 = PhotoImage(file = "C:\\Users\\res0130160\\OneDrive - Firjan\\Arquivos\\Kindly\\btnRedefinir.PNG")
        self.img3 = PhotoImage(file = "C:\\Users\\res0130160\\OneDrive - Firjan\\Arquivos\\Kindly\\btnSetinha.PNG")
    

        self.lbl1 = Label(self.jan, image = self.img1)
        self.lbl1.place(relx = 0, rely = 0, relwidth =1, relheight = 1)
    

        self.btn1 = Button(self.jan, bg = "#131644",bd = 0, activebackground = "#131644", image = self.img2 ,command = lambda: self.teladoador1())
        self.btn1.place(relx = 0.29, rely = 0.63, relwidth = 0.42, relheight = 0.14)
        
        self.btn2 = Button(self.jan, bg = "#131644",bd = 0, activebackground = "#131644", image = self.img3 ,command = lambda: self.teladoador2())
        self.btn2.place(relx = 0.03, rely = 0.06, relwidth = 0.15, relheight = 0.06)
    

        global entrada1
        entrada1 = StringVar()
        self.ent1 = Entry(self.jan, bg = "#131644", font = "Century\ Gothic 14",fg = "white",bd = 0, textvariable = entrada1,insertbackground='white')
        self.ent1.place(relx = 0.155, rely = 0.398, relwidth = 0.69, relheight = 0.055)
        entrada1.set("Digite sua nova senha")

        global entrada2
        entrada2 = StringVar()
        self.ent2 = Entry(self.jan, bg = "#131644", font = "Century\ Gothic 14",fg = "white",bd = 0, textvariable = entrada2,insertbackground='white')
        self.ent2.place(relx = 0.155, rely = 0.523, relwidth = 0.69, relheight = 0.055)
        entrada2.set("Confirme sua nova senha")
            
        self.ent1.bind("<1>",self.limpard51)
        self.ent2.bind("<1>",self.limpard52)
        self.lbl1.bind("<1>",self.voltatexto)
        
    def limpard51(self,evento=None):
        self.limpar(entrada1, "Digite sua nova senha")
    
    def limpard52(self,evento=None):
        self.limpar(entrada2, "Confirme sua nova senha")
        
    def voltatexto(self,vento=None):
        x = entrada1.get()
        if x == "":
            entrada1.set("Digite sua nova senha")
        y = entrada2.get()
        if y == "":
            entrada2.set("Confirme sua nova senha")
    
    def teladoador6(self):
   
        self.img1 = PhotoImage(file = "C:\\Users\\res0130160\\OneDrive - Firjan\\Arquivos\\Kindly\\Doador6.png")
        self.img2 = PhotoImage(file = "C:\\Users\\res0130160\\OneDrive - Firjan\\Arquivos\\Kindly\\btnCadastrar.PNG")
        self.img3 = PhotoImage(file = "C:\\Users\\res0130160\\OneDrive - Firjan\\Arquivos\\Kindly\\btnSetinha.PNG")

        self.lbl1 = Label(self.jan, image = self.img1)
        self.lbl1.place(relx = 0, rely = 0, relwidth =1, relheight = 1)
    

        self.btn1 = Button(self.jan, bg = "#131644",bd = 0, activebackground = "#131644", image = self.img2 ,command = lambda: self.conexãod6())
        self.btn1.place(relx = 0.29, rely = 0.8, relwidth = 0.42, relheight = 0.15)
        
        self.btn2 = Button(self.jan, bg = "#131644",bd = 0, activebackground = "#131644", image = self.img3 ,command = lambda: self.teladoador1())
        self.btn2.place(relx = 0.03, rely = 0.055, relwidth = 0.15, relheight = 0.06)
        

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

        self.ent1.bind("<1>",self.limpard61)
        self.ent2.bind("<1>",self.limpard62)
        self.ent3.bind("<1>",self.limpard63)
        self.ent4.bind("<1>",self.limpard64)
        self.lbl1.bind("<1>",self.voltatexto)

    def limpard61(self,evento=None):
        self.limpar(entrada1, "Digite seu nome de usuário")
    
    def limpard62(self,evento=None):
        self.limpar(entrada2, "Digite seu e-mail")
            
    def limpard63(self,evento=None):
        self.limpar(entrada3, "Digite sua senha")
    
    def limpard64(self,evento=None):
        self.limpar(entrada4, "Confirme sua senha")
            
    
    def voltatexto(self,vento=None):
        x = entrada1.get()
        if x == "":
            entrada1.set("Digite seu nome de usuário") 
        y = entrada2.get()
        if y == "":
            entrada2.set("Digite seu e-mail")
        z = entrada3.get()
        if z == "":
            entrada3.set("Digite sua senha") 
        a = entrada4.get()
        if a == "":
            entrada4.set("Confirme sua senha")

    def conexãod6(self):
        self.nomescrito = entrada1.get()
        self.emailescrito = entrada2.get()
        self.senhaescrita = entrada3.get()
        self.senhaescrita2 = entrada4.get()
        self.x = False 
        try:
            print(self.emailescrito)
            cursor.execute("SELECT email FROM doadores WHERE email = '{}'".format(self.emailescrito))
            for i in cursor:
                for x in i:
                    self.listad1_1.append(x)
            self.emaildoador = self.listad1_1[0]
            print(self.emaildoador)
            if self.emaildoador == self.emailescrito:
                self.lbl2 = Label(self.jan, text = "E-mail já utilizado!", font = "Century\ Gothic 12", fg = "#FE4A49", bg = "#131644")
                self.lbl2.place(relx = 0.12, rely = 0.5, relwidth = 0.5, relheight = 0.05)
            else:
                self.x = True
            
        except Exception as e: 
            print(e)
            self.lbl2 = Label(self.jan, text = "E-mail já utilizado", font = "Century\ Gothic 14", fg = "#FE4A49", bg = "#131644")
            self.lbl2.place(relx = 0.12, rely = 0.5, relwidth = 0.5, relheight = 0.05)
    
        if self.x == True:
            self.teladoador1()
    
    def teladoador7(self):  
        self.img1 = PhotoImage(file = "C:\\Users\\res0130160\\OneDrive - Firjan\\Arquivos\\Kindly\\Doador7.png")
        self.img2 = PhotoImage(file = "C:\\Users\\res0130160\\OneDrive - Firjan\\Arquivos\\Kindly\\btnPerfil.PNG")
        self.img3 = PhotoImage(file = "C:\\Users\\res0130160\\OneDrive - Firjan\\Arquivos\\Kindly\\btnChat.PNG")
        self.img4 = PhotoImage(file = "C:\\Users\\res0130160\\OneDrive - Firjan\\Arquivos\\Kindly\\btnLupa.PNG")
        self.img5 = PhotoImage(file = "C:\\Users\\res0130160\\OneDrive - Firjan\\Arquivos\\Kindly\\btnPerfilmaior.PNG")
    

        self.lbl1 = Label(self.jan, image = self.img1)
        self.lbl1.place(relx = 0, rely = 0, relwidth =1, relheight = 1)
        
        self.lbl2 = Label(self.jan, bg = "#BDAB9F", fg = "black", text = "Nome da instituição", font = " Century\ Gothic 14")
        self.lbl2.place(relx = 0.18, rely = 0.145, relwidth =0.62, relheight = 0.04)
        
        self.lbl3 = Label(self.jan, bg = "#BDAB9F", fg = "black", text = "Nome da instituição", font = " Century\ Gothic 14")
        self.lbl3.place(relx = 0.18, rely = 0.695, relwidth =0.62, relheight = 0.04)
        

        self.btn1 = Button(self.jan, bg = "#131644",bd = 0, activebackground = "#131644", image = self.img2 ,command = lambda: self.teladoador10())
        self.btn1.place(relx = 0.035, rely = 0.009, relwidth = 0.12, relheight = 0.08)
       
        self.btn2 = Button(self.jan, bg = "#131644",bd = 0, activebackground = "#131644", image = self.img3 ,command = lambda: self.teladoador9())
        self.btn2.place(relx = 0.64, rely = 0.009, relwidth = 0.15, relheight = 0.08)
        
        self.btn3 = Button(self.jan, bg = "#131644",bd = 0, activebackground = "#131644", image = self.img4 ,command = lambda: self.teladoador12())
        self.btn3.place(relx = 0.83, rely = 0.009, relwidth = 0.15, relheight = 0.08)
        
        self.btn4 = Button(self.jan, bg = "#131644",bd = 0, activebackground = "#131644", image = self.img5 ,command = lambda: self.teladoador8())
        self.btn4.place(relx = 0.02, rely = 0.1, relwidth = 0.17, relheight = 0.12)
        
        self.btn5 = Button(self.jan, bg = "#131644",bd = 0, activebackground = "#131644", image = self.img5 ,command = lambda: self.teladoador8())
        self.btn5.place(relx = 0.02, rely = 0.65, relwidth = 0.17, relheight = 0.12)
    
    def teladoador8(self):   
        self.img1 = PhotoImage(file = "C:\\Users\\res0130160\\OneDrive - Firjan\\Arquivos\\Kindly\\Doador8.png")
        self.img2 = PhotoImage(file = "C:\\Users\\res0130160\\OneDrive - Firjan\\Arquivos\\Kindly\\btnPerfilgg.PNG")
        self.img3 = PhotoImage(file = "C:\\Users\\res0130160\\OneDrive - Firjan\\Arquivos\\Kindly\\btnSetinha.PNG")
        self.img4 = PhotoImage(file = "C:\\Users\\res0130160\\OneDrive - Firjan\\Arquivos\\Kindly\\btnChat.PNG")
        self.img5 = PhotoImage(file = "C:\\Users\\res0130160\\OneDrive - Firjan\\Arquivos\\Kindly\\btnDinheiro.PNG")
    

        self.lbl1 = Label(self.jan, image = self.img1)
        self.lbl1.place(relx = 0, rely = 0, relwidth =1, relheight = 1)
        
        self.lbl2 = Label(self.jan, bg = "#BDAB9F", fg = "black", text = "Nome da instituição", font = " Century\ Gothic 14")
        self.lbl2.place(relx = 0.32, rely = 0.165, relwidth =0.62, relheight = 0.04)


        self.btn1 = Button(self.jan, bg = "#131644",bd = 0, activebackground = "#131644", image = self.img2 ,command = lambda: self.teste())
        self.btn1.place(relx = 0.05, rely = 0.123, relwidth = 0.22, relheight = 0.14)
        
        self.btn2 = Button(self.jan, bg = "#131644",bd = 0, activebackground = "#131644", image = self.img3 ,command = lambda: self.teladoador7())
        self.btn2.place(relx = 0.05, rely = 0.03, relwidth = 0.15, relheight = 0.06)
        
        self.btn3 = Button(self.jan, bg = "#131644",bd = 0, activebackground = "#131644", image = self.img4 ,command = lambda: self.teladoador13())
        self.btn3.place(relx = 0.2, rely = 0.02, relwidth = 0.22, relheight = 0.08)
        
        self.btn4 = Button(self.jan, bg = "#131644",bd = 0, activebackground = "#131644", image = self.img5 ,command = lambda: self.teladoador14())
        self.btn4.place(relx = 0.82, rely = 0.015, relwidth = 0.15, relheight = 0.08)
        
    def teladoador9(self):
        self.img1 = PhotoImage(file = "C:\\Users\\res0130160\\OneDrive - Firjan\\Arquivos\\Kindly\\Inst10.png")
        self.img2 = PhotoImage(file = "C:\\Users\\res0130160\\OneDrive - Firjan\\Arquivos\\Kindly\\btnPerfilmaior.PNG")
        self.img3 = PhotoImage(file = "C:\\Users\\res0130160\\OneDrive - Firjan\\Arquivos\\Kindly\\btnSetinha.PNG")
    
        self.lbl1 = Label(self.jan, image = self.img1)
        self.lbl1.place(relx = 0, rely = 0, relwidth =1, relheight = 1)
    
    
        self.btn1 = Button(self.jan, bg = "#131644",bd = 0, activebackground = "gray",command = lambda: self.teladoador13())
        self.btn1.place(relx = 0, rely = 0.125, relwidth = 1, relheight = 0.11)
       
        self.btn2 = Button(self.jan, bg = "#131644",bd = 0, activebackground = "#131644", image = self.img2 ,command = lambda: self.teladoador8())
        self.btn2.place(relx = 0.05, rely = 0.125, relwidth = 0.17, relheight = 0.11)
        
        self.btn1 = Button(self.jan, bg = "#131644",bd = 0, activebackground = "gray",command = lambda: self.teladoador13())
        self.btn1.place(relx = 0, rely = 0.235, relwidth = 1, relheight = 0.11)
       
        self.btn2 = Button(self.jan, bg = "#131644",bd = 0, activebackground = "#131644", image = self.img2 ,command = lambda: self.teladoador8())
        self.btn2.place(relx = 0.05, rely = 0.235, relwidth = 0.17, relheight = 0.11)
        
        self.btn1 = Button(self.jan, bg = "#131644",bd = 0, activebackground = "gray",command = lambda: self.teladoador13())
        self.btn1.place(relx = 0, rely = 0.345, relwidth = 1, relheight = 0.11)
       
        self.btn2 = Button(self.jan, bg = "#131644",bd = 0, activebackground = "#131644", image = self.img2 ,command = lambda: self.teladoador8())
        self.btn2.place(relx = 0.05, rely = 0.345, relwidth = 0.17, relheight = 0.11)
        
        self.btn1 = Button(self.jan, bg = "#131644",bd = 0, activebackground = "gray",command = lambda: self.teladoador13())
        self.btn1.place(relx = 0, rely = 0.455, relwidth = 1, relheight = 0.11)
       
        self.btn2 = Button(self.jan, bg = "#131644",bd = 0, activebackground = "#131644", image = self.img2 ,command = lambda: self.teladoador8())
        self.btn2.place(relx = 0.05, rely = 0.455, relwidth = 0.17, relheight = 0.11)
        
        self.btn1 = Button(self.jan, bg = "#131644",bd = 0, activebackground = "gray",command = lambda: self.teladoador13())
        self.btn1.place(relx = 0, rely = 0.565, relwidth = 1, relheight = 0.11)
       
        self.btn2 = Button(self.jan, bg = "#131644",bd = 0, activebackground = "#131644", image = self.img2 ,command = lambda: self.teladoador8())
        self.btn2.place(relx = 0.05, rely = 0.565, relwidth = 0.17, relheight = 0.11)
        
        self.btn1 = Button(self.jan, bg = "#131644",bd = 0, activebackground = "gray",command = lambda: self.teladoador13())
        self.btn1.place(relx = 0, rely = 0.675, relwidth = 1, relheight = 0.11)
       
        self.btn2 = Button(self.jan, bg = "#131644",bd = 0, activebackground = "#131644", image = self.img2 ,command = lambda: self.teladoador8())
        self.btn2.place(relx = 0.05, rely = 0.675, relwidth = 0.17, relheight = 0.11)
        
        self.btn1 = Button(self.jan, bg = "#131644",bd = 0, activebackground = "gray",command = lambda: self.teladoador13())
        self.btn1.place(relx = 0, rely = 0.785, relwidth = 1, relheight = 0.11)
       
        self.btn2 = Button(self.jan, bg = "#131644",bd = 0, activebackground = "#131644", image = self.img2 ,command = lambda: self.teladoador8())
        self.btn2.place(relx = 0.05, rely = 0.785, relwidth = 0.17, relheight = 0.11)
        
        self.btn1 = Button(self.jan, bg = "#131644",bd = 0, activebackground = "gray",command = lambda: self.teladoador13())
        self.btn1.place(relx = 0, rely = 0.895, relwidth = 1, relheight = 0.11)
       
        self.btn2 = Button(self.jan, bg = "#131644",bd = 0, activebackground = "#131644", image = self.img2 ,command = lambda: self.teladoador8())
        self.btn2.place(relx = 0.05, rely = 0.895, relwidth = 0.17, relheight = 0.11)
        
        self.btn3 = Button(self.jan, bg = "#131644",bd = 0, activebackground = "#131644", image = self.img3 ,command = lambda: self.teladoador8())
        self.btn3.place(relx = 0.07, rely = 0.03, relwidth = 0.15, relheight = 0.06)

        
        self.lbl2 = Label(self.jan, bg = "#131644", fg = "white", text = "Nome da instituição", font = " Century\ Gothic 14",anchor = "w")
        self.lbl2.place(relx = 0.26, rely = 0.145, relwidth =0.55, relheight = 0.04)
        
        self.lbl3 = Label(self.jan, bg = "#131644", fg = "white", text = "Msg...", font = " Century\ Gothic 10",anchor= "w")
        self.lbl3.place(relx = 0.26, rely = 0.185, relwidth =0.55, relheight = 0.03)
        
        self.lbl2 = Label(self.jan, bg = "#131644", fg = "white", text = "Nome da instituição", font = " Century\ Gothic 14",anchor = "w")
        self.lbl2.place(relx = 0.26, rely = 0.255, relwidth =0.55, relheight = 0.04)
        
        self.lbl3 = Label(self.jan, bg = "#131644", fg = "white", text = "Msg...", font = " Century\ Gothic 10",anchor= "w")
        self.lbl3.place(relx = 0.26, rely = 0.295, relwidth =0.55, relheight = 0.03)
        
        self.lbl2 = Label(self.jan, bg = "#131644", fg = "white", text = "Nome da instituição", font = " Century\ Gothic 14",anchor = "w")
        self.lbl2.place(relx = 0.26, rely = 0.365, relwidth =0.55, relheight = 0.04)
        
        self.lbl3 = Label(self.jan, bg = "#131644", fg = "white", text = "Msg...", font = " Century\ Gothic 10",anchor= "w")
        self.lbl3.place(relx = 0.26, rely = 0.405, relwidth =0.55, relheight = 0.03)
        
        self.lbl2 = Label(self.jan, bg = "#131644", fg = "white", text = "Nome da instituição", font = " Century\ Gothic 14",anchor = "w")
        self.lbl2.place(relx = 0.26, rely = 0.475, relwidth =0.55, relheight = 0.04)
        
        self.lbl3 = Label(self.jan, bg = "#131644", fg = "white", text = "Msg...", font = " Century\ Gothic 10",anchor= "w")
        self.lbl3.place(relx = 0.26, rely = 0.515, relwidth =0.55, relheight = 0.03)
        
        self.lbl2 = Label(self.jan, bg = "#131644", fg = "white", text = "Nome da instituição", font = " Century\ Gothic 14",anchor = "w")
        self.lbl2.place(relx = 0.26, rely = 0.585, relwidth =0.55, relheight = 0.04)
        
        self.lbl3 = Label(self.jan, bg = "#131644", fg = "white", text = "Msg...", font = " Century\ Gothic 10",anchor= "w")
        self.lbl3.place(relx = 0.26, rely = 0.625, relwidth =0.55, relheight = 0.03)
        
        self.lbl2 = Label(self.jan, bg = "#131644", fg = "white", text = "Nome da instituição", font = " Century\ Gothic 14",anchor = "w")
        self.lbl2.place(relx = 0.26, rely = 0.695, relwidth =0.55, relheight = 0.04)
        
        self.lbl3 = Label(self.jan, bg = "#131644", fg = "white", text = "Msg...", font = " Century\ Gothic 10",anchor= "w")
        self.lbl3.place(relx = 0.26, rely = 0.735, relwidth =0.55, relheight = 0.03)
        
        self.lbl2 = Label(self.jan, bg = "#131644", fg = "white", text = "Nome da instituição", font = " Century\ Gothic 14",anchor = "w")
        self.lbl2.place(relx = 0.26, rely = 0.805, relwidth =0.55, relheight = 0.04)
        
        self.lbl3 = Label(self.jan, bg = "#131644", fg = "white", text = "Msg...", font = " Century\ Gothic 10",anchor= "w")
        self.lbl3.place(relx = 0.26, rely = 0.845, relwidth =0.55, relheight = 0.03)
        
        self.lbl2 = Label(self.jan, bg = "#131644", fg = "white", text = "Nome da instituição", font = " Century\ Gothic 14",anchor = "w")
        self.lbl2.place(relx = 0.26, rely = 0.915, relwidth =0.55, relheight = 0.04)
        
        self.lbl3 = Label(self.jan, bg = "#131644", fg = "white", text = "Msg...", font = " Century\ Gothic 10",anchor= "w")
        self.lbl3.place(relx = 0.26, rely = 0.955, relwidth =0.55, relheight = 0.03)
        
    def teladoador10(self):
        self.img1 = PhotoImage(file = "C:\\Users\\res0130160\\OneDrive - Firjan\\Arquivos\\Kindly\\Doador10.png")
        self.img2 = PhotoImage(file = "C:\\Users\\res0130160\\OneDrive - Firjan\\Arquivos\\Kindly\\btnPerfilgg.PNG")
        self.img3 = PhotoImage(file = "C:\\Users\\res0130160\\OneDrive - Firjan\\Arquivos\\Kindly\\btnSetinha.PNG")
        self.img4 = PhotoImage(file = "C:\\Users\\res0130160\\OneDrive - Firjan\\Arquivos\\Kindly\\btnAddcartao.PNG")

        self.lbl1 = Label(self.jan, image = self.img1)
        self.lbl1.place(relx = 0, rely = 0, relwidth =1, relheight = 1)
        
        self.lbl2 = Label(self.jan, bg = "#BDAB9F", fg = "black", text = "Nome do doador", font = " Century\ Gothic 14")
        self.lbl2.place(relx = 0.31, rely = 0.165, relwidth =0.62, relheight = 0.04)
        

        self.btn1 = Button(self.jan, bg = "#131644",bd = 0, activebackground = "#131644", image = self.img2 ,command = lambda: self.teste())
        self.btn1.place(relx = 0.05, rely = 0.123, relwidth = 0.22, relheight = 0.14)
        
        self.btn2 = Button(self.jan, bg = "#131644",bd = 0, activebackground = "#131644", image = self.img3 ,command = lambda: self.teladoador7())
        self.btn2.place(relx = 0.055, rely = 0.025, relwidth = 0.15, relheight = 0.06)
        
        self.btn3 = Button(self.jan, bg = "#131644",bd = 0, activebackground = "#131644", image = self.img4 ,command = lambda: self.teladoador11())
        self.btn3.place(relx = 0.13, rely = 0.74, relwidth = 0.72, relheight = 0.15)
    
    def teladoador11(self):  
        self.img1 = PhotoImage(file = "C:\\Users\\res0130160\\OneDrive - Firjan\\Arquivos\\Kindly\\Doador11.png")
        self.img2 = PhotoImage(file = "C:\\Users\\res0130160\\OneDrive - Firjan\\Arquivos\\Kindly\\btnCadastrar.PNG")
        self.img3 = PhotoImage(file = "C:\\Users\\res0130160\\OneDrive - Firjan\\Arquivos\\Kindly\\btnSetinha.PNG")
    

        self.lbl1 = Label(self.jan, image = self.img1)
        self.lbl1.place(relx = 0, rely = 0, relwidth =1, relheight = 1)
    

        self.btn1 = Button(self.jan, bg = "#131644",bd = 0, activebackground = "#131644", image = self.img2 ,command = lambda: self.teladoador10())
        self.btn1.place(relx = 0.29, rely = 0.8, relwidth = 0.42, relheight = 0.15)
        
        self.btn2 = Button(self.jan, bg = "#131644",bd = 0, activebackground = "#131644", image = self.img3 ,command = lambda: self.teladoador10())
        self.btn2.place(relx = 0.055, rely = 0.025, relwidth = 0.15, relheight = 0.06)
        

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

        self.ent1.bind("<1>",self.limpard111)
        self.ent1.bind("<KeyRelease>",self.maiusculo)
        self.ent2.bind("<1>",self.limpard112)
        self.ent3.bind("<1>",self.limpard113)
        self.ent4.bind("<1>",self.limpard114)
        self.ent5.bind("<1>",self.limpard115)
        self.ent6.bind("<1>",self.limpard116)
        self.lbl1.bind("<1>",self.voltatexto)
    
    def limpard111(self,evento=None):
        self.limpar(entrada1, "Nome do cartão")
    
    def limpard112(self,evento=None):
        self.limpar(entrada2, "CPF/CNPJ")
            
    def limpard113(self,evento=None):
        self.limpar(entrada3, "Número do cartão")
    
    def limpard114(self,evento=None):
        self.limpar(entrada4, "CVC")
        
    def limpard115(self,evento=None):
        self.limpar(entrada5, "Vencimento")
    
    def limpard116(self,evento=None):
        self.limpar(entrada6, "Bandeira")
            
    
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
        
    def teladoador12(self):  
        self.img1 = PhotoImage(file = "C:\\Users\\res0130160\\OneDrive - Firjan\\Arquivos\\Kindly\\Doador12.png")
        self.img2 = PhotoImage(file = "C:\\Users\\res0130160\\OneDrive - Firjan\\Arquivos\\Kindly\\btnLupinha.PNG")
        self.img3 = PhotoImage(file = "C:\\Users\\res0130160\\OneDrive - Firjan\\Arquivos\\Kindly\\btnSetinha.PNG")

        self.lbl1 = Label(self.jan, image = self.img1)
        self.lbl1.place(relx = 0, rely = 0, relwidth =1, relheight = 1)
        
       
        self.btn1 = Button(self.jan, bg = "#FEAD77",bd = 0, activebackground = "#FEAD77", image = self.img2 ,command = lambda: self.pesquisa())
        self.btn1.place(relx = 0.86, rely = 0.14, relwidth = 0.1, relheight = 0.075)
        
        self.btn2 = Button(self.jan, bg = "#131644",bd = 0, activebackground = "#131644", image = self.img3 ,command = lambda: self.teladoador7())
        self.btn2.place(relx = 0.06, rely = 0.03, relwidth = 0.15, relheight = 0.06)
    

        global entrada1
        entrada1 = StringVar()
        self.ent1 = Entry(self.jan, bg = "#FEAD77", font = "Century\ Gothic 14",fg = "white", textvariable = entrada1, bd = 0)
        self.ent1.place(relx = 0.045, rely = 0.14, relwidth = 0.82, relheight = 0.075)
        entrada1.set("Digite aqui...")
        
        self.ent1.bind("<1>",self.limpard121)
        self.lbl1.bind("<1>",self.voltatexto)

        self.listb1 = Listbox(self.jan, bg = "#131644",fg = "white", font = "Century\ Gothic 14", bd = 0, selectbackground = "#FEAD77")
        self.listb1.place(relx = 0.01, rely = 0.23, relwidth = 0.98, relheight = 0.41)
        
    def pesquisa(self):
        self.listb1.insert(END, "Nome do instituto")
        self.listb1.insert(END, "Nome do instituto")
        self.listb1.insert(END, "Nome do instituto")
        
    def limpard121(self,evento=None):
        self.limpar(entrada1, "Digite aqui...")
    
    def voltatexto(self,vento=None):
        x = entrada1.get()
        if x == "":
            entrada1.set("Digite aqui...")
    
    def teladoador13(self): 
        self.img1 = PhotoImage(file = "C:\\Users\\res0130160\\OneDrive - Firjan\\Arquivos\\Kindly\\Doador13.png")
        self.img2 = PhotoImage(file = "C:\\Users\\res0130160\\OneDrive - Firjan\\Arquivos\\Kindly\\btnPerfilmaior.PNG")
        self.img3 = PhotoImage(file = "C:\\Users\\res0130160\\OneDrive - Firjan\\Arquivos\\Kindly\\btnSetinha.PNG")
    
    
        self.lbl1 = Label(self.jan, image = self.img1)
        self.lbl1.place(relx = 0, rely = 0, relwidth =1, relheight = 1)
        

        self.btn1 = Button(self.jan,text = "Nome da instituição", font = "Century\ Gothic 14",fg = "white", bg = "#131644",bd = 0, activebackground = "gray",command = lambda: self.teste())
        self.btn1.place(relx = 0.23, rely = 0.01, relwidth = 0.78, relheight = 0.09)
       
        self.btn2 = Button(self.jan, bg = "#131644",bd = 0, activebackground = "#131644", image = self.img2 ,command = lambda: self.teladoador8())
        self.btn2.place(relx = 0.21, rely = 0.01, relwidth = 0.17, relheight = 0.08)
        
        self.btn3 = Button(self.jan, bg = "#131644",bd = 0, activebackground = "#131644", image = self.img3 ,command = lambda: self.teladoador9())
        self.btn3.place(relx = 0.03, rely = 0.025, relwidth = 0.15, relheight = 0.06)
    

        global entrada1
        entrada1 = StringVar()
        self.ent1 = Entry(self.jan, bg = "#131644", font = "Century\ Gothic 14",fg = "white",bd = 3, textvariable = entrada1)
        self.ent1.place(relx = 0.01, rely = 0.565, relwidth = 0.98, relheight = 0.08)
        entrada1.set("Digite aqui...")
        
        self.ent1.bind("<1>",self.limpard131)
        self.lbl1.bind("<1>",self.voltatexto)
            
    def limpard131(self,evento=None):
        self.limpar(entrada1, "Digite aqui...")
    
    def voltatexto(self,vento=None):
        x = entrada1.get()
        if x == "":
            entrada1.set("Digite aqui...")
    
    def teladoador14(self): 
        self.img1 = PhotoImage(file = "C:\\Users\\res0130160\\OneDrive - Firjan\\Arquivos\\Kindly\\Doador14.png")
        self.img2 = PhotoImage(file = "C:\\Users\\res0130160\\OneDrive - Firjan\\Arquivos\\Kindly\\btnXapagar.PNG")
        self.img3 = PhotoImage(file = "C:\\Users\\res0130160\\OneDrive - Firjan\\Arquivos\\Kindly\\btnCerto.PNG")
        self.img4 = PhotoImage(file = "C:\\Users\\res0130160\\OneDrive - Firjan\\Arquivos\\Kindly\\btnSetinha.PNG")
        self.imgbt1 = PhotoImage(file = "C:\\Users\\res0130160\\OneDrive - Firjan\\Arquivos\\Kindly\\btnum1.PNG")
        self.imgbt2 = PhotoImage(file = "C:\\Users\\res0130160\\OneDrive - Firjan\\Arquivos\\Kindly\\btnum2.PNG")
        self.imgbt3 = PhotoImage(file = "C:\\Users\\res0130160\\OneDrive - Firjan\\Arquivos\\Kindly\\btnum3.PNG")
        self.imgbt4 = PhotoImage(file = "C:\\Users\\res0130160\\OneDrive - Firjan\\Arquivos\\Kindly\\btnum4.PNG")
        self.imgbt5 = PhotoImage(file = "C:\\Users\\res0130160\\OneDrive - Firjan\\Arquivos\\Kindly\\btnum5.PNG")
        self.imgbt6 = PhotoImage(file = "C:\\Users\\res0130160\\OneDrive - Firjan\\Arquivos\\Kindly\\btnum6.PNG")
        self.imgbt7 = PhotoImage(file = "C:\\Users\\res0130160\\OneDrive - Firjan\\Arquivos\\Kindly\\btnum7.PNG")
        self.imgbt8 = PhotoImage(file = "C:\\Users\\res0130160\\OneDrive - Firjan\\Arquivos\\Kindly\\btnum8.PNG")
        self.imgbt9 = PhotoImage(file = "C:\\Users\\res0130160\\OneDrive - Firjan\\Arquivos\\Kindly\\btnum9.PNG")
        self.imgbt0 = PhotoImage(file = "C:\\Users\\res0130160\\OneDrive - Firjan\\Arquivos\\Kindly\\btnum0.PNG")
    

        self.lbl1 = Label(self.jan, image = self.img1)
        self.lbl1.place(relx = 0, rely = 0, relwidth =1, relheight = 1)
    

        self.btn1 = Button(self.jan, bg = "#131644",bd = 0, activebackground = "#131644", image = self.img2 ,command = lambda: self.apagar())
        self.btn1.place(relx = 0.1, rely = 0.81, relwidth = 0.2, relheight = 0.12)
        self.btn2 = Button(self.jan, bg = "#131644",bd = 0, activebackground = "#131644", image = self.img3 ,command = lambda: self.teste())
        self.btn2.place(relx = 0.7, rely = 0.81, relwidth = 0.2, relheight = 0.12)
        self.btn3 = Button(self.jan, bg = "#131644",bd = 0, activebackground = "#131644", image = self.img4 ,command = lambda: self.teladoador8())
        self.btn3.place(relx = 0.07, rely = 0.03, relwidth = 0.15, relheight = 0.06)
        
        self.btnnum = Button(self.jan, bg = "#131644", image = self.imgbt1, activebackground= "#131644", bd = 0, command = lambda: self.nums(1))
        self.btnnum.place(relx = 0.09, rely = 0.42, relwidth = 0.2, relheight = 0.12)
        
        self.btnnum = Button(self.jan, bg = "#131644", image = self.imgbt2, activebackground= "#131644", bd = 0, command = lambda: self.nums(2))
        self.btnnum.place(relx = 0.397, rely = 0.42, relwidth = 0.2, relheight = 0.12)
        
        self.btnnum = Button(self.jan, bg = "#131644", image = self.imgbt3, activebackground= "#131644", bd = 0, command = lambda: self.nums(3))
        self.btnnum.place(relx = 0.7, rely = 0.42, relwidth = 0.2, relheight = 0.12)
        
        self.btnnum = Button(self.jan, bg = "#131644", image = self.imgbt4, activebackground= "#131644", bd = 0, command = lambda: self.nums(4))
        self.btnnum.place(relx = 0.09, rely = 0.55, relwidth = 0.2, relheight = 0.12)
        
        self.btnnum = Button(self.jan, bg = "#131644", image = self.imgbt5, activebackground= "#131644", bd = 0, command = lambda: self.nums(5))
        self.btnnum.place(relx = 0.397, rely = 0.55, relwidth = 0.2, relheight = 0.12)
        
        self.btnnum = Button(self.jan, bg = "#131644", image = self.imgbt6, activebackground= "#131644", bd = 0, command = lambda: self.nums(6))
        self.btnnum.place(relx = 0.703, rely = 0.55, relwidth = 0.2, relheight = 0.12)
        
        self.btnnum = Button(self.jan, bg = "#131644", image = self.imgbt7, activebackground= "#131644", bd = 0, command = lambda: self.nums(7))
        self.btnnum.place(relx = 0.09, rely = 0.68, relwidth = 0.2, relheight = 0.12)
        
        self.btnnum = Button(self.jan, bg = "#131644", image = self.imgbt8, activebackground= "#131644", bd = 0, command = lambda: self.nums(8))
        self.btnnum.place(relx = 0.397, rely = 0.68, relwidth = 0.2, relheight = 0.12)
        
        self.btnnum = Button(self.jan, bg = "#131644", image = self.imgbt9, activebackground= "#131644", bd = 0, command = lambda: self.nums(9))
        self.btnnum.place(relx = 0.7, rely = 0.68, relwidth = 0.2, relheight = 0.12)
        
        self.btnnum = Button(self.jan, bg = "#131644", image = self.imgbt0, activebackground= "#131644", bd = 0, command = lambda: self.nums(0))
        self.btnnum.place(relx = 0.4, rely = 0.814, relwidth = 0.2, relheight = 0.12)
   

        global entrada1
        entrada1 = StringVar()
        self.ent1 = Entry(self.jan, disabledbackground="#131644", font = "Century\ Gothic 14",disabledforeground= "white", textvariable = entrada1, bd = 0,state = "disabled", justify = "center")
        self.ent1.place(relx = 0.19, rely = 0.27, relwidth = 0.62, relheight = 0.05)
        entrada1.set("")

        self.lbl2 = Label(self.jan, text = "R$", font = "Century\ Gothic 14", bg = "#131644", fg = "white")
        self.lbl2.place(relx = 0.2, rely = 0.27, relwidth = 0.06, relheight = 0.05)
        
    def nums(self,n):
        self.textoent = entrada1.get()
        self.textoent = self.textoent + str(n)
        self.textoent = self.textoent.replace(",","") 
        self.textoent = self.textoent.replace(".","") 
        
        if len(self.textoent)>2:
            self.textoent = self.textoent[:len(self.textoent) -2] + ',' + self.textoent[-2:]
        
        if len(self.textoent)>6:
            self.textoent = self.textoent[:len(self.textoent) -6] + '.' + self.textoent[-6:]

        if len(self.textoent)>10:
            self.textoent = self.textoent[:len(self.textoent) -10] + '.' + self.textoent[-10:]
        
        if len(self.textoent)>14:
            self.textoent = self.textoent[:len(self.textoent) -14] + '.' + self.textoent[-14:]
        
        entrada1.set(str(self.textoent))
    
    def apagar(self):
        entrada1.set("")
        
Kindly()