import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import simpledialog

class Aluno:
    def __init__(self, nome, cpf, email, tipoAula, nomeProfessor, nroAulas):
        self.__nome = nome
        self.__cpf = cpf
        self.__email = email
        self.__tipoAula = tipoAula
        self.__nomeProfessor = nomeProfessor
        self.__nroAulas = nroAulas

    @property
    def nome(self):
        return self.__nome
    @property
    def cpf(self):
        return self.__cpf
    @property
    def email(self):
        return self.__email
    @property
    def tipoAula(self):
        return self.__tipoAula
    @property
    def nomeProfessor(self):
        return self.__nomeProfessor
    @property
    def nroAulas(self):
        return self.__nroAulas

class LimiteInsereAluno(tk.Toplevel):
    def __init__(self, controle, listaNomeProfessores):
        tk.Toplevel.__init__(self)
        self.geometry('400x200')
        self.title("Cadastrar Profissional")
        self.controle = controle

        self.frameNome = tk.Frame(self)
        self.frameCPF = tk.Frame(self)
        self.frameEmail = tk.Frame(self)
        self.frameTipoAula = tk.Frame(self)
        self.frameNomeProfessor = tk.Frame(self)
        self.frameNroAulas = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        self.frameNome.pack()
        self.frameCPF.pack()
        self.frameEmail.pack()
        self.frameTipoAula.pack()
        self.frameNomeProfessor.pack()
        self.frameNroAulas.pack()
        self.frameButton.pack()

        #Preenchimento Manual
        self.labelNome = tk.Label(self.frameNome,text="Nome: ")
        self.labelCPF = tk.Label(self.frameCPF,text="CPF: ")
        self.labelEmail = tk.Label(self.frameEmail,text="Email: ")
        self.labelNome.pack(side="left")
        self.labelCPF.pack(side="left")  
        self.labelEmail.pack(side="left") 
        self.inputNome = tk.Entry(self.frameNome, width=25)
        self.inputNome.pack(side="left")
        self.inputCPF = tk.Entry(self.frameCPF, width=25)
        self.inputCPF.pack(side="left")
        self.inputEmail = tk.Entry(self.frameEmail, width=25)
        self.inputEmail.pack(side="left")

        #Escolha Tipo de Aula
        self.labelTipoAula = tk.Label(self.frameTipoAula,text="Tipo Aula: ")
        self.labelTipoAula.pack(side="left")
        self.escolhaComboTipoAula = tk.StringVar()
        self.comboboxTipoAula = ttk.Combobox(self.frameTipoAula, width = 20 , textvariable = self.escolhaComboTipoAula)
        self.comboboxTipoAula.pack(side="left")
        self.comboboxTipoAula['values'] = ['Pilates', 'Funcional']

        #Escolha Professor
        self.labelNomeProfessor = tk.Label(self.frameNomeProfessor,text="Professor: ")
        self.labelNomeProfessor.pack(side="left")
        self.escolhaComboNomeProfessor = tk.StringVar()
        self.comboboxNomeProfessor = ttk.Combobox(self.frameNomeProfessor, width = 20 , textvariable = self.escolhaComboNomeProfessor)
        self.comboboxNomeProfessor.pack(side="left")
        self.comboboxNomeProfessor['values'] = listaNomeProfessores

        #Escolha Nro de Aulas
        self.labelNroAulas = tk.Label(self.frameNroAulas,text="Nro Aulas: ")
        self.labelNroAulas.pack(side="left")
        self.escolhaComboNroAulas = tk.StringVar()
        self.comboboxNroAulas = ttk.Combobox(self.frameNroAulas, width = 20 , textvariable = self.escolhaComboNroAulas)
        self.comboboxNroAulas.pack(side="left")
        self.comboboxNroAulas['values'] = [2, 3, 4]

        self.buttonSubmit = tk.Button(self.frameButton ,text="Cadastrar")
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", controle.enterHandler)
      
        self.buttonClear = tk.Button(self.frameButton ,text="Limpar")   
        self.buttonClear.pack(side="left")
        self.buttonClear.bind("<Button>", controle.clearHandler)

        self.buttonFecha = tk.Button(self.frameButton ,text="Fechar") 
        self.buttonFecha.pack(side="left")
        self.buttonFecha.bind("<Button>", controle.fechaHandler)

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)

class LimiteConsultaAluno():
    def __init__(self, textoAluno):
        messagebox.showinfo('Aluno Buscado', textoAluno)

class LimiteListaAlunos():
    def __init__(self, listaAlunos):
        messagebox.showinfo('Lista de Alunos', listaAlunos)

class CtrlAluno():
    def __init__(self, controlePrincipal):
        self.ctrlPrincipal = controlePrincipal
        self.listaAlunosCadastrados = []
    
    def inserirAluno(self):
        listaNomeProfessores = self.ctrlPrincipal.ctrlProfissional.getListaNomesProfissionais()
        self.limiteInsercaoAluno = LimiteInsereAluno(self, listaNomeProfessores) 

    def enterHandler(self, event):
        nome = self.limiteInsercaoAluno.inputNome.get()
        cpf = self.limiteInsercaoAluno.inputCPF.get()
        email = self.limiteInsercaoAluno.inputEmail.get()
        tipoAula = self.limiteInsercaoAluno.escolhaComboTipoAula.get()
        professor = self.limiteInsercaoAluno.escolhaComboNomeProfessor.get()
        nroAulas = self.limiteInsercaoAluno.escolhaComboNroAulas.get()

        if nome == "" or cpf == "" or email == "" or tipoAula == "" or professor == "" or nroAulas == "":
            messagebox.showwarning("Erro Aluno", "Erro: Preencha todos os campos.")
            return

        for buscaAluno in self.listaAlunosCadastrados:
            if buscaAluno.cpf == cpf:
                messagebox.showwarning("Erro Aluno", "Erro: CPF ja cadastrado.")
                self.limiteInsercaoAluno.inputCPF.delete(0, len(self.limiteInsercaoAluno.inputCPF.get()))
                return
        
        for buscaAluno in self.listaAlunosCadastrados:
            if buscaAluno.email == email:
                messagebox.showwarning("Erro Aluno", "Erro: E-mail ja cadastrado.")
                self.limiteInsercaoAluno.inputEmail.delete(0, len(self.limiteInsercaoAluno.inputEmail.get()))
                return
        
        cadastroAluno = Aluno(nome, cpf, email, tipoAula, professor, nroAulas)
        self.listaAlunosCadastrados.append(cadastroAluno)
        self.limiteInsercaoAluno.mostraJanela('Sucesso', 'Aluno(a) cadastrado(a) com sucesso')
        self.ctrlPrincipal.ctrlProfissional.adicionarAluno(cadastroAluno)
        self.clearHandler(event)

    def clearHandler(self, event):
        self.limiteInsercaoAluno.inputNome.delete(0, len(self.limiteInsercaoAluno.inputNome.get()))
        self.limiteInsercaoAluno.inputCPF.delete(0, len(self.limiteInsercaoAluno.inputCPF.get()))
        self.limiteInsercaoAluno.inputEmail.delete(0, len(self.limiteInsercaoAluno.inputEmail.get()))

    def fechaHandler(self, event):
        self.limiteInsercaoAluno.destroy()

    def consultarAluno(self):
        consultaAluno = simpledialog.askstring("Consultar Aluno", "Digite o CPF do aluno(a): ")
        textoConsultaAluno = ''

        if consultaAluno:
            for buscaAluno in self.listaAlunosCadastrados:
                if buscaAluno.cpf == consultaAluno:
                    textoConsultaAluno += "Aluno(a): " + buscaAluno.nome + '\n'
                    textoConsultaAluno += " - CPF: " + buscaAluno.cpf + '\n'
                    textoConsultaAluno += " - Email: " + buscaAluno.email + '\n'
                    textoConsultaAluno += " - Tipo de Aula: " + buscaAluno.tipoAula + '\n'
                    textoConsultaAluno += " - Professor: " + buscaAluno.nomeProfessor + '\n'
                    textoConsultaAluno += " - Nro Aulas: " + str(buscaAluno.nroAulas) + '\n'

                    valorAula = self.ctrlPrincipal.ctrlProfissional.getValorAulaProfissional(buscaAluno.tipoAula, buscaAluno.nomeProfessor)
                    if buscaAluno.nroAulas == '3':
                        valorAula = valorAula * 1.4
                    if buscaAluno.nroAulas == '4':
                        valorAula = valorAula * 1.8
                    valorAula = valorAula * 1.5
                    textoConsultaAluno += " - Mensalidade: R$" + str(valorAula) + '\n'
                    
                    self.limiteConsultaAluno = LimiteConsultaAluno(textoConsultaAluno)
                    return
                
            messagebox.showwarning("Erro Aluno", "Erro: Aluno(a) não encontrado(a)")

    def listarAluno(self):
        listaAlunos = 'Lista de Alunos\n\n'
        for aluno in self.listaAlunosCadastrados:
            listaAlunos += "Aluno(a): " + aluno.nome + '\n'
            listaAlunos += " - CPF: " + aluno.cpf + '\n'
            listaAlunos += " - Email: " + aluno.email + '\n'
            listaAlunos += " - Tipo de Aula: " + aluno.tipoAula + '\n'
            listaAlunos += " - Professor(a): " + aluno.nomeProfessor + '\n'
            listaAlunos += " - Nro Aulas: " + str(aluno.nroAulas) + '\n'
        self.limiteLista = LimiteListaAlunos(listaAlunos)