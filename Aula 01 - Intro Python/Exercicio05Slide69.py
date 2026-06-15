#Leia um conjunto de nomes e os armazene numa lista. 
#Em seguida, leia um nome e verifique se o mesmo faz parte dessa lista

listaNomes = []

i = 0
quant = int(input("Quantos nomes deseja ler? "))
while i < quant:
    nome = input("Digite um nome: ")
    listaNomes.append(nome)
    i = i + 1

#i = 's'
#while i == "s":
#    nome = input("Digite um nome: ")
#    listaNomes.append(nome)
#    i = input("Deseja cadastrar mais um nome? (s/n): ")

verificaNome = input("Digite o nome que deseja verificar: ")
if verificaNome in listaNomes:
    print(verificaNome + ' está na lista')
else:
    print(verificaNome + ' não está na lista')
