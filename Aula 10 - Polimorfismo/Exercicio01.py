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

    def calculaValorImposto(self, renda):
        if renda < 1903.99:
            aliquota = 0
        elif renda < 2826.65:
            aliquota = 7.5
        elif renda < 3751.05:
            aliquota = 15
        elif renda < 4664.68:
            aliquota = 22.5
        else:
            aliquota = 27.5
        return (renda * aliquota)/100

    @abstractmethod
    def calculaSalario(self):
        pass

class ProfDE(Professor):
    def __init__(self, nome, matricula, cargaHoraria, salarioBruto):
        super().__init__(nome, matricula, cargaHoraria)
        self.__salarioBruto = salarioBruto

    @property
    def salarioBruto(self):
        return self.__salarioBruto

    @salarioBruto.setter 
    def salarioBruto(self, salarioBruto): 
        self.__salarioBruto = salarioBruto
    
    def calculaSalario(self):
        previdencia = self.__salarioBruto * 0.11
        aliquota = self.calculaValorImposto(self.salarioBruto)
        return self.__salarioBruto - (previdencia + aliquota)

class ProfHorista(Professor):
    def __init__(self, nome, matricula, cargaHoraria, salarioHoraBruto):
        super().__init__(nome, matricula, cargaHoraria)
        self.__salarioHoraBruto = salarioHoraBruto

    @property
    def salarioHoraBruto(self):
        return self.__salarioHoraBruto

    @salarioHoraBruto.setter
    def salarioHoraBruto(self, salarioHoraBruto):
        self.__salarioHoraBruto = salarioHoraBruto 

    def calculaSalario(self):
        renda = self.__salarioHoraBruto * self.cargaHoraria
        aliquota = self.calculaValorImposto(renda)
        return renda - aliquota

if __name__ == "__main__":
    prof1 = ProfDE('Joao', 12345, 40, 5000)
    prof2 = ProfHorista('Paulo', 54321, 30, 75)
    prof3 = ProfHorista('Ana', 56789, 38, 95)
    prof1.salarioBruto = 6000
    prof2.salarioHoraBruto = 85
    profs = [prof1, prof2, prof3]
    for prof in profs:
        print ('Nome: {} - Salário: {}'.format(prof.nome, prof.calculaSalario()))

