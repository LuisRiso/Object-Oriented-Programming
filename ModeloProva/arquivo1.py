#Aluna: Camily Victal Finamor
#Matricula: 2024001197

import tkinter as tk
from tkinter import messagebox
from tkinter.ttk import Combobox

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#CLASSE MODEL
class MODELO:
    def __init__(self, atributo1, atributo2, atributo3, atributo4, atributo5, atributo6):
        self.__atributo1 = atributo1
        self.__atributo2 = atributo2
        self.__atributo3 = atributo3
        self.__atributo4 = atributo4
        self.__atributo5 = atributo5
        self.__atributo6 = atributo6

    @property
    def atributo1(self):
        return self.__atributo1
    
    @property
    def atributo2(self):
        return self.__atributo2
    
    @property
    def atributo3(self):
        return self.__atributo3
    
    @property
    def atributo4(self):
        return self.__atributo4
    
    @property
    def atributo5(self):
        return self.__atributo5
    
    @property
    def atributo6(self):
        return self.__atributo6

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#VIEW DA FUNÇÃO 1 (geralmente view de cadastrar)
class ViewCadastrar(tk.Toplevel):
    def __init__(self, controlador):
        tk.Toplevel.__init__(self)
        self.controlador = controlador
        self.geometry('300x250')
        self.title('-TITULO-DA-JANELA-')
    
        #AQUI VEM OS FRAMES, LABELS, COMBOBOX E DEMAIS WIDGETS
        self.framebotao = tk.Frame(self)
        self.framebotao.pack()

        self.botaoCadastrar = tk.Button(self.framebotao, text='Cadastrar', command=self.controlador.salvarFuncao)
        self.botaoCadastrar.pack(side='left',pady=5, padx=5)
        self.botaoClear = tk.Button(self.framebotao, text='Limpar', command=self.controlador.limparCampos)
        self.botaoClear.pack(side='left', pady=5)

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#VIEW DA FUNÇÃO 2 (geralmente view de consultar)
class ViewConsultar(tk.Toplevel):
    def __init__(self, controlador):
        tk.Toplevel.__init__(self)
        self.controlador = controlador
        self.geometry('300x250')
        self.title('-TITULO-DA-JANELA-')

        #AQUI VEM OS FRAMES, LABELS, COMBOBOX E DEMAIS WIDGETS
        self.framebotao = tk.Frame(self)
        self.framebotao.pack()

        self.botaoconsulta = tk.Button(self.framebotao, text='Consultar', command= self.controlador.procurarFuncao)
        self.botaoconsulta.pack(side='left')
        self.botaolimpa = tk.Button(self.framebotao, text='Limpar', command=self.controlador.limparCampoConsulta)
        self.botaolimpa.pack(side='left')

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#VIEW MOSTRAR (geralmente é uma classe q recebe uma mensagem pra chamar uma messagebox para listar as consultas)
class ViewMostrar:
    def __init__(self, mensagem):
        messagebox.showinfo('-TITULO-DA-MESSAGEBOX-', mensagem)

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#CONTROLADOR ARQUIVO1
class ControladorArquivo1:
    def __init__(self, controladorPrincipal):
        self.controladorPrincipal = controladorPrincipal
        self.listaDEOBJETOSDOCONTEXTO = []
    
    def NomedaFunçao1(self): #definindo as funções que são chamadas no controlador principal da main e que inicializaam as views de cada arquvio, ou seja, as janelas secundárias
        self.ViewCadastrar = ViewCadastrar(self) #caso precise de uma combobox na view de uma lista do arquivo2, chama o controlador principal do arquivo2 com a função get e passa aqui na view depois do self

    def NomedaFunçao2(self):
        self.ViewConsultar = ViewConsultar(self)

    def salvarFuncao(self):
        #geralmente a primeira coisa a ser feita é os gets dos atributos atraves dos imputs e combobox
        #depois vem o if not atributos para validar
        pass

    def procurarFuncao(self):
        #geralmente a primeira coisa a ser feita é os gets dos atributos atraves dos imputs e combobox
        #depois vem o if not atributos para validar
        self.mostrar = ViewMostrar(mensagem)
        pass

    def getObjetodaLista(self, atributo):
        for objeto in self.listaDEOBJETOSDOCONTEXTO:
            if objeto.atributo == atributo:
                return objeto
            
    def getLista(self):
        lista = []
        for objeto in self.listaDEOBJETOSDOCONTEXTO:
            lista.append(objeto)
        return lista

    def limparCampoConsulta(self):
        self.ViewConsultar.nomedowidget.delete(0, tk.END)

    def limparCampos(self):
        self.ViewCadastrar.nomedowidget.delete(0, tk.END)
        