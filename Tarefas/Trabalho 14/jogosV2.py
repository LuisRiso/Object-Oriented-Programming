import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import simpledialog
import os.path
import pickle

class ErroCadastroCampos(Exception):
    pass

class ErroCodigoDuplicado(Exception):
    pass

class ErroTituloDuplicado(Exception):
    pass

class ErroCodigoAvaliacao(Exception):
    pass

class Jogo():
    def __init__(self, codigo, titulo, console, genero, preco, notaAvaliacoes):
        self.__codigo = codigo
        self.__titulo = titulo
        self.console = console
        self.genero = genero
        self.preco = preco
        self.__avaliacoes = []
        self.__notaAvaliacoes = notaAvaliacoes
    
    @property
    def codigo(self):
        return self.__codigo

    @property
    def titulo(self):
        return self.__titulo
    
    @property
    def console(self):
        return self.__console
    @console.setter
    def console(self, valor):
        self.consoles = ['XBox', 'PlayStation', 'Switch', 'PC']
        if valor == "":
            raise ValueError("Console não pode ser vazio")
        if not valor in self.consoles:
            raise ValueError("Console inválido: {}".format(valor))
        else:
            self.__console = valor

    @property
    def genero(self):
        return self.__genero
    @genero.setter
    def genero(self, valor):
        self.generos = ['Ação', 'Aventura', 'Estratégia', 'RPG', 'Esporte', 'Simulação']
        if valor == "":
            raise ValueError("Gênero não pode ser vazio")
        if not valor in self.generos:
            raise ValueError("Gênero inválido: {}".format(valor))
        else:
            self.__genero = valor

    @property
    def preco(self):
        return self.__preco
    @preco.setter
    def preco(self, valor):
        if valor == "":
            raise ValueError("Preço não pode ser vazio")
        valor = float(valor)
        if valor <= 0:
                raise ValueError("Erro Preco: O preço não pode ser negativo.")
        elif valor >= 500:
                raise ValueError("Erro Preco: O preço deve ser menor do que R$500,00.")
        else:
            self.__preco = valor

    @property
    def avaliacoes(self):
        return self.__avaliacoes
    
    @property
    def notaAvaliacoes(self):
        return self.__notaAvaliacoes
    
    def calculaMedia(self):
        if not self.__avaliacoes:
            self.__notaAvaliacoes = 1
            print('Média: {}'.format(self.__notaAvaliacoes))
        mediaAvaliacoes = sum(self.__avaliacoes) / len(self.__avaliacoes)
        self.__notaAvaliacoes = int(mediaAvaliacoes) + (1 if mediaAvaliacoes % 1 != 0 else 0)
        #print('Média: {}'.format(self.__notaAvaliacoes))
    
    def getJogo(self):
        return "Codigo: " + str(self.codigo)\
        + "\nTitulo: " + str(self.titulo)\
        + "\nConsole: " + str(self.console)\
        + "\nGênero: " + str(self.genero)\
        + "\nPreco: R$" + str(self.preco)
    
    
class LimiteInsireJogo(tk.Toplevel):
    def __init__(self, controle):
        tk.Toplevel.__init__(self)
        self.geometry('400x200')
        self.title("Cadastrar Jogo")
        self.controle = controle

        self.frameCodigo = tk.Frame(self)
        self.frameTitulo = tk.Frame(self)
        self.frameConsole = tk.Frame(self)
        self.frameGenero = tk.Frame(self)
        self.framePreco = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        self.frameCodigo.pack()
        self.frameTitulo.pack()
        self.frameConsole.pack()
        self.frameGenero.pack()
        self.framePreco.pack()
        self.frameButton.pack()

        #Preenchimento Manual
        self.labelCodigo = tk.Label(self.frameCodigo, text="Codigo:", width=6, anchor="w")  #width: Largura fixa, anchor: alinhado à esquerda
        self.labelCodigo.pack(side="left", padx=5)
        self.inputCodigo = tk.Entry(self.frameCodigo, width=25)
        self.inputCodigo.pack(side="left", padx=5)

        self.labelTitulo = tk.Label(self.frameTitulo, text="Título:", width=6, anchor="w")
        self.labelTitulo.pack(side="left", padx=5)
        self.inputTitulo = tk.Entry(self.frameTitulo, width=25)
        self.inputTitulo.pack(side="left", padx=5)

        self.labelConsole = tk.Label(self.frameConsole, text="Console:", width=6, anchor="w") 
        self.labelConsole.pack(side="left", padx=5)
        self.inputConsole = tk.Entry(self.frameConsole, width=25)
        self.inputConsole.pack(side="left", padx=5)

        self.labelGenero = tk.Label(self.frameGenero, text="Gênero:", width=6, anchor="w")
        self.labelGenero.pack(side="left", padx=5)
        self.inputGenero = tk.Entry(self.frameGenero, width=25)
        self.inputGenero.pack(side="left", padx=5)

        self.labelPreco = tk.Label(self.framePreco, text="Preço:", width=6, anchor="w")
        self.labelPreco.pack(side="left", padx=5)
        self.inputPreco = tk.Entry(self.framePreco, width=25)
        self.inputPreco.pack(side="left", padx=5)

        self.buttonSubmit = tk.Button(self.frameButton ,text="Cadastrar")
        self.buttonSubmit.pack(side="left", pady=5)
        self.buttonSubmit.bind("<Button>", controle.cadastraHandler)
      
        self.buttonClear = tk.Button(self.frameButton ,text="Limpar")   
        self.buttonClear.pack(side="left", pady=5)
        self.buttonClear.bind("<Button>", controle.clearInsereHandler)

        self.buttonFecha = tk.Button(self.frameButton ,text="Fechar") 
        self.buttonFecha.pack(side="left", pady=5)
        self.buttonFecha.bind("<Button>", controle.fechaInsereHandler)

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)

class LimiteAvaliaJogo(tk.Toplevel):
    def __init__(self, controle):
        tk.Toplevel.__init__(self)
        self.geometry('400x200')
        self.title("Avaliar Jogo")
        self.controle = controle

        self.frameCodigo = tk.Frame(self)
        self.frameCodigo.pack()
        self.frameAvaliacao = tk.Frame(self)
        self.frameAvaliacao.pack()
        self.frameButton = tk.Frame(self)
        self.frameButton.pack()

        #Insere Codigo
        self.labelCodigo = tk.Label(self.frameCodigo,text="Codigo: ")
        self.labelCodigo.pack(side="left")
        self.inputCodigo = tk.Entry(self.frameCodigo, width=25)
        self.inputCodigo.pack(side="left")

        #Insere Nota
        self.labelAvaliacao = tk.Label(self.frameAvaliacao,text="Nota Jogo: ")
        self.labelAvaliacao.pack(side="left")
        self.escolhaComboAvaliacao = tk.StringVar()
        self.comboboxAvaliacao = ttk.Combobox(self.frameAvaliacao, width = 20 , textvariable = self.escolhaComboAvaliacao)
        self.comboboxAvaliacao.pack(side="left")
        self.comboboxAvaliacao['values'] = [1, 2, 3, 4, 5]

        self.buttonSubmit = tk.Button(self.frameButton ,text="Avaliar")
        self.buttonSubmit.pack(side="left", pady=10)
        self.buttonSubmit.bind("<Button>", controle.avaliaHandler)

        self.buttonFecha = tk.Button(self.frameButton ,text="Fechar") 
        self.buttonFecha.pack(side="left", pady=10)
        self.buttonFecha.bind("<Button>", controle.fechaAvaliaHandler)
    
    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)

class LimiteContultaJogo(tk.Toplevel):
    def __init__(self, controle):
        tk.Toplevel.__init__(self)
        self.geometry('400x400')
        self.title("Avaliar Jogo")
        self.controle = controle

        #Escolha da Nota para Exibit os Jogos
        self.frameComboAvaliacao = tk.Frame(self)
        self.frameComboAvaliacao.pack(pady=3)
        self.labelAvaliacao = tk.Label(self.frameComboAvaliacao,text="Nota Jogo: ")
        self.labelAvaliacao.pack(side="left")
        self.escolhaComboAvaliacao = tk.StringVar()
        self.comboboxAvaliacao = ttk.Combobox(self.frameComboAvaliacao, width = 20 , textvariable = self.escolhaComboAvaliacao)
        self.comboboxAvaliacao.pack(side="left")
        self.comboboxAvaliacao['values'] = [1, 2, 3, 4, 5]
        self.comboboxAvaliacao.bind("<<ComboboxSelected>>", controle.mostrarJogos)

        #Caixa de Exibição dos Jogos
        self.frameJogos = tk.Frame(self)
        self.frameJogos.pack()
        self.textJogos = tk.Text(self.frameJogos, height=20,width=30)
        self.textJogos.pack()
        self.textJogos.config(state=tk.DISABLED)

        self.frameButton = tk.Frame(self)
        self.frameButton.pack()
        self.buttonFecha = tk.Button(self.frameButton ,text="Fechar") 
        self.buttonFecha.pack(side="left", pady=10)
        self.buttonFecha.bind("<Button>", controle.fechaConsultaHandler)

#class LimiteListaJogos():
#    def __init__(self, textoLista):
#        messagebox.showinfo('Lista de Jogos', textoLista)

class CtrlJogo():
    def __init__(self):
        if not os.path.isfile("jogos.pickle"):
            self.listaJogosCadastrados = []
        else:
            with open("jogos.pickle", "rb") as f:
                self.listaJogosCadastrados = pickle.load(f)

    def salvarJogos(self):
        if len(self.listaJogosCadastrados) != 0:
            with open("jogos.pickle", "wb") as f:
                pickle.dump(self.listaJogosCadastrados, f)      

    def inserirJogo(self):
        self.limiteInsercaoJogo = LimiteInsireJogo(self)

    def avaliarJogo(self):
        self.limiteAvaliacaoJogo = LimiteAvaliaJogo(self)

    def consultarJogo(self):
        self.limiteConsultaJogo = LimiteContultaJogo(self)

    #Funções Cadastro Jogo
    def cadastraHandler(self, event):
        codigo = self.limiteInsercaoJogo.inputCodigo.get()
        titulo = self.limiteInsercaoJogo.inputTitulo.get()
        console = self.limiteInsercaoJogo.inputConsole.get()
        genero = self.limiteInsercaoJogo.inputGenero.get()
        preco = self.limiteInsercaoJogo.inputPreco.get()
        try:
            if codigo == "" or titulo == "" or console == "" or genero == "" or preco == "":
                raise ErroCadastroCampos()
        except ErroCadastroCampos:
            messagebox.showwarning("Erro Profissional", "Erro Campos: Preencha todos os campos de cadastro")
            return
        
        preco = preco.replace(',', '.')
        try:
            preco = float(preco)  # Converte o valor para float
        except ValueError:
            messagebox.showwarning("Erro Jogo", "Erro Preco: O valor unitário deve ser numérico.")
            return
        try:
            for jogo in self.listaJogosCadastrados:
                if jogo.codigo == codigo:
                    raise ErroCodigoDuplicado()
                if jogo.titulo == titulo:
                    raise ErroTituloDuplicado()
        except ErroCodigoDuplicado:
            messagebox.showwarning("Erro Código", "Codigo já cadastrado: {}".format(codigo))
            return
        except ErroTituloDuplicado:
            messagebox.showwarning("Erro Código", "Codigo já cadastrado: {}".format(titulo))
            return
        
        try:
            jogo = Jogo(codigo, titulo, console, genero, preco, int(1))
            self.listaJogosCadastrados.append(jogo)            
            self.limiteInsercaoJogo.mostraJanela('Sucesso', 'Jogo cadastrado com sucesso')
            self.clearInsereHandler(event)
        except ValueError as error:
            self.limiteInsercaoJogo.mostraJanela('Erro', error)  

    def clearInsereHandler(self, event):
        self.limiteInsercaoJogo.inputCodigo.delete(0, len(self.limiteInsercaoJogo.inputCodigo.get()))
        self.limiteInsercaoJogo.inputTitulo.delete(0, len(self.limiteInsercaoJogo.inputTitulo.get()))
        self.limiteInsercaoJogo.inputConsole.delete(0, len(self.limiteInsercaoJogo.inputConsole.get()))
        self.limiteInsercaoJogo.inputGenero.delete(0, len(self.limiteInsercaoJogo.inputGenero.get()))
        self.limiteInsercaoJogo.inputPreco.delete(0, len(self.limiteInsercaoJogo.inputPreco.get()))

    def fechaInsereHandler(self, event):
        self.limiteInsercaoJogo.destroy()

    #Funções Avaliação Jogo
    def avaliaHandler(self, event):
        codigo = self.limiteAvaliacaoJogo.inputCodigo.get()
        nota = int(self.limiteAvaliacaoJogo.escolhaComboAvaliacao.get())
        try:
            for buscaCodigo in self.listaJogosCadastrados:
                if buscaCodigo.codigo == codigo:
                    buscaCodigo.avaliacoes.append(nota)
                    buscaCodigo.calculaMedia()
                    self.limiteAvaliacaoJogo.mostraJanela('Sucesso', 'Avaliacao feita com sucesso')
                    self.clearAvaliaHandler(event)
                    return
            raise ErroCadastroCampos()
        except ErroCadastroCampos:
            messagebox.showwarning("Erro Avaliacao", "Erro Codigo: Preencha um código ja cadastrado")
            return

    def clearAvaliaHandler(self, event):
        self.limiteAvaliacaoJogo.escolhaComboAvaliacao.set("")

    def fechaAvaliaHandler(self, event):
        self.limiteAvaliacaoJogo.destroy()

    def mostrarJogos(self, event):
        notaEscolhida = int(self.limiteConsultaJogo.comboboxAvaliacao.get())
        self.limiteConsultaJogo.textJogos.config(state='normal') 
        self.limiteConsultaJogo.textJogos.delete(index1='1.0', index2=tk.END)
        for buscaJogo in self.listaJogosCadastrados:
            if buscaJogo.notaAvaliacoes == notaEscolhida:
                jogoEncontrado = buscaJogo.getJogo()
                jogoEncontrado += "\n\n"
                self.limiteConsultaJogo.textJogos.insert(index=1.0, chars=jogoEncontrado)
        self.limiteConsultaJogo.textJogos.config(state='disabled')

    def fechaConsultaHandler(self, event):
        self.limiteConsultaJogo.destroy()
    
    #def listarJogo(self):
    #   textoLista = ""
    #    if not self.listaJogosCadastrados:
    #        textoLista += "Ainda não há jogos"
    #        self.limiteListaJogo = LimiteListaJogos(textoLista)
    #    else:
    #        for buscaJogo in self.listaJogosCadastrados:
    #            textoLista += buscaJogo.getJogo()
    #            textoLista += "\nAvaliações: "
    #            for buscaAvaliacaoJogo in buscaJogo.avaliacoes:
    #                textoLista += str(buscaAvaliacaoJogo) + ", "
    #            textoLista += "\n\n"
    #        self.limiteListaJogo = LimiteListaJogos(textoLista)
