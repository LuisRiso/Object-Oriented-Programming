class Produto():
    def __init__(self, codigo, descricao, valorUnitario):
        self.__codigo = codigo
        self.__descricao = descricao
        self.__valorUnitario = valorUnitario

    @property
    def codigo(self):
        return self.__codigo
    @property
    def descricao(self):
        return self.__descricao
    @property
    def valorUnitario(self):
        return self.__valorUnitario

class CtrlProduto():
    def __init__(self):
        self.listaProdutos = [
            Produto(901, 'Refeicao', 40),
            Produto(902, 'Refeicao Crianca', 20),
            Produto(903, 'Guarana lata', 6),
            Produto(904, 'Coca Cola lata', 6),
            Produto(905, 'Suco laranja 400 ml', 8),
            Produto(906, 'Cerveja Heineken lata', 8),
            Produto(907, 'Agua mineral 500 ml', 4),
            Produto(908, 'Sorvete Kibon', 8),
            Produto(909, 'Chocolate Alpino', 6),
            Produto(910, 'Chocolate Lacta', 5)
        ]

    #def getProduto(self, codigo):
    #    prod = None
    #    for product in self.listaProdutos:
    #        if product.codigo == codigo:
    #            prod = product
    #    return prod

    def getListaProdutos(self):
        listaProdutos = []
        for product in self.listaProdutos:
            listaProdutos.append(product)
        return listaProdutos

    def getListaDescricaoProdutos(self):
        listaDescricaoProdutos = []
        for product in self.listaProdutos:
            listaDescricaoProdutos.append(product.descricao)
        return listaDescricaoProdutos

