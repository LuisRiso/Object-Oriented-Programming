################################################################################
#--------------------Sistema Cadastro Professor e Aluno------------------------#
#-----------Nome: Luís Gustavo Riso Santos --- Matricula: 2024002372-----------#
################################################################################

class erroCPF(Exception):
    pass

class titulacaoInvalida(Exception):
    pass

class cursoInvalido(Exception):
    pass

class idadeInvalida(Exception):
    pass

class Pessoa():
    def __init__(self, nome ,endereco, idade, cpf):
        self.__nome = nome
        self.__endereco = endereco
        self.__idade = idade
        self.__cpf = cpf

    @property
    def nome(self):
        return self.__nome
    @nome.setter
    def nome(self, valor):
        self.__nome = valor

    @property
    def endereco(self):
        return self.__endereco
    @endereco.setter
    def endereco(self, valor):
        self.__endereco = valor

    @property
    def idade(self):
        return self.__idade
    @idade.setter
    def idade(self, valor):
        self.__idade = valor

    @property
    def cpf(self):
        return self.__cpf
    @cpf.setter
    def cpf(self, valor):
        self.__cpf = valor

#------------------------------------------------------------------------------#

class Professor(Pessoa):
    def __init__(self, nome, endereco, idade, cpf, titulacao):
        super().__init__(nome, endereco, idade, cpf)
        self.__titulacao = titulacao
        self.validacaoCriterios() #ser de Doutor e Idade >= 30

    @property
    def titulacao(self):
        return self.__titulacao
    @titulacao.setter
    def titulacao(self, valor):
        self.__titulacao = valor

    def validacaoCriterios(self):
        if self.titulacao.lower() != "doutor":
            raise titulacaoInvalida("Erro: Professor(a) {} possui titulação abaixo da estipulada, necessário ser um Doutor".format(self.nome))
        if self.idade < 30:
            raise idadeInvalida(("Erro: Professor(a) {} deve ter idade igual ou maior que 30 anos.".format(self.nome)))
    
    def printDescricao(self):
        print("Professor(a): {}".format(self.nome))
        print("Titulacao: {}".format(self.__titulacao))
        print("Endereço: {}".format(self.endereco))
        print("Idade: {}".format(self.idade))
        print("CPF: {}\n".format(self.cpf))
        
#------------------------------------------------------------------------------#

class Aluno(Pessoa):
    def __init__(self, nome, endereco, idade, cpf, curso):
        super().__init__(nome, endereco, idade, cpf)
        self.__curso = curso
        self.validacaoCriterios() #ser de CCO ou SIN e Idade >= 18

    @property
    def curso(self):
        return self.__curso
    @curso.setter
    def curso(self, valor):
        self.__curso = valor

    def validacaoCriterios(self):
        if self.curso.upper() not in ["CCO", "SIN"]:
            raise cursoInvalido("Erro: Aluno {} precisa estar cadastro em SIN ou CCO".format(self.nome))
        if self.idade < 18:
            raise idadeInvalida(("Erro: Aluno(a) {} deve ter idade igual ou maior que 18 anos.".format(self.nome)))
    
    def printDescricao(self):
        print("Aluno(a): {}".format(self.nome))
        print("Curso: {}".format(self.__curso))
        print("Endereço: {}".format(self.endereco))
        print("Idade: {}".format(self.idade))
        print("CPF: {}\n".format(self.cpf))

class CadastroPessoa():
    def __init__(self):
        self.__pessoasCadastradas = []
        self.__cpf = set()

    @property
    def pessoasCadastradas(self):
        return self.__pessoasCadastradas
    @property
    def cpf(self):
        return self.__cpf
    
    def cadastraPessoa(self, pessoa):
        if pessoa.cpf in self.__cpf:
            raise erroCPF("CPF Invalido para {} pois já está cadastrado no sistema".format(pessoa.nome))
        self.cpf.add(pessoa.cpf)
        self.pessoasCadastradas.append(pessoa)

    def listarCadastros(self):
        for pessoa in self.__pessoasCadastradas:
            pessoa.printDescricao()

if __name__ == "__main__":

    cadastro = CadastroPessoa()

    # Lista de pessoas com alguns dados inválidos
    dadosPessoasCadastro = [
        ("Professor", "Dr Carlos", "Rua A, 123", 40, "12345678901", "Doutor"),      # Válido
        ("Professor", "Dr Ana", "Rua B, 456", 29, "23456789012", "Doutor"),         # Inválido (idade < 30)
        ("Professor", "Dr Paulo", "Rua C, 789", 45, "67890123456", "Mestre"),       # Inválido (titulação != Doutor)
        ("Professor", "Dr Julia", "Rua D, 101", 50, "78901234567", "Doutor"),       # Válido
        ("Aluno", "Pedro", "Av. Central, 202", 20, "34567890123", "CCO"),           # Válido
        ("Aluno", "Maria", "Av. Sul, 303", 17, "45678901234", "SIN"),               # Inválido (idade < 18)
        ("Aluno", "João", "Rua E, 404", 22, "56789012345", "ENG"),                  # Inválido (curso != CCO ou SIN)
        ("Aluno", "Alice", "Rua F, 505", 19, "89012345678", "SIN"),                 # Válido
        ("Professor", "Dr Roberto", "Av. Norte, 606", 34, "12389045601", "Doutor"), # Válido
        ("Professor", "Dr Helena", "Rua G, 707", 32, "45612378901", "Doutor"),      # Válido
        ("Aluno", "Lucas", "Rua H, 808", 25, "78945612302", "CCO"),                 # Válido
        ("Aluno", "Beatriz", "Av. Oeste, 909", 18, "78945612302", "SIN")            # Válido
    ]

    for tipo, nome, endereco, idade, cpf, extra in dadosPessoasCadastro:
        
        try:
            if tipo == "Professor":
                pessoa = Professor(nome, endereco, idade, cpf, extra)
            elif tipo == "Aluno":
                pessoa = Aluno(nome, endereco, idade, cpf, extra)
            cadastro.cadastraPessoa(pessoa)

        except erroCPF as e:
            print(e) 
        except titulacaoInvalida as e:
            print(e)
        except cursoInvalido as e:
            print(e)
        except idadeInvalida as e:
            print(e)

    print("\nCadastro resultante:")
    cadastro.listarCadastros()

