from abc import ABC, abstractmethod

################################################################################
#Classe Associativa -> PontoFuncionario
class PontoFunc():
    def __init__(self, mes, ano, nroFaltas, nroAtrasos):
        self.__mes = mes
        self.__ano = ano
        self.__nroFaltas = nroFaltas
        self.__nroAtrasos = nroAtrasos

#---Definindo Getters
    @property
    def mes(self):
        return self.__mes
    @property
    def ano(self):
        return self.__ano
    @property
    def nroFaltas(self):
        return self.__nroFaltas
    @nroFaltas.setter
    def nroFaltas(self, valor):
        self.__nroFaltas = valor
    @property
    def nroAtrasos(self):
        return self.__nroAtrasos
    @nroAtrasos.setter
    def nroAtrasos(self, valor):
        self.__nroAtrasos = valor

#---Função Para Somar o Número de Faltas no Ponto de um Funcionario em um Mes e Ano
    def lancaFaltas(self, nroFaltas):
        self.__nroFaltas = self.__nroFaltas + nroFaltas
        return

#---Função Para Somar o Número de Atrasos no Ponto de um Funcionario em um Mes e Ano
    def lancaAtrasos(self, nroAtrasos):
        self.nroAtrasos = self.__nroAtrasos + nroAtrasos
        return
    
################################################################################
#Classe Abstrata -> Funcionario
class Funcionario(ABC):
    def __init__(self, codigo, nome):
        self.__codigo = codigo
        self.__nome = nome
        self.__pontoMensalFunc = []

 #--Definindo Getters           
    @property
    def codigo(self):
        return self.__codigo
    @property
    def nome(self):
        return self.__nome
    @property
    def pontoMensalFunc(self):
        return self.__pontoMensalFunc

#---Função para Criar o Ponto do Funcionário
    def adicionaPonto(self, mes, ano, nroFaltas, nroAtrasos):
        self.__pontoMensalFunc.append(PontoFunc(mes, ano, nroFaltas, nroAtrasos))

#---Função Para Busca o Ponto de um Funcionario  em um dado mês e ano para Alterar o Nro de Faltas
    def lancaFaltas(self, mes, ano, nroFaltas):
        for ponto in self.__pontoMensalFunc:
            if mes == ponto.mes and ano == ponto.ano:
                ponto.lancaFaltas(nroFaltas)
                return

#---Função Para Busca o Ponto de um Funcionario  em um dado mês e ano para Alterar o Nro de Atrasos
    def lancaAtrasos(self, mes, ano, nroAtrasos):
        for ponto in self.__pontoMensalFunc:
            if mes == ponto.mes and ano == ponto.ano:
                ponto.lancaAtrasos(nroAtrasos)
                return

#---Função para Imprimir As Informações dos Funcionarios
    def imprimeFolha(self, mes, ano):
        print('Código: {}'.format(self.__codigo))
        print('Nome: {}'.format(self.__nome))
        print('Salário líquido: {:.2f}'.format(self.calculaSalario(mes, ano))) #"{:.2f}"
        print('Bonus: {:.2f}'.format(self.calculaBonus(mes, ano))) #"{:.2f}"

#---Função Abstrata para Calcular o Salário dos Funcionarios: Professores e Técnicos
    @abstractmethod
    def calculaSalario():
        pass

#---Função Abstrata para Calcular o Bonus dos Funcionarios: Professores e Técnicos
    @abstractmethod
    def calculaBonus():
        pass

################################################################################
#Classe Concreta -> Professor
class Professor(Funcionario):
    def __init__(self, codigo, nome, titulacao, salarioHora, nroAulas):
        super().__init__(codigo, nome)
        self.__titulacao = titulacao
        self.__salarioHora = salarioHora
        self.__nroAulas = nroAulas

#---Definindo Getters   
    @property
    def titulacao(self):
        return self.__titulacao
    @property
    def salarioHora(self):
        return self.__salarioHora
    @property
    def nroAulas(self):
        return self.__nroAulas

#---Função Contreta do Método Abstrado para Calcular o Salário do Professor  
    def calculaSalario(self, mes, ano):
        for ponto in self.pontoMensalFunc:
            if mes == ponto.mes and ano == ponto.ano:
                return ((self.__salarioHora * self.__nroAulas) - (self.__salarioHora * ponto.nroFaltas))

#---Função Contreta do Método Abstrado para Calcular o Bonus do Professor   
    def calculaBonus(self, mes, ano):
        for ponto in self.pontoMensalFunc:
            if mes == ponto.mes and ano == ponto.ano:
                if ponto.nroAtrasos <= 10:
                    salarioProf = ((self.__salarioHora * self.__nroAulas) - (self.__salarioHora * ponto.nroFaltas))
                    return ((salarioProf * (10 - ponto.nroAtrasos))/100)
                else:
                    return 0

################################################################################
#Classe Concreta -> TecAdmin (Tecnico Administrativo)
class TecAdmin(Funcionario):
    def __init__(self, codigo, nome, funcao, salarioMensal):
        super().__init__(codigo, nome)
        self.__funcao = funcao
        self.__salarioMensal = salarioMensal

#---Definindo Getters
    @property
    def funcao(self):
        return self.__funcao
    @property
    def salarioMensal(self):
        return self.__salarioMensal

#---Função Contreta do Método Abstrado para Calcular o Salário do Tecnico Administrativo 
    def calculaSalario(self, mes, ano):
        for ponto in self.pontoMensalFunc:
            if mes == ponto.mes and ano == ponto.ano:
                return (self.__salarioMensal - ((self.__salarioMensal/30)*ponto.nroFaltas))

#---Função Contreta do Método Abstrado para Calcular o Bonus do Tecnico Administrativo    
    def calculaBonus(self, mes, ano):
        for ponto in self.pontoMensalFunc:
            if mes == ponto.mes and ano == ponto.ano:
                if ponto.nroAtrasos <= 8:
                    salarioTec = (self.__salarioMensal - ((self.__salarioMensal/30)*ponto.nroFaltas))
                    return ((salarioTec * (8 - ponto.nroAtrasos))/100)
                else:
                    return 0

if __name__ == "__main__":
    funcionarios = []

    prof = Professor(1, "Joao", "Doutor", 45.35, 32)
    prof.adicionaPonto(4, 2021, 0, 0)
    prof.lancaFaltas(4, 2021, 2)
    prof.lancaAtrasos(4, 2021, 3)
    funcionarios.append(prof)

    tec = TecAdmin(2, "Pedro", "Analista Contábil", 3600)
    tec.adicionaPonto(4, 2021, 0, 0)
    tec.lancaFaltas(4, 2021, 3)
    tec.lancaAtrasos(4, 2021, 4)

    funcionarios.append(tec)
    for func in funcionarios:
        func.imprimeFolha(4, 2021)
        print()