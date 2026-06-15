import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import simpledialog

class Comanda():
    def __init__(self, nroComanda):
        self.__nroComanda = nroComanda
        self.__produtosComanda = {}

    @property
    def nroComanda(self):
        return self.__nroComanda
    @property
    def produtosComanda(self):
        return self.__produtosComanda
    
class LimiteCriaCupom(tk.Toplevel):
    def __init__(self, controle, listaDescricaoProdutos):
        tk.Toplevel.__init__(self)
        self.geometry('500x300')
        self.title("Cupom Fiscal")
        self.controle = controle

        self.frameNroComanda = tk.Frame(self)
        self.frameProdutoComanda = tk.Frame(self)
        self.frameQuantidadeProduto = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        self.frameNroComanda.pack()
        self.frameProdutoComanda.pack()
        self.frameQuantidadeProduto.pack()
        self.frameButton.pack()        

        #Preenchimento Nro Comanda
        self.labelComanda = tk.Label(self.frameNroComanda, text="Numero Comanda:", width=15, anchor="w")  #width: Largura fixa, anchor: alinhado à esquerda
        self.labelComanda.pack(side="left", padx=5)
        self.inputComanda = tk.Entry(self.frameNroComanda, width=25)
        self.inputComanda.pack(side="left", padx=5)

        #Preenchimento Produto Escolhido
        self.labelProdutoComanda = tk.Label(self.frameProdutoComanda,text="Produto: ", width=10, anchor="w")
        self.labelProdutoComanda.pack(side="left")
        self.escolhaComboProdutoComanda = tk.StringVar()
        self.comboboxProdutoComanda = ttk.Combobox(self.frameProdutoComanda, width = 25 , textvariable = self.escolhaComboProdutoComanda)
        self.comboboxProdutoComanda.pack(side="left", padx=5)
        self.comboboxProdutoComanda['values'] = listaDescricaoProdutos

        #Preenchimento Quantidade Produto Escolhido
        self.labelQuantidadeProduto = tk.Label(self.frameQuantidadeProduto, text="Quantidade Produto:", width=20, anchor="w") 
        self.labelQuantidadeProduto.pack(side="left", padx=5)
        self.inputQuantidadeProduto = tk.Entry(self.frameQuantidadeProduto, width=25)
        self.inputQuantidadeProduto.pack(side="left", padx=5)

        self.buttonSubmit = tk.Button(self.frameButton ,text="Cadastrar")
        self.buttonSubmit.pack(side="left", pady=5)
        self.buttonSubmit.bind("<Button>", controle.enterHandler)
      
        self.buttonClear = tk.Button(self.frameButton ,text="Limpar")   
        self.buttonClear.pack(side="left", pady=5)
        self.buttonClear.bind("<Button>", controle.clearHandler)

        self.buttonFecha = tk.Button(self.frameButton ,text="Fechar") 
        self.buttonFecha.pack(side="left", pady=5)
        self.buttonFecha.bind("<Button>", controle.fechaHandler)

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)    

class LimiteConsultaComanda(tk.Toplevel):
    def __init__(self, textoComanda):
        messagebox.showinfo('Comanda Consultada', textoComanda)

#class LimiteMostraCupom():
#    def __init__(self, str):
#        messagebox.showinfo('Lista de Cupons', str)

class CtrlComanda():
    def __init__(self, controlePrincipal):
        self.ctrlPrincipal = controlePrincipal
        self.listaComandasCriadas = []

    def cadastrarComanda(self):
        self.listaProdutosCupom = []
        listaDescricaoProdutos = self.ctrlPrincipal.ctrlProduto.getListaDescricaoProdutos()
        self.limiteInsercaoComanda = LimiteCriaCupom(self, listaDescricaoProdutos)

    def enterHandler(self, event):
        nroComanda = self.limiteInsercaoComanda.inputComanda.get()
        produto = self.limiteInsercaoComanda.escolhaComboProdutoComanda.get()
        quantidadeProduto = self.limiteInsercaoComanda.inputQuantidadeProduto.get()

        if nroComanda == "" or produto == "" or quantidadeProduto == "":
            messagebox.showwarning("Erro Comanda", "Erro: Preencha todos os campos.")
            return
        
        listaProdutos = self.ctrlPrincipal.ctrlProduto.getListaProdutos()

        sinal = 0
        for buscaComanda in self.listaComandasCriadas:
            if nroComanda == buscaComanda.nroComanda:
                sinal = 1
        
        if sinal == 0:
            comandaCadastrada = Comanda(nroComanda)
            self.listaComandasCriadas.append(comandaCadastrada)
        
        for buscaComanda in self.listaComandasCriadas:
            if buscaComanda.nroComanda == nroComanda:
                for product in listaProdutos:
                    if produto == product.descricao: 
                        if product not in buscaComanda.produtosComanda: #alterar o product para product.codigo
                            buscaComanda.produtosComanda[product.codigo] = {
                                    "descricao": product.descricao,
                                    "quantidadeProduto": int(quantidadeProduto),
                                    "precoTotalProduto": int(product.valorUnitario * quantidadeProduto) #alterar para float(product.valorUnitario) * int(quantidadeProduto)
                                }
                        else:
                            buscaComanda.produtosComanda[product.codigo]["quantidadeProduto"] += int(quantidadeProduto)
                            buscaComanda.produtosComanda[product.codigo]["precoTotalProduto"] += float(product.valorUnitario) * int(quantidadeProduto)
                        
        self.limiteInsercaoComanda.mostraJanela('Sucesso', 'Comanda(a) atualizada(a) com sucesso')
        self.clearHandler(event)

    def clearHandler(self, event):
        self.limiteInsercaoComanda.inputComanda.delete(0, len(self.limiteInsercaoComanda.inputComanda.get()))
        self.limiteInsercaoComanda.escolhaComboProdutoComanda.set(value='')
        self.limiteInsercaoComanda.inputQuantidadeProduto.delete(0, len(self.limiteInsercaoComanda.inputQuantidadeProduto.get()))

    def fechaHandler(self, event):
        self.limiteInsercaoComanda.destroy()

    def imprimirComanda(self):
        consultaNroComanda = simpledialog.askstring("Consultar Comanda", "Digite o código da comanda: ")
        textoComanda = ''
        if consultaNroComanda:
            for comanda in self.listaComandasCriadas:
                if consultaNroComanda == comanda.nroComanda:
                    textoComanda = f"Comanda: {comanda.nroComanda}\n"
                    textoComanda += "Produtos Inseridos:\n"
                    textoComanda += "Codigo | Descrição | Quant. | Total\n"
                    valorTotalComanda = 0

                    for codigoProduto, dadosProduto in comanda.produtosComanda.items():
                        textoComanda += f"{codigoProduto:<11} | {dadosProduto['descricao']:<13} | {dadosProduto['quantidadeProduto']:<10} | R$ {dadosProduto['precoTotalProduto']:.2f}\n"
                        valorTotalComanda += int(dadosProduto["precoTotalProduto"])
                    
                    textoComanda += "Valor Total: R$ " + str(valorTotalComanda) + '\n'
                    self.limiteConsulta = LimiteConsultaComanda(textoComanda)
                    return
                
            messagebox.showwarning("Erro Consulta", "Erro: Digite uma comanda existente.")
            return




