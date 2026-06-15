from abc import ABC, abstractmethod

################################################################################
#Classe Abstrata -> Terreno
class Terreno(ABC):
    def __init__(self, localizacao, preco):
        self.__localizacao = localizacao
        self.__preco = preco

#---Definindo Getters e Setters        
    @property
    def localizacao(self):
        return self.__localizacao
    @localizacao.setter
    def localizacao(self, valor):
        self.__localizacao = valor   
    @property
    def preco(self):
        return self.__preco
    @preco.setter
    def preco(self, valor):
        self.__preco = valor

#---Criando Método Abstrato para as Classes Concretas  
    @abstractmethod
    def calculaPeso(): #Peso Terro = (preco / area do terreno) --> Custo por m²
        pass

################################################################################
#Classe Concreta -> Terreno Circular
class TerrenoCircular(Terreno):
    def __init__(self, localizacao, preco, raio):
        super().__init__(localizacao, preco)
        self.__raio = raio

#---Definindo Getters e Setters    
    @property
    def raio(self):
        return self.__raio
    @raio.setter
    def raio(self, valor):
        self.__raio = valor

#---Definindo Método Concreto para Terrano Circular do Método Abstrato   
    def calculaPeso(self):
        return (self.preco / (self.__raio*self.__raio*3.14))

################################################################################
#Classe Concreta -> Terreno Retangular
class TerrenoRetangular(Terreno):
    def __init__(self, localizacao, preco, ladoMenor, ladoMaior):
        super().__init__(localizacao, preco)
        self.__ladoMenor = ladoMenor
        self.__ladoMaior= ladoMaior

#---Definindo Getters e Setters    
    @property
    def ladoMenor(self):
        return self.__ladoMenor
    @ladoMenor.setter
    def ladoMenor(self, valor):
        self.__ladoMenor = valor
    @property
    def ladoMaior(self):
        return self.__ladoMaior
    @ladoMaior.setter
    def ladoMaior(self, valor):
        self.__ladoMaior = valor

#---Definindo Método Concreto para Terrano Retangular do Método Abstrato 
    def calculaPeso(self):
        return (self.preco / (self.__ladoMenor * self.__ladoMaior))
    
################################################################################

if __name__ == "__main__":
    terrenos = []

#---Iniciando Inserção de Valores
    terreno1 = TerrenoCircular("Pinheiros", 70000, 15)
    terrenos.append(terreno1)
    terreno2 = TerrenoRetangular("Morumbi", 75000, 20, 35)
    terrenos.append(terreno2)
    terreno3 = TerrenoCircular("Florianopolis", 110000, 20)
    terrenos.append(terreno3)
    
#--Imprimindo os Terrenos se a função index
#    print("\nTerrenos:")
#    for terreno in terrenos:
#        print(f'Localização: {terreno.localizacao}, Preço: R${terreno.preco}, Peso: R${"{:.2f}".format(terreno.calculaPeso())}')

#--Imprimindo os Terrenos com a função index --> Utilizada para imprimir o número do terreno
    print("\nLista dos Terrenos:")
    for index, terreno in enumerate(terrenos, start=1):
        print(f'\nTerreno{index}:')
        print(f'Localização: {terreno.localizacao} - Preço: R${terreno.preco} - Peso: R${"{:.2f}".format(terreno.calculaPeso())}')

#--Encontrando o Terreno com Melhor Custo --> Terreno com o Menor Peso
    print("\nO Terreno com Melhor Custo é o com as seguintes caracteristicas: ")
    melhorCusto = min(terrenos, key=lambda terreno: terreno.calculaPeso())
    print(f'Localização: {melhorCusto.localizacao} \nPreço: R${melhorCusto.preco} \nPeso: R${"{:.2f}".format(melhorCusto.calculaPeso())}')
    print()