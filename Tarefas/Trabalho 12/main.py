import tkinter as tk
import artista as artist
import album as record
import playlist as playList
import musica as music

class LimitePrincipal():
    def __init__(self, root, controle):
        self.controle = controle
        self.root = root
        self.root.geometry('300x250')
        self.menubar = tk.Menu(self.root)        
        self.artistaMenu = tk.Menu(self.menubar)
        self.albumMenu = tk.Menu(self.menubar)
        self.playlistMenu = tk.Menu(self.menubar)

        self.artistaMenu.add_command(label="Cadastrar", \
                    command=self.controle.inserirArtista)
        self.artistaMenu.add_command(label="Consultar", \
                    command=self.controle.consultarArtista)
        #self.artistaMenu.add_command(label="Listar", \
        #            command=self.controle.listarArtista)
        self.menubar.add_cascade(label="Artista", \
                    menu=self.artistaMenu)

        self.albumMenu.add_command(label="Cadastrar", \
                    command=self.controle.inserirAlbum)
        self.albumMenu.add_command(label="Consultar", \
                    command=self.controle.consultarAlbum)
        #self.albumMenu.add_command(label="Listar", \
        #            command=self.controle.listarAlbum)
        self.menubar.add_cascade(label="Album", \
                   menu=self.albumMenu)
        
        self.playlistMenu.add_command(label="Cadastrar", \
                    command=self.controle.inserirPlaylist)
        self.playlistMenu.add_command(label="Consultar", \
                    command=self.controle.consultarPlaylist)
        #self.playlistMenu.add_command(label="Listar", \
        #            command=self.controle.listarPlaylist)
        self.menubar.add_cascade(label="Playlist", \
                    menu=self.playlistMenu)
        
        self.root.config(menu=self.menubar)

class ControlePrincipal():
    def __init__(self):
        self.root = tk.Tk()
        
        self.ctrlArtista = artist.CtrlArtista()
        self.ctrlAlbum = record.CtrlAlbum(self)
        self.ctrlPlaylist = playList.CtrlPlaylist(self)
        self.ctrlMusica = music.CtrlMusica()

        self.limite = LimitePrincipal(self.root, self)
        self.root.title("Sistema MP3")
        self.root.mainloop()

    def inserirArtista(self):
        self.ctrlArtista.inserirArtista()
    def consultarArtista(self):
        self.ctrlArtista.consultarArtista()
    #def listarArtista(self):
    #    self.ctrlArtista.listarArtista()
    
    def inserirAlbum(self):
        self.ctrlAlbum.inserirAlbum()
    def consultarAlbum(self):
        self.ctrlAlbum.consultarAlbum()
    #def listarAlbum(self):
    #    self.ctrlAlbum.listarAlbum()
    
    def inserirPlaylist(self):
        self.ctrlPlaylist.inserirPlaylist()
    def consultarPlaylist(self):
        self.ctrlPlaylist.consultarPlaylist()
    #def listarPlaylist(self):
    #    self.ctrlPlaylist.listarPlaylist()

if __name__ == "__main__":
    c = ControlePrincipal()