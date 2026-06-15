from abc import ABC, abstractmethod

class Professor(ABC):
    def __init__(self, nome, matricula, cargaHoraria):
        self.__nome = nome
        self.__matricula = matricula
        self.__cargaHoraria = cargaHoraria

    #a properte é equivalente ao getter
    #o getter funciona para voce obter um valor
    #nesse caso, o property referencia a propriedade para obter o valor dela
    @property 
    def nome(self):
        return self.__nome
    
    #alteração de uma propriedade é feita através dos setters
    #regra, sempre definir um setter para cada property criada
    @nome.setter 
    def nome(self, valor): 
        self.__nome = valor

    @property
    def matricula(self):
        return self.__matricula
    @matricula.setter
    def matricula(self, valor):
        self.__matricula = valor

    @property
    def cargaHoraria(self):
        return self.__cargaHoraria
    @cargaHoraria.setter
    def cargaHoraria(self, valor):
        self.__cargaHoraria = valor

    @abstractmethod
    def calculaSalario(self):
        pass

class ProfDE(Professor):
    def __init__(self, nome, matricula, cargaHoraria, salario):
        super().__init__(nome, matricula, cargaHoraria)
        self.__salario = salario

    @property #referencia o método e retorna isso
    def salario(self):
        return self.__salario

    @salario.setter #alteração de uma propriedade é feita através dos setters
    def salario(self, salario): #regra, sempre definir um setter para cada property criada
        self.__salario = salario

    def calculaSalario(self):
        return self.__salario

class ProfHorista(Professor):
    def __init__(self, nome, matricula, cargaHoraria, salarioHora):
        super().__init__(nome, matricula, cargaHoraria)
        self.__salarioHora = salarioHora

    @property
    def salarioHora(self):
        return self.__salarioHora

    @salarioHora.setter
    def salarioHora(self, salarioHora):
        self.__salarioHora = salarioHora 

    def calculaSalario(self):
        return self.__salarioHora * self.cargaHoraria

if __name__ == "__main__":
    prof1 = ProfDE('Joao', 12345, 40, 5000)
    prof2 = ProfHorista('Paulo', 54321, 30, 75)
    prof3 = ProfHorista('Ana', 56789, 38, 95)
    prof1.salario = 6000
    prof2.salarioHora = 85
    profs = [prof1, prof2, prof3]
    for prof in profs:
        print ('Nome: {} - Salário: {}'.format(prof.nome, prof.calculaSalario()))

