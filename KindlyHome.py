from tkinter import *
from threading import Timer
from tkinter import filedialog
import random
import string
import mysql.connector 
import re
import os

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

global regex
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

global nd
nd = ""

class Kindly():
    def __init__(self):
        self.jan = Tk()
        self.jan.geometry("375x667+550+20")
        self.jan.title("Kindly")
        self.jan.config(bg = "white")
        self.jan.resizable(False,False)
        self.jan.iconbitmap(os.path.abspath("logoKindly.ico"))
        self.imagens()
        self.labels()
        
        self.listad1_1 = []
        self.listad1_2 = []
        self.listad2_1 = []
        self.listad5_1 = []
        self.listad6_1 = []
        
        self.lbl2T = False
        self.lbl3T = False
        self.lbl4T = False
        self.lbl5T = False
        self.lbl6T = False
        
        self.lbli1T = False
        self.lbli2T = False
        self.lbli3T = False
        self.lbli4T = False
        self.lbli5T = False

        self.lblc1T = False
        self.lblc2T = False
        self.lblc3T = False
        self.lblc4T = False
        self.lblc5T = False
        self.lblc6T = False
        self.lblc7T = False
        self.lblc8T = False
        self.lblc9T = False
        self.lblc10T = False
        
        t = Timer(2, self.Padrao2)
        t.start()
        
        self.jan.mainloop()
        
    def teste(self):
        print("sla")
    
    def selecionar(self):
        self.nomearq = filedialog.askopenfilename(initialdir ="C:/", title = "Escolher Arquivo")
    
    def validarcpf(self,cpf):
        cpf = ''.join(re.findall(r'\d', str(cpf)))

        if not cpf or len(cpf) < 11:
            return False

        antigo = [int(d) for d in cpf]

        # Gera CPF com novos dígitos verificadores e compara com CPF informado
        novo = antigo[:9]
        while len(novo) < 11:
            resto = sum([v * (len(novo) + 1 - i) for i, v in enumerate(novo)]) % 11

            digito_verificador = 0 if resto <= 1 else 11 - resto

            novo.append(digito_verificador)

        if novo == antigo:
            return cpf

        return False
    
    def imagens(self):    
        self.img1 = PhotoImage(file = os.path.abspath("Padrao1.png"))
    
    def labels(self):
        self.lbl1 = Label(self.jan, image = self.img1)
        self.lbl1.place(relx = 0, rely = 0, relwidth =1, relheight = 1)
    
    def Padrao2(self):
        self.img1 = PhotoImage(file = os.path.abspath("Padrao2.png"))
        self.img2 = PhotoImage(file = os.path.abspath("btn1 TelaPadrao2.PNG"))
        self.img3 = PhotoImage(file = os.path.abspath("btn2 TelaPadrao2.PNG"))
    
        self.lbl1 = Label(self.jan, image = self.img1)
        self.lbl1.place(relx = 0, rely = 0, relwidth =1, relheight = 1)
    
        self.btn1 = Button(self.jan, bg = "#131644",bd = 0, activebackground = "#131644", image = self.img2 ,command = lambda: self.telainst1())
        self.btn1.place(relx = 0.13, rely = 0.42, relwidth = 0.74, relheight = 0.15)
        self.btn2 = Button(self.jan, bg = "#131644",bd = 0, activebackground = "#131644", image = self.img3 ,command = lambda: self.teladoador1())
        self.btn2.place(relx = 0.13, rely = 0.58, relwidth = 0.74, relheight = 0.15)

    
    def telainst1(self):

        self.img1 = PhotoImage(file = os.path.abspath("Inst1.png"))
        self.img2 = PhotoImage(file = os.path.abspath("btnEntrar.PNG"))
        self.img3 = PhotoImage(file = os.path.abspath("btnSetinha.PNG"))


        self.lbl1 = Label(self.jan, image = self.img1)
        self.lbl1.place(relx = 0, rely = 0, relwidth =1, relheight = 1)


        self.btn1 = Button(self.jan, bg = "#131644",bd = 0, activebackground = "#131644", image = self.img2 ,command = lambda: self.conexãoi1())
        self.btn1.place(relx = 0.29, rely = 0.565, relwidth = 0.42, relheight = 0.15)
        
        self.btn2 = Button(self.jan, bg = "#131644",bd = 0, activebackground = "#131644", image = self.img3 ,command = lambda: self.Padrao2())
        self.btn2.place(relx = 0.03, rely = 0.055, relwidth = 0.15, relheight = 0.06)
        
        self.btn3 = Button(self.jan, text = "Crie agora", font = "Century\ Gothic 18",fg = "#FD824F", bg = "#131644",bd = 0, activebackground = "#131644",command = lambda: self.telainst2e3())
        self.btn3.place(relx = 0.33, rely = 0.84, relwidth = 0.33, relheight = 0.05)


        global entrada1
        entrada1 = StringVar()
        self.ent1 = Entry(self.jan, bg = "#131644", font = "Century\ Gothic 14",fg = "white",bd = 0, textvariable = entrada1,insertbackground='white')
        self.ent1.place(relx = 0.16, rely = 0.368, relwidth = 0.68, relheight = 0.06)
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
    
    def conexãoi1(self):
        self.emailescrito = entrada1.get()
        self.senhaescrita = entrada2.get()
        self.x = False
        try:
            cursor.execute("SELECT email FROM doadortuicoes WHERE email = '{}'".format(self.emailescrito))
            for i in cursor:
                for x in i:
                    self.listad1_1.append(x)
            self.emaildoador = self.listad1_1[0]
            self.listad1_1 = []
            if self.emaildoador == self.emailescrito:
                self.x = True
            else:
                self.lbl2 = Label(self.jan, text = "E-mail e/ou código", font = "Century\ Gothic 14", fg = "#FE4A49", bg = "#131644")
                self.lbl2.place(relx = 0.16, rely = 0.28, relwidth = 0.68, relheight = 0.06)
            
            cursor.execute("SELECT codigo FROM doadortuicoes WHERE email = '{}'".format(self.emailescrito))
            for i in cursor:
                for x in i:
                    self.listad1_2.append(x)
            self.senhadoador = self.listad1_2[0]
            self.listad1_2 = []
            if self.senhadoador == self.senhaescrita:
                self.x = True
            else:
                self.x = False
                self.lbl2 = Label(self.jan, text = "E-mail e/ou código inválidos", font = "Century\ Gothic 14", fg = "#FE4A49", bg = "#131644")
                self.lbl2.place(relx = 0.16, rely = 0.29, relwidth = 0.68, relheight = 0.05)
        except Exception as e: 
            print(e)
            self.x = False
            self.lbl2 = Label(self.jan, text = "E-mail e/ou código inválidos", font = "Century\ Gothic 14", fg = "#FE4A49", bg = "#131644")
            self.lbl2.place(relx = 0.16, rely = 0.29, relwidth = 0.68, relheight = 0.05)
        
        if self.x == True:
            global emailinst
            emailinst = self.emaildoador
            self.telainst5()
    
    def telainst2e3(self):
        self.img1 = PhotoImage(file = os.path.abspath("Inst2.png"))
        self.img2 = PhotoImage(file = os.path.abspath("btnCadastrar.PNG"))
        self.img3 = PhotoImage(file = os.path.abspath("btnSetinha.PNG"))
    
        
        self.lbl1 = Label(self.jan, image = self.img1)
        self.lbl1.place(relx = 0, rely = 0, relwidth =1, relheight = 1)
    
        
        self.btn1 = Button(self.jan, bg = "#131644",bd = 0, activebackground = "#131644", image = self.img2 ,command = lambda: self.conexãoi2())
        self.btn1.place(relx = 0.29, rely = 0.62, relwidth = 0.42, relheight = 0.15)
        
        self.btn2 = Button(self.jan, bg = "#131644",bd = 0, activebackground = "#131644", image = self.img3 ,command = lambda: self.telainst1())
        self.btn2.place(relx = 0.03, rely = 0.055, relwidth = 0.15, relheight = 0.06)
        
        self.btn3 = Button(self.jan, text = "clique aqui", font = "Century\ Gothic 18",fg = "#FD824F", bg = "#131644",bd = 0, activebackground = "#131644",command = lambda: self.telainst4())
        self.btn3.place(relx = 0.32, rely = 0.9, relwidth = 0.37, relheight = 0.05)


        global entrada1
        entrada1 = StringVar()
        self.ent1 = Entry(self.jan, bg = "#131644", font = "Century\ Gothic 14",fg = "white",bd = 0, textvariable = entrada1,insertbackground='white')
        self.ent1.place(relx = 0.155, rely = 0.28, relwidth = 0.69, relheight = 0.055)
        entrada1.set("Digite o nome da instituição")
        
        global entrada2
        entrada2 = StringVar()
        self.ent2 = Entry(self.jan, bg = "#131644", font = "Century\ Gothic 14",fg = "white",bd = 0, textvariable = entrada2,insertbackground='white')
        self.ent2.place(relx = 0.155, rely = 0.4, relwidth = 0.68, relheight = 0.055)
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

    def conexãoi2(self):
        self.nomescrito = entrada1.get()
        self.emailescrito = entrada2.get()
        self.codigoescrito = entrada3.get()
        self.x = False 
        self.y = False
        self.z = False
        try:
            if(re.fullmatch(regex, self.emailescrito)):
                if self.lbli2T == True:
                    self.lbld66.destroy()
                    self.lbli2T = False
                cursor.execute("SELECT email FROM doadortuicoes WHERE email = '{}'".format(self.emailescrito))
                for i in cursor:
                    for x in i:
                        self.listad6_1.append(x)
                self.emaildoador = self.listad6_1[0]
                self.listad6_1 = []
                if self.emaildoador == self.emailescrito:
                    if self.lbli2T == True:
                        self.lbld66.destroy()
                    if self.lbli3T == False:
                        self.lbld62 = Label(self.jan, text = "E-mail já utilizado!", font = "Century\ Gothic 12", fg = "#FE4A49", bg = "#131644")
                        self.lbld62.place(relx = 0.135, rely = 0.47, relwidth = 0.4, relheight = 0.04)
                        self.lbli3T = True
                else:
                    self.x = True
                    if self.lbli3T == True:
                        self.lbld62.destroy()
            else:
                if self.lbli3T == True:
                        self.lbld62.destroy()
                if self.lbli2T == False:
                    self.lbld66 = Label(self.jan, text = "E-mail inválido!", font = "Century\ Gothic 12", fg = "#FE4A49", bg = "#131644")
                    self.lbld66.place(relx = 0.11, rely = 0.47, relwidth = 0.4, relheight = 0.03)
                    self.lbli2T = True
        
        except Exception as e:
            print(e)
            self.x = True
            print(self.lbli2T)
            if self.lbli3T == True:
                self.lbld62.destroy()
                self.lbli3T = False
            if self.lbli2T == True:
                self.lbld66.destroy()
                self.lbli2T = False
    
        if self.codigoescrito == "" or self.codigoescrito == "Digite seu código":
            if self.lbli5T == True:
                self.lbl5.destroy()
                self.lbli5T = False
            if self.lbli4T == False:
                self.lbl4 = Label(self.jan, text = "Digite o código!", font = "Century\ Gothic 12", fg = "#FE4A49", bg = "#131644")
                self.lbl4.place(relx = 0.12, rely = 0.59, relwidth = 0.4, relheight = 0.03)
                self.lbli4T = True
        else:
            try:
                cursor.execute("SELECT codigo FROM doadortuicoes WHERE codigo = '{}'".format(self.codigoescrito))
                for i in cursor:
                    for x in i:
                        self.listad6_1.append(x)
                self.codigoinst = self.listad6_1[0]
                self.listad6_1 = []
                if self.codigoinst == self.codigoescrito:
                    cursor.execute("SELECT id FROM doadortuicoes WHERE codigo = '{}'".format(self.codigoescrito))
                    for i in cursor:
                        for x in i:
                            self.listad6_1.append(x)
                    self.idinst = self.listad6_1[0]
                    self.listad6_1 = []
                    self.y = True
            except Exception as e:
                print(e)
                if self.lbli5T == False:
                    self.lbl5 = Label(self.jan, text = "Código inválido!", font = "Century\ Gothic 12", fg = "#FE4A49", bg = "#131644")
                    self.lbl5.place(relx = 0.12, rely = 0.59, relwidth = 0.4, relheight = 0.03)
                    self.lbli5T = True
        
        if self.nomescrito == "" or self.nomescrito == "Digite o nome da instituição":
            if self.lbli1T == False:
                self.lbl1 = Label(self.jan, text = "Digite o nome!", font = "Century\ Gothic 12", fg = "#FE4A49", bg = "#131644")
                self.lbl1.place(relx = 0.1, rely = 0.35, relwidth = 0.4, relheight = 0.03)
                self.lbli1T = True
        else:
            self.z = True
            if self.lbli1T == True:
                self.lbl1.destroy()

        if self.x == True and self.y == True and self.z == True:
            print(self.nomescrito)
            print(self.emailescrito)
            print(self.idinst)
            try:
                cursor.execute(f"UPDATE doadortuicoes SET nome = '{self.nomescrito}', email = '{self.emailescrito}' where id = '{self.idinst}'")
                conexao.commit()
                self.telainst1()
            except:
                print("deu ruim")
    

    def telainst4(self):
           
        self.img1 = PhotoImage(file = os.path.abspath("Inst4.png"))
        self.img2 = PhotoImage(file = os.path.abspath("btnSetaL.PNG"))
    
        self.lbl1 = Label(self.jan, image = self.img1)
        self.lbl1.place(relx = 0, rely = 0, relwidth =1, relheight = 1)

        self.btn1 = Button(self.jan, bg = "#131644",bd = 0, activebackground = "#131644", image = self.img2 ,command = lambda: self.telainst2e3())
        self.btn1.place(relx = 0.13, rely = 0.75, relwidth = 0.74, relheight = 0.15)

    def telainst5(self):
        cursor.execute("SELECT nome FROM doadortuicoes WHERE email = '{}'".format(emailinst))
        for i in cursor:
            for x in i:
                self.listad6_1.append(x)
            global nomedoador 
            nomedoador= self.listad6_1[0]
            self.listad6_1 = []
        self.img1 = PhotoImage(file = os.path.abspath("Inst5.png"))
        self.img2 = PhotoImage(file = os.path.abspath("btnPerfil.PNG"))
        self.img3 = PhotoImage(file = os.path.abspath("btnChat.PNG"))
        self.img4 = PhotoImage(file = os.path.abspath("btnLupa.PNG"))
        self.img5 = PhotoImage(file = os.path.abspath("btnPerfilmaior.PNG"))
        self.img6 = PhotoImage(file = os.path.abspath("btn+.PNG"))
    
    
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
         
        self.img1 = PhotoImage(file = os.path.abspath("Inst6.png"))
        self.img2 = PhotoImage(file = os.path.abspath("btnPostar.PNG"))
        self.img3 = PhotoImage(file = os.path.abspath("btnCamera.PNG"))
        self.img4 = PhotoImage(file = os.path.abspath("btnSetinha.PNG"))
    
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
          
        self.img1 = PhotoImage(file = os.path.abspath("Inst7.png"))
        self.img2 = PhotoImage(file = os.path.abspath("btnPerfilgg.PNG"))
        self.img3 = PhotoImage(file = os.path.abspath("btnDinheiro.PNG"))
        self.img4 = PhotoImage(file = os.path.abspath("btnSetinha.PNG"))
        self.img5 = PhotoImage(file = os.path.abspath("btnCamerabranca.PNG"))
    
    
        self.lbl1 = Label(self.jan, image = self.img1)
        self.lbl1.place(relx = 0, rely = 0, relwidth =1, relheight = 1)
        
        self.lbl2 = Label(self.jan, bg = "#BDAB9F", fg = "black", text = nomedoador, font = " Century\ Gothic 14")
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
        self.img1 = PhotoImage(file = os.path.abspath("Inst8.png"))
        self.img2 = PhotoImage(file = os.path.abspath("btnPerfilmaior.PNG"))
        self.img3 = PhotoImage(file = os.path.abspath("btnSetinha.PNG"))
    
        
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
       
        self.img1 = PhotoImage(file = os.path.abspath("Inst9.png"))
        self.img2 = PhotoImage(file = os.path.abspath("btnPerfilgg.PNG"))
        self.img3 = PhotoImage(file = os.path.abspath("btnSetinha.PNG"))
    
        
        self.lbl1 = Label(self.jan, image = self.img1)
        self.lbl1.place(relx = 0, rely = 0, relwidth =1, relheight = 1)
        
        self.lbl2 = Label(self.jan, bg = "#BDAB9F", fg = "black", text = "Nome da instituição", font = " Century\ Gothic 14")
        self.lbl2.place(relx = 0.32, rely = 0.165, relwidth =0.62, relheight = 0.04)
        
   
        self.btn1 = Button(self.jan, bg = "#131644",bd = 0, activebackground = "#131644", image = self.img2 ,command = lambda: self.teste())
        self.btn1.place(relx = 0.05, rely = 0.123, relwidth = 0.22, relheight = 0.14)
        
        self.btn2 = Button(self.jan, bg = "#131644",bd = 0, activebackground = "#131644", image = self.img3 ,command = lambda: self.telainst5())
        self.btn2.place(relx = 0.07, rely = 0.03, relwidth = 0.15, relheight = 0.06)
    
    def telainst10(self):  
        self.img1 = PhotoImage(file = os.path.abspath("Inst10.png"))
        self.img2 = PhotoImage(file = os.path.abspath("btnPerfilmaior.PNG"))
        self.img3 = PhotoImage(file = os.path.abspath("btnSetinha.PNG"))
    

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
        
        self.img1 = PhotoImage(file = os.path.abspath("Inst11.png"))
        self.img2 = PhotoImage(file = os.path.abspath("btnPerfilmaior.PNG"))
        self.img3 = PhotoImage(file = os.path.abspath("btnSetinha.PNG"))
    

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
        self.img1 = PhotoImage(file = os.path.abspath("Inst12.png"))
        self.img2 = PhotoImage(file = os.path.abspath("btnPerfilgg.PNG"))
        self.img3 = PhotoImage(file = os.path.abspath("btnSetinha.PNG"))
    
        
        self.lbl1 = Label(self.jan, image = self.img1)
        self.lbl1.place(relx = 0, rely = 0, relwidth =1, relheight = 1)
        
        self.lbl2 = Label(self.jan, bg = "#BDAB9F", fg = "black", text = "Nome do doador", font = " Century\ Gothic 14")
        self.lbl2.place(relx = 0.31, rely = 0.165, relwidth =0.62, relheight = 0.04)
        
        
        self.btn1 = Button(self.jan, bg = "#131644",bd = 0, activebackground = "#131644", image = self.img2 ,command = lambda: self.teste())
        self.btn1.place(relx = 0.05, rely = 0.123, relwidth = 0.22, relheight = 0.14)
        
        self.btn2 = Button(self.jan, bg = "#131644",bd = 0, activebackground = "#131644", image = self.img3 ,command = lambda: self.telainst10())
        self.btn2.place(relx = 0.04, rely = 0.025, relwidth = 0.15, relheight = 0.06)
    
    def telainst13(self):   
        self.img1 = PhotoImage(file = os.path.abspath("doador12.png"))
        self.img2 = PhotoImage(file = os.path.abspath("btnLupinha.PNG"))
        self.img3 = PhotoImage(file = os.path.abspath("btnSetinha.PNG"))
    

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
        self.lbl1.bind("<1>",self.voltatextoi13)
 
        self.listb1 = Listbox(self.jan, bg = "#131644",fg = "white", font = "Century\ Gothic 14", bd = 0, selectbackground = "#FEAD77")
        self.listb1.place(relx = 0.01, rely = 0.23, relwidth = 0.98, relheight = 0.41)
        
    def pesquisa(self):
        self.listb1.insert(END, "Nome do instituto")
        self.listb1.insert(END, "Nome do instituto")
        self.listb1.insert(END, "Nome do instituto")
        
            
    def limpar131(self,evento=None):
        self.limpar(entrada1, "Digite aqui...")
    
    def voltatextoi13(self,vento=None):
        x = entrada1.get()
        if x == "":
            entrada1.set("Digite aqui...")

    def teladoador1(self):    
        self.img1 = PhotoImage(file = os.path.abspath("Doador1.png"))
        self.img2 = PhotoImage(file = os.path.abspath("btnEntrar.PNG"))
        self.img3 = PhotoImage(file = os.path.abspath("btnSetinha.PNG"))    

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
        self.lbl1.bind("<1>",self.voltatextod1)
        
    def limpard11(self,evento=None):
        self.limpar(entrada1, "Digite seu e-mail")
    
    def limpard12(self,evento=None):
        self.limpar(entrada2, "Digite sua senha")
    
    def voltatextod1(self,vento=None):
        x = entrada1.get()
        if x == "":
            entrada1.set("Digite seu e-mail") 
        y = entrada2.get()
        if y == "":
            entrada2.set("Digite sua senha")

    def conexãod1(self):
        self.emailescrito = entrada1.get()
        self.senhaescrita = entrada2.get()
        self.x = False
        try:
            cursor.execute("SELECT email FROM doadores WHERE email = '{}'".format(self.emailescrito))
            for i in cursor:
                for x in i:
                    self.listad1_1.append(x)
            self.emaildoador = self.listad1_1[0]
            self.listad1_1 = []
            if self.emaildoador == self.emailescrito:
                self.x = True
            else:
                self.lbl2 = Label(self.jan, text = "E-mail e/ou senha inválidos", font = "Century\ Gothic 14", fg = "#FE4A49", bg = "#131644")
                self.lbl2.place(relx = 0.16, rely = 0.28, relwidth = 0.68, relheight = 0.06)
            
            cursor.execute("SELECT senha FROM doadores WHERE email = '{}'".format(self.emailescrito))
            for i in cursor:
                for x in i:
                    self.listad1_2.append(x)
            self.senhadoador = self.listad1_2[0]
            self.listad1_2 = []
            if self.senhadoador == self.senhaescrita:
                self.x = True
            else:
                self.x = False
                self.lbl2 = Label(self.jan, text = "E-mail e/ou senha inválidos", font = "Century\ Gothic 14", fg = "#FE4A49", bg = "#131644")
                self.lbl2.place(relx = 0.16, rely = 0.29, relwidth = 0.68, relheight = 0.05)
        except Exception as e: 
            print(e)
            self.x = False
            self.lbl2 = Label(self.jan, text = "E-mail e/ou senha inválidos", font = "Century\ Gothic 14", fg = "#FE4A49", bg = "#131644")
            self.lbl2.place(relx = 0.16, rely = 0.29, relwidth = 0.68, relheight = 0.05)
        
        if self.x == True:
            global email 
            email = self.emailescrito
            self.teladoador7()
        
    def teladoador2(self):
        self.img1 = PhotoImage(file = os.path.abspath("doador2.png"))
        self.img2 = PhotoImage(file = os.path.abspath("btnSetaR.PNG"))
        self.img3 = PhotoImage(file = os.path.abspath("btnSetinha.PNG"))
    
 
        self.lbl1 = Label(self.jan, image = self.img1)
        self.lbl1.place(relx = 0, rely = 0, relwidth =1, relheight = 1)

        self.btn1 = Button(self.jan, bg = "#131644",bd = 0, activebackground = "#131644", image = self.img2 ,command = lambda: self.conexãod2())
        self.btn1.place(relx = 0.29, rely = 0.65, relwidth = 0.42, relheight = 0.14)
        
        self.btn2 = Button(self.jan, bg = "#131644",bd = 0, activebackground = "#131644", image = self.img3 ,command = lambda: self.teladoador1())
        self.btn2.place(relx = 0.03, rely = 0.06, relwidth = 0.15, relheight = 0.06)
    

        global entrada1
        entrada1 = StringVar()
        self.ent1 = Entry(self.jan, bg = "#131644", font = "Century\ Gothic 14",fg = "white",bd = 0, textvariable = entrada1,insertbackground='white')
        self.ent1.place(relx = 0.155, rely = 0.545, relwidth = 0.69, relheight = 0.055)
        entrada1.set("Digite seu e-mail")
        
        self.ent1.bind("<1>",self.limpard21)
        self.lbl1.bind("<1>",self.voltatextod2)
            
    def limpard21(self,evento=None):
        self.limpar(entrada1, "Digite seu e-mail")
    
    def voltatextod2(self,vento=None):
        x = entrada1.get()
        if x == "":
            entrada1.set("Digite seu e-mail")
    
    def createcodigo(self):
        possibilidades = string.ascii_uppercase + string.digits
        global result_str
        result_str = ''.join(random.choice(possibilidades) for i in range(6))
        print(result_str)
            
    def conexãod2(self):
        self.emailescrito = entrada1.get()
        try:
            cursor.execute("SELECT email FROM doadores WHERE email = '{}'".format(self.emailescrito))
            for i in cursor:
                for x in i:
                    self.listad2_1.append(x)
            self.emaildoador = self.listad2_1[0]
            self.listad2_1 = []
            if self.emaildoador == self.emailescrito:
                self.x = True
            else:
                self.lbl2 = Label(self.jan, text = "E-mail inválido", font = "Century\ Gothic 14", fg = "#FE4A49", bg = "#131644")
                self.lbl2.place(relx = 0.13, rely = 0.6, relwidth = 0.4, relheight = 0.06)
                self.x = False
        except Exception as e: 
            print(e)
            self.lbl2 = Label(self.jan, text = "E-mail inválido", font = "Century\ Gothic 14", fg = "#FE4A49", bg = "#131644")
            self.lbl2.place(relx = 0.13, rely = 0.61, relwidth = 0.4, relheight = 0.05)
            self.x = False
        
        if self.x == True:
            self.teladoador3()
        
            
    def teladoador3(self):
        self.createcodigo()
        
        self.img1 = PhotoImage(file = os.path.abspath("doador3.png"))
        self.img2 = PhotoImage(file = os.path.abspath("btnVerificar.PNG"))
        self.img3 = PhotoImage(file = os.path.abspath("btnSetinha.PNG"))

        self.lbl1 = Label(self.jan, image = self.img1)
        self.lbl1.place(relx = 0, rely = 0, relwidth =1, relheight = 1)
    

        self.btn1 = Button(self.jan, bg = "#131644",bd = 0, activebackground = "#131644", image = self.img2 ,command = lambda: self.conexãod3())
        self.btn1.place(relx = 0.29, rely = 0.55, relwidth = 0.42, relheight = 0.14)
        
        self.btn2 = Button(self.jan, bg = "#131644",bd = 0, activebackground = "#131644", image = self.img3 ,command = lambda: self.teladoador2())
        self.btn2.place(relx = 0.03, rely = 0.06, relwidth = 0.15, relheight = 0.06)
    

        global entrada1
        entrada1 = StringVar()
        self.ent1 = Entry(self.jan, bg = "#131644", font = "Century\ Gothic 14",fg = "white",bd = 0, textvariable = entrada1,insertbackground='white')
        self.ent1.place(relx = 0.155, rely = 0.46, relwidth = 0.69, relheight = 0.055)
        entrada1.set("Insira o código")
        
        self.ent1.bind("<1>",self.limpard31)
        self.lbl1.bind("<1>",self.voltatextod3)

            
    def limpard31(self,evento=None):
        self.limpar(entrada1, "Insira o código")
    
    def voltatextod3(self,vento=None):
        x = entrada1.get()
        if x == "":
            entrada1.set("Insira o código")

    def conexãod3(self):
        self.codigoescrito = entrada1.get()
        if result_str == self.codigoescrito:
            self.teladoador5()
        else:
            self.teladoador4()

    def teladoador4(self):
         
        self.img1 = PhotoImage(file = os.path.abspath("doador4.png"))
        self.img2 = PhotoImage(file = os.path.abspath("btnVerificar.PNG"))
        self.img3 = PhotoImage(file = os.path.abspath("btnReenviar.PNG"))
        self.img4 = PhotoImage(file = os.path.abspath("btnSetinha.PNG"))
    
 
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
        self.lbl1.bind("<1>",self.voltatextod4)
            
    def limpard41(self,evento=None):
        self.limpar(entrada1, "Insira o código")
    
    def voltatextod4(self,vento=None):
        x = entrada1.get()
        if x == "":
            entrada1.set("Insira o código")
    
    def conexãod4(self):
        self.codigoescrito = entrada1.get()
            
    def teladoador5(self):
  
        self.img1 = PhotoImage(file = os.path.abspath("doador5.png"))
        self.img2 = PhotoImage(file = os.path.abspath("btnRedefinir.PNG"))
        self.img3 = PhotoImage(file = os.path.abspath("btnSetinha.PNG"))
    

        self.lbl1 = Label(self.jan, image = self.img1)
        self.lbl1.place(relx = 0, rely = 0, relwidth =1, relheight = 1)
    

        self.btn1 = Button(self.jan, bg = "#131644",bd = 0, activebackground = "#131644", image = self.img2 ,command = lambda: self.conexãod5())
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
        self.lbl1.bind("<1>",self.voltatextod5)
        
    def limpard51(self,evento=None):
        self.limpar(entrada1, "Digite sua nova senha")
    
    def limpard52(self,evento=None):
        self.limpar(entrada2, "Confirme sua nova senha")
        
    def voltatextod5(self,vento=None):
        x = entrada1.get()
        if x == "":
            entrada1.set("Digite sua nova senha")
        y = entrada2.get()
        if y == "":
            entrada2.set("Confirme sua nova senha")
    
    def conexãod5(self):
        self.senhaescritad5 = entrada1.get()
        self.senhaescritad5_2 = entrada2.get()
        cursor.execute("SELECT id FROM doadores WHERE email = '{}'".format(self.emailescrito))
        for i in cursor:
            for x in i:
                self.listad5_1.append(x)
        self.iddoador = self.listad5_1[0]
        if self.senhaescritad5 == self.senhaescritad5_2:
            cursor.execute(f'UPDATE doadores SET senha = "{self.senhaescritad5}" where id = {self.iddoador}')
            conexao.commit()
            self.teladoador1()
        else:
            self.lbl2 = Label(self.jan, text = "Senha digitada incorretamente", font = "Century\ Gothic 12", fg = "#FE4A49", bg = "#131644")
            self.lbl2.place(relx = 0.13, rely = 0.59, relwidth = 0.7, relheight = 0.05)
    
    def teladoador6(self):
        
        self.img1 = PhotoImage(file = os.path.abspath("doador6.png"))
        self.img2 = PhotoImage(file = os.path.abspath("btnCadastrar.PNG"))
        self.img3 = PhotoImage(file = os.path.abspath("btnSetinha.PNG"))

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
        entrada1.set("Digite seu nome completo")
        
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
        self.lbl1.bind("<1>",self.voltatextod6)

    def limpard61(self,evento=None):
        self.limpar(entrada1, "Digite seu nome completo")
        y = entrada2.get()
        if y == "":
            entrada2.set("Digite seu e-mail")
        z = entrada3.get()
        if z == "":
            entrada3.set("Digite sua senha") 
        a = entrada4.get()
        if a == "":
            entrada4.set("Confirme sua senha")
    
    def limpard62(self,evento=None):
        self.limpar(entrada2, "Digite seu e-mail")
        x = entrada1.get()
        if x == "":
            entrada1.set("Digite seu nome completo")
        z = entrada3.get()
        if z == "":
            entrada3.set("Digite sua senha") 
        a = entrada4.get()
        if a == "":
            entrada4.set("Confirme sua senha")
    
    def limpard63(self,evento=None):
        self.limpar(entrada3, "Digite sua senha")
        x = entrada1.get()
        if x == "":
            entrada1.set("Digite seu nome completo") 
        y = entrada2.get()
        if y == "":
            entrada2.set("Digite seu e-mail")
        a = entrada4.get()
        if a == "":
            entrada4.set("Confirme sua senha")
    
    def limpard64(self,evento=None):
        self.limpar(entrada4, "Confirme sua senha")
        x = entrada1.get()
        if x == "":
            entrada1.set("Digite seu nome completo") 
        y = entrada2.get()
        if y == "":
            entrada2.set("Digite seu e-mail")
        z = entrada3.get()
        if z == "":
            entrada3.set("Digite sua senha") 
        a = entrada4.get()
    
    def voltatextod6(self,vento=None):
        x = entrada1.get()
        if x == "":
            entrada1.set("Digite seu nome completo") 
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
        self.y = False
        self.z = False
        
        try:
            if(re.fullmatch(regex, self.emailescrito)):
                if self.lbl6T == True:
                    self.lbld66.destroy()
                    self.lbl6T = False
                cursor.execute("SELECT email FROM doadores WHERE email = '{}'".format(self.emailescrito))
                for i in cursor:
                    for x in i:
                        self.listad6_1.append(x)
                self.emaildoador = self.listad6_1[0]
                self.listad6_1 = []
                if self.emaildoador == self.emailescrito:
                    if self.lbl2T == False:
                        self.lbld62 = Label(self.jan, text = "E-mail já utilizado!", font = "Century\ Gothic 12", fg = "#FE4A49", bg = "#131644")
                        self.lbld62.place(relx = 0.1, rely = 0.5, relwidth = 0.5, relheight = 0.05)
                        self.lbl2T = True
                    else:
                        self.lbl2T = True
                else:
                    self.x = True
                    if self.lbl2T == True:
                        self.lbld62.destroy()
            else:
                if self.lbl6T == False:
                    self.lbld66 = Label(self.jan, text = "E-mail inválido!", font = "Century\ Gothic 12", fg = "#FE4A49", bg = "#131644")
                    self.lbld66.place(relx = 0.11, rely = 0.5, relwidth = 0.4, relheight = 0.05)
                    self.lbl6T = True
        
        except Exception as e:
            print(e)
            self.x = True
            print(self.lbl6T)
            if self.lbl2T == True:
                self.lbld62.destroy()
                self.lbl2T = False
            if self.lbl6T == True:
                self.lbld66.destroy()
                self.lbl6T = False
    
        if self.senhaescrita == "" or self.senhaescrita2 == "" or self.senhaescrita == "Digite sua senha" or self.senhaescrita2 == "Confirme sua senha":
            if self.lbl4T == False:
                if self.lbl3T == True:
                    self.lbl3.destroy()
                    self.lbl3T = False
                self.lbl4 = Label(self.jan, text = "Digite a senha!", font = "Century\ Gothic 12", fg = "#FE4A49", bg = "#131644")
                self.lbl4.place(relx = 0.1, rely = 0.76, relwidth = 0.4, relheight = 0.05)
                self.lbl4T = True
        else:
            if self.senhaescrita == self.senhaescrita2:
                self.y = True
                if self.lbl3T == True:
                    self.lbl3.destroy()
                    self.lbl3T = False
                if self.lbl4T == True:
                    self.lbl4.destroy()
                    self.lbl4T = False
        
            else:
                if self.lbl3T == False:
                    if self.lbl4T == True:
                        self.lbl4.destroy()
                        self.lbl4T = False
                    self.lbl3 = Label(self.jan, text = "Senha digitada incorretamente!", font = "Century\ Gothic 12", fg = "#FE4A49", bg = "#131644")
                    self.lbl3.place(relx = 0.14, rely = 0.76, relwidth = 0.7, relheight = 0.05)
                    self.lbl3T = True
        
        if self.nomescrito == "" or self.nomescrito == "Digite seu nome completo":
            self.lbl5 = Label(self.jan, text = "Digite o nome!", font = "Century\ Gothic 12", fg = "#FE4A49", bg = "#131644")
            self.lbl5.place(relx = 0.1, rely = 0.37, relwidth = 0.4, relheight = 0.05)
            self.lbl5T = True
        else:
            self.z = True
            if self.lbl5T == True:
                self.lbl5.destroy()

        if self.x == True and self.y == True and self.z == True:
            cursor.execute("insert into doadores (nome,email,senha) values (%s,%s,%s);",(self.nomescrito,self.emailescrito, self.senhaescrita))
            conexao.commit()
            self.teladoador1()
    
    def teladoador7(self):  
        cursor.execute("SELECT nome FROM doadores WHERE email = '{}'".format(email))
        for i in cursor:
            for x in i:
                self.listad6_1.append(x)
            global nomedoador 
            nomedoador= self.listad6_1[0]
            self.listad6_1 = []
        
        self.img1 = PhotoImage(file = os.path.abspath("doador7.png"))
        self.img2 = PhotoImage(file = os.path.abspath("btnPerfil.PNG"))
        self.img3 = PhotoImage(file = os.path.abspath("btnChat.PNG"))
        self.img4 = PhotoImage(file = os.path.abspath("btnLupa.PNG"))
        self.img5 = PhotoImage(file = os.path.abspath("btnPerfilmaior.PNG"))
    

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
        self.img1 = PhotoImage(file = os.path.abspath("doador8.png"))
        self.img2 = PhotoImage(file = os.path.abspath("btnPerfilgg.PNG"))
        self.img3 = PhotoImage(file = os.path.abspath("btnSetinha.PNG"))
        self.img4 = PhotoImage(file = os.path.abspath("btnChat.PNG"))
        self.img5 = PhotoImage(file = os.path.abspath("btnDinheiro.PNG"))
    

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
        self.img1 = PhotoImage(file = os.path.abspath("Inst10.png"))
        self.img2 = PhotoImage(file = os.path.abspath("btnPerfilmaior.PNG"))
        self.img3 = PhotoImage(file = os.path.abspath("btnSetinha.PNG"))
    
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
        global nd
        nd = 1
        print(nd)
        self.img1 = PhotoImage(file = os.path.abspath("doador10.png"))
        self.img2 = PhotoImage(file = os.path.abspath("btnPerfilgg.PNG"))
        self.img3 = PhotoImage(file = os.path.abspath("btnSetinha.PNG"))
        self.img4 = PhotoImage(file = os.path.abspath("btnAddcartao.PNG"))

        self.lbl1 = Label(self.jan, image = self.img1)
        self.lbl1.place(relx = 0, rely = 0, relwidth =1, relheight = 1)
        
        self.lbl2 = Label(self.jan, bg = "#BDAB9F", fg = "black", text = nomedoador, font = " Century\ Gothic 14")
        self.lbl2.place(relx = 0.31, rely = 0.165, relwidth =0.62, relheight = 0.04)
        
        self.listb1 = Listbox(self.jan, bg = "#131644",fg = "white", font = "Century\ Gothic 14", bd = 0, selectbackground = "#FEAD77", highlightbackground = "#FEAD77")
        self.listb1.place(relx = 0.09, rely = 0.63, relwidth = 0.8, relheight = 0.23)
        
        
        self.btn1 = Button(self.jan, bg = "#131644",bd = 0, activebackground = "#131644", image = self.img2 ,command = lambda: self.teste())
        self.btn1.place(relx = 0.05, rely = 0.123, relwidth = 0.22, relheight = 0.14)
        
        self.btn2 = Button(self.jan, bg = "#131644",bd = 0, activebackground = "#131644", image = self.img3 ,command = lambda: self.teladoador7())
        self.btn2.place(relx = 0.055, rely = 0.025, relwidth = 0.15, relheight = 0.06)
        
        self.btn3 = Button(self.jan, bg = "#131644",bd = 0, activebackground = "#131644", image = self.img4 ,command = lambda: self.teladoador11())
        self.btn3.place(relx = 0.13, rely = 0.86, relwidth = 0.72, relheight = 0.15)
    
        self.conexaod10()
        
    def conexaod10(self):
        try:
            cursor.execute("SELECT id FROM doadores WHERE email = '{}'".format(email))
            for i in cursor:
                for x in i:
                    self.listad6_1.append(x)
                self.iddoador = self.listad6_1[0]
                self.listad6_1 = []
            
            cursor.execute("SELECT numcard FROM cartoes WHERE iduser = '{}'".format(self.iddoador))
            for i in cursor:
                for x in i:
                    self.listad6_1.append(x)
            print(self.listad6_1)
            for i in self.listad6_1:
                i = i.split("-")
                z = "XXXX-XXXX-XXXX-" + i[len(i) - 1]
                self.listb1.insert(END, z)
            self.listad6_1 = []
        except Exception as e:
            print(e)

    def teladoador11(self):  
        
        
        self.img1 = PhotoImage(file = os.path.abspath("doador11.png"))
        self.img2 = PhotoImage(file = os.path.abspath("btnCadastrar.PNG"))
        self.img3 = PhotoImage(file = os.path.abspath("btnSetinha.PNG"))
    

        self.lbl1 = Label(self.jan, image = self.img1)
        self.lbl1.place(relx = 0, rely = 0, relwidth =1, relheight = 1)
    

        self.btn1 = Button(self.jan, bg = "#131644",bd = 0, activebackground = "#131644", image = self.img2 ,command = lambda: self.conexaod11())
        self.btn1.place(relx = 0.29, rely = 0.85, relwidth = 0.42, relheight = 0.15)
        
        self.btn2 = Button(self.jan, bg = "#131644",bd = 0, activebackground = "#131644", image = self.img3 ,command = lambda: self.escolhatl())
        self.btn2.place(relx = 0.055, rely = 0.025, relwidth = 0.15, relheight = 0.06)
        

        global entrada1
        entrada1 = StringVar()
        self.ent1 = Entry(self.jan, bg = "#131644", font = "Century\ Gothic 14",fg = "white",bd = 0, textvariable = entrada1,insertbackground='white')
        self.ent1.place(relx = 0.155, rely = 0.2, relwidth = 0.69, relheight = 0.055)
        entrada1.set("Nome do cartão")
        
        global entrada2
        entrada2 = StringVar()
        self.ent2 = Entry(self.jan, bg = "#131644", font = "Century\ Gothic 14",fg = "white",bd = 0, textvariable = entrada2,insertbackground='white')
        self.ent2.place(relx = 0.155, rely = 0.317, relwidth = 0.68, relheight = 0.055)
        entrada2.set("CPF")
        
        global entrada3
        entrada3 = StringVar()
        self.ent3 = Entry(self.jan, bg = "#131644", font = "Century\ Gothic 14",fg = "white",bd = 0, textvariable = entrada3,insertbackground='white')
        self.ent3.place(relx = 0.155, rely = 0.43, relwidth = 0.68, relheight = 0.055)
        entrada3.set("Número do cartão")
        
        global entrada4
        entrada4 = StringVar()
        self.ent4 = Entry(self.jan, bg = "#131644", font = "Century\ Gothic 14",fg = "white",bd = 0, textvariable = entrada4,insertbackground='white')
        self.ent4.place(relx = 0.155, rely = 0.545, relwidth = 0.68, relheight = 0.055)
        entrada4.set("CVC")
        
        global entrada5
        entrada5 = StringVar()
        self.ent5 = Entry(self.jan, bg = "#131644", font = "Century\ Gothic 14",fg = "white",bd = 0, textvariable = entrada5,insertbackground='white')
        self.ent5.place(relx = 0.155, rely = 0.66, relwidth = 0.68, relheight = 0.055)
        entrada5.set("Vencimento")
        
        global entrada6
        entrada6 = StringVar()
        self.ent6 = Entry(self.jan, bg = "#131644", font = "Century\ Gothic 14",fg = "white",bd = 0, textvariable = entrada6,insertbackground='white')
        self.ent6.place(relx = 0.155, rely = 0.778, relwidth = 0.68, relheight = 0.055)
        entrada6.set("Bandeira")

        self.ent1.bind("<1>",self.limpard111)
        self.ent1.bind("<KeyRelease>",self.maiusculo)
        self.ent2.bind("<1>",self.limpard112)
        self.ent3.bind("<1>",self.limpard113)
        self.ent3.bind("<KeyRelease>",self.arrumar)
        self.ent4.bind("<1>",self.limpard114)
        self.ent4.bind("<KeyRelease>",self.arrumar2)
        self.ent5.bind("<1>",self.limpard115)
        self.ent5.bind("<KeyRelease>",self.arrumar3)
        self.ent6.bind("<1>",self.limpard116)
        self.lbl1.bind("<1>",self.voltatextod11)
    
    def limpard111(self,evento=None):
        self.limpar(entrada1, "Nome do cartão")
    
    def limpard112(self,evento=None):
        self.limpar(entrada2, "CPF")
            
    def limpard113(self,evento=None):
        self.limpar(entrada3, "Número do cartão")
    
    def limpard114(self,evento=None):
        self.limpar(entrada4, "CVC")
        
    def limpard115(self,evento=None):
        self.limpar(entrada5, "Vencimento")
    
    def limpard116(self,evento=None):
        self.limpar(entrada6, "Bandeira")
            
    
    def voltatextod11(self,evento=None):
        x = entrada1.get()
        if x == "":
            entrada1.set("Nome do cartão") 
        y = entrada2.get()
        if y == "":
            entrada2.set("CPF")
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
        
    def escolhatl(self):
        if nd == 1:
            self.teladoador10()
        if nd == 2:
            self.teladoador16()
            
    def arrumar(self,evento=None):
        self.numcard = entrada3.get()
        if len(self.numcard) < 20:
            print(len(self.numcard))
            if len(self.numcard)==4:
                self.numcard = self.numcard + '-' 
                entrada3.set(self.numcard)
                self.ent3.icursor(END)
            if len(self.numcard)==9:
                self.numcard = self.numcard + '-' 
                entrada3.set(self.numcard)
                self.ent3.icursor(END)
            if len(self.numcard)==14:
                self.numcard = self.numcard + '-'
                entrada3.set(self.numcard)
                self.ent3.icursor(END)
        else:
            entrada3.set(self.numcard[:len(self.numcard) -1])
    def arrumar2(self,evento=None):
        self.cvccard = entrada4.get()
        if len(self.cvccard) < 4:
            entrada4.set(self.cvccard)
        else:
            entrada4.set(self.cvccard[:len(self.cvccard) -1])
    
    def arrumar3(self,evento=None):
        self.vencimentocard = entrada5.get()
        if len(self.vencimentocard) < 6:
            if len(self.vencimentocard)==2:
                self.vencimentocard = self.vencimentocard + '/'
                entrada5.set(self.vencimentocard)
                self.ent5.icursor(END)
        else:
            entrada5.set(self.vencimentocard[:len(self.vencimentocard) -1])

    def conexaod11(self):
        self.nomescrito = entrada1.get()
        self.cpfescrito = entrada2.get()
        self.numcard = entrada3.get()
        self.cvccard = entrada4.get()
        self.vencimentocard = entrada5.get()
        self.bandeiracard = entrada6.get()
        
        self.x1 = False 
        self.x2 = False
        self.x3 = False
        self.x4 = False
        self.x5 = False
        self.x6 = False
        
        if self.nomescrito == "" or self.nomescrito == "Nome do cartão":
            if self.lblc1T == False:
                self.lblc1 = Label(self.jan, text = "Digite o nome!", font = "Century\ Gothic 12", fg = "#FE4A49", bg = "#131644")
                self.lblc1.place(relx = 0.1, rely = 0.26, relwidth = 0.4, relheight = 0.04)
                self.lblc1T = True
        else:
            self.x1 = True
            if self.lblc1T == True:
                self.lblc1.destroy()
                self.lblc1T = False
        
        if self.cpfescrito == "" or self.cpfescrito == "CPF":
            if self.lblc2T == False:
                self.lblc2 = Label(self.jan, text = "Digite o CPF!", font = "Century\ Gothic 12", fg = "#FE4A49", bg = "#131644")
                self.lblc2.place(relx = 0.08, rely = 0.38, relwidth = 0.4, relheight = 0.04)
                self.lblc2T = True
        else:
            try:
                y = self.validarcpf(self.cpfescrito)
                if y == self.cpfescrito: 
                    self.x2 = True
                    if self.lblc2T == True:
                        self.lblc2.destroy()
                        self.lblc2T = False
                    if self.lblc7T == True:
                        self.lblc7.destroy()
                        self.lblc7T = False
                else:
                    if self.lblc2T == True:
                        self.lblc2t.destroy()
                        self.lblc2T = False
                    if self.lblc7T == False:
                        self.lblc7 = Label(self.jan, text = "CPF inválido!", font = "Century\ Gothic 12", fg = "#FE4A49", bg = "#131644")
                        self.lblc7.place(relx = 0.08, rely = 0.38, relwidth = 0.4, relheight = 0.04)
                        self.lblc7T = True
            except Exception as e:
                print(e)
                
        if self.numcard == "" or self.numcard == "Número do cartão":
            if self.lblc3T == False:
                self.lblc3 = Label(self.jan, text = "Digite o número!", font = "Century\ Gothic 12", fg = "#FE4A49", bg = "#131644")
                self.lblc3.place(relx = 0.11, rely = 0.495, relwidth = 0.4, relheight = 0.04)
                self.lblc3T = True
        else:
            print(len(self.numcard))
            if len(self.numcard) == 19:
                for i in self.numcard:
                    if i.isnumeric():
                        self.x3 = True
                        if self.lblc3T == True:
                            self.lblc3.destroy()
                            self.lblc3T = False
                        if self.lblc8T == True:
                            self.lblc8.destroy()
                            self.lblc8T = False
                    else:
                        if self.lblc3T == True:
                            self.lblc3.destroy()
                            self.lblc3T = False
                        if self.lblc8T == True:
                            self.lblc8.destroy()
                            self.lblc8T = False
                        
                        if self.lblc8T == False:
                            self.lblc8 = Label(self.jan, text = "Número inválido!", font = "Century\ Gothic 12", fg = "#FE4A49", bg = "#131644")
                            self.lblc8.place(relx = 0.11, rely = 0.495, relwidth = 0.4, relheight = 0.04)
                            self.lblc8T = True
            else:
                if self.lblc3T == True:
                    self.lblc3.destroy()
                    self.lblc3T = False
                if self.lblc8T == True:
                    self.lblc8.destroy()
                    self.lblc8T = False
                
                if self.lblc8T == False:
                    self.lblc8 = Label(self.jan, text = "Número inválido!", font = "Century\ Gothic 12", fg = "#FE4A49", bg = "#131644")
                    self.lblc8.place(relx = 0.11, rely = 0.495, relwidth = 0.4, relheight = 0.04)
                    self.lblc8T = True
                        

        if self.cvccard == "" or self.cvccard == "CVC":
            if self.lblc4T == False:
                self.lblc4 = Label(self.jan, text = "Digite o CVC!", font = "Century\ Gothic 12", fg = "#FE4A49", bg = "#131644")
                self.lblc4.place(relx = 0.09, rely = 0.61, relwidth = 0.4, relheight = 0.04)
                self.lblc4T = True
        else:
            if len(self.cvccard) == 3:
                for i in self.cvccard:
                    if i.isnumeric():
                        self.x4 = True
                        if self.lblc4T == True:
                            self.lblc4.destroy()
                            self.lblc4T = False
                        if self.lblc9T == True:
                            self.lblc9.destroy()
                            self.lblc9T = False
                    else:
                        if self.lblc4T == True:
                            self.lblc4.destroy()
                            self.lblc4T = False
                        if self.lblc9T == True:
                            self.lblc9.destroy()
                            self.lblc9T = False
                        
                        if self.lblc9T == False:
                            self.lblc9 = Label(self.jan, text = "CVC inválido!", font = "Century\ Gothic 12", fg = "#FE4A49", bg = "#131644")
                            self.lblc9.place(relx = 0.11, rely = 0.61, relwidth = 0.4, relheight = 0.04)
                            self.lblc9T = True
            else:
                if self.lblc4T == True:
                    self.lblc4.destroy()
                    self.lblc4T = False
                if self.lblc9T == True:
                    self.lblc9.destroy()
                    self.lblc9T = False
                
                if self.lblc9T == False:
                    self.lblc9 = Label(self.jan, text = "CVC inválido!", font = "Century\ Gothic 12", fg = "#FE4A49", bg = "#131644")
                    self.lblc9.place(relx = 0.11, rely = 0.61, relwidth = 0.4, relheight = 0.04)
                    self.lblc9T = True
        
        if self.vencimentocard == "" or self.vencimentocard == "Vencimento":
            if self.lblc5T == False:
                self.lblc5 = Label(self.jan, text = "Digite o vencimento!", font = "Century\ Gothic 12", fg = "#FE4A49", bg = "#131644")
                self.lblc5.place(relx = 0.1, rely = 0.72, relwidth = 0.5, relheight = 0.04)
                self.lblc5T = True
        else:
            if len(self.vencimentocard) == 5:
                for i in self.vencimentocard:
                    if i.isnumeric():
                        self.venc1 = self.vencimentocard[:len(self.vencimentocard) -3]
                        for i in range(1,13):
                            self.lm = ["01","02","03","04","05","06","07","08","09","10","11","12"]
                            if self.venc1 == self.lm[i-1]:
                                self.x5 = True
                                if self.lblc5T == True:
                                    self.lblc5.destroy()
                                    self.lblc5T = False
                                if self.lblc10T == True:
                                    self.lblc10.destroy()
                                    self.lblc10T = False
                                break
                                break
                    else:
                        if self.lblc5T == True:
                            self.lblc5.destroy()
                            self.lblc5T = False
                        if self.lblc10T == True:
                            self.lblc10.destroy()
                            self.lblc10T = False
                        
                        if self.lblc10T == False:
                            self.lblc10 = Label(self.jan, text = "Validade inválido!", font = "Century\ Gothic 12", fg = "#FE4A49", bg = "#131644")
                            self.lblc10.place(relx = 0.11, rely = 0.72, relwidth = 0.4, relheight = 0.04)
                        self.lblc10T = True
            else:
                if self.lblc5T == True:
                    self.lblc5.destroy()
                    self.lblc5T = False
                if self.lblc10T == True:
                    self.lblc10.destroy()
                    self.lblc10T = False
                
                if self.lblc10T == False:
                    self.lblc10 = Label(self.jan, text = "Validade inválido!", font = "Century\ Gothic 12", fg = "#FE4A49", bg = "#131644")
                    self.lblc10.place(relx = 0.11, rely = 0.61, relwidth = 0.4, relheight = 0.04)
                    self.lblc10T = True

        if self.bandeiracard == "" or self.bandeiracard == "Bandeira":
            if self.lblc6T == False:
                self.lblc6 = Label(self.jan, text = "Digite a bandeira!", font = "Century\ Gothic 12", fg = "#FE4A49", bg = "#131644")
                self.lblc6.place(relx = 0.12, rely = 0.84, relwidth = 0.4, relheight = 0.04)
                self.lblc6T = True
        else:
            self.x6 = True
            if self.lblc6T == True:
                self.lblc6.destroy()
                self.lblc6T = False
        
        if self.x1 == True and self.x2 == True and self.x3 == True and self.x4 == True and self.x5 == True and self.x6 == True:
            cursor.execute("SELECT id FROM doadores WHERE email = '{}'".format(email))
            for i in cursor:
                for x in i:
                    self.listad6_1.append(x)
                self.iddoador = self.listad6_1[0]
                self.listad6_1 = []
            
            cursor.execute(f"insert into cartoes (nomeuser,cpfuser,numcard,cvccard,vencicard,bandeiracard,iduser) values (%s,%s,%s,%s,%s,%s,%s);",(self.nomescrito,self.cpfescrito, self.numcard, self.cvccard, self.vencimentocard,self.bandeiracard,self.iddoador))
            conexao.commit()
            if nd == 1:
                self.teladoador10()
            if nd == 2:
                self.teladoador16()
        
    def teladoador12(self):  
        self.img1 = PhotoImage(file = os.path.abspath("doador12.png"))
        self.img2 = PhotoImage(file = os.path.abspath("btnLupinha.PNG"))
        self.img3 = PhotoImage(file = os.path.abspath("btnSetinha.PNG"))

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
        self.lbl1.bind("<1>",self.voltatextod121)

        self.listb1 = Listbox(self.jan, bg = "#131644",fg = "white", font = "Century\ Gothic 14", bd = 0, selectbackground = "#FEAD77")
        self.listb1.place(relx = 0.01, rely = 0.23, relwidth = 0.98, relheight = 0.41)
        
    def pesquisa(self):
        self.listb1.insert(END, "Nome do instituto")
        self.listb1.insert(END, "Nome do instituto")
        self.listb1.insert(END, "Nome do instituto")
        

    def limpard121(self,evento=None):
        self.limpar(entrada1, "Digite aqui...")
    
    def voltatextod121(self,vento=None):
        x = entrada1.get()
        if x == "":
            entrada1.set("Digite aqui...")
    
    def teladoador13(self): 
        self.img1 = PhotoImage(file = os.path.abspath("doador13.png"))
        self.img2 = PhotoImage(file = os.path.abspath("btnPerfilmaior.PNG"))
        self.img3 = PhotoImage(file = os.path.abspath("btnSetinha.PNG"))
    
    
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
        self.lbl1.bind("<1>",self.voltatextod131)
            
    def limpard131(self,evento=None):
        self.limpar(entrada1, "Digite aqui...")
    
    def voltatextod131(self,vento=None):
        x = entrada1.get()
        if x == "":
            entrada1.set("Digite aqui...")
    
    def teladoador14(self): 
        self.img1 = PhotoImage(file = os.path.abspath("doador14.png"))
        self.img2 = PhotoImage(file = os.path.abspath("btnXapagar.PNG"))
        self.img3 = PhotoImage(file = os.path.abspath("btnCerto.PNG"))
        self.img4 = PhotoImage(file = os.path.abspath("btnSetinha.PNG"))
        self.imgbt1 = PhotoImage(file = os.path.abspath("btnum1.PNG"))
        self.imgbt2 = PhotoImage(file = os.path.abspath("btnum2.PNG"))
        self.imgbt3 = PhotoImage(file = os.path.abspath("btnum3.PNG"))
        self.imgbt4 = PhotoImage(file = os.path.abspath("btnum4.PNG"))
        self.imgbt5 = PhotoImage(file = os.path.abspath("btnum5.PNG"))
        self.imgbt6 = PhotoImage(file = os.path.abspath("btnum6.PNG"))
        self.imgbt7 = PhotoImage(file = os.path.abspath("btnum7.PNG"))
        self.imgbt8 = PhotoImage(file = os.path.abspath("btnum8.PNG"))
        self.imgbt9 = PhotoImage(file = os.path.abspath("btnum9.PNG"))
        self.imgbt0 = PhotoImage(file = os.path.abspath("btnum0.PNG"))
    

        self.lbl1 = Label(self.jan, image = self.img1)
        self.lbl1.place(relx = 0, rely = 0, relwidth =1, relheight = 1)
    

        self.btn1 = Button(self.jan, bg = "#131644",bd = 0, activebackground = "#131644", image = self.img2 ,command = lambda: self.apagar())
        self.btn1.place(relx = 0.1, rely = 0.81, relwidth = 0.2, relheight = 0.12)
        self.btn2 = Button(self.jan, bg = "#131644",bd = 0, activebackground = "#131644", image = self.img3 ,command = lambda: self.teladoador15())
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
    
    def teladoador15(self):       
        self.img1 = PhotoImage(file = os.path.abspath("Doador15.png"))
        self.img2 = PhotoImage(file = os.path.abspath("btnCartao.PNG"))
        self.img3 = PhotoImage(file = os.path.abspath("btnBoleto.PNG"))
        self.img4 = PhotoImage(file = os.path.abspath("btnPix.PNG"))
        self.img5 = PhotoImage(file = os.path.abspath("btnSetinha.PNG"))
        
        self.lbl1 = Label(self.jan, image = self.img1)
        self.lbl1.place(relx = 0, rely = 0, relwidth =1, relheight = 1)
    
        
        self.btn1 = Button(self.jan, bg = "#131644",bd = 0, activebackground = "#131644", image = self.img2 ,command = lambda: self.teladoador16())
        self.btn1.place(relx = 0.298, rely = 0.26, relwidth = 0.4, relheight = 0.2)
        
        self.btn2 = Button(self.jan, bg = "#131644",bd = 0, activebackground = "#131644", image = self.img3 ,command = lambda: self.teste())
        self.btn2.place(relx = 0.29, rely = 0.48, relwidth = 0.42, relheight = 0.22)
        
        self.btn3 = Button(self.jan, bg = "#131644",bd = 0, activebackground = "#131644", image = self.img4 ,command = lambda: self.teste())
        self.btn3.place(relx = 0.255, rely = 0.71, relwidth = 0.5, relheight = 0.16)
        
        self.btn4 = Button(self.jan, bg = "#131644",bd = 0, activebackground = "#131644", image = self.img5 ,command = lambda: self.teladoador14())
        self.btn4.place(relx = 0.055, rely = 0.025, relwidth = 0.15, relheight = 0.06)
        
    def teladoador16(self):   
        global nd
        nd = 2
        self.img1 = PhotoImage(file = os.path.abspath("Doador16.png"))
        self.img2 = PhotoImage(file = os.path.abspath("btnPagar.PNG"))
        self.img3 = PhotoImage(file = os.path.abspath("btnSetinha.PNG"))
        self.img4 = PhotoImage(file = os.path.abspath("btnAddcartao.PNG"))
    
        self.lbl1 = Label(self.jan, image = self.img1)
        self.lbl1.place(relx = 0, rely = 0, relwidth =1, relheight = 1)
           
        self.listb1 = Listbox(self.jan, bg = "#131644",fg = "white", font = "Century\ Gothic 14", bd = 0, selectbackground = "#FEAD77", highlightbackground = "#FEAD77")
        self.listb1.place(relx = 0.15, rely = 0.21, relwidth = 0.7, relheight = 0.4)
        
        self.btn1 = Button(self.jan, bg = "#131644",bd = 0, activebackground = "#131644", image = self.img2 ,command = lambda: self.teladoador17())
        self.btn1.place(relx = 0.3, rely = 0.78, relwidth = 0.4, relheight = 0.14)
        
        self.btn2 = Button(self.jan, bg = "#131644",bd = 0, activebackground = "#131644", image = self.img3 ,command = lambda: self.teladoador15())
        self.btn2.place(relx = 0.055, rely = 0.025, relwidth = 0.15, relheight = 0.06)
        
        self.btn3 = Button(self.jan, bg = "#131644",bd = 0, activebackground = "#131644", image = self.img4 ,command = lambda: self.teladoador11())
        self.btn3.place(relx = 0.14, rely = 0.64, relwidth = 0.72, relheight = 0.15)
        
        self.conexaod10()
    
    def teladoador17(self):    
        self.img1 = PhotoImage(file = os.path.abspath("Doador17.png"))
    
        self.lbl1 = Label(self.jan, image = self.img1)
        self.lbl1.place(relx = 0, rely = 0, relwidth =1, relheight = 1)
        
        t = Timer(2, self.teladoador8)
        t.start()

Kindly()