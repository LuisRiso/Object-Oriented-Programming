#Escreva uma função que receba um float representando o valor da temperatura em Celsius e retorne a temperatura equivalente em Farenheit. 
#Em seguida, escreva um código que leia uma temperatura em Celsius e informe o valor equivalente em Farenheit.

#Converte Celsius para Farenheit
def tempFarenheit(celsius):
    farenheit = ((9*celsius + 160)/5)
    return farenheit

#Converte Farenheit para Celsius
#def tempCelsius(gF):
#    celsius = (5*(gF - 32))/9

gC = float(input("Digite sua temperatura em Celsius: "))
tempF = tempFarenheit(gC)
print("A temperatura em Farenheit é: " + str(tempF) + "º")