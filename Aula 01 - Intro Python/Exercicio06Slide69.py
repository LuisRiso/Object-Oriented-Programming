#Leia uma string e verifique se a mesma é um palíndromo

str = input("Digite uma string: ")
palindromo = True
for i in range(0, int(len(str)/2)): #len(str) puxa o tamanho da string
    if str[i] != str[len(str)-i-1]: #comparação entre inicio e final da string
        palindromo = False
        break
if palindromo:
    print(str + " é um palindromo")
else:
    print(str + " não é um palindromo")