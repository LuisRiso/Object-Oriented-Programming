#Nome: João Guilherme Alvarenga Serapião
#Matricula: 2024006925

from datetime import date

class Transacao:
    def __init__(self, valor, data):
        self.valor = valor
        self.data = data

class Saque(Transacao):
    def __init__(self, valor, data):
        super().__init__(valor, data)

class Deposito(Transacao):
    def __init__(self, valor, data):
        super().__init__(valor, data)

class Transferencia(Transacao):
    def __init__(self, valor, data, tipoTransf):
        super().__init__(valor, data)
        self.tipoTransf = tipoTransf

class Conta:
    def __init__(self, numero, titular, limite, senha):
        self.numero = numero
        self.titular = titular
        self.limite = limite
        self.senha = senha
        self.transacoes = []

    def adicionaDeposito(self, valor, data, favorecido):
        deposito = Deposito(valor, data)
        self.transacoes.append(deposito)

    def adicionaSaque(self, valor, data, senha):
        if senha != self.senha:
            return False
        if self.calculaSaldo() < valor:
            return False
        saque = Saque(valor, data)
        self.transacoes.append(saque)
        return True

    def adicionaTransf(self, valor, data, senha, contaFavorecido):
        if senha != self.senha:
            return False
        if self.calculaSaldo() < valor:
            return False
        transf_debito = Transferencia(valor, data, "D")
        transf_credito = Transferencia(valor, data, "C")
        self.transacoes.append(transf_debito)
        contaFavorecido.transacoes.append(transf_credito)
        return True

    def calculaSaldo(self):
        saldo = 0
        for transacao in self.transacoes:
            if isinstance(transacao, Deposito) or (isinstance(transacao, Transferencia) and transacao.tipoTransf == "C"):
                saldo += transacao.valor
            elif isinstance(transacao, Saque) or (isinstance(transacao, Transferencia) and transacao.tipoTransf == "D"):
                saldo -= transacao.valor
        return saldo + self.limite

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
