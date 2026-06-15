import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog

class Profissional:
    def __init__(self, nome, cpf, email, aulaPilates, aulaFuncional):
        self.__nome = nome
        self.__cpf = cpf
        self.__email = email
        self.__aulaPilates = aulaPilates
        self.__aulaFuncional = aulaFuncional
        self.__alunoMatriculados = []

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
    def aulaPilates(self):
        return self.__aulaPilates
    @property
    def aulaFuncional(self):
        return self.__aulaFuncional
    @property
    def alunoMatriculados(self):
        return self.__alunoMatriculados

class LimiteInsereProfissional(tk.Toplevel):
    def __init__(self, controle):
        tk.Toplevel.__init__(self)
        self.geometry('400x200')
        self.title("Cadastrar Profissional")
        self.controle = controle

        self.frameNome = tk.Frame(self)
        self.frameCPF = tk.Frame(self)
        self.frameEmail = tk.Frame(self)
        self.frameAulaPilates = tk.Frame(self)
        self.frameAulaFuncional = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        self.frameNome.pack()
        self.frameCPF.pack()
        self.frameEmail.pack()
        self.frameAulaPilates.pack()
        self.frameAulaFuncional.pack()
        self.frameButton.pack()

        self.labelNome = tk.Label(self.frameNome,text="Nome: ")
        self.labelCPF = tk.Label(self.frameCPF,text="CPF: ")
        self.labelEmail = tk.Label(self.frameEmail,text="Email: ")
        self.labelAulaPilates = tk.Label(self.frameAulaPilates,text="Valor Pilates: ")
        self.labelAulaFuncional = tk.Label(self.frameAulaFuncional,text="Valor Funcional: ")
        self.labelNome.pack(side="left")
        self.labelCPF.pack(side="left")  
        self.labelEmail.pack(side="left")  
        self.labelAulaPilates.pack(side="left")  
        self.labelAulaFuncional.pack(side="left")  

        self.inputNome = tk.Entry(self.frameNome, width=20)
        self.inputNome.pack(side="left")
        self.inputCPF = tk.Entry(self.frameCPF, width=20)
        self.inputCPF.pack(side="left")
        self.inputEmail = tk.Entry(self.frameEmail, width=20)
        self.inputEmail.pack(side="left")
        self.inputAulaPilates = tk.Entry(self.frameAulaPilates, width=20)
        self.inputAulaPilates.pack(side="left")
        self.inputAulaFuncional = tk.Entry(self.frameAulaFuncional, width=20)
        self.inputAulaFuncional.pack(side="left")

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

class LimiteFaturamentoProfessor():
    def __init__(self, textoFaturamento):
        messagebox.showinfo('Faturamento Professor', textoFaturamento)

class LimiteListaProfissional():
    def __init__(self, listaProfissionais):
        messagebox.showinfo('Lista de Profissionais', listaProfissionais)

class CtrlProfissional():
    def __init__(self):
        self.listaProfissionaisCadastrados = []

    def getValorAulaProfissional(self, tipoAula, nomeProfissional):
        if tipoAula == 'Pilates':
            for buscaProfissional in self.listaProfissionaisCadastrados:
                if buscaProfissional.nome == nomeProfissional:
                    return buscaProfissional.aulaPilates
        else:
            for buscaProfissional in self.listaProfissionaisCadastrados:
                if buscaProfissional.nome == nomeProfissional:
                    return buscaProfissional.aulaFuncional

    def getListaNomesProfissionais(self):
        listaNomesProfissionais = []
        for buscaProfissional in self.listaProfissionaisCadastrados:
            listaNomesProfissionais.append(buscaProfissional.nome)
        return listaNomesProfissionais

    def adicionarAluno(self, alunoCadastrado):
        for buscaProfessor in self.listaProfissionaisCadastrados:
            if buscaProfessor.nome == alunoCadastrado.nomeProfessor:
                buscaProfessor.alunoMatriculados.append(alunoCadastrado)

    def inserirProfissional(self):
        self.limiteInsercaoProfissional = LimiteInsereProfissional(self) 

    def enterHandler(self, event):
        nome = self.limiteInsercaoProfissional.inputNome.get()
        cpf = self.limiteInsercaoProfissional.inputCPF.get()
        email = self.limiteInsercaoProfissional.inputEmail.get()
        valorPilates = self.limiteInsercaoProfissional.inputAulaPilates.get()
        valorFuncional = self.limiteInsercaoProfissional.inputAulaFuncional.get()

        if nome == "" or cpf == "" or email == "" or valorPilates == "" or valorFuncional == "":
            messagebox.showwarning("Erro Profissional", "Erro: Preencha todos os campos")
            return

        # Validação de numerica do valor
        valorPilates = valorPilates.replace(',', '.')
        valorFuncional = valorFuncional.replace(',', '.')
        try:
            valorPilates = float(valorPilates)  # Converte o valor para float
            valorFuncional = float(valorFuncional)  # Converte o valor para float
        except ValueError:
            messagebox.showwarning("Erro Profissional", "Erro: O valor unitário deve ser numérico. Use vírgulas ou pontos.")
            return

        for buscaProfissional in self.listaProfissionaisCadastrados:
            if buscaProfissional.cpf == cpf:
                messagebox.showwarning("Erro Profissional", "Erro: CPF ja cadastrado.")
                self.limiteInsercaoProfissional.inputCPF.delete(0, len(self.limiteInsercaoProfissional.inputCPF.get()))
                return
        
        for buscaProfissional in self.listaProfissionaisCadastrados:
            if buscaProfissional.email == email:
                messagebox.showwarning("Erro Profissional", "Erro: E-mail ja cadastrado.")
                self.limiteInsercaoProfissional.inputEmail.delete(0, len(self.limiteInsercaoProfissional.inputEmail.get()))
                return
        
        cadastroProfissional = Profissional(nome, cpf, email, valorPilates, valorFuncional)
        self.listaProfissionaisCadastrados.append(cadastroProfissional)
        self.limiteInsercaoProfissional.mostraJanela('Sucesso', 'Profissional cadastrado com sucesso')
        self.clearHandler(event)

    def clearHandler(self, event):
        self.limiteInsercaoProfissional.inputNome.delete(0, len(self.limiteInsercaoProfissional.inputNome.get()))
        self.limiteInsercaoProfissional.inputCPF.delete(0, len(self.limiteInsercaoProfissional.inputCPF.get()))
        self.limiteInsercaoProfissional.inputEmail.delete(0, len(self.limiteInsercaoProfissional.inputEmail.get()))
        self.limiteInsercaoProfissional.inputAulaPilates.delete(0, len(self.limiteInsercaoProfissional.inputAulaPilates.get()))
        self.limiteInsercaoProfissional.inputAulaFuncional.delete(0, len(self.limiteInsercaoProfissional.inputAulaFuncional.get()))

    def fechaHandler(self, event):
        self.limiteInsercaoProfissional.destroy()

    def listarProfissional(self):
        listaProfissionais = 'Lista de Profissionais\n\n'
        for profissional in self.listaProfissionaisCadastrados:
            listaProfissionais += "Profissional: " + profissional.nome + '\n'
            listaProfissionais += " - CPF: " + profissional.cpf + '\n'
            listaProfissionais += " - Email: " + profissional.email + '\n'
            listaProfissionais += " - R$" + str(profissional.aulaPilates) + '\n'
            listaProfissionais += " - R$" + str(profissional.aulaFuncional) + '\n'
        self.limiteLista = LimiteListaProfissional(listaProfissionais)
    
    def faturamentoProfissional(self):
        consultaProfissional = simpledialog.askstring("Consultar Profissional", "Digite o CPF do professor: ")
        textoConsultaProfessor = ''
        pilates = 0
        funcional = 0
        if consultaProfissional:
            for buscaProfissional in self.listaProfissionaisCadastrados:
                if buscaProfissional.cpf == consultaProfissional:
                    textoConsultaProfessor += 'Profissional: ' + buscaProfissional.nome + '\n'
                    for aluno in buscaProfissional.alunoMatriculados:
                        if aluno.tipoAula == 'Pilates':
                            if aluno.nroAulas == '2':
                                pilates += buscaProfissional.aulaPilates
                            if aluno.nroAulas == '3':
                                pilates += buscaProfissional.aulaPilates * 1.4
                            if aluno.nroAulas == '4':
                                pilates += buscaProfissional.aulaPilates * 1.8
                        else:
                            if aluno.nroAulas == '2':
                                funcional += buscaProfissional.aulaFuncional
                            if aluno.nroAulas == '3':
                                funcional += buscaProfissional.aulaFuncional * 1.4
                            if aluno.nroAulas == '4':
                                funcional += buscaProfissional.aulaFuncional * 1.8
                    textoConsultaProfessor += 'Valor Pilates: R$' + str(pilates) + '\n'
                    textoConsultaProfessor += 'Valor Funcional: R$' + str(funcional) + '\n'
                    
                    self.limiteFaturamentoProfessor = LimiteFaturamentoProfessor(textoConsultaProfessor)
                    return
            messagebox.showwarning("Erro Profissional", "Erro: Professor não encontrado")