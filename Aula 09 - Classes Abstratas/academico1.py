from abc import ABC, abstractmethod

class Pessoa(ABC):
    def __init__(self, nome, endereco, idade):
        self.__nome = nome
        self.__endereco = endereco
        self.__idade = idade 

    @property
    def nome(self):
        return self.__nome

    @property
    def endereco(self):
        return self.__endereco

    @property
    def idade(self):
        return self.__idade

    @abstractmethod
    def printDescricao(self): #qualquer classe que herder o método abstrato, deve implementar um método concreto para usa-lo
        pass

class Professor(Pessoa):
    def __init__(self, nome, endereco, idade, titulacao):
        super().__init__(nome, endereco, idade)
        self.__titulacao = titulacao

    @property
    def titulacao(self):
        return self.__titulacao

    #Se não inserir o método abstrato, o sistema não permitirá rodar o programa
    def printDescricao(self):
        print('Nome: {}'.format(self.nome))
        print('Endereço: {}'.format(self.endereco))
        print('Idade: {}'.format(self.idade))
        print('Titulação: {}'.format(self.titulacao))  
        print('Disciplinas ministradas:')    

class Aluno(Pessoa):
    def __init__(self, nome, endereco, idade, curso):
        super().__init__(nome, endereco, idade)
        self.__curso = curso

    @property
    def curso(self):
        return self.__curso

    #Se não inserir o método abstrato, o sistema não permitirá rodar o programa
    def printDescricao(self):
        print('Nome: {}'.format(self.nome))
        print('Endereço: {}'.format(self.endereco))
        print('Idade: {}'.format(self.idade))
        print('Curso: {}'.format(self.curso)) 
        print('Disciplinas cursadas:')         

if __name__ == "__main__":
    prof = Professor('Joao','Av. BPS, 1303', 44, 'doutorado')
    prof.printDescricao()
    print()
    aluno = Aluno('Pedro','Av. Cesario Alvim, 205', 20, 'SIN')
    aluno.printDescricao()