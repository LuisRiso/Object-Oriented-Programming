class Musica():
    def __init__(self, tituloMusica, artista, album, nroFaixa):
        self.__tituloMusica = tituloMusica
        self.__artista = artista
        self.__album = album
        self.__nroFaixa = nroFaixa

    @property
    def tituloMusica(self):
        return self.__tituloMusica
    @property
    def artista(self):
        return self.__artista
    @property
    def album(self):
        return self.__album
    @property
    def nroFaixa(self):
        return self.__nroFaixa
    
class CtrlMusica():
    def __init__(self):
        self.listaMusicasCadastradas = []
    
    def criarMusica(self, tituloMusica, artista, album, nroFaixa):
        novaMusica = Musica(tituloMusica, artista, album, nroFaixa)
        self.listaMusicasCadastradas.append(novaMusica)
        return novaMusica

    def getMusica(self):
        pass