'''
Considere um vetor de números inteiros positivos, com mesmo número de pares e ímpares.
Elabore um algoritmo iterativo para construir um vetor de saída em que os números pares e ímpares estejam alternados, nas duas situações abaixo.
Para cada situação, calcule detalhadamente a complexidade de tempo e espaço de seu algoritmo e justifique se o algoritmo é ou não estável.
Implemente as duas soluções e teste-as.
a) com a possibilidade de usar um vetor auxiliar de mesmo tamanho do vetor de entrada;
b) sem a possibilidade de usar espaço adicional.
'''
# A)

def alternaParImparA(vetorA,n):

    vetorAux = []
    saida = []

    for i in range(n):
        saida.append(0)

    for i in range(n//2):
        vetorAux.append(0)

    auxiliar = 0
    for i in range(n):
        if vetorA[i] % 2 != 0:
            vetorAux[auxiliar] = vetorA[i]
            vetorA[i] = -1
            auxiliar = auxiliar + 1

    auxiliar = 0
    auxiliarImpar = 0
    for i in range(n):
        if vetorA[i] != -1:
            saida[auxiliar] = vetorA[i]
            saida[auxiliar + 1] = vetorAux[auxiliarImpar]

            auxiliar = auxiliar + 2
            auxiliarImpar = auxiliarImpar + 1

    return saida


def alternaParImparB(vetorA, n):

    saida = []
    
    for i in range(n):
        saida.append(0) # complexidade do append = con

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

# B)

def alternaParImparC(vetorA, n):

    auxiliar = n // 2
    for i in range(n // 2):
        if vetorA[i] % 2 != 0:
            iaux = -1
            while iaux == -1:
                if vetorA[auxiliar] % 2 == 0:
                    iaux = vetorA[auxiliar]
                    vetorA[auxiliar] = vetorA[i]
                    vetorA[i] = iaux
                    auxiliar = auxiliar + 1
                else:
                    auxiliar = auxiliar + 1
                    
    auxiliar = n-2
    for i in range(n // 2):
        
        print(i, auxiliar)
        if i % 2 != 0:
            auxTroca = vetorA[auxiliar]
            vetorA[auxiliar] = vetorA[i]
            vetorA[i] = auxTroca
            auxiliar = auxiliar - 2


    return vetorA


# print(alternaParImparA([1,1,1,2,2,2],6))
# print(alternaParImparB([1,4,3,1,2,2],6))
print(alternaParImparC([1,1,1,2,2,2,1,2],8))