from pynput.keyboard import Key, Controller
keyboard = Controller()
keyboard.type("Hello World!")

if len(self.texto) > 2:
            self.textomaior = self.textomaior.replace(",",self.texto[len(self.texto)-3])
            self.textomaior = self.texto[len(self.texto)-3] + ","
            self.textomenor = self.texto[len(self.texto)-2] + str(n)
            self.texto = self.textomaior + self.textomenor