import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog

class Produto():
    def __init__(self, codigo, valorUnitario, descricao):
        self.__codigo = codigo
        self.__valorUnitario = valorUnitario
        self.__descricao = descricao

    @property
    def codigo(self):
        return self.__codigo
    @property
    def valorUnitario(self):
        return self.__valorUnitario
    @property
    def descricao(self):
        return self.__descricao
    
class LimiteInsereProduto(tk.Toplevel):
    def __init__(self, controle):
        tk.Toplevel.__init__(self)
        self.geometry('250x100')
        self.title("Produto")
        self.controle = controle

        self.frameCodigo = tk.Frame(self)
        self.frameValor = tk.Frame(self)
        self.frameDescricao = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        self.frameCodigo.pack()
        self.frameValor.pack()
        self.frameDescricao.pack()
        self.frameButton.pack()

        self.labelCodigo = tk.Label(self.frameCodigo,text="Codigo: ")
        self.labelValor = tk.Label(self.frameValor,text="Valor Unitario: ")
        self.labelDescricao = tk.Label(self.frameDescricao,text="Descricao: ")
        self.labelCodigo.pack(side="left")
        self.labelValor.pack(side="left")  
        self.labelDescricao.pack(side="left")  

        self.inputCodigo = tk.Entry(self.frameCodigo, width=20)
        self.inputCodigo.pack(side="left")
        self.inputValorUnitario = tk.Entry(self.frameValor, width=20)
        self.inputValorUnitario.pack(side="left")
        self.inputDescricao = tk.Entry(self.frameDescricao, width=20)
        self.inputDescricao.pack(side="left")

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

class LimiteConsultaProduto():
    def __init__(self, str):
        messagebox.showinfo('Produto Consultado', str)

class LimiteListaProduto():
    def __init__(self, str):
        messagebox.showinfo('Lista de Produtos', str)

class CtrlProduto():
    def __init__(self):
        self.listaProdutos = []
        self.codigosCadastrados = set()

    def getProduto(self, codigo):
        prod = None
        for product in self.listaProdutos:
            if product.codigo == codigo:
                prod = product
        return prod

    def getListaCodigosProdutos(self):
        listaCodigosProdutos = []
        for product in self.listaProdutos:
            listaCodigosProdutos.append(product.codigo)
        return listaCodigosProdutos

    def inserirProduto(self):
        self.limiteInsercao = LimiteInsereProduto(self) 

    def consultarProduto(self):
        consultaCodigo = simpledialog.askstring("Consultar Produto", "Digite o código do produto: ")
        codigoProduto = ''
        if consultaCodigo:
            for product in self.listaProdutos:
                if product.codigo == consultaCodigo:
                    codigoProduto += "Código: " + product.codigo + '\n' + "Descrição: " + product.descricao + '\n' + "Valor Unitário: R$" + product.valorUnitario + '\n'
                    self.limiteConsulta = LimiteConsultaProduto(codigoProduto)
                    return
            codigoProduto += "Digite um código que já esteja cadastrado" + '\n'
            self.limiteConsulta = LimiteConsultaProduto(codigoProduto)

    def listarProduto(self):
        str = 'Codigo. -- Valor -- Descricao\n'
        for product in self.listaProdutos:
            str += product.codigo + ' -- ' + "R$" + product.valorUnitario + ' -- ' + product.descricao + '\n'
        self.limiteLista = LimiteListaProduto(str)

    def enterHandler(self, event):
        codigo = self.limiteInsercao.inputCodigo.get()
        valor = self.limiteInsercao.inputValorUnitario.get()
        descricao = self.limiteInsercao.inputDescricao.get()

        if codigo == "":
            self.limiteInsercao.mostraJanela('Erro Código Produto', 'Erro: insira um codigo para o produto')
            return

        # Validação de numerica do valor
        valor = valor.replace(',', '.')
        try:
            valor = float(valor)  # Converte o valor para float
        except ValueError:
            self.limiteInsercao.mostraJanela('Erro', 'O valor unitário deve ser numérico. Use vírgulas ou pontos.')
            return

        if codigo in self.codigosCadastrados:
            self.limiteInsercao.mostraJanela('Erro Código Produto', 'Erro: insira um codigo que não esteja sendo utilizado')
            self.clearHandler(event)
            return
        else:
            valor = str(valor)
            produto = Produto(codigo, valor, descricao)
            self.codigosCadastrados.add(codigo)
            self.listaProdutos.append(produto)
            self.limiteInsercao.mostraJanela('Sucesso', 'Produto cadastrado com sucesso')
            self.clearHandler(event)

    def clearHandler(self, event):
        self.limiteInsercao.inputCodigo.delete(0, len(self.limiteInsercao.inputCodigo.get()))
        self.limiteInsercao.inputValorUnitario.delete(0, len(self.limiteInsercao.inputValorUnitario.get()))
        self.limiteInsercao.inputDescricao.delete(0, len(self.limiteInsercao.inputDescricao.get()))

    def fechaHandler(self, event):
        self.limiteInsercao.destroy()