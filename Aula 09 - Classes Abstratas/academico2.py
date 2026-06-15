from abc import ABC, abstractmethod

class Pessoa(ABC):
    def __init__(self, nome, endereco, idade, listaDisciplinas):
        self.__nome = nome
        self.__endereco = endereco
        self.__idade = idade 
        self.__listaDisciplinas = listaDisciplinas 

    @property
    def nome(self):
        return self.__nome

    @property
    def endereco(self):
        return self.__endereco

    @property
    def idade(self):
        return self.__idade
    
    @property
    def listaDisciplinas(self):
        return self.__listaDisciplinas

    @abstractmethod
    def printDescricao(self): #qualquer classe que herder o método abstrato, deve implementar um método concreto para usa-lo
        pass

    

class Professor(Pessoa):
    def __init__(self, nome, endereco, idade, titulacao, listaDisciplinas):
        super().__init__(nome, endereco, idade, listaDisciplinas)
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
        for disciplina in self.listaDisciplinas:
            print("Nome: {} - Carga Horaria {}".format(disciplina.nomeDisciplina, disciplina.cargaHoraria))

class Aluno(Pessoa):
    def __init__(self, nome, endereco, idade, curso, listaDisciplinas):
        super().__init__(nome, endereco, idade, listaDisciplinas)
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
        for disciplina in self.listaDisciplinas:
            print("Nome: {} - Carga Horaria {}".format(disciplina.nomeDisciplina, disciplina.cargaHoraria))     

class Disciplina():
    def __init__(self, nomeDisciplina, cargaHoraria):
        self.__nomeDisciplina = nomeDisciplina
        self.__cargaHoraria = cargaHoraria

    @property 
    def nomeDisciplina(self):
        return self.__nomeDisciplina
    
    @property
    def cargaHoraria(self):
        return self.__cargaHoraria

if __name__ == "__main__":
    #Definindo as disciplinas no main
    disciplina01 = Disciplina("Programacao 00", 64)
    disciplina02 = Disciplina("Estrutura de Dados", 64)
    disciplina03 = Disciplina("Banco de Dados", 64)

    listaDisciplina01 = [disciplina01, disciplina02] #lista contendo as disciplinas para o professor
    listaDisciplina02 = [disciplina02, disciplina03] #lista contendo as disciplinas para o aluno

    prof = Professor('Joao','Av. BPS, 1303', 44, 'doutorado', listaDisciplina01)
    prof.printDescricao()
    print()
    aluno = Aluno('Pedro','Av. Cesario Alvim, 205', 20, 'SIN', listaDisciplina02)
    aluno.printDescricao()