from tkinter import *

class Padrao2():
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
        self.jan.mainloop()
        
    def imagens(self):    
        self.img1 = PhotoImage(file = "C:\\Users\\Pichau\\OneDrive - Firjan\\Arquivos\\Kindly\\Doador14.png")
        self.img2 = PhotoImage(file = "C:\\Users\\Pichau\\OneDrive - Firjan\\Arquivos\\Kindly\\btnXapagar.PNG")
        self.img3 = PhotoImage(file = "C:\\Users\\Pichau\\OneDrive - Firjan\\Arquivos\\Kindly\\btnCerto.PNG")
        self.img4 = PhotoImage(file = "C:\\Users\\Pichau\\OneDrive - Firjan\\Arquivos\\Kindly\\btnSetinha.PNG")
        self.imgbt1 = PhotoImage(file = "C:\\Users\\Pichau\\OneDrive - Firjan\\Arquivos\\Kindly\\btnum1.PNG")
        self.imgbt2 = PhotoImage(file = "C:\\Users\\Pichau\\OneDrive - Firjan\\Arquivos\\Kindly\\btnum2.PNG")
        self.imgbt3 = PhotoImage(file = "C:\\Users\\Pichau\\OneDrive - Firjan\\Arquivos\\Kindly\\btnum3.PNG")
        self.imgbt4 = PhotoImage(file = "C:\\Users\\Pichau\\OneDrive - Firjan\\Arquivos\\Kindly\\btnum4.PNG")
        self.imgbt5 = PhotoImage(file = "C:\\Users\\Pichau\\OneDrive - Firjan\\Arquivos\\Kindly\\btnum5.PNG")
        self.imgbt6 = PhotoImage(file = "C:\\Users\\Pichau\\OneDrive - Firjan\\Arquivos\\Kindly\\btnum6.PNG")
        self.imgbt7 = PhotoImage(file = "C:\\Users\\Pichau\\OneDrive - Firjan\\Arquivos\\Kindly\\btnum7.PNG")
        self.imgbt8 = PhotoImage(file = "C:\\Users\\Pichau\\OneDrive - Firjan\\Arquivos\\Kindly\\btnum8.PNG")
        self.imgbt9 = PhotoImage(file = "C:\\Users\\Pichau\\OneDrive - Firjan\\Arquivos\\Kindly\\btnum9.PNG")
        self.imgbt0 = PhotoImage(file = "C:\\Users\\Pichau\\OneDrive - Firjan\\Arquivos\\Kindly\\btnum0.PNG")
    
    def labels(self):
        self.lbl1 = Label(self.jan, image = self.img1)
        self.lbl1.place(relx = 0, rely = 0, relwidth =1, relheight = 1)
    
    def botoes(self):
        self.btn1 = Button(self.jan, bg = "#131644",bd = 0, activebackground = "#131644", image = self.img2 ,command = lambda: self.apagar())
        self.btn1.place(relx = 0.1, rely = 0.81, relwidth = 0.2, relheight = 0.12)
        self.btn2 = Button(self.jan, bg = "#131644",bd = 0, activebackground = "#131644", image = self.img3 ,command = lambda: self.teste())
        self.btn2.place(relx = 0.7, rely = 0.81, relwidth = 0.2, relheight = 0.12)
        self.btn3 = Button(self.jan, bg = "#131644",bd = 0, activebackground = "#131644", image = self.img4 ,command = lambda: self.teste())
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
   
    def entries(self):
        global entrada1
        entrada1 = StringVar()
        self.ent1 = Entry(self.jan, disabledbackground="#131644", font = "Century\ Gothic 14",disabledforeground= "white", textvariable = entrada1, bd = 0,state = "disabled")
        self.ent1.place(relx = 0.19, rely = 0.27, relwidth = 0.62, relheight = 0.05)
        entrada1.set("")

    def teste(self):
        print("sla")
        
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
    
Padrao2()
        