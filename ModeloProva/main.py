#Aluna: Camily Victal Finamor
#Matricula: 2024001197

import tkinter as tk
import arquivo1 as arq1
import arquivo02 as arq2

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#CLASSE VIEW MAIN
class ViewPrincipal:
    def __init__(self, janela, controlador):
        self.janela = janela
        self.controlador = controlador
        self.janela.geometry('300x250')

        self.menu = tk.Menu(self.janela)
        self.menu1 = tk.Menu(self.menu)
        self.menu2 = tk.Menu(self.menu)

        self.menu1.add_command(label='-nome-da-opçao-', command=self.controlador.NomedaFunçao1)
        self.menu1.add_command(label='-nome-da-opçao-', command=self.controlador.NomedaFunçao2)
        self.menu1.add_command(label='-nome-da-opçao-', command=self.controlador.NomedaFunçao3)
        self.menu.add_cascade(label='-nome-da-cascata-', menu=self.menu1)

        self.menu2.add_command(label='-nome-da-opçao-', command=self.controlador.NomedaFunçao4)
        self.menu2.add_command(label='-nome-da-opçao-', command=self.controlador.NomedaFunçao5)
        self.menu.add_cascade(label='-nome-da-cascata-', menu=self.menu2)

        self.janela.config(menu=self.menu)

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#CLASSE CONTROLADORA MAIN
class ControladorPrincipal:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('-Nome-do-contexto')

        self.ControladorArquivo1 = arq1.ControladorArquivo1(self) #fazendo a ligação do controlador principal com os controladores dos demais arquivos
        self.ControladorArquivo2 = arq2.ControladorArquivo2(self) #passar o self(controlador principal) se precisar de coisas no arq1 q são do arq 2 por exemplo

        self.ViewPrincipal = ViewPrincipal(self.root, self)
        self.root.mainloop()

    def NomedaFunçao1(self):
        return self.ControladorArquivo1.NomedaFunçao1() #definindo as funções de callback do menu da view principal, elas chamam os controladores dos outros arquivos com as funções que abrem as respectivcas janelas secundarias
    
    def NomedaFunçao2(self):
        return self.ControladorArquivo1.NomedaFunçao2()
    
    def NomedaFunçao3(self):
        return self.ControladorArquivo1.NomedaFunçao3()

    def NomedaFunçao4(self):
        return self.ControladorArquivo2.NomedaFunçao4()
    
    def NomedaFunçao5(self):
        return self.ControladorArquivo2.NomedaFunçao5()
    
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#MAIN
if __name__ == '__main__':
    c = ControladorPrincipal()