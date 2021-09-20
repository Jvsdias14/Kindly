from tkinter import *

class TelaInst8():
    def __init__(self):
        self.jan = Tk()
        self.jan.geometry("375x667+750+220")
        self.jan.title("Kindly")
        self.jan.config(bg = "white")
        self.jan.resizable(False,False)
        self.imagens()
        self.labelfundo()
        self.botoes()
        self.labels()
        self.jan.mainloop()
        
    def imagens(self):    
        self.img1 = PhotoImage(file = "C:\\Users\\Pichau\\OneDrive - Firjan\\Arquivos\\Kindly\\Inst8.png")
        self.img2 = PhotoImage(file = "C:\\Users\\Pichau\\OneDrive - Firjan\\Arquivos\\Kindly\\btnPerfilmaior.PNG")
        self.img3 = PhotoImage(file = "C:\\Users\\Pichau\\OneDrive - Firjan\\Arquivos\\Kindly\\btnSetinha.PNG")
    
    def labelfundo(self):
        self.lbl1 = Label(self.jan, image = self.img1)
        self.lbl1.place(relx = 0, rely = 0, relwidth =1, relheight = 1)
    
    def labels(self):
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
        
        
    def botoes(self):
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
        
        self.btn3 = Button(self.jan, bg = "#131644",bd = 0, activebackground = "#131644", image = self.img3 ,command = lambda: self.teste())
        self.btn3.place(relx = 0.07, rely = 0.03, relwidth = 0.15, relheight = 0.06)
        
    def teste(self):
        print("sla")

TelaInst8()