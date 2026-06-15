import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import simpledialog

class Playlist():
    def __init__(self, nomePlaylist):
        self.__nomePlaylist = nomePlaylist
        self.__musicas = []

    @property
    def nomePlaylist(self):
        return self.__nomePlaylist
    @property
    def musicas(self):
        return self.__musicas
    
class LimiteInserePlaylist(tk.Toplevel):
    def __init__(self, controle, listaNomeArtistas):
        tk.Toplevel.__init__(self)
        self.geometry('400x310')
        self.title("Cadastro Playlist")
        self.controle = controle
        self.musicasSelecionadas = []

        self.frameNomePlaylist = tk.Frame(self)
        self.frameNomeArtista = tk.Frame(self)
        self.frameMusicaArtista = tk.Frame(self)
        self.frameButtonMusica = tk.Frame(self)
        self.frameButton = tk.Frame(self)

        self.frameNomePlaylist.pack()
        self.frameNomeArtista.pack()
        self.frameMusicaArtista.pack()
        self.frameButtonMusica.pack()
        self.frameButton.pack()

        #Inserção Nome Playlist
        self.labelNomePlaylist = tk.Label(self.frameNomePlaylist,text="Nome Playlist: ")
        self.labelNomePlaylist.pack(side="left", pady=1)
        self.inputNomePlaylist = tk.Entry(self.frameNomePlaylist, width=20)
        self.inputNomePlaylist.pack(side="left", pady=1)

        #Escolha do Artista
        self.labelArtista = tk.Label(self.frameNomeArtista,text="Selecione Artista: ")
        self.labelArtista.pack(side="left", pady=1)
        self.escolhaCombo = tk.StringVar()
        self.combobox = ttk.Combobox(self.frameNomeArtista, width = 15 , textvariable = self.escolhaCombo)
        self.combobox.pack(side="left", pady=1)
        self.combobox['values'] = listaNomeArtistas
        self.combobox.bind("<<ComboboxSelected>>", controle.atualizarMusicas)  #Vai atualizar as músicas ao selecionar artista

        #Insercao Musica
        self.labelMusica = tk.Label(self.frameMusicaArtista,text="Musicas do artista: ")
        self.labelMusica.pack(side="top", anchor="center", pady=1)
        self.listbox = tk.Listbox(self.frameMusicaArtista)
        self.listbox.pack(side="left")

        self.buttonInsere = tk.Button(self.frameButtonMusica ,text="Inserir Musica")           
        self.buttonInsere.pack(side="top", anchor="center", pady=1)
        self.buttonInsere.bind("<Button>", controle.inserirMusica) 

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

class LimiteConsultaPlaylist():
    def __init__(self, textoConsulta):
        messagebox.showinfo('Playlist Buscada', textoConsulta)

#class LimiteListaPlaylist():
#    def __init__(self, textoLista):
#        messagebox.showinfo('Lista de Playlists', textoLista)

class CtrlPlaylist():
    def __init__(self, controlePrincipal):
        self.ctrlPrincipal = controlePrincipal
        self.listaPlaylistCriadas = []

    #Função para iniciar a criação de uma playlist
    def inserirPlaylist(self):
        listaNomeArtistas = self.ctrlPrincipal.ctrlArtista.getListaNomeArtistas()
        self.limiteInsercaoPlaylist = LimiteInserePlaylist(self, listaNomeArtistas)

    #Atualiza a listbox com as músicas do artista selecionado
    def atualizarMusicas(self, event):
        artistaNome = self.limiteInsercaoPlaylist.combobox.get()
        self.limiteInsercaoPlaylist.listbox.delete(0, tk.END)  #Limpa as músicas do listbox

        artista = self.ctrlPrincipal.ctrlArtista.getArtistas(artistaNome)
        for musica in artista.musicas:
            self.limiteInsercaoPlaylist.listbox.insert(tk.END, musica.tituloMusica)

    #Função para inserir as musicas temporariamente em uma lista para insere-la depois
    def inserirMusica(self, event):
        nomeMusicaSelecionada = self.limiteInsercaoPlaylist.listbox.get(tk.ACTIVE) #armazena a musica selecionada -> tk.ACTIVE especifica item selecionado
        nomeArtista = self.limiteInsercaoPlaylist.combobox.get()
        musicaSelecionada = self.ctrlPrincipal.ctrlArtista.getMusicaArtistas(nomeArtista, nomeMusicaSelecionada)
        self.limiteInsercaoPlaylist.musicasSelecionadas.append(musicaSelecionada)
        self.limiteInsercaoPlaylist.mostraJanela('Sucesso', 'Musica inserida na playlist')
        self.limiteInsercaoPlaylist.listbox.delete(tk.ACTIVE) #removo a musica que já foi selecionado da lista

    #Função de Cadastro da Playlist
    def enterHandler(self, event):
        tituloPlaylist = self.limiteInsercaoPlaylist.inputNomePlaylist.get()

        if not tituloPlaylist:
            messagebox.showwarning("Erro Playlist", "Erro: Preencha todos os campos de cadastro")
            return

        if not self.limiteInsercaoPlaylist.musicasSelecionadas:
            messagebox.showwarning("Erro", "Adicione pelo menos uma música no album")
            return

        tituloPlaylist = tituloPlaylist.title()

        for buscaPlaylist in self.listaPlaylistCriadas:
            if buscaPlaylist.nomePlaylist == tituloPlaylist:
                messagebox.showwarning("Erro Playlist", "Erro: nome playlist já usado")
                self.clearHandler(event)
                return
        
        playlist = Playlist(tituloPlaylist)
        for adicaoMusica in self.limiteInsercaoPlaylist.musicasSelecionadas:
            playlist.musicas.append(adicaoMusica)
        self.listaPlaylistCriadas.append(playlist)

        self.limiteInsercaoPlaylist.mostraJanela('Sucesso', 'Playlist criada com sucesso')
        self.limiteInsercaoPlaylist.destroy()

    #Função de Limpeza da Tela de Cadastro do Album
    def clearHandler(self, event):
        self.limiteInsercaoPlaylist.inputNomePlaylist.delete(0, len(self.limiteInsercaoPlaylist.inputNomePlaylist.get()))
        self.limiteInsercaoPlaylist.escolhaCombo.set(value='')

    #Função para Fechar a Tela de Cadastro do Album
    def fechaHandler(self, event):
        self.limiteInsercaoPlaylist.destroy()

    #Função de Consultar uma Playlist Criada
    def consultarPlaylist(self):
        consultaPlaylist = simpledialog.askstring("Consultar Album", "Digite o nome do album: ")
        textoConsulta = ''
        if consultaPlaylist:
            consultaPlaylist = consultaPlaylist.title()
            for buscaPlaylist in self.listaPlaylistCriadas:
                if buscaPlaylist.nomePlaylist == consultaPlaylist:
                    textoConsulta += "Nome: " + buscaPlaylist.nomePlaylist + '\n'
                    textoConsulta += " Musicas:" + '\n'
                    for buscaMusicaAlbum in buscaPlaylist.musicas:
                        textoConsulta += "  " + buscaMusicaAlbum.tituloMusica + '\n'
                    self.limiteConsultaPlaylist = LimiteConsultaPlaylist(textoConsulta)
                    return
            messagebox.showwarning("Erro Album", "Erro: Album  não encontrado")

    #Função para Listar Todas as Playlists já Criadas
    #def listarPlaylist(self):
    #    textoLista = 'Lista Playlists\n\n'
    #    for buscaPlaylist in self.listaPlaylistCriadas:
    #        textoLista += 'Playlist: ' + buscaPlaylist.nomePlaylist + '\n'
    #        textoLista += "Musicas: " + '\n'
    #        for buscaMusicaPlaylist in buscaPlaylist.musicas:
    #            textoLista += buscaMusicaPlaylist.tituloMusica + '\n'
    #        textoLista += "------------" + '\n'
    #    self.limiteListaPlaylist = LimiteListaPlaylist(textoLista)
