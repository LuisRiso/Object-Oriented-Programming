#Leia valores numéricos e os coloque numa lista. A leitura termina quando o valor 0 for digitado. 
# Em seguida, calcule a média dos valores digitados e informe o usuário.

lista = [] #criação da lista
while True:
    nro = int(input("Digite um número: "))
    if nro == 0: #quebra o código com o valor 0
            break
    else:
        lista.append(nro) #adiciona o numero a lista
soma = 0
for nro in lista:
    soma += nro
media = soma / len(lista) #len me da o comprimento da lista
print("A média é: " + str(media))