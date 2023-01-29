'''
5. Considere o problema de calcular 2^n, para um dado n fornecido como parâmetro do algoritmo.
Você deve formular duas soluções para o problema:
a) algoritmo recursivo que calcula o que se pede aplicando a fórmula:
 2^n = 2^n-1 + 2^n-1;

b) algoritmo iterativo no qual está livre para usar o que desejar.

'''

expoente = 50

# A) 

def elevacao2a(n):
    if n == 0:
        return 1
    else:
        return elevacao2a(n-1) + elevacao2a(n-1)

print(elevacao2a(expoente))

# B)

def elevacao2b(n):

    saida = 1
    for x in range(n):
        saida = 2 * saida

    return saida

print(elevacao2b(expoente))