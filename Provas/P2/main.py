#Luis Gustavo Riso Santos
#2024002372

import tkinter as tk
import comandasV3 as comanda
import produtos as produto

class LimitePrincipal():
    def __init__(self, root, controle):
        self.controle = controle
        self.root = root
        self.root.geometry('300x250')
        self.menubar = tk.Menu(self.root)        
        self.comandaMenu = tk.Menu(self.menubar)
        
        self.comandaMenu.add_command(label="Lançar Comanda", \
                    command=self.controle.cadastrarComanda)
        self.comandaMenu.add_command(label="Imprimir Comanda", \
                    command=self.controle.imprimirComanda)
        self.comandaMenu.add_command(label="Calcular Faturamento", \
                    command=self.controle.calcularFaturamento)
        self.menubar.add_cascade(label="Comanda", \
                    menu=self.comandaMenu)

        self.root.config(menu=self.menubar)

class ControlePrincipal():
    def __init__(self):
        self.root = tk.Tk()
        
        self.ctrlProduto = produto.CtrlProduto()
        self.ctrlComanda = comanda.CtrlComanda(self)

        self.limite = LimitePrincipal(self.root, self)
        self.root.title("Sistema Comandas")
        self.root.mainloop()
    
    def cadastrarComanda(self):
        self.ctrlComanda.cadastrarComanda()
    def imprimirComanda(self):
        self.ctrlComanda.imprimirComanda()
    def calcularFaturamento(self):
        self.ctrlComanda.calcularFaturamento()

if __name__ == "__main__":
    c = ControlePrincipal()
