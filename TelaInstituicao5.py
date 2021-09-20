from tkinter import *

class TelaIsnt5():
    def __init__(self):
        self.jan = Tk()
        self.jan.geometry("375x667+750+220")
        self.jan.title("Kindly")
        self.jan.config(bg = "white")
        self.jan.resizable(False,False)
        self.imagens()
        self.labels()
        self.botoes()
        self.jan.mainloop()
        
    def imagens(self):    
        self.img1 = PhotoImage(file = "C:\\Users\\Pichau\\OneDrive - Firjan\\Arquivos\\Kindly\\Inst5.png")
        self.img2 = PhotoImage(file = "C:\\Users\\Pichau\\OneDrive - Firjan\\Arquivos\\Kindly\\btnPerfil.PNG")
        self.img3 = PhotoImage(file = "C:\\Users\\Pichau\\OneDrive - Firjan\\Arquivos\\Kindly\\btnChat.PNG")
        self.img4 = PhotoImage(file = "C:\\Users\\Pichau\\OneDrive - Firjan\\Arquivos\\Kindly\\btnLupa.PNG")
        self.img5 = PhotoImage(file = "C:\\Users\\Pichau\\OneDrive - Firjan\\Arquivos\\Kindly\\btnPerfilmaior.PNG")
        self.img6 = PhotoImage(file = "C:\\Users\\Pichau\\OneDrive - Firjan\\Arquivos\\Kindly\\btn+.PNG")
    
    def labels(self):
        self.lbl1 = Label(self.jan, image = self.img1)
        self.lbl1.place(relx = 0, rely = 0, relwidth =1, relheight = 1)
        
        self.lbl2 = Label(self.jan, bg = "#BDAB9F", fg = "black", text = "Nome da instituição", font = " Century\ Gothic 14")
        self.lbl2.place(relx = 0.18, rely = 0.145, relwidth =0.62, relheight = 0.04)
        
        self.lbl3 = Label(self.jan, bg = "#BDAB9F", fg = "black", text = "Nome da instituição", font = " Century\ Gothic 14")
        self.lbl3.place(relx = 0.18, rely = 0.695, relwidth =0.62, relheight = 0.04)
        
    def botoes(self):
        self.btn1 = Button(self.jan, bg = "#131644",bd = 0, activebackground = "#131644", image = self.img2 ,command = lambda: self.teste())
        self.btn1.place(relx = 0.035, rely = 0.009, relwidth = 0.12, relheight = 0.08)
       
        self.btn2 = Button(self.jan, bg = "#131644",bd = 0, activebackground = "#131644", image = self.img3 ,command = lambda: self.teste())
        self.btn2.place(relx = 0.64, rely = 0.009, relwidth = 0.15, relheight = 0.08)
        
        self.btn3 = Button(self.jan, bg = "#131644",bd = 0, activebackground = "#131644", image = self.img4 ,command = lambda: self.teste())
        self.btn3.place(relx = 0.83, rely = 0.009, relwidth = 0.15, relheight = 0.08)
        
        self.btn4 = Button(self.jan, bg = "#131644",bd = 0, activebackground = "#131644", image = self.img5 ,command = lambda: self.teste())
        self.btn4.place(relx = 0.02, rely = 0.1, relwidth = 0.17, relheight = 0.12)
        
        self.btn5 = Button(self.jan, bg = "#131644",bd = 0, activebackground = "#131644", image = self.img5 ,command = lambda: self.teste())
        self.btn5.place(relx = 0.02, rely = 0.65, relwidth = 0.17, relheight = 0.12)
        
        self.btn6 = Button(self.jan, bd = 0, image = self.img6 ,command = lambda: self.teste())
        self.btn6.place(relx = 0.8, rely = 0.75, relwidth = 0.17, relheight = 0.09)

    def teste(self):
        print("sla")

TelaIsnt5()
        