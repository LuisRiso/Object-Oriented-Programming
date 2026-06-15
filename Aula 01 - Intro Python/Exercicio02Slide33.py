import random # importanto pacote

num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))

nroGerado = random.randrange(num1, num2)
print("Número Gerado: " + str(nroGerado))

#if (num1 < num2):
#    print(random.randrange(num1,num2))
#else:
#    print(random.randrange(num2,num1))