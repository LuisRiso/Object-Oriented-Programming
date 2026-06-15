import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog

class Artista():
    def __init__(self, nomeArtista):
        self.__nomeArtista = nomeArtista
        self.__albuns = []
        self.__musicas = []

    @property
    def nomeArtista(self):
        return self.__nomeArtista
    @property
    def albuns(self):
        return self.__albuns
    @property
    def musicas(self):
        return self.__musicas
    
class LimiteInsereArtista(tk.Toplevel):
    def __init__(self, controle):
        tk.Toplevel.__init__(self)
        self.geometry('250x100')
        self.title("Cadastro Artista")
        self.controle = controle

        self.frameNome = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        self.frameNome.pack()
        self.frameButton.pack()

        #Obter o Nome do Artista
        self.labelNome = tk.Label(self.frameNome,text="Codigo: ")
        self.labelNome.pack(side="left")
        self.inputNome = tk.Entry(self.frameNome, width=20)
        self.inputNome.pack(side="left")

        #Botão de Cadastro
        self.buttonSubmit = tk.Button(self.frameButton ,text="Cadastrar")
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", controle.enterHandler)
      
        #Botão de Limpeza
        self.buttonClear = tk.Button(self.frameButton ,text="Limpar")   
        self.buttonClear.pack(side="left")
        self.buttonClear.bind("<Button>", controle.clearHandler)

        #Botão de Fechar a Janela
        self.buttonFecha = tk.Button(self.frameButton ,text="Fechar") 
        self.buttonFecha.pack(side="left")
        self.buttonFecha.bind("<Button>", controle.fechaHandler)

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)

class LimiteConsultaArtista():
    def __init__(self, textoConsulta):
        messagebox.showinfo('Lista de Artistas', textoConsulta)

#class LimiteListaArtista():
#    def __init__(self, textoLista):
#        messagebox.showinfo('Lista de Artistas', textoLista)

class CtrlArtista():
    def __init__(self):
        self.listaArtistasCadastrados = [
            Artista("Vários Artistas")
        ]

    def getArtistas(self, nomeArtista):
        artist = None
        for buscaArtista in self.listaArtistasCadastrados:
            if buscaArtista.nomeArtista == nomeArtista:
                artist = buscaArtista
        return artist

    def getMusicaArtistas(self, nomeArtista, nomeMusicaSelecionada):
        musicaSelecionada = None
        for buscaArtista in self.listaArtistasCadastrados:
            if buscaArtista.nomeArtista == nomeArtista:
                for buscaMusica in buscaArtista.musicas:
                    if buscaMusica.tituloMusica == nomeMusicaSelecionada:
                        musicaSelecionada = buscaMusica
        return musicaSelecionada

    #Função para Pegar Todos os Nomes de Artistas e Enviar para o Album
    def getListaNomeArtistas(self):
        listaNomeArtista = []
        for artista in self.listaArtistasCadastrados:
            listaNomeArtista.append(artista.nomeArtista)
        return listaNomeArtista

    #Função para Inserir um Album Criado na Lista de Albuns do Artista
    def adicionarAlbumArtista(self, albumArtista):
        for buscaArtista in self.listaArtistasCadastrados:
            if buscaArtista.nomeArtista == albumArtista.artista:
                buscaArtista.albuns.append(albumArtista)
                self.adicionarMusicaArtista(albumArtista)

    def adicionarMusicaArtista(self, albumArtista):
        for buscaArtista in self.listaArtistasCadastrados:
            if buscaArtista.nomeArtista == albumArtista.artista:
                for buscaMusica in albumArtista.faixas:
                    buscaArtista.musicas.append(buscaMusica)
                
    #Função para Iniciar a Criação do Artista
    def inserirArtista(self):
        self.limiteInsercaoArtista = LimiteInsereArtista(self) 

    #Função de Cadastro de um Novo Artista
    def enterHandler(self, event):
        nomeArtista = self.limiteInsercaoArtista.inputNome.get()

        if nomeArtista == "":
            self.limiteInsercaoArtista.mostraJanela('Erro Código Artista', 'Erro: insira um nome válido')
            return

        nomeArtista = nomeArtista.title()

        for buscaArtista in self.listaArtistasCadastrados:
            if buscaArtista.nomeArtista == nomeArtista:
                self.limiteInsercaoArtista.mostraJanela('Erro Artista', 'Erro: artista já cadastrado')
                self.clearHandler(event)
                return
        
        cadastroArtista = Artista(nomeArtista)
        self.listaArtistasCadastrados.append(cadastroArtista)
        self.limiteInsercaoArtista.mostraJanela('Sucesso', 'Artista cadastrado com sucesso')
        self.clearHandler(event)

    #Função de Limpeza da Tela de Cadastro do Artista
    def clearHandler(self, event):
        self.limiteInsercaoArtista.inputNome.delete(0, len(self.limiteInsercaoArtista.inputNome.get()))

    #Função para Fechar a Tela de Cadastro do Artista
    def fechaHandler(self, event):
        self.limiteInsercaoArtista.destroy()

    #Função para Consultar os Albuns e Musicas Que o Artista Possui
    def consultarArtista(self):
        consultaNome = simpledialog.askstring("Consultar Artista", "Digite o nome do artista: ")
        consultaNome = consultaNome.title()
        textoConsulta = ''
        if consultaNome:
            for buscaArtista in self.listaArtistasCadastrados:
                if buscaArtista.nomeArtista == consultaNome:
                    textoConsulta += "Nome: " + buscaArtista.nomeArtista + '\n'
                    if buscaArtista.albuns:
                        textoConsulta += "Albuns: " + '\n'
                        for buscaAlbum in buscaArtista.albuns:
                            textoConsulta += " Album: " + buscaAlbum.tituloAlbum + '\n'
                            textoConsulta += "  Musicas Album: " + '\n'
                            for buscaMusica in buscaAlbum.faixas:
                                textoConsulta += "   Faixa: " + str(buscaMusica.nroFaixa) + ' - ' + buscaMusica.tituloMusica + '\n'
                    self.limiteConsultaArtista = LimiteConsultaArtista(textoConsulta)
                    return
            messagebox.showwarning("Erro Artista", "Erro: Artista não encontrado")

    #Função para Listas Todos os Artistas Cadastrados com seus Albuns e Musicas
    #def listarArtista(self):
    #    textoLista = 'Nome Artistas\n'
    #    for buscaArtista in self.listaArtistasCadastrados:
    #        textoLista += buscaArtista.nomeArtista + '\n'
    #        textoLista += "Albuns: " + '\n'
    #        for buscaAlbum in buscaArtista.albuns:
    #            textoLista += "Titulo: " + buscaAlbum.tituloAlbum + '\n'
    #        textoLista += "Musicas: " + '\n'
    #        for buscaMusica in buscaArtista.musicas:
    #            textoLista += "Faixa: " + str(buscaMusica.nroFaixa) + ' - ' + buscaMusica.tituloMusica + '\n'
    #    self.limiteListaArtista = LimiteListaArtista(textoLista)