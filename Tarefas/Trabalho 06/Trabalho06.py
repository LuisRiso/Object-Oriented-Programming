#----------------------Sistema de Controle Bancário----------------------------#
#-----------Nome: Luís Gustavo Riso Santos --- Matricula: 2024002372-----------#
################################################################################
#from abc import ABC, abstractmethod
from datetime import date
################################################################################
#--------------------------Superclasse | Transacao-----------------------------#
class Transacao:
    def __init__(self, valor, data):
        self.__valor = valor
        self.__data = data
#--------------------------Definindo Getters e Setters-------------------------#
    @property
    def valor(self):
        return self.__valor
    @valor.setter
    def valor(self, valor):
        self.__valor = valor
    @property
    def data(self):
        return self.__data
    @data.setter
    def data(self, valor):
        self.__data = valor

################################################################################
#---------------------------Subclasse | Saque----------------------------------#
class Saque(Transacao):
    def __init__(self, valor, data, senha):
        super().__init__(valor, data)
        self.__senha = senha
#--------------------------Definindo Getters e Setters-------------------------#
    @property
    def senha(self):
        return self.__senha
    @senha.setter
    def senha(self, valor):
        self.__senha = valor

################################################################################
#---------------------------Subclasse | Deposito-------------------------------#
class Deposito(Transacao):
    def __init__(self, valor, data, nomeDepositante):
        super().__init__(valor, data)
        self.__nomeDepositante = nomeDepositante
#--------------------------Definindo Getters e Setters-------------------------#
    @property
    def nomeDepositante(self):
        return self.__nomeDepositante
    
################################################################################
#------------------------Subclasse | Transferencia-----------------------------#
class Transferencia(Transacao):
    def __init__(self, valor, data, senha, tipoTransf):
        super().__init__(valor, data)
        self.__senha = senha
        self.__tipoTransf = tipoTransf # "D" para débito e "C" para crédito
#--------------------------Definindo Getters e Setters-------------------------#
    @property
    def senha(self):
        return self.__senha
    @senha.setter
    def senha(self, valor):
        self.__senha = valor
    @property
    def tipoTransf(self):
        return self.__tipoTransf

################################################################################
#--------------------------Classe | Transferencia------------------------------#
class Conta:
    def __init__(self, nroConta, nome, limite, senha):
        self.__nroConta = nroConta
        self.__nome = nome
        self.__limite = limite
        self.__senha = senha
        self.__transacoes = []
#--------------------------Definindo Getters e Setters-------------------------#
    @property
    def nroConta(self):
        return self.__nroConta
    @property
    def nome(self):
        return self.__nome
    @property
    def limite(self):
        return self.__limite
    @property
    def senha(self):
        return self.__senha
    @property
    def transacoes(self):
        return self.__transacoes
    
#-------------------------------Definindo Funções------------------------------#
#------------------------------------------------------------------------------#
#Função Deposito --> Realiza depositos na conta da pessoa
#------------------------------------------------------------------------------#
    def adicionaDeposito(self, valor, data, nomeDepositante):
        self.__transacoes.append(Deposito(valor, data, nomeDepositante))

#------------------------------------------------------------------------------#
#Função Saque --> Realiza saques/retiradas na conta da pessoa
#Recebe como valor adicional a senha digitada pela pessoa
#Tem como verificar se a senha esta correta e se o saldo é positivo para retirada
#------------------------------------------------------------------------------#
    def adicionaSaque(self, valor, data, senha):
        if senha != self.__senha:
            return False
        if self.calculaSaldo() < valor:
            return False
        self.__transacoes.append(Saque(valor, data, senha))

#------------------------------------------------------------------------------#
#Função Transferencia --> Realiza transferencias entre duas contas
#Recebe como valor adicional a senha digitada pela pessoa e a conta para transferencia
#Tem como verificar se a senha esta correta e se o saldo é positivo para transferencia
#------------------------------------------------------------------------------#
    def adicionaTransf(self, valor, data, senha, contaFavorecido):
        if senha != self.__senha:
            return False
        if self.calculaSaldo() < valor:
            return False
        self.__transacoes.append(Transferencia(valor, data, senha, "D"))
        contaFavorecido.transacoes.append(Transferencia(valor, data, senha, "C"))

#------------------------------------------------------------------------------#
#Função calculaSaldo
#Faz o calculo dos depositos, saques e transferencias da conta
#Verifica se haverá um valor positivo ou negativo na conta
#------------------------------------------------------------------------------#
    def calculaSaldo(self):
        saldo = 0
        for trans in self.transacoes:
            if isinstance(trans, Deposito) or (isinstance(trans, Transferencia) and trans.tipoTransf == "C"):
                saldo += trans.valor
            elif isinstance(trans, Saque) or (isinstance(trans, Transferencia) and trans.tipoTransf == "D"):
                saldo -= trans.valor
        return saldo + self.limite

################################################################################
#---------------------Main Com os Valores da Atividade-------------------------#
if __name__ == "__main__":
    c1 = Conta(1234, 'Jose da Silva', 1000, 'senha1')
    c1.adicionaDeposito(5000, date.today(), 'Antonio Maia')
    if c1.adicionaSaque(2000, date.today(), 'senha1') == False:
        print('Não foi possível realizar o saque no valor de 2000')
    if c1.adicionaSaque(1000, date.today(), 'senha-errada') == False: # deve falhar
        print('Não foi possível realizar o saque no valor de 1000')

    c2 = Conta(4321, 'Joao Souza', 1000, 'senha2')
    c2.adicionaDeposito(3000, date.today(), 'Maria da Cruz')
    if c2.adicionaSaque(1500, date.today(), 'senha2') == False:
        print('Não foi possível realizar o saque no valor de 1500')
    if c2.adicionaTransf(5000, date.today(), 'senha2', c1) == False: # deve falhar
        print('Não foi possível realizar a transf no valor de 5000')
    if c2.adicionaTransf(800, date.today(), 'senha2', c1) == False:
        print('Não foi possível realizar a transf no valor de 800')
    print('--------')
    print('Saldo de c1: {}'.format(c1.calculaSaldo())) # deve imprimir 4800
    print('Saldo de c2: {}'.format(c2.calculaSaldo())) # deve imprimir 1700