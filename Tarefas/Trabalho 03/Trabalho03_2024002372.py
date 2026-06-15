from abc import ABC, abstractmethod

########################################################################################################################
#Classe Abstrata -> Empregada
class Empregada (ABC):
    def __init__(self, nome, telefone):
        self.__nome = nome
        self.__telefone = telefone

#Definindo Getters e Setters    
    @property
    def nome(self):
        return self.__nome
    @nome.setter
    def nome(self, valor):
        self.__nome = valor
    @property
    def telefone(self):
        return self.__telefone
    @telefone.setter
    def telefone(self, valor):
        self.__telefone = valor

#Método Abstrata Calculo Salário
    @abstractmethod
    def getSalario():
        pass

########################################################################################################################
#Classe Concreta Empregada -> Horista
class Horista(Empregada):
    def __init__(self, nome, telefone, horasTrabalhadas, valorPorHora):
        super().__init__(nome, telefone)
        self.__horasTrabalhadas = horasTrabalhadas
        self.__valorPorHora = valorPorHora

#Definindo Getters e Setters    
    @property
    def horasTralhadas(self):
        return self.__horasTrabalhas
    @horasTralhadas.setter
    def horasTrabalhadas(self, valor):
        self.__horasTrabalhadas = valor
    @property
    def valorPorHora(self):
        return self.__valorPorHora
    @valorPorHora.setter
    def valorPorHora(self, valor):
        self.__valorPorHora = valor

#Método Concreto Calculo Salário Empregada Horista
    def getSalario(self):
        return self.__horasTrabalhadas * self.__valorPorHora
    
########################################################################################################################
#Classe Concreta Empregada -> Diarista
class Diarista(Empregada):
    def __init__(self, nome, telefone, diasTrabalhados, valorPorDia):
        super().__init__(nome, telefone)
        self.__diasTrabalhados = diasTrabalhados
        self.__valorPorDia = valorPorDia

#Definindo Getters e Setters    
    @property
    def diasTrabalhados(self):
        return self.__diasTrabalhados
    @diasTrabalhados.setter
    def diasTrabalhados(self, valor):
        self.__diasTrabalhados = valor
    @property
    def valorPorDia(self):
        return self.__valorPorDia
    @valorPorDia.setter
    def valorPorDia(self, valor):
        self.__valorPorDia = valor

#Método Concreto Calculo Salário Empregada Diarista
    def getSalario(self):
        return self.__diasTrabalhados * self.__valorPorDia
    
########################################################################################################################
#Classe Concreta Empregada -> Mensalista
class Mensalista(Empregada):
    def __init__(self, nome, telefone, valorMensal):
        super().__init__(nome, telefone)
        self.__valorMensal = valorMensal

#Definindo Getters e Setters    
    @property
    def valorMensal(self):
        return self.__valorMensal
    @valorMensal.setter
    def valorMensal(self, valor):
        self.__valorMensal = valor

#Método Concreto Calculo Salário Empregada Mensalista
    def getSalario(self):
        return self.__valorMensal
    
########################################################################################################################
#Iniciando Main para Realizar a Alocação de Dados
if __name__ == "__main__":
    empregadas = []

#Iniciando Inserção de Valores
    horista01 = Horista("Alana", "(35) 98888-8888", 160, 12)
    empregadas.append(horista01)
    diarista01 = Diarista("Joana", "(35) 97777-7777", 20, 65)
    empregadas.append(diarista01)
    mensalista01 = Mensalista("Diana", "(35) 95555-5555", 1200)
    empregadas.append(mensalista01)

#Impressão Nomes e Salários e Calculo Salario Mais Barato
    melhorValor = horista01.getSalario()
    print("\n--Todas as Empregadas--\n")
    for index, empregada in enumerate(empregadas):
        print("Empregada: {} - Valor Mensal: R${}".format(empregada.nome, empregada.getSalario()))
        if melhorValor > empregadas[index].getSalario():
            melhorValor = empregadas[index].getSalario()
            indice = index
#Impressão Empregada Mais Barata
    print("\n---Empregada Mais Barata---\n")
    print("Nome: {}".format(empregadas[indice].nome))
    print("Telefone: {}".format(empregadas[indice].telefone))
    print("Salario: R${}\n".format(empregadas[indice].getSalario()))