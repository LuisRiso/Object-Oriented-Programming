import tkinter as tk
import profissional as professor
import aluno as estudante

class LimitePrincipal():
    def __init__(self, root, controle):
        self.controle = controle
        self.root = root
        self.root.geometry('300x250')
        self.menubar = tk.Menu(self.root)        
        self.profissionalMenu = tk.Menu(self.menubar)
        self.alunoMenu = tk.Menu(self.menubar)

        self.profissionalMenu.add_command(label="Cadastrar", \
                    command=self.controle.inserirProfissional)
        self.profissionalMenu.add_command(label="Listar", \
                    command=self.controle.listarProfissional)
        self.profissionalMenu.add_command(label="Faturamento", \
                    command=self.controle.faturamentoProfissional)
        self.menubar.add_cascade(label="Profissional", \
                    menu=self.profissionalMenu)

        self.alunoMenu.add_command(label="Cadastrar", \
                    command=self.controle.inserirAluno)
        self.alunoMenu.add_command(label="Consultar", \
                    command=self.controle.consultarAluno)
        #self.alunoMenu.add_command(label="Listar", \
        #            command=self.controle.listarAluno)
        self.menubar.add_cascade(label="Aluno", \
                   menu=self.alunoMenu)
        
        self.root.config(menu=self.menubar)

class ControlePrincipal():
    def __init__(self):
        self.root = tk.Tk()
        
        self.ctrlProfissional = professor.CtrlProfissional()
        self.ctrlAluno = estudante.CtrlAluno(self)

        self.limite = LimitePrincipal(self.root, self)
        self.root.title("Sistema Pilates")
        self.root.mainloop()

    def inserirProfissional(self):
        self.ctrlProfissional.inserirProfissional()
    def listarProfissional(self):
        self.ctrlProfissional.listarProfissional()
    def faturamentoProfissional(self):
        self.ctrlProfissional.faturamentoProfissional()
    
    def inserirAluno(self):
        self.ctrlAluno.inserirAluno()
    def consultarAluno(self):
        self.ctrlAluno.consultarAluno()
    #def listarAluno(self):
    #    self.ctrlAluno.listarAluno() 

if __name__ == "__main__":
    c = ControlePrincipal()