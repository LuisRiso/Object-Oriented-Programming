
class Veiculo:

    def __init__(self, marca, cor, motorLigado):
        self.__marca = marca
        self.__cor = cor
        self.__motorLigado = motorLigado

    #Método usado para acessar uma propriedade/atributo de uma classe
    @property
    def marca(self):
        return self.__marca

    @property
    def cor(self):
        return self.__cor

    @property
    def motorLigado(self):
        return self.__motorLigado

    def ligaMotor(self):
        if self.__motorLigado == True:
            print('Motor já está ligado')
        else:
            self.__motorLigado = True
            print('O motor acaba de ser ligado')

class Carro(Veiculo):

    def __init__(self, marca, cor, motorLigado, portaMalasCheio):
        #Toda vez que for criar um objeto na subclasse, será preciso chamar o construtor da super classe
        #O contrutor nesse caso é o método "__init__"
        super().__init__(marca, cor, motorLigado) #Chamada para ativar o construtor da superclasse passando atributos da super classe
        self.__portaMalasCheio = portaMalasCheio

    @property
    def portaMalasCheio(self):
        return self.__portaMalasCheio

    def enchePortaMalas(self):
        if(self.__portaMalasCheio == True):
            print('O porta malas já está cheio')
        else:
            self.__portaMalasCheio = True
            print('O porta malas acaba de ser cheio')

    def mostraAtributos(self):
        print('Este carro é um {} {}'.format(self.marca, self.cor))
        if(self.motorLigado):
            print('Seu motor está ligado')
        else:
            print('Seu motor está desligado')
        if(self.portaMalasCheio):
            print('Seu porta malas está cheio')
        else:
            print('Seu porta malas está vazio')

class Motocicleta(Veiculo):

    def __init__(self, marca, cor, motorLigado, estilo):
        #chama o construtor da superclasse
        super().__init__(marca, cor, motorLigado)
        self.__estilo = estilo

    @property
    def estilo(self):
        return self.__estilo

    def mostraAtributos(self):
        print('Esta moto é uma {} {} {}'.format(self.marca, self.cor, self.estilo))
        if(self.motorLigado):
            print('Seu motor está ligado')
        else:
            print('Seu motor está desligado')

if __name__ == "__main__":
    m = Motocicleta('Honda', 'azul', False, 'naked')
    m.mostraAtributos()
    m.ligaMotor()
    m.mostraAtributos()
    print('------------')
    c = Carro('Chevrolet', 'branco', False, False)
    c.mostraAtributos()
    c.enchePortaMalas()
    c.ligaMotor()
    c.mostraAtributos()

       