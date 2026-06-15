################################################################################
#-----------------------Sistema Emissao Nota Fiscal----------------------------#
#-----------Nome: Luís Gustavo Riso Santos --- Matricula: 2024002372-----------#
################################################################################
from abc import ABC, abstractmethod
from datetime import date
#--------------------------Classe | Itens Vendidos-----------------------------#
#Registra cada item vendido para uma classe Venda com seu cod, quant e preco
class ItemVenda():
    def __init__(self, codProd, quant, precoUnit):
        self.__codProd = codProd
        self.__quant = quant
        self.__precoUnit = precoUnit
    
    @property
    def codProd(self):
        return self.__codProd
    @property
    def quant(self):
        return self.__quant
    @property
    def precoUnit(self):
        return self.__precoUnit
    
#--------------------------Classe Abstrata | Venda-----------------------------#
#Registra a NF, a data emissao e os itens vendidos
#Calcula o total vendido na venda
class Venda(ABC):
    def __init__(self, nroNF, dtEmissao):
        self.__nroNF = nroNF
        self.__dtEmissao = dtEmissao
        self.__itens = []

    @property
    def nroNF(self):
        return self.__nroNF
    @property
    def dtEmissao(self):
        return self.__dtEmissao
    @property
    def itens(self):
        return self.__itens
    
    def adicionaItem(self, codProd, quant, precoUnit):
        self.__itens.append(ItemVenda(codProd, quant, precoUnit))
    
    def calculaTotalVendido(self):
        Total = 0.0
        for item in self.__itens:
            Total += item.quant * item.precoUnit
        return Total
    
    @abstractmethod
    def geraNF():
        pass
    @abstractmethod
    def calculaImposto():
        pass

#-------------------------Classe Concreta | Venda PF---------------------------#
#Registra a cpf e nome do comprador
#Calcula o total de imposto
#Gera a NF para a pessoa fisica
class VendaPF(Venda):
    def __init__(self, nroNF, dtEmissao, cpf, nome):
        super().__init__(nroNF, dtEmissao)
        self.__cpf = cpf
        self.__nome = nome
    
    @property
    def cpf(self):
        return self.__cpf
    @property
    def nome(self):
        return self.__nome
    
    def calculaImposto(self):
        return (self.calculaTotalVendido() * (9.0/100.0))

    def geraNF(self):
        print("-----Nota Fiscal PF-----")
        print("Nro Nota Fiscal: {}".format(self.nroNF))
        print("Data Emissao: {}".format(self.dtEmissao))
        print("Cliente: {}".format(self.__nome))
        print("CPF: {}".format(self.cpf))
        print()
        print("Itens Vendidos")
        for item in self.itens:
            print("Codigo Produto: {}".format(item.codProd))
            print("Quantidade Produto: {}".format(item.quant))
            print("Preco Produto: {}".format(item.precoUnit))
            print()
        print("Total Faturado: {}".format(self.calculaTotalVendido()))
        print("Imposto Total: {}".format(self.calculaImposto()))

    
#-------------------------Classe Concreta | Venda PJ---------------------------#
#Registra a cpf e nome do comprador
#Calcula o total de imposto
#Gera a NF para a pessoa fisica
class VendaPJ(Venda):
    def __init__(self, nroNF, dtEmissao, cnpj, nomeFantasia):
        super().__init__(nroNF, dtEmissao)
        self.__cnpj = cnpj
        self.__nomeFantasia = nomeFantasia
    
    @property
    def cnpj(self):
        return self.__cnpj
    @property
    def nomeFantasia(self):
        return self.__nomeFantasia

    def calculaImposto(self):
        return (self.calculaTotalVendido() * (6/100))

    def geraNF(self):
        print("-----Nota Fiscal PJ-----")
        print("Nro Nota Fiscal: {}".format(self.nroNF))
        print("Data Emissao: {}".format(self.dtEmissao))
        print("Cliente: {}".format(self.__nomeFantasia))
        print("CNPJ: {}".format(self.cnpj))
        print()
        print("Itens Vendidos")
        for item in self.itens:
            print("Codigo Produto: {}".format(item.codProd))
            print("Quantidade Produto: {}".format(item.quant))
            print("Preco Produto: {}".format(item.precoUnit))
            print()
        print("Total Faturado: {}".format(self.calculaTotalVendido()))
        print("Imposto Total: {}".format(self.calculaImposto()))

#--------------------------------Código do Main--------------------------------#
#Registra as informações de vendas de clientes
if __name__ == "__main__":
    totalFaturado = 0
    totalImposto = 0
    vendas = []
    vendapf = VendaPF(1000, date.today(), '123456789', 'Joao')
    vendapf.adicionaItem(100, 10, 10)
    vendapf.adicionaItem(100, 10, 20)
    vendapf.adicionaItem(100, 10, 30)
    vendas.append(vendapf)
    vendapj = VendaPJ(1001, date.today(), '987654321', 'Silva Ltda')
    vendapj.adicionaItem(200, 100, 10)
    vendapj.adicionaItem(201, 100, 20)
    vendas.append(vendapj)
    for venda in vendas:
        totalFaturado += venda.calculaTotalVendido()
        totalImposto += venda.calculaImposto()
    print('Total faturado: {}'.format(totalFaturado))
    print('Total pago em impostos: {}'.format(totalImposto))
    #Geração da NF - Não está no main do trabalho
    #Feito como teste de implementacao
    #print()
    #for venda in vendas:
    #    venda.geraNF()
    #    print("\n----------xxx----------\n")