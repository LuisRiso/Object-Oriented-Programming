#Renda Alíquota
#De 1.903,99 até 2.826,65 7,5%
#De 2.826,66 até 3.751,05 15%
#De 3.751,06 até 4.664,68 22,5%
#Acima de 4.664,68 27,5%

renda = float(input("Digite sua renda mensal: "))

if renda < 1903.99:
    aliquota = 0
    imposto = 1903.99*aliquota
elif renda <= 2826.65:
    aliquota = 7.5
    imposto = 2826.65*(aliquota/100)
elif renda <= 3751.05:
    aliquota = 15
    imposto = 3751.05*(aliquota/100)
elif renda <= 4664.68:
    aliquota = 22.5
    imposto = 4664.68*(aliquota/100)
elif renda > 4664.68:
    aliquota = 27.5
    imposto = 466468*(aliquota/100)

print('Aliquota: ' + str(aliquota))
print('Imposto: ' + str(imposto))