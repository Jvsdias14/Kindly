from tkinter import *
from threading import Timer
from tkinter import filedialog

###### from TelaDoador1 import TelaInst1


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

global nt
nt = ""

global nomeinstpost
nomeinstpost = ""

global idinstpost 
idinstpost = []

global msgpost 
msgpost = []

global imgpost 
imgpost = []

global nomeinst
nomeinst = []

global edoador
edoador = False

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
        
    global instituicao
    instituicao = "Nome do instituto"
    def teste(self):
        print("sla")
    
    
    def selecionar(self):
        global nomearq
        nomearq = filedialog.askopenfilename(initialdir ="C:/", title = "Escolher Arquivo")
    
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
    
    def Padrao3(self):
        self.img1 = PhotoImage(file = os.path.abspath("Padrao3.png"))
        self.img2 = PhotoImage(file = os.path.abspath("btnConfirmarB.PNG"))
        self.img3 = PhotoImage(file = os.path.abspath("btnSetaL.PNG"))
    
        self.lbl1 = Label(self.jan, image = self.img1)
        self.lbl1.place(relx = 0, rely = 0, relwidth =1, relheight = 1)
    
        self.btn1 = Button(self.jan, bg = "#131644",bd = 0, activebackground = "#131644", image = self.img2 ,command = lambda: self.Padrao2())
        self.btn1.place(relx = 0.13, rely = 0.42, relwidth = 0.74, relheight = 0.15)
        
        self.btn2 = Button(self.jan, bg = "#131644",bd = 0, activebackground = "#131644", image = self.img3 ,command = lambda: self.escolhatl2())
        self.btn2.place(relx = 0.13, rely = 0.58, relwidth = 0.74, relheight = 0.15)

    def escolhatl2(self):
        if nt == 1:
            self.telainst7()
        if nt == 2:
            self.teladoador10()

    
    def telainst1(self):
        self.img1 = PhotoImage(file = os.path.abspath("Inst1.png"))
        self.img2 = PhotoImage(file = os.path.abspath("btnEntrar.PNG"))
        self.img3 = PhotoImage(file = os.path.abspath("btnSetinha.PNG"))
        self.img4 = PhotoImage(file = os.path.abspath("btnOlho.PNG"))


        self.lbl1 = Label(self.jan, image = self.img1)
        self.lbl1.place(relx = 0, rely = 0, relwidth =1, relheight = 1)


        self.btn1 = Button(self.jan, bg = "#131644",bd = 0, activebackground = "#131644", image = self.img2 ,command = lambda: self.conexãoi1())
        self.btn1.place(relx = 0.29, rely = 0.565, relwidth = 0.42, relheight = 0.15)
        
        self.btn2 = Button(self.jan, bg = "#131644",bd = 0, activebackground = "#131644", image = self.img3 ,command = lambda: self.Padrao2())
        self.btn2.place(relx = 0.03, rely = 0.055, relwidth = 0.15, relheight = 0.06)
        
        self.btn3 = Button(self.jan, text = "Crie agora", font = "Century\ Gothic 18",fg = "#FD824F", bg = "#131644",bd = 0, activebackground = "#131644",command = lambda: self.telainst2e3())
        self.btn3.place(relx = 0.33, rely = 0.84, relwidth = 0.33, relheight = 0.05)
        
        self.btn4 = Button(self.jan, bg = "#131644",bd = 0, activebackground = "#131644", image = self.img4)
        self.btn4.place(relx = 0.88, rely = 0.47, relwidth = 0.08, relheight = 0.06)

        global entrada1
        entrada1 = StringVar()
        self.ent1 = Entry(self.jan, bg = "#131644", font = "Century\ Gothic 14",fg = "white",bd = 0, textvariable = entrada1,insertbackground='white',disabledbackground = "#131644",disabledforeground = "white")
        self.ent1.place(relx = 0.16, rely = 0.368, relwidth = 0.68, relheight = 0.06)
        #entrada1.set("Digite seu e-mail")
        entrada1.set("Pestalozzi@gmail.com")
        
        global entrada2
        entrada2 = StringVar()
        self.ent2 = Entry(self.jan, bg = "#131644", font = "Century\ Gothic 14",fg = "white",bd = 0, textvariable = entrada2,insertbackground='white',disabledbackground = "#131644",disabledforeground = "white")
        self.ent2.place(relx = 0.16, rely = 0.468, relwidth = 0.68, relheight = 0.06)
        #entrada2.set("Digite seu código")
        entrada2.set("VJxxtDAPU9")
        
        self.ent1.bind("<1>",self.limparti1_1)
        self.ent2.bind("<1>",self.limparti1_2)
        self.btn4.bind("<1>",self.mostrari1_1)
        self.btn4.bind("<ButtonRelease-1>",self.mostrari1_2)
        self.lbl1.bind("<1>",self.voltatextoI1)

    def limparti1_1(self,evento=None):
        self.ent1.config(state=NORMAL)
        x = entrada1.get()
        if x == "Digite seu e-mail":
            entrada1.set("")
        else:
            entrada1.set(x) 
        x2 = entrada2.get()
        if x2 == "":
            entrada2.set("Digite seu código")
            self.ent2.config(show="")
        elif x2 == "Digite seu código":
            self.ent2.config(show="")
        else:
            entrada2.set(x2) 
         
    def limparti1_2(self,evento=None):
        self.ent2.config(state=NORMAL)
        self.ent2.config(show="*")
        x = entrada2.get()
        if x == "Digite seu código":
            entrada2.set("")
        else:
            entrada2.set(x) 
        x2 = entrada1.get()
        if x2 == "":
            entrada1.set("Digite seu e-mail")
        else:
            entrada1.set(x2) 

            
    def voltatextoI1(self,vento=None):
        x = entrada1.get()
        if x == "":
            entrada1.set("Digite seu e-mail") 
            self.ent1.config(state=DISABLED)
        y = entrada2.get()
        if y == "":
            entrada2.set("Digite seu código")
            self.ent2.config(state=DISABLED)
            self.ent2.config(show="")
    
    def mostrari1_1(self,event=None):
        z = entrada2.get()
        if z != "Digite seu código":
            self.ent2.config(show="")
    def mostrari1_2(self,event=None):
        z = entrada2.get()
        if z != "Digite seu código":
            self.ent2.config(show="*")
    
    def conexãoi1(self):
        self.emailescrito = entrada1.get()
        self.senhaescrita = entrada2.get()
        self.x = False
        try:
            cursor.execute("SELECT email FROM instituicoes WHERE email = '{}'".format(self.emailescrito))
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
            
            cursor.execute("SELECT codigo FROM instituicoes WHERE email = '{}'".format(self.emailescrito))
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
            print(emailinst)
            try:
                cursor.execute("SELECT id,nome FROM instituicoes WHERE email = '{}'".format(emailinst))
                for i in cursor:
                    for x in i:
                        self.listad6_1.append(x)
                    global idlogado
                    idlogado= self.listad6_1[0]
                    global nomelogado 
                    nomelogado = self.listad6_1[1]
                    self.listad6_1 = []
            except Exception as e:
                print(e)
            self.telainst5(1)
    
    def telainst2e3(self):
        self.img1 = PhotoImage(file = os.path.abspath("Inst2.png"))
        self.img2 = PhotoImage(file = os.path.abspath("btnCadastrar.PNG"))
        self.img3 = PhotoImage(file = os.path.abspath("btnSetinha.PNG"))
        self.img4 = PhotoImage(file = os.path.abspath("btnOlho.PNG"))
    
        
        self.lbl1 = Label(self.jan, image = self.img1)
        self.lbl1.place(relx = 0, rely = 0, relwidth =1, relheight = 1)
    
        
        self.btn1 = Button(self.jan, bg = "#131644",bd = 0, activebackground = "#131644", image = self.img2 ,command = lambda: self.conexãoi2())
        self.btn1.place(relx = 0.29, rely = 0.62, relwidth = 0.42, relheight = 0.15)
        
        self.btn2 = Button(self.jan, bg = "#131644",bd = 0, activebackground = "#131644", image = self.img3 ,command = lambda: self.telainst1())
        self.btn2.place(relx = 0.03, rely = 0.055, relwidth = 0.15, relheight = 0.06)
        
        self.btn3 = Button(self.jan, text = "clique aqui", font = "Century\ Gothic 18",fg = "#FD824F", bg = "#131644",bd = 0, activebackground = "#131644",command = lambda: self.telainst4())
        self.btn3.place(relx = 0.32, rely = 0.9, relwidth = 0.37, relheight = 0.05)
        
        self.btn4 = Button(self.jan, bg = "#131644",bd = 0, activebackground = "#131644", image = self.img4)
        self.btn4.place(relx = 0.88, rely = 0.52, relwidth = 0.08, relheight = 0.06)


        global entrada1
        entrada1 = StringVar()
        self.ent1 = Entry(self.jan, bg = "#131644", font = "Century\ Gothic 14",fg = "white",bd = 0, textvariable = entrada1,insertbackground='white',disabledbackground = "#131644",disabledforeground = "white")
        self.ent1.place(relx = 0.155, rely = 0.28, relwidth = 0.69, relheight = 0.055)
        entrada1.set("Digite o nome da instituição")
        
        global entrada2
        entrada2 = StringVar()
        self.ent2 = Entry(self.jan, bg = "#131644", font = "Century\ Gothic 14",fg = "white",bd = 0, textvariable = entrada2,insertbackground='white',disabledbackground = "#131644",disabledforeground = "white")
        self.ent2.place(relx = 0.155, rely = 0.4, relwidth = 0.68, relheight = 0.055)
        entrada2.set("Digite seu e-mail")
        
        global entrada3
        entrada3 = StringVar()
        self.ent3 = Entry(self.jan, bg = "#131644", font = "Century\ Gothic 14",fg = "white",bd = 0, textvariable = entrada3,insertbackground='white',disabledbackground = "#131644",disabledforeground = "white")
        self.ent3.place(relx = 0.155, rely = 0.522, relwidth = 0.68, relheight = 0.055)
        entrada3.set("Digite seu código")
        
        self.ent1.bind("<1>",self.limparti2_1)
        self.ent2.bind("<1>",self.limparti2_2)
        self.ent3.bind("<1>",self.limparti2_3)
        self.lbl1.bind("<1>",self.voltatextoI2)
        self.btn4.bind("<1>",self.mostrari2_1)
        self.btn4.bind("<ButtonRelease-1>",self.mostrari2_2)

    def limparti2_1(self,evento=None):
        self.ent1.config(state=NORMAL)
        self.ent3.config(show="*")
        x = entrada1.get()
        if x == "Digite o nome da instituição":
            entrada1.set("")
        else:
            entrada1.set(x) 
        x2 = entrada2.get()
        if x2 == "":
            entrada2.set("Digite seu e-mail")
        else:
            entrada2.set(x2) 
        x3 = entrada3.get()
        if x3 == "":
            entrada3.set("Digite seu código")
            self.ent3.config(show="")
        elif x3 == "Digite seu código":
            self.ent3.config(show="")
        else:
            entrada3.set(x3) 
         
    def limparti2_2(self,evento=None):
        self.ent2.config(state=NORMAL)
        self.ent3.config(show="*")
        x = entrada2.get()
        if x == "Digite seu e-mail":
            entrada2.set("")
        else:
            entrada2.set(x) 
        x2 = entrada1.get()
        if x2 == "":
            entrada1.set("Digite o nome da instituição")
        else:
            entrada1.set(x2) 
        x3 = entrada3.get()
        if x3 == "":
            entrada3.set("Digite seu código")
            self.ent3.config(show="")
        elif x3 == "Digite seu código":
            self.ent3.config(show="")
        else:
            entrada3.set(x3) 
    
    def limparti2_3(self,evento=None):
        self.ent3.config(state=NORMAL)
        self.ent3.config(show="*")
        x = entrada3.get()
        if x == "Digite seu código":
            entrada3.set("")
        else:
            entrada3.set(x) 
        x2 = entrada1.get()
        if x2 == "":
            entrada1.set("Digite o nome da instituição")
        else:
            entrada1.set(x2) 
        x3 = entrada2.get()
        if x3 == "":
            entrada2.set("Digite seu e-mail")
        else:
            entrada2.set(x3) 
            
    def voltatextoI2(self,event=None):
        x = entrada1.get()
        if x == "":
            entrada1.set("Digite o nome da instituição") 
            self.ent1.config(state=DISABLED)
        y = entrada2.get()
        if y == "":
            entrada2.set("Digite seu e-mail")
            self.ent2.config(state=DISABLED)
        z = entrada3.get()
        if z == "":
            entrada3.set("Digite seu código")
            self.ent3.config(state=DISABLED)
            self.ent3.config(show="")
    
    def mostrari2_1(self,event=None):
        z = entrada3.get()
        if z != "Digite seu código":
            self.ent3.config(show="")
    def mostrari2_2(self,event=None):
        z = entrada3.get()
        if z != "Digite seu código":
            self.ent3.config(show="*")
    
    
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
                cursor.execute("SELECT email FROM instituicoes WHERE email = '{}'".format(self.emailescrito))
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
                cursor.execute("SELECT codigo FROM instituicoes WHERE codigo = '{}'".format(self.codigoescrito))
                for i in cursor:
                    for x in i:
                        self.listad6_1.append(x)
                self.codigoinst = self.listad6_1[0]
                self.listad6_1 = []
                if self.codigoinst == self.codigoescrito:
                    cursor.execute("SELECT id FROM instituicoes WHERE codigo = '{}'".format(self.codigoescrito))
                    for i in cursor:
                        for x in i:
                            self.listad6_1.append(x)
                    self.idlogado= self.listad6_1[0]
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
                cursor.execute(f"UPDATE instituicoes SET nome = '{self.nomescrito}', email = '{self.emailescrito}' where id = '{self.idinst}'")
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

    def telainst5(self,tipo):
        global nomeinstpost
        global nomeinst
        print(nomeinstpost)
        global idinstpost
        global msgpost
        global imgpost
        
        idinstpost = []
        nomeinst = []
        msgpost = []
        imgpost = []
        
        try:
            sql =  ("select t1.id AS idInst,t1.nome AS nome,t1.email AS email,t2.id AS idPostagem,t2.mensagem AS mensagem,t2.foto AS foto "
                    "from (instituicoes t1 join postagem t2 on(t1.id = t2.idinst)) "
                    "order by idPostagem desc")
            
            cursor.execute(sql)
            for i in cursor.fetchall():
                idinstpost.append(i[0])
                nomeinst.append(i[1])
                msgpost.append(i[4])
                imgpost.append(i[5])

        except Exception as e:
            print(e)
        
        self.img1 = PhotoImage(file = os.path.abspath("Inst5.png"))
        self.img2 = PhotoImage(file = os.path.abspath("btnPerfil.PNG"))
        self.img3 = PhotoImage(file = os.path.abspath("btnChat.PNG"))
        self.img4 = PhotoImage(file = os.path.abspath("btnLupa.PNG"))
        self.img5 = PhotoImage(file = os.path.abspath("btnPerfilmaior.PNG"))
        self.img6 = PhotoImage(file = os.path.abspath("btn+.PNG"))
        self.img7 = PhotoImage(file = imgpost[0])
        self.img8 = PhotoImage(file = imgpost[1])
        #self.img7 = self.img7.subsample(1,1)
    
    
        self.lbl1 = Label(self.jan, image = self.img1)
        self.lbl1.place(relx = 0, rely = 0, relwidth =1, relheight = 1)        

        self.lbl = Label(self.jan, bg = "#131644")
        self.lbl.place(relx = 0, rely = 0.2, relwidth =1, relheight = 0.4)
        
        self.lbl2 = Label(self.jan, bg = "#BDAB9F", fg = "black", text = nomeinst[0], font = " Century\ Gothic 14", anchor ="w")
        self.lbl2.place(relx = 0.18, rely = 0.145, relwidth =0.7, relheight = 0.04)
        
        self.lbl3 = Label(self.jan, bg = "#BDAB9F", fg = "black", text = nomeinst[1], font = " Century\ Gothic 14",anchor ="w")
        self.lbl3.place(relx = 0.18, rely = 0.695, relwidth =0.7, relheight = 0.04)
        
        self.lbl4 = Label(self.jan, bg = "#131644", fg = "white", text = msgpost[0], font = " Century\ Gothic 14", anchor ="w" )
        self.lbl4.place(relx = 0.09, rely = 0.54, relwidth =0.82, relheight = 0.06)
        
        self.lbl5 = Label(self.jan, image = self.img7, borderwidth=2, relief="groove")
        self.lbl5.place(relx = 0.09, rely = 0.23, relwidth =0.82, relheight = 0.3)
        
        self.lbl5 = Label(self.jan, image = self.img8, borderwidth=2, relief="groove")
        self.lbl5.place(relx = 0.09, rely = 0.78, relwidth =0.82, relheight = 0.3)
        

        if tipo == 1:
            self.btn6 = Button(self.jan, bd = 2 ,bg = "#131644", image = self.img6, command = lambda: self.telainst6())
            self.btn6.place(relx = 0.8, rely = 0.85, relwidth = 0.14, relheight = 0.082)
            
            self.btn1 = Button(self.jan, bg = "#131644",bd = 0, activebackground = "#131644", image = self.img2 ,command = lambda: self.telainst7())
            self.btn1.place(relx = 0.035, rely = 0.009, relwidth = 0.12, relheight = 0.08)
        
            self.btn2 = Button(self.jan, bg = "#131644",bd = 0, activebackground = "#131644", image = self.img3 ,command = lambda: self.telainst10())
            self.btn2.place(relx = 0.64, rely = 0.009, relwidth = 0.15, relheight = 0.08)
            
            self.btn3 = Button(self.jan, bg = "#131644",bd = 0, activebackground = "#131644", image = self.img4 ,command = lambda: self.telainst13())
            self.btn3.place(relx = 0.83, rely = 0.009, relwidth = 0.15, relheight = 0.08)
            
            self.btn4 = Button(self.jan, bg = "#131644",bd = 0, activebackground = "#131644", image = self.img5 ,command = lambda: self.telainst9())
            self.btn4.place(relx = 0.02, rely = 0.115, relwidth = 0.17, relheight = 0.09)
            
            self.btn5 = Button(self.jan, bg = "#131644",bd = 0, activebackground = "#131644", image = self.img5 ,command = lambda: self.telainst9())
            self.btn5.place(relx = 0.02, rely = 0.67, relwidth = 0.17, relheight = 0.09)
        
        else:
            self.btn1 = Button(self.jan, bg = "#131644",bd = 0, activebackground = "#131644", image = self.img2 ,command = lambda: self.teladoador10())
            self.btn1.place(relx = 0.035, rely = 0.009, relwidth = 0.12, relheight = 0.08)
        
            self.btn2 = Button(self.jan, bg = "#131644",bd = 0, activebackground = "#131644", image = self.img3 ,command = lambda: self.teladoador9())
            self.btn2.place(relx = 0.64, rely = 0.009, relwidth = 0.15, relheight = 0.08)
            
            self.btn3 = Button(self.jan, bg = "#131644",bd = 0, activebackground = "#131644", image = self.img4 ,command = lambda: self.telainst13())
            self.btn3.place(relx = 0.83, rely = 0.009, relwidth = 0.15, relheight = 0.08)
            
            self.btn4 = Button(self.jan, bg = "#131644",bd = 0, activebackground = "#131644", image = self.img5 ,command = lambda: self.teladoador8())
            self.btn4.place(relx = 0.02, rely = 0.115, relwidth = 0.17, relheight = 0.09)
            
            self.btn5 = Button(self.jan, bg = "#131644",bd = 0, activebackground = "#131644", image = self.img5 ,command = lambda: self.teladoador8())
            self.btn5.place(relx = 0.02, rely = 0.67, relwidth = 0.17, relheight = 0.09)
    

    def telainst6(self):
        self.img1 = PhotoImage(file = os.path.abspath("Inst6.png"))
        self.img2 = PhotoImage(file = os.path.abspath("btnPostar.PNG"))
        self.img3 = PhotoImage(file = os.path.abspath("btnCamera.PNG"))
        self.img4 = PhotoImage(file = os.path.abspath("btnSetinha.PNG"))
    
        self.lbl1 = Label(self.jan, image = self.img1)
        self.lbl1.place(relx = 0, rely = 0, relwidth =1, relheight = 1)
    
    
        self.btn1 = Button(self.jan, bg = "#131644",bd = 0, activebackground = "#131644", image = self.img2 ,command = lambda: self.algo2())
        self.btn1.place(relx = 0.4, rely = 0.33, relwidth = 0.42, relheight = 0.1)
        
        self.btn2 = Button(self.jan, bg = "#131644",bd = 0, activebackground = "#131644", image = self.img3 ,command = lambda: self.selecionar())
        self.btn2.place(relx = 0.14, rely = 0.33, relwidth = 0.2, relheight = 0.1)
        
        self.btn3 = Button(self.jan, bg = "#131644",bd = 0, activebackground = "#131644", image = self.img4 ,command = lambda: self.telainst5(1))
        self.btn3.place(relx = 0.07, rely = 0.03, relwidth = 0.15, relheight = 0.06)
    
    
        global entrada1
        entrada1 = StringVar()
        self.ent1 = Entry(self.jan, bg = "#131644", font = "Century\ Gothic 14",fg = "white",bd = 0, textvariable = entrada1,insertbackground='white')
        self.ent1.place(relx = 0.155, rely = 0.23, relwidth = 0.69, relheight = 0.055)
        entrada1.set("Digite aqui...")
        
        self.ent1.bind("<1>",self.limpari6_1)
        self.lbl1.bind("<1>",self.voltatextoi6_1)
            
    def limpari6_1(self,evento=None):
        self.ent1.config(state=NORMAL)
        x = entrada1.get()
        if x == "Digite aqui...":
            entrada1.set("")
        else:
            entrada1.set(x) 
    
    def voltatextoi6_1(self,vento=None):
        x = entrada1.get()
        if x == "":
            entrada1.set("Digite aqui...") 
            self.ent1.config(state=DISABLED)
    
    def algo2(self,evento=None):       
        x = entrada1.get()
        if x != "":
            cursor.execute(f"insert into postagem (idinst,mensagem,foto) values (%s,%s,%s);",(idinstpost[0],x,nomearq))
            conexao.commit()
        
        self.telainst5(1)
        
    def telainst7(self):
        global nt
        nt = 1
        self.img1 = PhotoImage(file = os.path.abspath("Inst7.png"))
        self.img2 = PhotoImage(file = os.path.abspath("btnPerfilgg.PNG"))
        self.img3 = PhotoImage(file = os.path.abspath("btnDinheiro.PNG"))
        self.img4 = PhotoImage(file = os.path.abspath("btnSetinha.PNG"))
        self.img5 = PhotoImage(file = os.path.abspath("btnCamerabranca.PNG"))
        self.img6 = PhotoImage(file = os.path.abspath("btnLogout.PNG"))
    
    
        self.lbl1 = Label(self.jan, image = self.img1)
        self.lbl1.place(relx = 0, rely = 0, relwidth =1, relheight = 1)
        
        self.lbl2 = Label(self.jan, bg = "#BDAB9F", fg = "black", text = nomelogado, font = " Century\ Gothic 14")
        self.lbl2.place(relx = 0.32, rely = 0.165, relwidth =0.62, relheight = 0.04)
        

        self.btn1 = Button(self.jan, bg = "#131644",bd = 0, activebackground = "#131644", image = self.img2 ,command = lambda: self.teste())
        self.btn1.place(relx = 0.05, rely = 0.123, relwidth = 0.22, relheight = 0.14)
       
        self.btn2 = Button(self.jan, bg = "#131644",bd = 0, activebackground = "#131644", image = self.img3 ,command = lambda: self.telainst8())
        self.btn2.place(relx = 0.63, rely = 0.015, relwidth = 0.15, relheight = 0.08)
        
        self.btn3 = Button(self.jan, bg = "#131644",bd = 0, activebackground = "#131644", image = self.img4 ,command = lambda: self.telainst5(1))
        self.btn3.place(relx = 0.07, rely = 0.03, relwidth = 0.15, relheight = 0.06)
        
        self.btn4 = Button(self.jan, bg = "white",bd = 0, activebackground = "white", image = self.img5 ,command = lambda: self.selecionar())
        self.btn4.place(relx = 0.16, rely = 0.56, relwidth = 0.16, relheight = 0.1)

        self.btn5 = Button(self.jan, bg = "#131644",bd = 0, activebackground = "#131644", image = self.img6 ,command = lambda: self.Padrao3())
        self.btn5.place(relx = 0.8, rely = 0.02, relwidth = 0.15, relheight = 0.08)
        
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
        
        self.lbl2 = Label(self.jan, bg = "#BDAB9F", fg = "black", text = nomeinst[0], font = " Century\ Gothic 14")
        self.lbl2.place(relx = 0.32, rely = 0.165, relwidth =0.62, relheight = 0.04)
        
   
        self.btn1 = Button(self.jan, bg = "#131644",bd = 0, activebackground = "#131644", image = self.img2 ,command = lambda: self.teste())
        self.btn1.place(relx = 0.05, rely = 0.123, relwidth = 0.22, relheight = 0.14)
        
        self.btn2 = Button(self.jan, bg = "#131644",bd = 0, activebackground = "#131644", image = self.img3 ,command = lambda: self.telainst5(1))
        self.btn2.place(relx = 0.07, rely = 0.03, relwidth = 0.15, relheight = 0.06)
    
    def telainst10(self):  
        try:
            global ultimamensagem
            ultimamensagem = []
            global instituicaochat
            instituicaochat = []
        
            global doadorchat
            doadorchat = []
               
            sql = ("SELECT distinct t1.iddoador, t2.nome, t1.mensagem "
                    "FROM chat t1 "
                    "join instituicoes t2 on t1.idinst = t2.id "
            )
             
            if edoador == True:
                sql += "where t1.iddoador = " + str(idlogado)
            else:                    
                sql += "where t1.idinst = " + str(idlogado)
            sql += " and t1.id = (select max(t3.id) from chat t3 where t3.iddoador = t1.iddoador and t3.idinst = t1.idinst)"
            
            cursor.execute(sql)            
            
            for i in cursor.fetchall():
                instituicaochat.append(i[1])
                ultimamensagem.append(i[2])
                doadorchat.append(i[1])
            
            cursor.execute("select * from doadores where id = {}").format(doadorchat([0]))
            for i in cursor:
                for x in i:
                    self.listad6_1.append(x)
                    nomedoador = self.listad6_1[0]
                    
            
        except Exception as e:
            print(e)
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
        
        self.btn3 = Button(self.jan, bg = "#131644",bd = 0, activebackground = "#131644", image = self.img3 ,command = lambda: self.telainst5(1))
        self.btn3.place(relx = 0.07, rely = 0.03, relwidth = 0.15, relheight = 0.06)
        
        
        self.lbl2 = Label(self.jan, bg = "#131644", fg = "white", text = "João Victor Sampaio Dias", font = " Century\ Gothic 14",anchor = "w")
        self.lbl2.place(relx = 0.26, rely = 0.145, relwidth =0.55, relheight = 0.04)
        
        self.lbl3 = Label(self.jan, bg = "#131644", fg = "white", text = ultimamensagem[0], font = " Century\ Gothic 10",anchor= "w")
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
        self.img1 = PhotoImage(file = os.path.abspath("doador13.png"))
        self.img2 = PhotoImage(file = os.path.abspath("btnPerfilmaior.PNG"))
        self.img3 = PhotoImage(file = os.path.abspath("btnSetinha.PNG"))
        self.img4 = PhotoImage(file = os.path.abspath("btnBalao.PNG"))
        self.img5 = PhotoImage(file = os.path.abspath("btnBalao2.PNG"))
    
        self.lbl1 = Label(self.jan, image = self.img1)
        self.lbl1.place(relx = 0, rely = 0, relwidth =1, relheight = 1)
        
        self.lbl1 = Label(self.jan, image = self.img5,bg = "#131644")
        self.lbl1.place(relx = 0.3, rely = 0.12, relwidth =0.64, relheight = 0.2)
        self.lbl1 = Label(self.jan,text ="Bom dia, posso realizar visitas?",font = " Century\ Gothic 14",fg = "black",bg = "white", anchor = "w")
        self.lbl1.place(relx = 0.33, rely = 0.17, relwidth =0.4, relheight = 0.06)
        

        self.btn1 = Button(self.jan,text = "João Victor Sampaio Dias", font = "Century\ Gothic 14",fg = "white", bg = "#131644",bd = 0,anchor = "w",activebackground = "gray",command = lambda: self.teste())
        self.btn1.place(relx = 0.38, rely = 0.01, relwidth = 0.58, relheight = 0.09)
       
        self.btn2 = Button(self.jan, bg = "#131644",bd = 0, activebackground = "#131644", image = self.img2 ,command = lambda: self.telainst9())
        self.btn2.place(relx = 0.21, rely = 0.01, relwidth = 0.17, relheight = 0.1)
        
        self.btn3 = Button(self.jan, bg = "#131644",bd = 0, activebackground = "#131644", image = self.img3 ,command = lambda: self.telainst10())
        self.btn3.place(relx = 0.03, rely = 0.025, relwidth = 0.15, relheight = 0.06)
    
        global entrada1
        entrada1 = StringVar()
        self.ent1 = Entry(self.jan, bg = "#131644", font = "Century\ Gothic 14",fg = "white",bd = 3, textvariable = entrada1,disabledbackground = "#131644",disabledforeground = "white")
        self.ent1.place(relx = 0.01, rely = 0.565, relwidth = 0.98, relheight = 0.08)
        entrada1.set("Digite aqui...")
        
        self.ent1.bind("<1>",self.limpari11_1)
        self.lbl1.bind("<1>",self.voltatextoi11_1)
        self.jan.bind("<Return>",self.salvachat)
            
    def limpari11_1(self,evento=None):
        self.ent1.config(state=NORMAL)
        x = entrada1.get()
        if x == "Digite aqui...":
            entrada1.set("")
        else:
            entrada1.set(x) 
    
    def voltatextoi11_1(self,vento=None):
        x = entrada1.get()
        if x == "":
            entrada1.set("Digite aqui...") 
            self.ent1.config(state=DISABLED)
    
    def salvachat(self,evento=None):
        x = entrada1.get()
        print(x)
        self.lbl1 = Label(self.jan, image = self.img4,bg = "#131644")
        self.lbl1.place(relx = 0.3, rely = 0.12, relwidth =0.64, relheight = 0.2)
        self.lbl1 = Label(self.jan,text = x,font = " Century\ Gothic 14",fg = "black",bg = "#BDAB9F", anchor = "w")
        self.lbl1.place(relx = 0.33, rely = 0.17, relwidth =0.4, relheight = 0.06) 
        entrada1.set("")
    
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
        
        self.btn2 = Button(self.jan, bg = "#131644",bd = 0, activebackground = "#131644", image = self.img3 ,command = lambda: self.telainst5(1))
        self.btn2.place(relx = 0.06, rely = 0.03, relwidth = 0.15, relheight = 0.06)
    

        global entrada1
        entrada1 = StringVar()
        self.ent1 = Entry(self.jan, bg = "#FEAD77", font = "Century\ Gothic 14",fg = "white", textvariable = entrada1, bd = 0,insertbackground='white')
        self.ent1.place(relx = 0.045, rely = 0.14, relwidth = 0.82, relheight = 0.075)
        entrada1.set("Digite aqui...")
        
        self.ent1.bind("<1>",self.limpari13_1)
        self.lbl1.bind("<1>",self.voltatextoi13_1)
 
        self.listb1 = Listbox(self.jan, bg = "#131644",fg = "white", font = "Century\ Gothic 14", bd = 0, selectbackground = "#FEAD77")
        self.listb1.place(relx = 0.01, rely = 0.23, relwidth = 0.98, relheight = 0.41)
        
        self.listb1.bind("<1>",self.conexãoi13)

    
    def conexãoi13(self,evento = None):
        t = Timer(0.1, self.selectela2)
        t.start()
        
    def selectela2(self):
        self.indice = self.listb1.curselection()
        for i in self.indice:
            global instituicao 
            instituicao = self.listb1.get(i)
            if instituicao == nomelogado:
                self.telainst7()
            else:
                self.telainst9()
    
    def limpari13_1(self,evento=None):
        self.ent1.config(state=NORMAL)
        x = entrada1.get()
        if x == "Digite aqui...":
            entrada1.set("")
        else:
            entrada1.set(x) 
    
    def voltatextoi13_1(self,vento=None):
        x = entrada1.get()
        if x == "":
            entrada1.set("Digite aqui...") 
            self.ent1.config(state=DISABLED)

    def teladoador1(self):    
        self.img1 = PhotoImage(file = os.path.abspath("Doador1.png"))
        self.img2 = PhotoImage(file = os.path.abspath("btnEntrar.PNG"))
        self.img3 = PhotoImage(file = os.path.abspath("btnSetinha.PNG"))  
        self.img4 = PhotoImage(file = os.path.abspath("btnOlho.PNG"))  

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
        
        self.btn5 = Button(self.jan, bg = "#131644",bd = 0, activebackground = "#131644", image = self.img4)
        self.btn5.place(relx = 0.88, rely = 0.47, relwidth = 0.08, relheight = 0.06)

        global entrada1
        entrada1 = StringVar()
        self.ent1 = Entry(self.jan, bg = "#131644", font = "Century\ Gothic 14",fg = "white",bd = 0, textvariable = entrada1,insertbackground='white',disabledbackground = "#131644",disabledforeground = "white")
        self.ent1.place(relx = 0.16, rely = 0.36, relwidth = 0.68, relheight = 0.06)
        #entrada1.set("Digite seu e-mail")
        entrada1.set("jv@gmail.com")
        
        global entrada2
        entrada2 = StringVar()
        self.ent2 = Entry(self.jan, bg = "#131644", font = "Century\ Gothic 14",fg = "white",bd = 0, textvariable = entrada2,insertbackground='white',disabledbackground = "#131644",disabledforeground = "white")
        self.ent2.place(relx = 0.16, rely = 0.468, relwidth = 0.68, relheight = 0.06)
        #entrada2.set("Digite sua senha")
        entrada2.set("aaa")

        self.ent1.bind("<1>",self.limpartd1_1)
        self.ent2.bind("<1>",self.limpartd1_2)
        self.btn5.bind("<1>",self.mostrard1_1)
        self.btn5.bind("<ButtonRelease-1>",self.mostrard1_2)
        self.lbl1.bind("<1>",self.voltatextod1)

    def limpartd1_1(self,evento=None):
        self.ent1.config(state=NORMAL)
        x = entrada1.get()
        if x == "Digite seu e-mail":
            entrada1.set("")
        else:
            entrada1.set(x) 
        x2 = entrada2.get()
        if x2 == "":
            entrada2.set("Digite sua senha")
            self.ent2.config(show="")
        elif x2 == "Digite sua senha":
            self.ent2.config(show="")
        else:
            entrada2.set(x2) 
         
    def limpartd1_2(self,evento=None):
        self.ent2.config(state=NORMAL)
        self.ent2.config(show="*")
        x = entrada2.get()
        if x == "Digite sua senha":
            entrada2.set("")
        else:
            entrada2.set(x) 
        x2 = entrada1.get()
        if x2 == "":
            entrada1.set("Digite seu e-mail")
        else:
            entrada1.set(x2) 
 
    def voltatextod1(self,vento=None):
        x = entrada1.get()
        if x == "":
            entrada1.set("Digite seu e-mail") 
            self.ent1.config(state=DISABLED)
        y = entrada2.get()
        if y == "":
            entrada2.set("Digite sua senha")
            self.ent2.config(state=DISABLED)
            self.ent2.config(show="")
    
    def mostrard1_1(self,event=None):
        z = entrada2.get()
        if z != "Digite sua senha":
            self.ent2.config(show="")
    def mostrard1_2(self,event=None):
        z = entrada2.get()
        if z != "Digite sua senha":
            self.ent2.config(show="*")

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
            global edoador 
            edoador = True
            try:
                cursor.execute("SELECT id,nome FROM doadores WHERE email = '{}'".format(email))
                for i in cursor:
                    for x in i:
                        self.listad6_1.append(x)
                    global idlogado
                    idlogado= self.listad6_1[0]
                    global nomelogado 
                    nomelogado = self.listad6_1[1]
                    self.listad6_1 = []
            except Exception as e:
                print(e)
            self.telainst5(2)
            
        
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
        self.ent1 = Entry(self.jan, bg = "#131644", font = "Century\ Gothic 14",fg = "white",bd = 0, textvariable = entrada1,insertbackground='white',disabledbackground = "#131644",disabledforeground = "white")
        self.ent1.place(relx = 0.155, rely = 0.545, relwidth = 0.69, relheight = 0.055)
        entrada1.set("Digite seu e-mail")
        
        self.ent1.bind("<1>",self.limpard22_1)
        self.lbl1.bind("<1>",self.voltatextod22_1)
            
    def limpard22_1(self,evento=None):
        self.ent1.config(state=NORMAL)
        x = entrada1.get()
        if x == "Digite seu e-mail":
            entrada1.set("")
        else:
            entrada1.set(x) 
    
    def voltatextod22_1(self,vento=None):
        x = entrada1.get()
        if x == "":
            entrada1.set("Digite seu e-mail") 
            self.ent1.config(state=DISABLED)
    
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
        self.img4 = PhotoImage(file = os.path.abspath("btnOlho.PNG"))

        self.lbl1 = Label(self.jan, image = self.img1)
        self.lbl1.place(relx = 0, rely = 0, relwidth =1, relheight = 1)
    

        self.btn1 = Button(self.jan, bg = "#131644",bd = 0, activebackground = "#131644", image = self.img2 ,command = lambda: self.conexãod3())
        self.btn1.place(relx = 0.29, rely = 0.55, relwidth = 0.42, relheight = 0.14)
        
        self.btn2 = Button(self.jan, bg = "#131644",bd = 0, activebackground = "#131644", image = self.img3 ,command = lambda: self.teladoador2())
        self.btn2.place(relx = 0.03, rely = 0.06, relwidth = 0.15, relheight = 0.06)
        
        self.btn3 = Button(self.jan, bg = "#131644",bd = 0, activebackground = "#131644", image = self.img4)
        self.btn3.place(relx = 0.88, rely = 0.46, relwidth = 0.08, relheight = 0.06)
    

        global entrada1
        entrada1 = StringVar()
        self.ent1 = Entry(self.jan, bg = "#131644", font = "Century\ Gothic 14",fg = "white",bd = 0, textvariable = entrada1,insertbackground='white',disabledbackground = "#131644",disabledforeground = "white")
        self.ent1.place(relx = 0.155, rely = 0.46, relwidth = 0.69, relheight = 0.055)
        entrada1.set("Insira o código")
        
        self.ent1.bind("<1>",self.limpard3_1)
        self.lbl1.bind("<1>",self.voltatextod3_1)
        self.btn3.bind("<1>",self.mostrard3_1)
        self.btn3.bind("<ButtonRelease-1>",self.mostrard3_2)
          
    def limpard3_1(self,evento=None):
        self.ent1.config(state=NORMAL)
        self.ent1.config(show="*")
        x = entrada1.get()
        if x == "Insira o código":
            entrada1.set("")
        else:
            entrada1.set(x) 
    
    def voltatextod3_1(self,vento=None):
        x = entrada1.get()
        if x == "":
            entrada1.set("Insira o código") 
            self.ent1.config(state=DISABLED)
            self.ent1.config(show="")
    
    def mostrard3_1(self,event=None):
        z = entrada1.get()
        if z != "Insira o código":
            self.ent1.config(show="")
    def mostrard3_2(self,event=None):
        z = entrada1.get()
        if z != "Insira o código":
            self.ent1.config(show="*")
    

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
        self.img5 = PhotoImage(file = os.path.abspath("btnOlho.PNG"))
    
 
        self.lbl1 = Label(self.jan, image = self.img1)
        self.lbl1.place(relx = 0, rely = 0, relwidth =1, relheight = 1)
    

        self.btn1 = Button(self.jan, bg = "#131644",bd = 0, activebackground = "#131644", image = self.img2 ,command = lambda: self.teladoador5())
        self.btn1.place(relx = 0.29, rely = 0.59, relwidth = 0.42, relheight = 0.14)
        
        self.btn2 = Button(self.jan, bg = "#131644",bd = 0, activebackground = "#131644", image = self.img3 ,command = lambda: self.createcodigo())
        self.btn2.place(relx = 0.1, rely = 0.47, relwidth = 0.8, relheight = 0.14)
        
        self.btn3 = Button(self.jan, bg = "#131644",bd = 0, activebackground = "#131644", image = self.img4 ,command = lambda: self.teladoador2())
        self.btn3.place(relx = 0.03, rely = 0.06, relwidth = 0.15, relheight = 0.06)
        
        self.btn4 = Button(self.jan, bg = "#131644",bd = 0, activebackground = "#131644", image = self.img5)
        self.btn4.place(relx = 0.88, rely = 0.34, relwidth = 0.08, relheight = 0.06)

        global entrada1
        entrada1 = StringVar()
        self.ent1 = Entry(self.jan, bg = "#131644", font = "Century\ Gothic 14",fg = "white",bd = 0, textvariable = entrada1,insertbackground='white',disabledbackground = "#131644",disabledforeground = "white")
        self.ent1.place(relx = 0.155, rely = 0.335, relwidth = 0.69, relheight = 0.055)
        entrada1.set("Insira o código")
        
        self.ent1.bind("<1>",self.limpard4_1)
        self.lbl1.bind("<1>",self.voltatextod4_1)
        self.btn4.bind("<1>",self.mostrard4_1)
        self.btn4.bind("<ButtonRelease-1>",self.mostrard4_2)
          
    def limpard4_1(self,evento=None):
        self.ent1.config(state=NORMAL)
        self.ent1.config(show="*")
        x = entrada1.get()
        if x == "Insira o código":
            entrada1.set("")
        else:
            entrada1.set(x) 
    
    def voltatextod4_1(self,vento=None):
        x = entrada1.get()
        if x == "":
            entrada1.set("Insira o código") 
            self.ent1.config(state=DISABLED)
            self.ent1.config(show="")
    
    def mostrard4_1(self,event=None):
        z = entrada1.get()
        if z != "Insira o código":
            self.ent1.config(show="")
    def mostrard4_2(self,event=None):
        z = entrada1.get()
        if z != "Insira o código":
            self.ent1.config(show="*")
    
    def conexãod4(self):
        self.codigoescrito = entrada1.get()
            
    def teladoador5(self):
  
        self.img1 = PhotoImage(file = os.path.abspath("doador5.png"))
        self.img2 = PhotoImage(file = os.path.abspath("btnRedefinir.PNG"))
        self.img3 = PhotoImage(file = os.path.abspath("btnSetinha.PNG"))
        self.img4 = PhotoImage(file = os.path.abspath("btnOlho.PNG"))

        self.lbl1 = Label(self.jan, image = self.img1)
        self.lbl1.place(relx = 0, rely = 0, relwidth =1, relheight = 1)
    

        self.btn1 = Button(self.jan, bg = "#131644",bd = 0, activebackground = "#131644", image = self.img2 ,command = lambda: self.conexãod5())
        self.btn1.place(relx = 0.29, rely = 0.63, relwidth = 0.42, relheight = 0.14)
        
        self.btn2 = Button(self.jan, bg = "#131644",bd = 0, activebackground = "#131644", image = self.img3 ,command = lambda: self.teladoador2())
        self.btn2.place(relx = 0.03, rely = 0.06, relwidth = 0.15, relheight = 0.06)
        
        self.btn3 = Button(self.jan, bg = "#131644",bd = 0, activebackground = "#131644", image = self.img4)
        self.btn3.place(relx = 0.88, rely = 0.4, relwidth = 0.08, relheight = 0.06)
        
        self.btn4 = Button(self.jan, bg = "#131644",bd = 0, activebackground = "#131644", image = self.img4)
        self.btn4.place(relx = 0.88, rely = 0.53, relwidth = 0.08, relheight = 0.06)
    

        global entrada1
        entrada1 = StringVar()
        self.ent1 = Entry(self.jan, bg = "#131644", font = "Century\ Gothic 14",fg = "white",bd = 0, textvariable = entrada1,insertbackground='white',disabledbackground = "#131644",disabledforeground = "white")
        self.ent1.place(relx = 0.155, rely = 0.398, relwidth = 0.69, relheight = 0.055)
        entrada1.set("Digite sua nova senha")

        global entrada2
        entrada2 = StringVar()
        self.ent2 = Entry(self.jan, bg = "#131644", font = "Century\ Gothic 14",fg = "white",bd = 0, textvariable = entrada2,insertbackground='white',disabledbackground = "#131644",disabledforeground = "white")
        self.ent2.place(relx = 0.155, rely = 0.523, relwidth = 0.69, relheight = 0.055)
        entrada2.set("Confirme sua nova senha")
            
        self.ent1.bind("<1>",self.limpartd5_1)
        self.ent2.bind("<1>",self.limpartd5_2)
        self.btn3.bind("<1>",self.mostrard5_1)
        self.btn3.bind("<ButtonRelease-1>",self.mostrard5_2)
        self.btn4.bind("<1>",self.mostrard5_3)
        self.btn4.bind("<ButtonRelease-1>",self.mostrard5_4)
        self.lbl1.bind("<1>",self.voltatextod5)

    def limpartd5_1(self,evento=None):
        self.ent1.config(state=NORMAL)
        self.ent1.config(show="*")
        x = entrada1.get()
        if x == "Digite sua nova senha":
            entrada1.set("")
        else:
            entrada1.set(x) 
        x2 = entrada2.get()
        if x2 == "":
            entrada2.set("Confirme sua nova senha")
            self.ent2.config(show="")
        elif x2 == "Confirme sua nova senha":
            self.ent2.config(show="")
        else:
            entrada2.set(x2) 
         
    def limpartd5_2(self,evento=None):
        self.ent2.config(state=NORMAL)
        self.ent2.config(show="*")
        x = entrada2.get()
        if x == "Confirme sua nova senha":
            entrada2.set("")
        else:
            entrada2.set(x) 
        x2 = entrada1.get()
        if x2 == "":
            entrada1.set("Digite sua nova senha")
            self.ent1.config(show="")
        elif x2 == "Digite sua nova senha":
            self.ent1.config(show="")
        else:
            entrada1.set(x2) 
 
    def voltatextod5(self,vento=None):
        x = entrada1.get()
        if x == "":
            entrada1.set("Digite sua nova senha") 
            self.ent1.config(state=DISABLED)
            self.ent2.config(show="")
        y = entrada2.get()
        if y == "":
            entrada2.set("Confirme sua nova senha")
            self.ent2.config(state=DISABLED)
            self.ent2.config(show="")
    
    def mostrard5_1(self,event=None):
        z = entrada1.get()
        if z != "Digite sua nova senha":
            self.ent1.config(show="")
    def mostrard5_2(self,event=None):
        z = entrada1.get()
        if z != "Digite sua nova senha":
            self.ent1.config(show="*")
    def mostrard5_3(self,event=None):
        z = entrada2.get()
        if z != "Confirme sua nova senha":
            self.ent2.config(show="")
    def mostrard5_4(self,event=None):
        z = entrada2.get()
        if z != "Confirme sua nova senha":
            self.ent2.config(show="*")
    
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
        self.img4 = PhotoImage(file = os.path.abspath("btnOlho.PNG"))

        self.lbl1 = Label(self.jan, image = self.img1)
        self.lbl1.place(relx = 0, rely = 0, relwidth =1, relheight = 1)
    

        self.btn1 = Button(self.jan, bg = "#131644",bd = 0, activebackground = "#131644", image = self.img2 ,command = lambda: self.conexãod6())
        self.btn1.place(relx = 0.29, rely = 0.8, relwidth = 0.42, relheight = 0.15)
        
        self.btn2 = Button(self.jan, bg = "#131644",bd = 0, activebackground = "#131644", image = self.img3 ,command = lambda: self.teladoador1())
        self.btn2.place(relx = 0.03, rely = 0.055, relwidth = 0.15, relheight = 0.06)
        
        self.btn3 = Button(self.jan, bg = "#131644",bd = 0, activebackground = "#131644", image = self.img4)
        self.btn3.place(relx = 0.88, rely = 0.57, relwidth = 0.08, relheight = 0.06)

        self.btn4 = Button(self.jan, bg = "#131644",bd = 0, activebackground = "#131644", image = self.img4)
        self.btn4.place(relx = 0.88, rely = 0.7, relwidth = 0.08, relheight = 0.06)
        

        global entrada1
        entrada1 = StringVar()
        self.ent1 = Entry(self.jan, bg = "#131644", font = "Century\ Gothic 14",fg = "white",bd = 0, textvariable = entrada1,insertbackground='white',disabledbackground = "#131644",disabledforeground = "white")
        self.ent1.place(relx = 0.155, rely = 0.305, relwidth = 0.69, relheight = 0.055)
        entrada1.set("Digite seu nome completo")
        
        global entrada2
        entrada2 = StringVar()
        self.ent2 = Entry(self.jan, bg = "#131644", font = "Century\ Gothic 14",fg = "white",bd = 0, textvariable = entrada2,insertbackground='white',disabledbackground = "#131644",disabledforeground = "white")
        self.ent2.place(relx = 0.155, rely = 0.435, relwidth = 0.68, relheight = 0.055)
        entrada2.set("Digite seu e-mail")
        
        global entrada3
        entrada3 = StringVar()
        self.ent3 = Entry(self.jan, bg = "#131644", font = "Century\ Gothic 14",fg = "white",bd = 0, textvariable = entrada3,insertbackground='white',disabledbackground = "#131644",disabledforeground = "white")
        self.ent3.place(relx = 0.155, rely = 0.57, relwidth = 0.68, relheight = 0.055)
        entrada3.set("Digite sua senha")
        
        global entrada4
        entrada4 = StringVar()
        self.ent4 = Entry(self.jan, bg = "#131644", font = "Century\ Gothic 14",fg = "white",bd = 0, textvariable = entrada4,insertbackground='white',disabledbackground = "#131644",disabledforeground = "white")
        self.ent4.place(relx = 0.155, rely = 0.695, relwidth = 0.68, relheight = 0.055)
        entrada4.set("Confirme sua senha")

        self.ent1.bind("<1>",self.limpartd2_1)
        self.ent2.bind("<1>",self.limpartd2_2)
        self.ent3.bind("<1>",self.limpartd2_3)
        self.ent4.bind("<1>",self.limpartd2_4)
        self.lbl1.bind("<1>",self.voltatextod2)
        self.btn3.bind("<1>",self.mostrard2_1)
        self.btn3.bind("<ButtonRelease-1>",self.mostrard2_2)
        self.btn4.bind("<1>",self.mostrard2_3)
        self.btn4.bind("<ButtonRelease-1>",self.mostrard2_4)

    def limpartd2_1(self,evento=None):
        self.ent1.config(state=NORMAL)
        self.ent3.config(show="*")
        x = entrada1.get()
        if x == "Digite seu nome completo":
            entrada1.set("")
        else:
            entrada1.set(x) 
        x2 = entrada2.get()
        if x2 == "":
            entrada2.set("Digite seu e-mail")
        else:
            entrada2.set(x2) 
        x3 = entrada3.get()
        if x3 == "":
            entrada3.set("Digite sua senha")
            self.ent3.config(show="")
        elif x3 == "Digite sua senha":
            self.ent3.config(show="")
        else:
            entrada3.set(x3) 
        x4 = entrada4.get()
        if x4 == "":
            entrada4.set("Confirme sua senha")
            self.ent4.config(show="")
        elif x4 == "Digite sua senha":
            self.ent4.config(show="")
        else:
            entrada4.set(x4) 
         
    def limpartd2_2(self,evento=None):
        self.ent2.config(state=NORMAL)
        self.ent3.config(show="*")
        x = entrada2.get()
        if x == "Digite seu e-mail":
            entrada2.set("")
        else:
            entrada2.set(x) 
        x2 = entrada1.get()
        if x2 == "":
            entrada1.set("Digite seu nome completo")
        else:
            entrada1.set(x2) 
        x3 = entrada3.get()
        if x3 == "":
            entrada3.set("Digite sua senha")
            self.ent3.config(show="")
        elif x3 == "Digite sua senha":
            self.ent3.config(show="")
        else:
            entrada3.set(x3) 
        x4 = entrada4.get()
        if x4 == "":
            entrada4.set("Confirme sua senha")
            self.ent4.config(show="")
        elif x4 == "Confirme sua senha":
            self.ent4.config(show="")
        else:
            entrada4.set(x4) 
    
    def limpartd2_3(self,evento=None):
        self.ent3.config(state=NORMAL)
        self.ent3.config(show="*")
        x = entrada3.get()
        if x == "Digite sua senha":
            entrada3.set("")
        else:
            entrada3.set(x) 
        x2 = entrada1.get()
        if x2 == "":
            entrada1.set("Digite seu nome completo")
        else:
            entrada1.set(x2) 
        x3 = entrada2.get()
        if x3 == "":
            entrada2.set("Digite seu e-mail")
        else:
            entrada2.set(x3) 
        x4 = entrada4.get()
        if x4 == "":
            entrada4.set("Confirme sua senha")
            self.ent4.config(show="")
        elif x4 == "Confirme sua senha":
            self.ent4.config(show="")
        else:
            entrada4.set(x4) 
    
    def limpartd2_4(self,evento=None):
        self.ent4.config(state=NORMAL)
        self.ent4.config(show="*")
        x = entrada4.get()
        if x == "Confirme sua senha":
            entrada4.set("")
        else:
            entrada4.set(x) 
        x2 = entrada1.get()
        if x2 == "":
            entrada1.set("Digite seu nome completo")
        else:
            entrada1.set(x2) 
        x3 = entrada2.get()
        if x3 == "":
            entrada2.set("Digite seu e-mail")
        else:
            entrada2.set(x3) 
        x3 = entrada3.get()
        if x3 == "":
            entrada3.set("Digite sua senha")
            self.ent3.config(show="")
        elif x3 == "Digite sua senha":
            self.ent3.config(show="")
        else:
            entrada3.set(x3) 
            
    def voltatextod2(self,event=None):
        x = entrada1.get()
        if x == "":
            entrada1.set("Digite seu nome completo") 
            self.ent1.config(state=DISABLED)
        y = entrada2.get()
        if y == "":
            entrada2.set("Digite seu e-mail")
            self.ent2.config(state=DISABLED)
        z = entrada3.get()
        if z == "":
            entrada3.set("Digite sua senha")
            self.ent3.config(state=DISABLED)
            self.ent3.config(show="")
        z2 = entrada4.get()
        if z2 == "":
            entrada4.set("Confirme sua senha")
            self.ent4.config(state=DISABLED)
            self.ent4.config(show="")
    
    def mostrard2_1(self,event=None):
        z = entrada3.get()
        if z != "Digite sua senha":
            self.ent3.config(show="")
    def mostrard2_2(self,event=None):
        z = entrada3.get()
        if z != "Digite sua senha":
            self.ent3.config(show="*")
    def mostrard2_3(self,event=None):
        z = entrada4.get()
        if z != "Digite sua senha":
            self.ent4.config(show="")
    def mostrard2_4(self,event=None):
        z = entrada4.get()
        if z != "Confirme sua senha":
            self.ent4.config(show="*")

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
    
    
    def teladoador8(self):   
        self.img1 = PhotoImage(file = os.path.abspath("doador8.png"))
        self.img2 = PhotoImage(file = os.path.abspath("btnPerfilgg.PNG"))
        self.img3 = PhotoImage(file = os.path.abspath("btnSetinha.PNG"))
        self.img4 = PhotoImage(file = os.path.abspath("btnChat.PNG"))
        self.img5 = PhotoImage(file = os.path.abspath("btnDinheiro.PNG"))
    

        self.lbl1 = Label(self.jan, image = self.img1)
        self.lbl1.place(relx = 0, rely = 0, relwidth =1, relheight = 1)
        
        self.lbl2 = Label(self.jan, bg = "#BDAB9F", fg = "black", text = nomeinst[0], font = " Century\ Gothic 14",anchor = "w")
        self.lbl2.place(relx = 0.32, rely = 0.165, relwidth =0.62, relheight = 0.04)


        self.btn1 = Button(self.jan, bg = "#131644",bd = 0, activebackground = "#131644", image = self.img2 ,command = lambda: self.teste())
        self.btn1.place(relx = 0.05, rely = 0.123, relwidth = 0.22, relheight = 0.14)
        
        self.btn2 = Button(self.jan, bg = "#131644",bd = 0, activebackground = "#131644", image = self.img3 ,command = lambda: self.telainst5(2))
        self.btn2.place(relx = 0.05, rely = 0.03, relwidth = 0.15, relheight = 0.06)
        
        self.btn3 = Button(self.jan, bg = "#131644",bd = 0, activebackground = "#131644", image = self.img4 ,command = lambda: self.teladoador13())
        self.btn3.place(relx = 0.2, rely = 0.02, relwidth = 0.22, relheight = 0.08)
        
        self.btn4 = Button(self.jan, bg = "#131644",bd = 0, activebackground = "#131644", image = self.img5 ,command = lambda: self.teladoador14())
        self.btn4.place(relx = 0.82, rely = 0.015, relwidth = 0.15, relheight = 0.08)
        
    def teladoador9(self):
        try:
            global ultimamensagem
            ultimamensagem = []
            global instituicaochat
            instituicaochat = []
        
            global doadorchat
            doadorchat = []
               
            sql = ("SELECT distinct t1.idinst, t2.nome, t1.mensagem "
                    "FROM chat t1 "
                    "join instituicoes t2 on t1.idinst = t2.id "
            )
             
            if edoador == True:
                sql += "where t1.iddoador = " + str(idlogado)
            else:                    
                sql += "where t1.idinst = " + str(idlogado)
            sql += " and t1.id = (select max(t3.id) from chat t3 where t3.iddoador = t1.iddoador and t3.idinst = t1.idinst)"
            
            cursor.execute(sql)            
            
            for i in cursor.fetchall():
                instituicaochat.append(i[1])
                ultimamensagem.append(i[2])
                doadorchat.append(i[2])
        
            
        except Exception as e:
            print(e)

        
        self.img1 = PhotoImage(file = os.path.abspath("Inst10.png"))
        self.img2 = PhotoImage(file = os.path.abspath("btnPerfilmaior.PNG"))
        self.img3 = PhotoImage(file = os.path.abspath("btnSetinha.PNG"))
    
        self.lbl1 = Label(self.jan, image = self.img1)
        self.lbl1.place(relx = 0, rely = 0, relwidth =1, relheight = 1)
    
    
        if edoador:
            self.btn1 = Button(self.jan, bg = "#131644",bd = 0, activebackground = "gray",command = lambda: self.teladoador13())#doadorchat[0]
            self.btn1.place(relx = 0, rely = 0.125, relwidth = 1, relheight = 0.11)
        else:
            self.btn1 = Button(self.jan, bg = "#131644",bd = 0, activebackground = "gray",command = lambda: self.teladoador13())#instituicaochat[0]
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

        
        self.lbl2 = Label(self.jan, bg = "#131644", fg = "white", text = instituicaochat[0], font = " Century\ Gothic 14",anchor = "w")
        self.lbl2.place(relx = 0.26, rely = 0.145, relwidth =0.55, relheight = 0.04)
        
        self.lbl3 = Label(self.jan, bg = "#131644", fg = "white", text = ultimamensagem[0], font = " Century\ Gothic 10",anchor= "w")
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
        global nt
        nt = 2
        print(nd)
        self.img1 = PhotoImage(file = os.path.abspath("doador10.png"))
        self.img2 = PhotoImage(file = os.path.abspath("btnPerfilgg.PNG"))
        self.img3 = PhotoImage(file = os.path.abspath("btnSetinha.PNG"))
        self.img4 = PhotoImage(file = os.path.abspath("btnAddcartao.PNG"))
        self.img5 = PhotoImage(file = os.path.abspath("btnLogout.PNG"))
        

        self.lbl1 = Label(self.jan, image = self.img1)
        self.lbl1.place(relx = 0, rely = 0, relwidth =1, relheight = 1)
        
        self.lbl2 = Label(self.jan, bg = "#BDAB9F", fg = "black", text = nomelogado, font = " Century\ Gothic 14")
        self.lbl2.place(relx = 0.31, rely = 0.165, relwidth =0.62, relheight = 0.04)
        
        self.listb1 = Listbox(self.jan, bg = "#131644",fg = "white", font = "Century\ Gothic 14", bd = 0, selectbackground = "#FEAD77", highlightbackground = "#FEAD77")
        self.listb1.place(relx = 0.09, rely = 0.63, relwidth = 0.8, relheight = 0.23)
        
        
        self.btn1 = Button(self.jan, bg = "#131644",bd = 0, activebackground = "#131644", image = self.img2 ,command = lambda: self.teste())
        self.btn1.place(relx = 0.05, rely = 0.123, relwidth = 0.22, relheight = 0.14)
        
        self.btn2 = Button(self.jan, bg = "#131644",bd = 0, activebackground = "#131644", image = self.img3 ,command = lambda: self.telainst5(2))
        self.btn2.place(relx = 0.055, rely = 0.025, relwidth = 0.15, relheight = 0.06)
        
        self.btn3 = Button(self.jan, bg = "#131644",bd = 0, activebackground = "#131644", image = self.img4 ,command = lambda: self.teladoador11())
        self.btn3.place(relx = 0.13, rely = 0.86, relwidth = 0.72, relheight = 0.15)
        
        self.btn4 = Button(self.jan, bg = "#131644",bd = 0, activebackground = "#131644", image = self.img5 ,command = lambda: self.Padrao3())
        self.btn4.place(relx = 0.85, rely = 0.025, relwidth = 0.1, relheight = 0.06)
    
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
        self.ent1 = Entry(self.jan, bg = "#131644", font = "Century\ Gothic 14",fg = "white",bd = 0, textvariable = entrada1,insertbackground='white',disabledbackground = "#131644",disabledforeground = "white")
        self.ent1.place(relx = 0.155, rely = 0.26, relwidth = 0.69, relheight = 0.055)
        entrada1.set("Nome no cartão")
        
        global entrada2
        entrada2 = StringVar()
        self.ent2 = Entry(self.jan, bg = "#131644", font = "Century\ Gothic 14",fg = "white",bd = 0, textvariable = entrada2,insertbackground='white',disabledbackground = "#131644",disabledforeground = "white")
        self.ent2.place(relx = 0.155, rely = 0.377, relwidth = 0.68, relheight = 0.055)
        entrada2.set("CPF")
        
        global entrada3
        entrada3 = StringVar()
        self.ent3 = Entry(self.jan, bg = "#131644", font = "Century\ Gothic 14",fg = "white",bd = 0, textvariable = entrada3,insertbackground='white',disabledbackground = "#131644",disabledforeground = "white")
        self.ent3.place(relx = 0.155, rely = 0.5, relwidth = 0.68, relheight = 0.055)
        entrada3.set("Número do cartão")
        
        global entrada5
        entrada5 = StringVar()
        self.ent5 = Entry(self.jan, bg = "#131644", font = "Century\ Gothic 14",fg = "white",bd = 0, textvariable = entrada5,insertbackground='white',disabledbackground = "#131644",disabledforeground = "white")
        self.ent5.place(relx = 0.155, rely = 0.62, relwidth = 0.68, relheight = 0.055)
        entrada5.set("Vencimento")
        
        global entrada6
        entrada6 = StringVar()
        self.ent6 = Entry(self.jan, bg = "#131644", font = "Century\ Gothic 14",fg = "white",bd = 0, textvariable = entrada6,insertbackground='white',disabledbackground = "#131644",disabledforeground = "white")
        self.ent6.place(relx = 0.155, rely = 0.74, relwidth = 0.68, relheight = 0.055)
        entrada6.set("CVC")

        self.ent1.bind("<1>",self.limpartd11_1)
        self.ent1.bind("<KeyRelease>",self.maiusculo)
        self.ent2.bind("<1>",self.limpartd11_2)
        self.ent3.bind("<1>",self.limpartd11_3)
        self.ent3.bind("<KeyRelease>",self.arrumar)
        self.ent5.bind("<1>",self.limpartd11_5)
        self.ent5.bind("<KeyRelease>",self.arrumar3)
        self.ent6.bind("<1>",self.limpartd11_6)
        self.lbl1.bind("<1>",self.voltatextod11)

    def limpartd11_1(self,evento=None):
        self.ent1.config(state=NORMAL)
        x = entrada1.get()
        if x == "Nome no cartão":
            entrada1.set("")
        else:
            entrada1.set(x) 
        x2 = entrada2.get()
        if x2 == "":
            entrada2.set("CPF")
        else:
            entrada2.set(x2) 
        x3 = entrada3.get()
        if x3 == "":
            entrada3.set("Número do cartão")
        else:
            entrada3.set(x3) 
        x5 = entrada5.get()
        if x5 == "":
            entrada5.set("Vencimento")
        else:
            entrada5.set(x5)
        x6 = entrada6.get()
        if x6 == "":
            entrada6.set("CVC")
        else:
            entrada6.set(x6)
         
    def limpartd11_2(self,evento=None):
        self.ent2.config(state=NORMAL)
        x = entrada2.get()
        if x == "CPF":
            entrada2.set("")
        else:
            entrada2.set(x) 
        x2 = entrada1.get()
        if x2 == "":
            entrada1.set("Nome no cartão")
        else:
            entrada1.set(x2) 
        x3 = entrada3.get()
        if x3 == "":
            entrada3.set("Número do cartão")
        else:
            entrada3.set(x3) 
        x5 = entrada5.get()
        if x5 == "":
            entrada5.set("Vencimento")
        else:
            entrada5.set(x5)
        x6 = entrada6.get()
        if x6 == "":
            entrada6.set("CVC")
        else:
            entrada6.set(x6)
    
    def limpartd11_3(self,evento=None):
        self.ent3.config(state=NORMAL)
        x = entrada3.get()
        if x == "Número do cartão":
            entrada3.set("")
        else:
            entrada3.set(x) 
        x2 = entrada1.get()
        if x2 == "":
            entrada1.set("Nome no cartão")
        else:
            entrada1.set(x2) 
        x3 = entrada2.get()
        if x3 == "":
            entrada2.set("CPF")
        else:
            entrada2.set(x3) 
        x5 = entrada5.get()
        if x5 == "":
            entrada5.set("Vencimento")
        else:
            entrada5.set(x5)
        x6 = entrada6.get()
        if x6 == "":
            entrada6.set("CVC")
        else:
            entrada6.set(x6)
    
    def limpartd11_5(self,evento=None):
        self.ent5.config(state=NORMAL)
        x = entrada5.get()
        if x == "Vencimento":
            entrada5.set("")
        else:
            entrada5.set(x) 
        x2 = entrada1.get()
        if x2 == "":
            entrada1.set("Nome no cartão")
        else:
            entrada1.set(x2) 
        x3 = entrada2.get()
        if x3 == "":
            entrada2.set("CPF")
        else:
            entrada2.set(x3) 
        x5 = entrada3.get()
        if x5 == "":
            entrada3.set("Número do cartão")
        else:
            entrada3.set(x5)
        x6 = entrada6.get()
        if x6 == "":
            entrada6.set("CVC")
        else:
            entrada6.set(x6)
    
    def limpartd11_6(self,evento=None):
        self.ent6.config(state=NORMAL)
        x = entrada6.get()
        if x == "CVC":
            entrada6.set("")
        else:
            entrada6.set(x) 
        x2 = entrada1.get()
        if x2 == "":
            entrada1.set("Nome no cartão")
        else:
            entrada1.set(x2) 
        x3 = entrada2.get()
        if x3 == "":
            entrada2.set("CPF")
        else:
            entrada2.set(x3) 
        x5 = entrada3.get()
        if x5 == "":
            entrada3.set("Número do cartão")
        else:
            entrada3.set(x5)
        x6 = entrada5.get()
        if x6 == "":
            entrada5.set("Vencimento")
        else:
            entrada5.set(x6)
            
    def voltatextod11(self,event=None):
        x = entrada1.get()
        if x == "":
            entrada1.set("Nome no cartão") 
            self.ent1.config(state=DISABLED)
        y = entrada2.get()
        if y == "":
            entrada2.set("CPF")
            self.ent2.config(state=DISABLED)
        z = entrada3.get()
        if z == "":
            entrada3.set("Número do cartão")
            self.ent3.config(state=DISABLED)
        a = entrada5.get()
        if a == "":
            entrada5.set("Vencimento")
            self.ent5.config(state=DISABLED)
        b = entrada6.get()
        if b == "":
            entrada6.set("CVC")
            self.ent6.config(state=DISABLED)
    
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
        self.vencimentocard = entrada5.get()
        self.CVCcard = entrada6.get()
        
        self.x1 = False 
        self.x2 = False
        self.x3 = False
        self.x5 = False
        self.x6 = False
        
        if self.nomescrito == "" or self.nomescrito == "Nome no cartão":
            if self.lblc1T == False:
                self.lblc1 = Label(self.jan, text = "Digite o nome!", font = "Century\ Gothic 12", fg = "#FE4A49", bg = "#131644")
                self.lblc1.place(relx = 0.1, rely = 0.32, relwidth = 0.4, relheight = 0.04)
                self.lblc1T = True
        else:
            self.x1 = True
            if self.lblc1T == True:
                self.lblc1.destroy()
                self.lblc1T = False
        
        if self.cpfescrito == "" or self.cpfescrito == "CPF":
            if self.lblc2T == False:
                self.lblc2 = Label(self.jan, text = "Digite o CPF!", font = "Century\ Gothic 12", fg = "#FE4A49", bg = "#131644")
                self.lblc2.place(relx = 0.08, rely = 0.44, relwidth = 0.4, relheight = 0.04)
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
                        self.lblc7.place(relx = 0.08, rely = 0.44, relwidth = 0.4, relheight = 0.04)
                        self.lblc7T = True
            except Exception as e:
                print(e)
                
        if self.numcard == "" or self.numcard == "Número do cartão":
            if self.lblc3T == False:
                self.lblc3 = Label(self.jan, text = "Digite o número!", font = "Century\ Gothic 12", fg = "#FE4A49", bg = "#131644")
                self.lblc3.place(relx = 0.12, rely = 0.56, relwidth = 0.4, relheight = 0.04)
                self.lblc3T = True
        else:
            print(len(self.numcard))
            if len(self.numcard) == 19:
                self.numcard2 = self.numcard.split("-")
                for i in self.numcard2:
                    if i.isdigit():
                        print(i)
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
                            self.lblc8.place(relx = 0.12, rely = 0.56, relwidth = 0.4, relheight = 0.04)
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
                    self.lblc8.place(relx = 0.12, rely = 0.56, relwidth = 0.4, relheight = 0.04)
                    self.lblc8T = True
                        
        
        if self.vencimentocard == "" or self.vencimentocard == "Vencimento":
            if self.lblc5T == False:
                self.lblc5 = Label(self.jan, text = "Digite o vencimento!", font = "Century\ Gothic 12", fg = "#FE4A49", bg = "#131644")
                self.lblc5.place(relx = 0.115, rely = 0.685, relwidth = 0.5, relheight = 0.04)
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
                            self.lblc10 = Label(self.jan, text = "Vencimento inválido!", font = "Century\ Gothic 12", fg = "#FE4A49", bg = "#131644")
                            self.lblc10.place(relx = 0.115, rely = 0.685, relwidth = 0.5, relheight = 0.04)
                        self.lblc10T = True
            else:
                if self.lblc5T == True:
                    self.lblc5.destroy()
                    self.lblc5T = False
                if self.lblc10T == True:
                    self.lblc10.destroy()
                    self.lblc10T = False
                
                if self.lblc10T == False:
                    self.lblc10 = Label(self.jan, text = "Vencimento inválido!", font = "Century\ Gothic 12", fg = "#FE4A49", bg = "#131644")
                    self.lblc10.place(relx = 0.115, rely = 0.685, relwidth = 0.5, relheight = 0.04)
                    self.lblc10T = True

        if self.CVCcard == "" or self.CVCcard == "CVC":
            if self.lblc6T == False:
                self.lblc6 = Label(self.jan, text = "Digite a CVC!", font = "Century\ Gothic 12", fg = "#FE4A49", bg = "#131644")
                self.lblc6.place(relx = 0.135, rely = 0.81, relwidth = 0.4, relheight = 0.04)
                self.lblc6T = True
        else:
            self.x6 = True
            if self.lblc6T == True:
                self.lblc6.destroy()
                self.lblc6T = False
        
        if self.x1 == True and self.x2 == True and self.x3 == True and self.x5 == True and self.x6 == True:
            cursor.execute("SELECT id FROM doadores WHERE email = '{}'".format(email))
            for i in cursor:
                for x in i:
                    self.listad6_1.append(x)
                self.iddoador = self.listad6_1[0]
                self.listad6_1 = []
            
            cursor.execute(f"insert into cartoes (nomeuser,cpfuser,numcard,vencicard,cvccard,iduser) values (%s,%s,%s,%s,%s,%s);",(self.nomescrito,self.cpfescrito, self.numcard, self.vencimentocard,self.CVCcard,self.iddoador))
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
        
        self.btn2 = Button(self.jan, bg = "#131644",bd = 0, activebackground = "#131644", image = self.img3 ,command = lambda: self.telainst5(2))
        self.btn2.place(relx = 0.06, rely = 0.03, relwidth = 0.15, relheight = 0.06)
    

        global entrada1
        entrada1 = StringVar()
        self.ent1 = Entry(self.jan, bg = "#FEAD77", font = "Century\ Gothic 14",fg = "white", textvariable = entrada1, bd = 0)
        self.ent1.place(relx = 0.045, rely = 0.14, relwidth = 0.82, relheight = 0.075)
        entrada1.set("Digite aqui...")
        
        self.listb1 = Listbox(self.jan, bg = "#131644",fg = "white", font = "Century\ Gothic 14", bd = 0, selectbackground = "#FEAD77")
        self.listb1.place(relx = 0.01, rely = 0.23, relwidth = 0.98, relheight = 0.41)

        self.ent1.bind("<1>",self.limpard12_1)
        self.lbl1.bind("<1>",self.voltatextod12_1)
        self.listb1.bind("<1>",self.conexãod12)

    def pesquisa(self):
        self.pesq = entrada1.get()
        self.listb1.delete("0","end")
        if self.pesq == "":
            self.listb1.insert(END, "Instituição inexistente!")
        else:
            try:
                cursor.execute("SELECT nome FROM instituicoes WHERE nome like '%{}%'".format(self.pesq))
                for i in cursor:
                    for x in i:
                        self.listad6_1.append(x)
                
                self.resulpesq = self.listad6_1
                self.listad6_1 = []
                for i in range(len(self.resulpesq)):
                    self.listb1.insert(END, self.resulpesq[i])
                self.resulpesq = []
                
                self.results = self.listb1.get(0)
                print(self.results)
                if self.results == "":
                    self.listb1.insert(END, "Instituição inexistente!")
            except Exception as e:
                print(e)
    
    def conexãod12(self,evento = None):
        t = Timer(0.1, self.selectela)
        t.start()
        
    def selectela(self):
        self.indice = self.listb1.curselection()
        for i in self.indice:
            global instituicao 
            instituicao = self.listb1.get(i)
            self.teladoador8()
             
    def limpard12_1(self,evento=None):
        self.ent1.config(state=NORMAL)
        x = entrada1.get()
        if x == "Digite aqui...":
            entrada1.set("")
        else:
            entrada1.set(x) 
    
    def voltatextod12_1(self,vento=None):
        x = entrada1.get()
        if x == "":
            entrada1.set("Digite aqui...") 
            self.ent1.config(state=DISABLED)
    
    def teladoador13(self): 
        '''
        sql = ("SELECT t1.idinst, t2.nome, t1.mensagem , t3.nome, t1.quemEnviou "
                    "FROM chat t1 "
                    "join instituicoes t2 on t1.idinst = t2.id "
                    "join doadores t3 on t3.id = t1.iddoador "
                )
        if edoador == True:
            sql += "where t1.iddoador = " + str(idlogado) + " and t1.idinst = " + str(usuariochat)
        else:                    
            sql += "where t1.idinst = " + str(idlogado) + " and t1.iddoador = " + str(usuariochat)
        global quemEnviou
        quemEnviou = []
        
        cursor.execute(sql)            
        
        for i in cursor.fetchall():
            instituicaochat.append(i[1])
            ultimamensagem.append(i[2])
            doadorchat.append(i[3])
            quemEnviou.append(i[4])
        '''
             
        self.img1 = PhotoImage(file = os.path.abspath("doador13.png"))
        self.img2 = PhotoImage(file = os.path.abspath("btnPerfilmaior.PNG"))
        self.img3 = PhotoImage(file = os.path.abspath("btnSetinha.PNG"))
        self.img4 = PhotoImage(file = os.path.abspath("btnBalao.PNG"))
        self.img5 = PhotoImage(file = os.path.abspath("btnBalao2.PNG"))
    
        self.lbl1 = Label(self.jan, image = self.img1)
        self.lbl1.place(relx = 0, rely = 0, relwidth =1, relheight = 1)
        
        self.lbl1 = Label(self.jan, image = self.img4,bg = "#131644")
        self.lbl1.place(relx = 0.3, rely = 0.12, relwidth =0.64, relheight = 0.2)
        self.lbl1 = Label(self.jan,text ="Bom dia, posso realizar visitas?",font = " Century\ Gothic 14",fg = "black",bg = "#BDAB9F", anchor = "w")
        self.lbl1.place(relx = 0.33, rely = 0.17, relwidth =0.4, relheight = 0.06)
        
        self.lbl1 = Label(self.jan, image = self.img5,bg = "#131644")
        self.lbl1.place(relx = 0.3, rely = 0.22, relwidth =0.64, relheight = 0.2)
        self.lbl1 = Label(self.jan,text ="Claro, de acordo com a sua disponibilidade",font = " Century\ Gothic 14",fg = "black",bg = "white", anchor = "w")
        self.lbl1.place(relx = 0.33, rely = 0.27, relwidth =0.4, relheight = 0.06)
        '''
        if edoador:
            if quemEnviou[0] == "Doador":
                self.lbl1 = Label(self.jan, image = self.img4, text = ultimamensagem,font = " Century\ Gothic 14",fg = "black",bg = "#BDAB9F")
                self.lbl1.place(relx = 0.6, rely = 0.3, relwidth =0.3, relheight = 0.1)     
                #direita
            else:
                self.lbl1 = Label(self.jan, image = self.img4, text = ultimamensagem,font = " Century\ Gothic 14",fg = "black",bg = "#BDAB9F")
                self.lbl1.place(relx = 0.6, rely = 0.3, relwidth =0.3, relheight = 0.1) 
                #esquerda
        else:
            if quemEnviou[0] == "Doador":
                self.lbl1 = Label(self.jan, image = self.img4, text = ultimamensagem,font = " Century\ Gothic 14",fg = "black",bg = "#BDAB9F")
                self.lbl1.place(relx = 0.6, rely = 0.3, relwidth =0.3, relheight = 0.1) 
                #esquerda
            else:
                self.lbl1 = Label(self.jan, image = self.img4, text = ultimamensagem,font = " Century\ Gothic 14",fg = "black",bg = "#BDAB9F")
                self.lbl1.place(relx = 0.6, rely = 0.3, relwidth =0.3, relheight = 0.1) 
                #direita
        '''

        self.btn1 = Button(self.jan,text = nomeinst[0], font = "Century\ Gothic 14",fg = "white", bg = "#131644",bd = 0,anchor = "w",activebackground = "gray",command = lambda: self.teste())
        self.btn1.place(relx = 0.38, rely = 0.01, relwidth = 0.58, relheight = 0.09)
       
        self.btn2 = Button(self.jan, bg = "#131644",bd = 0, activebackground = "#131644", image = self.img2 ,command = lambda: self.teladoador8())
        self.btn2.place(relx = 0.21, rely = 0.01, relwidth = 0.17, relheight = 0.1)
        
        self.btn3 = Button(self.jan, bg = "#131644",bd = 0, activebackground = "#131644", image = self.img3 ,command = lambda: self.teladoador9())
        self.btn3.place(relx = 0.03, rely = 0.025, relwidth = 0.15, relheight = 0.06)
    
        global entrada1
        entrada1 = StringVar()
        self.ent1 = Entry(self.jan, bg = "#131644", font = "Century\ Gothic 14",fg = "white",bd = 3, textvariable = entrada1,disabledbackground = "#131644",disabledforeground = "white")
        self.ent1.place(relx = 0.01, rely = 0.565, relwidth = 0.98, relheight = 0.08)
        entrada1.set("Digite aqui...")
        
        self.ent1.bind("<1>",self.limpard13_1)
        self.lbl1.bind("<1>",self.voltatextod13_1)
        self.jan.bind("<Return>",self.salvachat)
            
    def limpard13_1(self,evento=None):
        self.ent1.config(state=NORMAL)
        x = entrada1.get()
        if x == "Digite aqui...":
            entrada1.set("")
        else:
            entrada1.set(x) 
    
    def voltatextod13_1(self,vento=None):
        x = entrada1.get()
        if x == "":
            entrada1.set("Digite aqui...") 
            self.ent1.config(state=DISABLED)
    
    def salvachat(self,evento=None):
        x = entrada1.get()
        print(x) 
        
        self.lbl1 = Label(self.jan, image = self.img4,bg = "#131644")
        self.lbl1.place(relx = 0.3, rely = 0.42, relwidth =0.64, relheight = 0.2)
        self.lbl1 = Label(self.jan,text = x,font = " Century\ Gothic 14",fg = "black",bg = "#BDAB9F", anchor = "w")
        self.lbl1.place(relx = 0.33, rely = 0.47, relwidth =0.4, relheight = 0.06) 
        
        entrada1.set("")
        '''if x != "":
            cursor.execute(f"insert into chat (iduser,idinst,mensagem) values (%s,%s,%s);",(idlogado,self.idinst,x))
            conexao.commit()'''
    
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
        self.btn2 = Button(self.jan, bg = "#131644",bd = 0, activebackground = "#131644", image = self.img3 ,command = lambda: self.conexãod14())
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
        
    def conexãod14(self):
        self.valor = entrada1.get()
        #cursor.execute(f"insert into pagamentos (valor,iduser,idinst) values (%s,%s,%s);",(self.valor,self.iddoador,self.idinst))
        #conexao.commit()
        self.teladoador15()
    
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