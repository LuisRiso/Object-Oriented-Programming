def mdc(m, n):
    while m%n != 0:
        oldm = m
        oldn = n
        m = oldn
        n = oldm%oldn
    return n

def mesmaFracao(f1, f2):
    return (f1.num == f2.num) and (f1.den == f2.den)


class Fracao():
    
    def __init__(self, num, den):
        self.__num = num        
        self.__den = den     
    #Função para imprimir a string pelo metodo especificado
    def __str__(self):
        return str(self.__num) + "/" + str(self.__den)

    @property
    def num(self):
        return self.__num

    @property
    def den(self):
        return self.__den       

    def simplifica(self):
        divComum = mdc(self.__num, self.__den)
        self.__num = self.__num // divComum
        self.__den = self.__den // divComum   

    def __add__(self,outraFrac):
        novoNum = self.__num * outraFrac.den + self.__den * outraFrac.num
        novoDen = self.__den * outraFrac.den
        divComum = mdc(novoNum, novoDen)
        return Fracao(novoNum//divComum, novoDen//divComum)        

class fracaoMista(Fracao):
    def __init__(self, num, den, parteInteira):
        super().__init__(num, den)
        self.__parteInteira = parteInteira
    
    @property
    def parteInteira(self):
        return self.__parteInteira

if __name__ == "__main__":
    frac1 = Fracao(1, 4) 
    frac2 = Fracao(1, 6)
    frac3 = frac1 + frac2 #chama a função __add__ pelo simbulo (+)
    print(frac3)
    print()
    frac1 = Fracao (3, 4)
    frac2 = Fracao(5, 6)
    frac3 = frac1 + frac2 #chama a função __add__ pelo simbulo (+)
    print(frac3)
