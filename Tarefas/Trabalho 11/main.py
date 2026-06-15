import tkinter as tk
import produto as product
import cupomFiscal as cupom

class LimitePrincipal():
    def __init__(self, root, controle):
        self.controle = controle
        self.root = root
        self.root.geometry('300x250')
        self.menubar = tk.Menu(self.root)        
        self.produtoMenu = tk.Menu(self.menubar)
        self.cupomMenu = tk.Menu(self.menubar)

        self.produtoMenu.add_command(label="Cadastrar", \
                    command=self.controle.inserirProduto)
        self.produtoMenu.add_command(label="Consultar", \
                    command=self.controle.consultarProduto)
        self.produtoMenu.add_command(label="Listar", \
                    command=self.controle.listarProduto)
        self.menubar.add_cascade(label="Produto", \
                    menu=self.produtoMenu)
        
        self.cupomMenu.add_command(label="Criar", \
                    command=self.controle.cadastrarCupom)
        self.cupomMenu.add_command(label="Consultar", \
                    command=self.controle.consultarCupom)
        self.cupomMenu.add_command(label="Listar", \
                    command=self.controle.listarCupom)
        self.menubar.add_cascade(label="CupomFiscal", \
                    menu=self.cupomMenu)
        
        self.root.config(menu=self.menubar)

class ControlePrincipal():
    def __init__(self):
        self.root = tk.Tk()
        
        self.ctrlProduto = product.CtrlProduto()
        self.ctrlCupom = cupom.CtrlCupomFiscal(self)

        self.limite = LimitePrincipal(self.root, self)
        self.root.title("Sistema Produto")
        self.root.mainloop()

    def inserirProduto(self):
        self.ctrlProduto.inserirProduto()
    def listarProduto(self):
        self.ctrlProduto.listarProduto()
    def consultarProduto(self):
        self.ctrlProduto.consultarProduto()

    def cadastrarCupom(self):
        self.ctrlCupom.cadastrarCupom()
    def listarCupom(self):
        self.ctrlCupom.listarCupom()
    def consultarCupom(self):
        self.ctrlCupom.consultarCupom()

if __name__ == "__main__":
    c = ControlePrincipal()