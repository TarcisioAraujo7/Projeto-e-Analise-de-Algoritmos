'''
2. O número de inversões de um vetor V de n elementos é o número de pares ordenados
(i,j) tais que 1 ≤ i < j ≤ n e V[i] > V[j]. Adapte o Mergesort para calcular o número
de inversões de um vetor dado. O consumo de tempo de sua função deve ser O(n log n)
no pior caso. Por exemplo, o vetor [1, 3, 4, 2] tem duas inversões pois possui dois pares
(i,j) que obedecem à restrição, que são, (2,4) e (3,4).
'''

def intercala(Y, comeco, meio, fim):



    tamanhoA = meio - comeco + 1
    tamanhoB = fim - meio 
    
    print(tamanhoA, " - ", tamanhoB)
    print("Começo", comeco)
    print("Meio", meio)
    print("Fim", fim)

    '''if tamanhoA > tamanhoB:
        tamanhoA = tamanhoA - 1
        tamanhoB = tamanhoB + 1

        vetorA = [0] * (tamanhoA)
        vetorB = [0] * (tamanhoB)

        for x in range(0, tamanhoA):
            vetorA[x] = Y[comeco + x]
    
        for z in range(0, tamanhoB):
            vetorB[z] = Y[meio  + z ]
    else:'''

    vetorA = [0] * (tamanhoA)
    vetorB = [0] * (tamanhoB)
    for x in range(0, tamanhoA):
        vetorA[x] = Y[comeco + x]
    
    for z in range(0, tamanhoB):
        vetorB[z] = Y[meio + 1 + z ]
    
    #[9,3,0,5,8,4]
    
    print(vetorA, vetorB)
    print('\n')

    i = 0
    j = 0 
    k = comeco

    while j < tamanhoB:
        if vetorA[i] > vetorB[j] and i < j:
            print("Contabilizou um")
            i = i + 1 
        else:
            
            j = j + 1 
            
        k = k + 1


    '''while i < tamanhoA:
        Y[k] = vetorA[i]
        i = i + 1
        k = k + 1


    while j < tamanhoB:
        Y[k] = vetorB[j]
        j = j + 1
        k = k + 1'''
    


def mergeSort(X, esq,dir):
    if esq < dir:

        meio = (dir + esq) // 2
        
        mergeSort(X, esq, meio)
        mergeSort(X, meio+1, dir)
        intercala(X,esq,meio,dir)

lista = [9,3,0,5,8,4]
f = len(lista)

mergeSort(lista, 0, f-1)

print(lista)