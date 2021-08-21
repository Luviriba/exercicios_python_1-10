# 6. Faça um programa que mostre a soma de dois valores, e depois mostre o antecessor e o sucessor do mesmo.
primeiroNúmero = int(input("Primeiro número"))
segundoNúmero = int(input("Segundo número"))
resutado = primeiroNúmero + segundoNúmero
print("a soma de {} e {} é igual a: {}". format(primeiroNúmero, segundoNúmero, resutado))
sucessor = resutado + 1
antecessor = resutado - 1
print("O sucessor de {} é: {}.". format(resutado, sucessor))
print("O antecessor de {} é: {}.". format(resutado, antecessor))
