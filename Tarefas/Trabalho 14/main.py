import tkinter as tk
import jogosV1 as jogo

class LimitePrincipal():
    def __init__(self, root, controle):
        self.controle = controle
        self.root = root
        self.root.geometry('300x250')
        self.menubar = tk.Menu(self.root)        
        self.jogoMenu = tk.Menu(self.menubar)
        self.saveMenu = tk.Menu(self.menubar)
        
        self.jogoMenu.add_command(label="Cadastrar", \
                    command=self.controle.inserirJogo)
        self.jogoMenu.add_command(label="Avaliar", \
                    command=self.controle.avaliarJogo)
        self.jogoMenu.add_command(label="Consultar", \
                    command=self.controle.consultarJogo)
        #self.jogoMenu.add_command(label="Listar", \
        #            command=self.controle.listarJogo)
        self.menubar.add_cascade(label="Jogo", \
                    menu=self.jogoMenu)
        
        self.saveMenu.add_command(label="Salvar", \
                    command=self.controle.salvarJogos)
        self.menubar.add_cascade(label="Sair", \
                    menu=self.saveMenu)

        self.root.config(menu=self.menubar)

class ControlePrincipal():
    def __init__(self):
        self.root = tk.Tk()
        
        self.ctrlJogo = jogo.CtrlJogo()

        self.limite = LimitePrincipal(self.root, self)
        self.root.title("Sistema Jogos")
        self.root.mainloop()
    
    def inserirJogo(self):
        self.ctrlJogo.inserirJogo()
    def avaliarJogo(self):
        self.ctrlJogo.avaliarJogo()
    def consultarJogo(self):
        self.ctrlJogo.consultarJogo()
    #def listarJogo(self):
    #    self.ctrlJogo.listarJogo()
    def salvarJogos(self):
        self.ctrlJogo.salvarJogos()
        self.root.destroy()

if __name__ == "__main__":
    c = ControlePrincipal()
