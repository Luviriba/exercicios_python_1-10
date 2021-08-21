# 7. Leia um número, mostre seu dobro, triplo, e raíz quadrada.
num = int(input("qual o número?"))
dobro = num * 2
triplo = num * 3
quadruplo = num * 4
quintuplo = num * 5
raiz = pow(num, 1/2)
print("o dobro de {} é {}". format(num, dobro))
print("o triplo de {} é {}". format(num, triplo))
print("o quadruplo de {} é {}". format(num, quadruplo))
print("O quintuplo de {} é {}". format(num, quintuplo))
print("A raiz quadrada de {} é {}". format(num, raiz))
