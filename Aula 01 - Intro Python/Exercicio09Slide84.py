#criando as listas
listaNomes = []
listaAlturas = []

#listando o nome e altura das pessoas
quant = int(input("Informe o nro de pessoas: "))
for x in range(quant):
    nome = input("Digite o nome: ")
    listaNomes.insert(x, nome)
    altura = float(input("Digite a altura: "))
    listaAlturas.insert(x,altura)

#definindo os maiores valores como os iniciais
maiorAlt = listaAlturas[0]
nomeMaior = listaNomes[0]
menorAlt = listaAlturas[0]
nomeMenor = listaNomes[0]

#comparando os valores
for i in range(1, quant): #a lista sempre começa no 0 e está comparando o restante da lista
    if listaAlturas[i] > maiorAlt:
        maiorAlt = listaAlturas[i]
        nomeMaior = listaNomes[i]
    if listaAlturas[i] < menorAlt:
        menorAlt = listaAlturas[i]
        nomeMenor = listaNomes[i]

print("O mais alto é {} e sua altura é {}".format(nomeMaior, str(maiorAlt)))
print("O mais baixo é {} e sua altura é {}".format(nomeMenor, str(menorAlt)))