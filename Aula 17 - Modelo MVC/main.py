import tkinter as tk
from tkinter import messagebox
import estudante as est #importa outro arquivo python -> no caso a entidade estudante
import disciplina as disc #importa outro arquivo python -> no caso a entidade disciplina
#para cada entidade que tivermos, vamos criar um arquivo python
#terá a classe controladora, a classe view e a classe entidade

class LimitePrincipal():
    def __init__(self, root, controle):
        self.controle = controle
        self.root = root
        self.root.geometry('300x200')
        self.menubar = tk.Menu(self.root)        
        self.estudanteMenu = tk.Menu(self.menubar)
        self.discipMenu = tk.Menu(self.menubar)
        self.turmaMenu = tk.Menu(self.menubar)     

        self.estudanteMenu.add_command(label="Insere", \
                    command=self.controle.insereEstudantes) #chamando a função de callback "insereEstudante"
        self.estudanteMenu.add_command(label="Mostra", \
                    command=self.controle.mostraEstudantes)
        self.menubar.add_cascade(label="Estudante", \
                    menu=self.estudanteMenu)

        self.discipMenu.add_command(label="Insere", \
                        command=self.controle.insereDisciplinas)
        self.discipMenu.add_command(label="Mostra", \
                    command=self.controle.mostraDisciplinas)
        self.menubar.add_cascade(label="Disciplina", \
                    menu=self.discipMenu)

        self.turmaMenu.add_command(label="Insere")
        self.menubar.add_cascade(label="Turma", \
                    menu=self.turmaMenu)        

        self.root.config(menu=self.menubar)

#vai controlar os outros controladores que fazem parte do programa
#instancia todos os controladores que fazem parte do código
class ControlePrincipal():       
    def __init__(self):
        self.root = tk.Tk()

        self.ctrlEstudante = est.CtrlEstudante() #instanciando o controlador da entidade estudante => executou o main do controlador estudante

        self.ctrlDisciplina = disc.CtrlDisciplina()

        self.limite = LimitePrincipal(self.root, self) #criação da tela inicial do Tkinter -> passa o controle para o limite

        self.root.title("Exemplo MVC")
        # Inicia o mainloop
        self.root.mainloop()
       
    #está pegando o controlador do estudanto e chamando uma função para o controlador do estudante
    #está passando o controle principal dele para o controlador estudante
    def insereEstudantes(self):
        self.ctrlEstudante.insereEstudantes() 

    def mostraEstudantes(self):
        self.ctrlEstudante.mostraEstudantes() #mesmo com o mesmo nome, está passando o controle para o controlador estudante

    def insereDisciplinas(self):
        self.ctrlDisciplina.insereDisciplinas() 

    def mostraDisciplinas(self):
        self.ctrlDisciplina.mostraDisciplinas() 

if __name__ == '__main__':
    c = ControlePrincipal()