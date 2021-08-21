# 9. Faça um programa que leia um valor em metros, mostre o valor convertido em centímetros, e milímetros.
metros = float(input("Digite quantos metros você quer converter"))
cent = metros * 100
mili = metros * 1000
print('{} metros convertido para centímetros é igual a {:.0f}cm,'.format(metros, cent))
print("{} metros convertido para milímetros é {:.0f}mm.".format(metros, mili))