from abc import ABC, abstractmethod

##########################################################################################################################################
#classe transação --> 0...*
class Transacao():
    def __init__(self, valor, desc):
        self.__valor = valor
        self.__desc = desc
    @property
    def valor(self):
        return self.valor
    @property
    def desc(self):
        return self.desc

##########################################################################################################################################
#classe mãe abstrata para conta
class Conta(ABC):
    def __init__(self, nroConta, nome, saldo):
        self.__nroConta = nroConta
        self.__nome = nome
        self.__saldo = saldo
        self.__listaTrans = []
        #é a lista que vai permitir criar uma transação e alocar uma transção na conta
        #inicia como uma lista vazia
        #cada conta concreta vai herder uma lista própria
        #as listas de transações não vai ser compartilhadas
        #assim, você consegue saber qual objeto fez a transação
#------------------------------------------------------------------------------------------------------------------------------------
    @property
    def nroConta(self):
        return self.__nroConta
    @nroConta.setter
    def nroConta(self, valor):
        self.__nroConta = valor
#------------------------------------------------------------------------------------------------------------------------------------
    @property
    def nome(self):
        return self.__nome
    @nome.setter
    def nome(self, valor):
        self.__nome = valor
#------------------------------------------------------------------------------------------------------------------------------------
    @property
    def saldo(self):
        return self.__saldo
    @saldo.setter
    def saldo(self, valor):
        self.__saldo = valor
 #------------------------------------------------------------------------------------------------------------------------------------   
    @property
    def listaTrans(self):
        return self.__listaTrans
#------------------------------------------------------------------------------------------------------------------------------------
    def deposito(self, valor, desc): #vai receber o valor do deposito e a descrição
        self.__listaTrans.append(Transacao(valor, desc)) #está instanciando o objeto transação e appendando ele em uma lista
        self.__saldo += valor #vai iterar o valor do deposito da transação no valor da conta
#------------------------------------------------------------------------------------------------------------------------------------
    def saque(self, valor, desc):
        if valor > 0:
            return False #função Booleana, para aqui se der errado
        if self.__saldo + valor < 0:
            return False #função Booleana, para aqui se der errado
        self.__listaTrans.append(Transacao(valor, desc))
        self.__saldo += valor
        return True #obrigatorio pois criamos uma função Booleana
#------------------------------------------------------------------------------------------------------------------------------------
    @abstractmethod
    def impExtrato():
        pass

##########################################################################################################################################
#classe Conta Limite
class ContaLimite(Conta):
    def __init__(self, nroConta, nome, saldo, limite):
        super().__init__(nroConta, nome, saldo)
        self.__limite = limite
#------------------------------------------------------------------------------------------------------------------------------------
    @property
    def limite(self):
        return self.__limite
 #------------------------------------------------------------------------------------------------------------------------------------   
    def saque(self, valor, desc):
        if valor > 0:
            return False  
        #vai considerar o limite adicional que ele tem permissao de sacar na conta
        #self.saldo --> está referenciando a super classe, não pode ter ser self.__saldo porque não está referenciado dentro da classe
        #self.limite --> puxa da própria property, então ele vai referenciar de qualquer jeito
        if self.saldo + self.__limite + valor < 0: #foi feita uma sobescrita de método
            return False 
        self.listaTrans.append(Transacao(valor, desc)) #a lista é uma propriedade da superclasse, não vai usar o __
        self.saldo += valor
        return True
#------------------------------------------------------------------------------------------------------------------------------------    
    def impExtrato(self):
        print("Nro Conta: {}".format(self.nroConta))
        print("Nome: {}".format(self.nome))
        print("Saldo: {}".format(self.saldo))
        print("Saldo + Limite: {}".format(self.saldo + self.__limite))

####################################################################################################################################################
#classe Conta Conrrente
class ContaCorrente(Conta):
    def __init__(self, nroConta, nome, saldo, mensalidade):
        super().__init__(nroConta, nome, saldo)
        self.__mensalidade = mensalidade
#------------------------------------------------------------------------------------------------------------------------------------
    @property
    def mensalidade(self):
        return self.__mensalidade
#------------------------------------------------------------------------------------------------------------------------------------
    def impExtrato(self):
        print("Nro Conta: {}".format(self.nroConta))
        print("Nome: {}".format(self.nome))
        print("Saldo: {}".format(self.saldo))
        print("Mensalidade: {}".format(self.__mensalidade))

####################################################################################################################################################
#classe Conta Poupança

class ContaPoupanca(Conta):
    def __init__(self, nroConta, nome, saldo, diaAniv):
        super().__init__(nroConta, nome, saldo)
        self.__diaAniv = diaAniv
#------------------------------------------------------------------------------------------------------------------------------------
    @property
    def diaAniv(self):
        return self.__diaAniv
#------------------------------------------------------------------------------------------------------------------------------------
    def impExtrato(self):
        print("Nro Conta: {}".format(self.nroConta))
        print("Nome: {}".format(self.nome))
        print("Saldo: {}".format(self.saldo))
        print("Dia Aniversario: {}".format(self.__diaAniv))

####################################################################################################################################################
#Inserção de valores
if __name__=="__main__":
    contas = [] #cria uma lista de contas para ser impresso em sequencia
#--------------------------------------------------------------------------------------
#Cria uma conta limite
    cl = ContaLimite(1111, "Ana Souza", 0, 1000)
    cl.deposito(1500, "Crédito salário")
    if cl.saque(-1200, "Pagto boleto"):
        print("Saque realiza na conta {}".format(cl.nroConta))
    else:
        print("Falha ao realizar o saque na conta {}".format(cl.nroConta))
    if cl.saque(-500, "Pix"):
        print("Saque realiza na conta {}".format(cl.nroConta)) 
    else:
        print("Falha ao realizar o saque na conta {}".format(cl.nroConta)) 
    
    contas.append(cl)
    print()
#--------------------------------------------------------------------------------------
#Cria uma conta corrente
    cc = ContaCorrente(1112, "Luis Riso", 0, 30)
    cc.deposito(3000, "Crédito salário")
    if cc.saque(-2200, "Pagto boleto"):
        print("Saque realiza na conta {}".format(cc.nroConta))
    else:
        print("Falha ao realizar o saque na conta {}".format(cc.nroConta))
    if cc.saque(-1000, "Pix"):
        print("Saque realiza na conta {}".format(cc.nroConta)) 
    else:
        print("Falha ao realizar o saque na conta {}".format(cc.nroConta)) 

    contas.append(cc)
    print()
#--------------------------------------------------------------------------------------
#Cria uma conta poupança
    cp = ContaPoupanca(1113, "João Cleber", 0, 16)
    cp.deposito(20000, "Crédito salário")
    if cp.saque(-6200.20, "Pagto boleto"):
        print("Saque realiza na conta {}".format(cp.nroConta))
    else:
        print("Falha ao realizar o saque na conta {}".format(cp.nroConta))
    if cp.saque(-1000, "Pix"):
        print("Saque realiza na conta {}".format(cp.nroConta)) 
    else:
        print("Falha ao realizar o saque na conta {}".format(cp.nroConta)) 

    contas.append(cp)
    print()
#--------------------------------------------------------------------------------------
#Imprime a lista de contas
    for conta in contas:
        conta.impExtrato()
        print()