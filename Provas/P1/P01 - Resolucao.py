from abc import ABC, abstractmethod
from abc import ABC

class Cliente:
    def __init__(self, nome, email):
        self.__nome = nome
        self.__email = email
    
    @property
    def nome(self):
        return self.__nome
    
    @property
    def email(self):
        return self.__email
    
class Pedido:
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
        self.__listaItens.append(item)

    def maquinaOk(self):
        # maquina ok se tem gabinete(100), placa mãe(200), processador(300), SSD(400),
        # memória RAM(500) e SO (600)
        gabinete = False
        placaMae = False
        processador = False
        ssd = False
        memoria = False
        so = False
        for item in self.__listaItens:
            if item.produto.codigo >= 700:
                pass
            elif item.produto.codigo >= 600:
                so = True
            elif item.produto.codigo >= 500:
                memoria = True
            elif item.produto.codigo >= 400:
                ssd = True
            elif item.produto.codigo >= 300:
                processador = True
            elif item.produto.codigo >= 200:
                placaMae = True
            elif item.produto.codigo >= 100:
                gabinete = True

        if gabinete & placaMae & processador & ssd & memoria & so:
            return True
        else:
            return False
        
    def imprimePedido(self):
        if not self.maquinaOk():
            return False
        else:
            strPedido = '\nCliente: ' + self.__cliente.nome + '\n\n'
            valorNota = 0
            strPedido += 'Quant - Produto - Preço Unit - Preço Total\n'
            for item in self.__listaItens:
                precoUnit = item.produto.preco + item.produto.calculaImposto()
                precoTotalItem = item.quant * precoUnit
                valorNota += precoTotalItem
                strPedido += str(item.quant) + '     - ' + item.produto.desc + ' - ' + str(precoUnit) + ' - ' + str(precoTotalItem) + '\n'
            strPedido += '\n'
            strPedido += 'Valor total: ' + str(valorNota)
            print(strPedido)
            return True
                    
class ItemPedido:
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
    def calculaImposto(self):
        pass

class ProdutoSoftware(Produto):
    def __init__(self, codigo, desc, preco, versao):
        super().__init__(codigo, desc, preco)
        self.__versao = versao

    @property
    def versao(self):
        return self.__versao
    
    def calculaImposto(self):
        #software até 399,99 paga 5% e acima de 400,00 para 7%
        if self.preco < 400:
            valorImposto = self.preco * 0.05
        else:
            valorImposto = self.preco * 0.07
        return valorImposto

class ProdutoHardware(Produto):
    def __init__(self, codigo, desc, preco, nroSerie):
        super().__init__(codigo, desc, preco)
        self.__nroSerie = nroSerie

    @property
    def nroSerie(self):
        return self.__nroSerie

    def calculaImposto(self):
        # Hardware até 499,99 paga 6%, acima de 500,00 paga 9%
        if self.preco < 500:
            valorImposto = self.preco * 0.06
        else:
            valorImposto = self.preco * 0.09
        return valorImposto
    

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