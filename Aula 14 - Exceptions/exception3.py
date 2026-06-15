# imprime o número recíproco apenas de números pares

try:
    num = int(input("Digite um número: "))
    assert num % 2 == 0 #assert -> operador que gera True o False | False dentro de um Try é considerado uma falha
except:
    print("Não é um número par!")
else:
    reciproco = 1/num
    print(reciproco)