import tkinter as tk
from tkinter import messagebox

class ModelCliente():
    def __init__(self, nome, email):
        self.__nome = nome
        self.__email = email

    @property
    def nome(self):
        return self.__nome

    @property
    def email(self):
        return self.__email

#master --> self.root recebido
#controller --> versão do controlador
class View():
    def __init__(self, master, controller):
        self.controller = controller #referencia na própria classe
        self.janela = tk.Frame(master) 
        self.janela.pack()
        self.frame1 = tk.Frame(self.janela)
        self.frame2 = tk.Frame(self.janela)
        self.frame1.pack()
        self.frame2.pack()
      
        self.labelInfo1 = tk.Label(self.frame1,text="Nome: ")
        self.labelInfo2 = tk.Label(self.frame2,text="Email: ")
        self.labelInfo1.pack(side="left")
        self.labelInfo2.pack(side="left")  

        self.inputText1 = tk.Entry(self.frame1, width=20)
        self.inputText1.pack(side="left")
        self.inputText2 = tk.Entry(self.frame2, width=20)
        self.inputText2.pack(side="left")             
      
        #Função de Callback --> sabe o que deve ser feito quando o usuário clicar
        #Essa função vai estar no controlador --> lá que o programa sabe o que fazer após o clique
        self.buttonSubmit = tk.Button(self.janela,text="Salva")  
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", controller.salvaHandler)
      
        self.buttonClear = tk.Button(self.janela,text="Limpa")      
        self.buttonClear.pack(side="left")
        self.buttonClear.bind("<Button>", controller.clearHandler)    

        self.buttonList = tk.Button(self.janela,text="Listar") 
        self.buttonList.pack(side="left")
        self.buttonList.bind("<Button>", controller.listaHandler)  

    def mostraJanela(self, titulo, mensagem):
        messagebox.showinfo(titulo, mensagem)
      
#serva para controlar a criação de clientes
#gerencia uma lista de clientes --> vai ser peenchida na View
class Controller():       
    def __init__(self):
        self.root = tk.Tk() #cria a janela principal (janela raiz)
        self.root.geometry('300x100') #tamanho da janela
        self.listaClientes = [] #gerencia uma lista de clientes que inicia vazia

        # Cria a view passando referência da janela principal e
        # de si próprio (controlador)
        self.view = View(self.root, self) #permite a "conversa" entre o controller o view
        #instancia a view e passa a instacia do controller para a view

        self.root.title("Exemplo MVC")
        # Inicia o mainloop
        self.root.mainloop()

    #usa o self.view para acessar os campos da view
    def salvaHandler(self, event):
        nomeCli = self.view.inputText1.get() 
        emailCli = self.view.inputText2.get()
        cliente = ModelCliente(nomeCli, emailCli) #criou uma instância de cliente --> objeto cliente resultante
        self.listaClientes.append(cliente) #apenda o novo objeto na lista de cliente
        self.view.mostraJanela('Sucesso', 'Cliente cadastrado com sucesso')
        self.clearHandler(event)

    def clearHandler(self, event):
        self.view.inputText1.delete(0, len(self.view.inputText1.get()))
        self.view.inputText2.delete(0, len(self.view.inputText2.get())) 
    
    def listaHandler(self, event):
        strClientes = ''
        for clientes in self.listaClientes:
            strClientes += clientes.nome + ' - ' + clientes.email + '\n'
        self.view.mostraJanela('Clientes', strClientes)
        

if __name__ == '__main__':
    c = Controller()