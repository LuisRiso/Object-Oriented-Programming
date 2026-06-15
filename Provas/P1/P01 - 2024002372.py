#----------------------Sistema de Gestão de Pedidos Loja-----------------------#
#-----------Nome: Luís Gustavo Riso Santos --- Matricula: 2024002372-----------#
################################################################################
from abc import ABC, abstractmethod
################################################################################
class Produto(ABC):
    def __init__(self, codigo, desc, preco):
        self.__codigo = codigo
        self.__desc = desc
        self.__preco = preco
    
    @property
    def codigo(self):
        return self.__codigo
    @property
    def desc(self):
        return self.__desc
    @property
    def preco(self):
        return self.__preco
    
    @abstractmethod
    def calculaImposto():
        pass

class ProdutoSoftware(Produto):
    def __init__(self, codigo, desc, preco, versao):
        super().__init__(codigo, desc, preco)
        self.__versao = versao
    
    @property
    def versao(self):
        return self.__versao

    def calculaImposto(self):
        if self.preco <= 399.99:
            return self.preco*1.05
        else:
            return self.preco*1.07

class ProdutoHardware(Produto):
    def __init__(self, codigo, desc, preco, nroSerie):
        super().__init__(codigo, desc, preco)
        self.__nroSerie = nroSerie
    
    @property
    def nroSerie(self):
        return self.__nroSerie
    
    def calculaImposto(self):
        if self.preco <= 499.99:
            return self.preco*1.06
        else:
            return self.preco*1.09

#------------------------------------------------------------------------------#

class ItemPedido():
    def __init__(self, nroItem, produto, quant):
        self.__nroItem = nroItem
        self.__produto = produto
        self.__quant = quant

    @property
    def nroItem(self):
        return self.__nroItem
    @property
    def produto(self):
        return self.__produto
    @property
    def quant(self):
        return self.__quant

#------------------------------------------------------------------------------#

class Pedido():
    def __init__(self, numero, cliente):
        self.__numero = numero
        self.__cliente = cliente
        self.__listaItens = []

    @property
    def numero(self):
        return self.__numero
    @property
    def cliente(self):
        return self.__cliente
    @property
    def listaItens(self):
        return self.__listaItens
    
    def addItem(self, item):
        if item.produto.codigo >= 100 and item.produto.codigo <= 599:
            self.listaItens.append(ItemPedido(item.nroItem, ProdutoHardware(item.produto.codigo, item.produto.desc, item.produto.preco, item.produto.nroSerie), item.quant))
        if item.produto.codigo >= 600 and item.produto.codigo <= 699:
            self.listaItens.append(ItemPedido(item.nroItem, ProdutoSoftware(item.produto.codigo, item.produto.desc, item.produto.preco, item.produto.versao), item.quant))
    
    def maquinaOk(self):
        gabinete = 0
        placaMae = 0
        processador = 0
        ssd = 0
        penteMemoria = 0
        SistemaOpp = 0
        for itens in self.__listaItens:
            if itens.produto.codigo >= 100 and itens.produto.codigo < 199:
                gabinete += 1
            if itens.produto.codigo >= 200 and itens.produto.codigo < 299:
                placaMae += 1
            if itens.produto.codigo >= 300 and itens.produto.codigo < 399:
                processador += 1
            if itens.produto.codigo >= 400 and itens.produto.codigo < 499:
                ssd += 1
            if itens.produto.codigo >= 500 and itens.produto.codigo < 599:
                penteMemoria += 1
            if itens.produto.codigo >= 600 and itens.produto.codigo < 699:
                SistemaOpp += 1

        if gabinete == 1 and placaMae == 1 and processador == 1 and ssd >= 1 and penteMemoria == 1 and SistemaOpp == 1:
            return True
        else:
            return False
    
    def imprimePedido(self):
        if self.maquinaOk() == 0:
            return False
        else:
            print("\n")
            print("Cliente: {}\n".format(self.__cliente.nome))
            print("Quant - Produto - Preço Unit - Preço Total")
            total = 0
            for itens in self.__listaItens:
                print("{}     - {} - {:.1f} - {:.1f}".format(itens.quant, itens.produto.desc, itens.produto.calculaImposto(), itens.produto.calculaImposto()*itens.quant))
                total += itens.produto.calculaImposto()*itens.quant
            print("\nValor total: {:.1f}\n".format(total))
            return True

#------------------------------------------------------------------------------#

class Cliente():
    def __init__(self, nome, email):
        self.__nome = nome
        self.__email = email

    @property
    def nome(self):
        return self.__nome
    @property
    def email(self):
        return self.__email

#------------------------------------------------------------------------------# 

if __name__ == "__main__":    
    prod1 = ProdutoHardware(101, 'Gabinete Padrão', 200, '12345')
    prod2 = ProdutoHardware(102, 'Gabinete Gamer', 300, '23451')
    prod3 = ProdutoHardware(201, 'Placa Mãe ASUS ROG', 1400, '345123')
    prod4 = ProdutoHardware(202, 'Placa Mãe Gigabyte Elite', 1800, '45123')
    prod5 = ProdutoHardware(301, 'Intel Core I5', 900, '51234')
    prod6 = ProdutoHardware(302, 'AMD Ryzen 7', 700, '67890')
    prod7 = ProdutoHardware(401, 'SSD 256', 200, '78906')
    prod8 = ProdutoHardware(402, 'SSD 512', 300, '89067')
    prod9 = ProdutoHardware(501, 'Pente memória 8GB', 180, '90678')
    prod10 = ProdutoSoftware(601, 'Windows 11 Home Edition', 250, '23H2')

    cliente1 = Cliente('João Santos', 'santos@gmail.com')
    cliente2 = Cliente('Maria Souza', 'souza@gmail.com')

    pedido1 = Pedido(1001, cliente1)
    pedido1.addItem(ItemPedido(1, prod1, 1))
    pedido1.addItem(ItemPedido(2, prod3, 1))
    pedido1.addItem(ItemPedido(3, prod7, 1))
    pedido1.addItem(ItemPedido(4, prod9, 2))
    if not pedido1.imprimePedido():
        print("\nPedido está incompleto")

    pedido2 = Pedido(1002, cliente2)
    pedido2.addItem(ItemPedido(1, prod2, 1))
    pedido2.addItem(ItemPedido(2, prod4, 1))
    pedido2.addItem(ItemPedido(3, prod6, 1))
    pedido2.addItem(ItemPedido(4, prod8, 1))
    pedido2.addItem(ItemPedido(5, prod9, 2))
    pedido2.addItem(ItemPedido(6, prod10, 1))
    if not pedido2.imprimePedido():
        print("\nPedido está incompleto")