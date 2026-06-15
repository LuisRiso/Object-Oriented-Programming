class Artista:
    def __init__(self, nome):
        self.__nome = nome
        #No construtor não há a definição de alguns e musicas, mas eles são listas do artista
        #Duas lista devido as ligações feitas no diagrama de classe
        self.__albuns = []
        self.__musicas = []

    @property
    def nome(self):
        return self.__nome

    @property
    def albuns(self):
        return self.__albuns

    @property
    def musicas(self):
        return self.__musicas
    #Toda vez que tiver listas criadas em uma classe, é preciso prover jeitos de adicionar coisas nessa lista
    #Tanto o addAlbum quanto o addMusica são os jeitos fornecidos para isso
    def addAlbum(self, album):
        self.__albuns.append(album)

    def addMusica(self, musica):
        self.__musicas.append(musica)

##########################################################################################################################

class Album:
    def __init__(self, titulo, artista, ano):
        self.__titulo = titulo
        self.__artista = artista
        self.__ano = ano
        #Possui uma lista de musicas (faixas) --> Ele agrega músicas lançadas em um album
        self.__faixas = []
        #Chamada da função para adicionar album na lista de albuns do artista
        artista.addAlbum(self) #Está passando o addAlbum para a propria classe sendo criada --> Indicado pelo (self)
                               #No processo de criação do album, ele já adiciona o album a lista de albuns do artista

    @property
    def titulo(self):
        return self.__titulo

    @property
    def artista(self):
        return self.__artista

    @property
    def ano(self):
        return self.__ano

    @property
    def faixas(self):
        return self.__faixas

    #Método para adicionar faixa
    #Funciona do jeito que na hora que você adiciona uma faixa no album --> O objeto Musica é criado junto
    def addFaixa(self, titulo, artista=None): #dois argumentos, se não passar o artista significa que o album é de um único artista, se houver artista significa que está em uma coletânea
        if artista is None:
            artista = self.__artista
        nroFaixa = len(self.__faixas) #define o nro da faixa pelo comprimento da lista de faixas 
        musica = Musica(titulo, artista, self, nroFaixa) #cria o Objeto Musica com nome da musica, artista associado, self = nome do album, nro da faixa
        #Chamada da função para adicionar musica no album
        self.__faixas.append(musica) #faz um append da música que acabou de ser criada na lista de faixas do album

##########################################################################################################################

class Musica:
    def __init__(self, titulo, artista, album, nroFaixa):
        self.__titulo = titulo
        self.__artista = artista
        self.__album = album
        self.__nroFaixa = nroFaixa
        #Chamada da função para adicionar musica na lista de musicas do artista
        artista.addMusica(self) #inserido a musica na lista de musica do artista --> Redundância do diagrama de classes para melhorar eficiencia

    @property
    def titulo(self):
        return self.__titulo
    
    @property
    def artista(self):
        return self.__artista

    @property
    def album(self):
        return self.__album

    @property
    def nroFaixa(self):
        return self.__nroFaixa

##########################################################################################################################

class Playlist:
    def __init__(self, nome):
        self.__nome = nome

        self.__musicas = []

    @property
    def nome(self):
        return self.__nome
    
    @property
    def musicas(self):
        return self.__musicas
    
    def addMusica(self, musica):
        self.__musicas.append(musica)

##########################################################################################################################

if __name__ == "__main__":    
    listaAlbuns = []
    art1 = Artista('Coldplay')
    album1 = Album('Mylo Xyloto', art1, 2011)
    album1.addFaixa('Paradise')
    album1.addFaixa('Hurts Like Heaven')
    album1.addFaixa('Charlie Brown') 
    listaAlbuns.append(album1)

    album2 = Album('A Head Full of Dreams', art1, 2015)
    album2.addFaixa('A Head Full of Dreams')
    album2.addFaixa('Birds')
    album2.addFaixa('Everglow')
    listaAlbuns.append(album2)

    art2 = Artista('Skank')
    album3 = Album('Siderado', art2, 1998)
    album3.addFaixa('Resposta')
    album3.addFaixa('Saideira')
    album3.addFaixa('Romance Noir')
    listaAlbuns.append(album3)

    print('')
    # Criar e exibir uma playlist com as músicas do album "Mylo Xyloto"
    playlist1 = Playlist('pl-mylo-xyloto')
    for musica in album1.faixas: #album1.faixas retorna a lista de faixar contidas no album
        playlist1.addMusica(musica)
    print(playlist1.nome)
    print('Musicas:')
    for musica in playlist1.musicas:
        print(musica.titulo)
    print('')

    # Criar e exibir uma playlist com todas as músicas do Coldplay   
    playlista2 = Playlist('pl-coldplay')
    for musica in art1.musicas: #vai na lista de musica do artista
        playlista2.addMusica(musica) 
    print(playlista2.nome)
    print('Musicas:')
    for musica in playlista2.musicas:
        print(musica.titulo)
    print('')

    # Criar e exibiir uma playlist contendo uma música de cada album
    playlista3 = Playlist('pl-coletanea')
    for album in listaAlbuns: #vai dar todos os albuns criados
        musicas = album.faixas #lista de todas as faixas do album --> vai virar o objeto musicas
        playlista3.addMusica(musicas[0]) #adiciona a Faixa 0 de cada album na playlist
    print(playlista3.nome)
    print('Musicas:')
    for musica in playlista3.musicas:
        print(musica.titulo)
    print('')