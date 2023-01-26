'''
Considere um vetor de números inteiros positivos, com mesmo número de pares e ímpares.
Elabore um algoritmo iterativo para construir um vetor de saída em que os números pares e ímpares estejam alternados, nas duas situações abaixo.
Para cada situação, calcule detalhadamente a complexidade de tempo e espaço de seu algoritmo e justifique se o algoritmo é ou não estável.
Implemente as duas soluções e teste-as.
a) com a possibilidade de usar um vetor auxiliar de mesmo tamanho do vetor de entrada;
b) sem a possibilidade de usar espaço adicional.
'''


# B)

def alternaParImpar(vetorA, n):

    saida = []
    
    for i in range(n):
        saida.append(0)
        
    print(saida)
    auxPar = 0
    auxImpar = 1
    for i in range(n):
        if vetorA[i] % 2 == 0:
            saida[auxPar] = vetorA[i]
            auxPar = auxPar + 2
        else:
            saida[auxImpar] = vetorA[i]
            auxImpar = auxImpar + 2

    return saida

print(alternaParImpar([1,4,3,1,2,2],6))