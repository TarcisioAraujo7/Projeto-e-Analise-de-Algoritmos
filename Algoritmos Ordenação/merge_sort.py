def mergeSort(X, esq,dir):
    if esq < dir:
        meio = (esq + dir) // 2
        mergeSort(X, esq, meio)
        mergeSort(X, meio+1, dir)

def intercala(Y, comeco, meio, fim):
    vetorA = []
    vetorB = []

    for x in range(comeco, meio):
        vetorA.append(Y[x])
    
    for x in range(meio, fim):
        vetorB.append(Y[x])

    tamanhoA = meio - comeco + 1
    tamanhoB = final - meio

    i = 1
    j = 1 
    k = comeco

    while i <= tamanhoA and j <= tamanhoB:
        # print("--------\n", vetorA[i], vetorB[j], Y)
        if vetorA[i] <= vetorB[j]:
            Y[k] = vetorA[i]
            i = i + 1 
        else:
            Y[k] = vetorB[j]
            j = j + 1 

    
    
    return Y

lista = [2,1,3,4,5]
final = len(lista)
print(intercala(lista, 0,(0+final)//2,final))