import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import simpledialog

class CupomFiscal():
    def __init__(self, nroCupom, itensCupom):
        self.__nroCupom = nroCupom
        self.__itensCupom = itensCupom

    @property
    def nroCupom(self):
        return self.__nroCupom
    @property
    def itensCupom(self):
        return self.__itensCupom
    
class LimiteCriaCupom(tk.Toplevel):
    def __init__(self, controle, listaCodigoProduct):
        tk.Toplevel.__init__(self)
        self.geometry('300x250')
        self.title("Cupom Fiscal")
        self.controle = controle

        self.frameCodigoCupom = tk.Frame(self)
        self.frameProduto = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        self.frameCodigoCupom.pack()
        self.frameProduto.pack()
        self.frameButton.pack()        

        self.labelCodigoCupom = tk.Label(self.frameCodigoCupom,text="Informe o código do cupom: ")
        self.labelCodigoCupom.pack(side="left")
        self.inputCodigoCupom = tk.Entry(self.frameCodigoCupom, width=20)
        self.inputCodigoCupom.pack(side="left")
          
        #feito por listabox
        self.labelProduto = tk.Label(self.frameProduto,text="Escolha o produto: ")
        self.labelProduto.pack(side="left") 
        self.listbox = tk.Listbox(self.frameProduto)
        self.listbox.pack(side="left")
        for codigo in listaCodigoProduct:
            self.listbox.insert(tk.END, codigo)


        self.buttonInsere = tk.Button(self.frameButton ,text="Inserir Produto")           
        self.buttonInsere.pack(side="left")
        self.buttonInsere.bind("<Button>", controle.inserirProduto)


        self.buttonCria = tk.Button(self.frameButton ,text="Cria Cupom")           
        self.buttonCria.pack(side="left")
        self.buttonCria.bind("<Button>", controle.criarCupom)

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)    

class LimiteConsultaCupom(tk.Toplevel):
    def __init__(self, str):
        messagebox.showinfo('Copum Consultado', str)

class LimiteMostraCupom():
    def __init__(self, str):
        messagebox.showinfo('Lista de Cupons', str)

class CtrlCupomFiscal():
    def __init__(self, controlePrincipal):
        self.ctrlPrincipal = controlePrincipal
        self.listaCuponsCriados = []
        self.nroCupomCadastrados = set()

    def cadastrarCupom(self):
        self.listaProdutosCupom = []
        listaCodigoProduct = self.ctrlPrincipal.ctrlProduto.getListaCodigosProdutos()
        self.limiteInsercaoCupom = LimiteCriaCupom(self, listaCodigoProduct)

    def criarCupom(self, event):
        codigoCupom = self.limiteInsercaoCupom.inputCodigoCupom.get()

        if codigoCupom == "":
            self.limiteInsercaoCupom.mostraJanela('Erro Código Cupom', 'Erro: insira um codigo para o cupom')
            return

        if codigoCupom in self.nroCupomCadastrados:
            self.limiteInsercaoCupom.mostraJanela('Erro Código Cupom', 'Erro: insira um codigo que não esteja sendo utilizado')
            return
        else:
            cupom = CupomFiscal(codigoCupom, self.listaProdutosCupom)
            self.nroCupomCadastrados.add(codigoCupom)
            self.listaCuponsCriados.append(cupom)
            self.limiteInsercaoCupom.mostraJanela('Sucesso', 'Cupom criado com sucesso')
            self.limiteInsercaoCupom.destroy()

    def inserirProduto(self, event):
        product = self.limiteInsercaoCupom.listbox.get(tk.ACTIVE)
        produto = self.ctrlPrincipal.ctrlProduto.getProduto(product)
        self.listaProdutosCupom.append(produto)
        self.limiteInsercaoCupom.mostraJanela('Sucesso', 'Produto inserido')

    def consultarCupom(self):
        consultaNroCupom = simpledialog.askstring("Consultar Cupom", "Digite o código do cupom: ")
        codigoCupom = ''
        if consultaNroCupom:

            for cupom in self.listaCuponsCriados:
                if cupom.nroCupom == consultaNroCupom:

                    agruparProdutos = {}
                    for produto in cupom.itensCupom:
                        if produto.codigo not in agruparProdutos:
                            agruparProdutos[produto.codigo] = {
                                "descricao": produto.descricao,
                                "quantidadeProduto": 1,
                                "precoTotalProduto": float(produto.valorUnitario),
                                "valorUnitario": produto.valorUnitario
                            }
                        else:
                            agruparProdutos[produto.codigo]["quantidadeProduto"] += 1
                            agruparProdutos[produto.codigo]["precoTotalProduto"] += float(produto.valorUnitario)

                    codigoCupom = f"Cupom: {cupom.nroCupom}\n"
                    codigoCupom += "Produtos Inseridos:\n"
                    codigoCupom += "Código | Descrição | Quant. | Total\n"
                    valorTotalCupom = 0

                    for codigoProduto, dadosProduto in agruparProdutos.items():
                        codigoCupom += f"{codigoProduto:<11} | {dadosProduto['descricao']:<13} | {dadosProduto['quantidadeProduto']:<10} | R$ {dadosProduto['precoTotalProduto']:.2f}\n"
                        valorTotalCupom += float(dadosProduto["precoTotalProduto"])
                    
                    codigoCupom += f"Valor Total: R$ {valorTotalCupom:.2f}"
                    self.limiteConsulta = LimiteConsultaCupom(codigoCupom)
                    return
                
            codigoCupom += "Digite um código que já esteja cadastrado" + '\n'
            self.limiteConsulta = LimiteConsultaCupom(codigoCupom)

    def listarCupom(self):
        str = ''
        for cupom in self.listaCuponsCriados:
            str += 'Código: ' +  cupom.nroCupom + '\n'
            str += 'Produtos:\n'
            for product in cupom.itensCupom:
                str += product.codigo + ' - R$' + product.valorUnitario + ' - ' + product.descricao + '\n'
            str += '---------------\n'
        self.limiteListaCupom = LimiteMostraCupom(str)

