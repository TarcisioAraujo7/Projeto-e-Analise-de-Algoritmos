
def intercala(Y, comeco, meio, fim):

    tamanhoA = meio - comeco + 1
    tamanhoB = fim - meio 
    
    vetorA = [0] * (tamanhoA)
    vetorB = [0] * (tamanhoB)

    for x in range(0, tamanhoA):
        vetorA[x] = Y[comeco + x]
    
    for z in range(0, tamanhoB):
        vetorB[z] = Y[meio + 1 + z ]

    i = 0
    j = 0 
    k = comeco

    while i < tamanhoA and j < tamanhoB:
        if vetorA[i] <= vetorB[j]:
            print(2)
            Y[k] = vetorA[i]
            i = i + 1 
        else:
            print(1)
            Y[k] = vetorB[j]
            j = j + 1 
            
        k = k + 1


    while i < tamanhoA:
        Y[k] = vetorA[i]
        i = i + 1
        k = k + 1


    while j < tamanhoB:
        Y[k] = vetorB[j]
        j = j + 1
        k = k + 1
    

def mergeSort(X, esq,dir):
    if esq < dir:

        meio = esq + (dir - esq) // 2


        mergeSort(X, esq, meio)
        mergeSort(X, meio+1, dir)

        intercala(X,esq,meio,dir)

lista = [3,4,1,2]
f = len(lista)

mergeSort(lista, 0, f-1)

print(lista)