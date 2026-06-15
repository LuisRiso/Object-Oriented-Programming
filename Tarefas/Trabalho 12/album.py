import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import simpledialog

class Album():
    def __init__(self, tituloAlbum, artista, ano):
        self.__tituloAlbum = tituloAlbum
        self.__artista = artista
        self.__ano = ano
        self.__faixas = []

    @property
    def tituloAlbum(self):
        return self.__tituloAlbum
    @property
    def artista(self):
        return self.__artista
    @property
    def ano(self):
        return self.__ano
    @property
    def faixas(self):
        return self.__faixas
    
class LimiteInsereAlbum(tk.Toplevel):
    def __init__(self, controle, listaNomeArtistas):
        tk.Toplevel.__init__(self)
        self.geometry('400x310')
        self.title("Cadastro Album")
        self.controle = controle
        self.musicasTemporarias = []

        self.frameTitulo = tk.Frame(self)
        self.frameArtista = tk.Frame(self)
        self.frameAno = tk.Frame(self)
        self.frameButtonMusic = tk.Frame(self)
        self.frameMusica = tk.Frame(self)
        self.frameButton = tk.Frame(self)

        self.frameTitulo.pack()
        self.frameArtista.pack()
        self.frameAno.pack()
        self.frameButtonMusic.pack()
        self.frameMusica.pack()
        self.frameButton.pack()

        #Insercao Titulo
        self.labelTitulo = tk.Label(self.frameTitulo,text="Titulo: ")
        self.labelTitulo.pack(side="left")
        self.inputTitulo = tk.Entry(self.frameTitulo, width=30)
        self.inputTitulo.pack(side="left")

        #Escolha Artista
        self.labelArtista = tk.Label(self.frameArtista,text="Artista: ")
        self.labelArtista.pack(side="left")
        self.escolhaCombo = tk.StringVar()
        self.combobox = ttk.Combobox(self.frameArtista, width = 30 , textvariable = self.escolhaCombo)
        self.combobox.pack(side="left")
        self.combobox['values'] = listaNomeArtistas

        #Insercao Ano
        self.labelAno = tk.Label(self.frameAno,text="Ano: ")
        self.labelAno.pack(side="left")
        self.inputAno = tk.Entry(self.frameAno, width=30)
        self.inputAno.pack(side="left")

        #Insercao Musica
        self.buttonMusic = tk.Button(self.frameButtonMusic, text="Add Música", command=controle.adicionarMusica)
        self.buttonMusic.pack(side="left")
        self.inputMusica = tk.Entry(self.frameButtonMusic, width=30)
        self.inputMusica.pack(side="left", padx=5)

        self.labelMusica = tk.Label(self.frameMusica, text="Músicas do Álbum:")
        self.labelMusica.pack()
        self.listMusicas = tk.Listbox(self.frameMusica, width=50, height=10)
        self.listMusicas.pack()

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

class LimiteConsultaAlbum():
    def __init__(self, textoConsulta):
        messagebox.showinfo('Album Buscado', textoConsulta)

#class LimiteListaAlbum():
#    def __init__(self, textoLista):
#        messagebox.showinfo('Lista de Albuns', textoLista)

class CtrlAlbum():
    def __init__(self, controlePrincipal):
        self.ctrlPrincipal = controlePrincipal
        self.listaAlbunsCadastrados = []
        
    #Pega a lista  de artistas e musicas para inserir no album
    def inserirAlbum(self):
        listaNomeArtistas = self.ctrlPrincipal.ctrlArtista.getListaNomeArtistas()
        self.limiteInsercaoAlbum = LimiteInsereAlbum(self, listaNomeArtistas) 

    def adicionarMusica(self):
        musica = self.limiteInsercaoAlbum.inputMusica.get()
        if musica:
            self.limiteInsercaoAlbum.musicasTemporarias.append(musica)
            self.limiteInsercaoAlbum.listMusicas.insert(tk.END, musica) #posiciona elemento inserido como ultimo da lista
            self.limiteInsercaoAlbum.inputMusica.delete(0, tk.END) #deleta o conteudo até o final do conteudo que havia sido inserido
        else:
            messagebox.showwarning("Erro", "Digite o título da música!")

    #Função de Cadastro do Album
    def enterHandler(self, event):
        tituloAlbum = self.limiteInsercaoAlbum.inputTitulo.get()
        artistaAlbum = self.limiteInsercaoAlbum.escolhaCombo.get()
        anoAlbum = self.limiteInsercaoAlbum.inputAno.get()

        if not tituloAlbum or not artistaAlbum or not anoAlbum:
            messagebox.showwarning("Erro Cadastro", "Erro: Preencha todos os campos de cadastro")
            return

        if not self.limiteInsercaoAlbum.musicasTemporarias:
            messagebox.showwarning("Erro", "Adicione pelo menos uma música no album")
            return

        tituloAlbum = tituloAlbum.title()

        for buscaAlbum in self.listaAlbunsCadastrados:
            if buscaAlbum.tituloAlbum == tituloAlbum:
                messagebox.showwarning("Erro Album", "Erro: album já cadastrado")
                self.clearHandler(event)
                return
        
        album = Album(tituloAlbum, artistaAlbum, anoAlbum)
        for nroFaixaAlbum, tituloMusica in enumerate(self.limiteInsercaoAlbum.musicasTemporarias, start=1):
            novaMusicaAlbum =  self.ctrlPrincipal.ctrlMusica.criarMusica(tituloMusica, artistaAlbum, tituloAlbum, nroFaixaAlbum)
            album.faixas.append(novaMusicaAlbum)
        self.listaAlbunsCadastrados.append(album) #inserir o album criado na lista da albuns

        self.ctrlPrincipal.ctrlArtista.adicionarAlbumArtista(album) #inserir o album no artista do album

        self.limiteInsercaoAlbum.mostraJanela('Sucesso', 'Album cadastrado com sucesso')
        self.limiteInsercaoAlbum.destroy()

    #Função de Limpeza da Tela de Cadastro do Album
    def clearHandler(self, event):
        self.limiteInsercaoAlbum.inputTitulo.delete(0, len(self.limiteInsercaoAlbum.inputTitulo.get()))
        self.limiteInsercaoAlbum.escolhaCombo.set(value='')
        self.limiteInsercaoAlbum.inputAno.delete(0, len(self.limiteInsercaoAlbum.inputAno.get()))

    #Função para Fechar a Tela de Cadastro do Album
    def fechaHandler(self, event):
        self.limiteInsercaoAlbum.destroy()

    #Função de Consultar um Album Criado
    def consultarAlbum(self):
        consultaAlbum = simpledialog.askstring("Consultar Album", "Digite o nome do album: ")
        consultaAlbum = consultaAlbum.title()
        textoConsulta = ''
        if consultaAlbum:
            consultaAlbum = consultaAlbum.title()
            for buscaAlbum in self.listaAlbunsCadastrados:
                if buscaAlbum.tituloAlbum == consultaAlbum:
                    textoConsulta += "Album: " + buscaAlbum.tituloAlbum + '\n'
                    textoConsulta += " Artista: " + buscaAlbum.artista + '\n'
                    textoConsulta += " Ano: " + buscaAlbum.ano + '\n'
                    textoConsulta += " Musicas: " + '\n'
                    for buscaMusicaAlbum in buscaAlbum.faixas:
                        textoConsulta += "  Faixa: " + str(buscaMusicaAlbum.nroFaixa) + ' - ' + buscaMusicaAlbum.tituloMusica + '\n'
                    self.limiteConsultaArtista = LimiteConsultaAlbum(textoConsulta)
                    return
            messagebox.showwarning("Erro Album", "Erro: Album  não encontrado")

    #Função para Listar Todos os Albuns já Criados
    #def listarAlbum(self):
    #    textoLista = 'Lista Albuns\n\n'
    #    for buscaAlbum in self.listaAlbunsCadastrados:
    #        textoLista += 'Album: ' + buscaAlbum.tituloAlbum + '\n'
    #        textoLista += 'Artista: ' + buscaAlbum.artista + '\n'
    #        textoLista += 'Ano: ' + buscaAlbum.ano + '\n'
    #        textoLista += "Musicas: " + '\n'
    #        for buscaMusicAlbum in buscaAlbum.faixas:
    #            textoLista += "Faixa: " + str(buscaMusicAlbum.nroFaixa) + " - " + buscaMusicAlbum.tituloMusica + '\n'
    #        textoLista += "------------" + '\n'
    #    self.limiteListaAlbum = LimiteListaAlbum(textoLista)