'''
4. Considere que você tem n fios para conectar, de tamanhos variados. Quando dois fios
são conectados, eles passam a ser considerados como um único fio. A realização de uma
conexão custa um valor proporcional à soma dos tamanhos dos fios que foram
conectados. Por exemplo, para conectar um fio de tamanho 3 com outro de tamanho 5, o
custo é 8x, onde x é o custo base de conexão. Elabore um algoritmo para determinar o
custo mínimo para realizar as conexões de n fios, gerando um único fio conectado.
Soluções quadráticas não serão aceitas.

Para o vetor de fios com tamanhos [2, 4, 8, 4, 5, 3] o custo mínimo para gerar um único
fio seria 65x. Este custo é obtido conectando-se os fios de tamanhos 2 e 3, consumindo
5x e gerando-se um fio de tamanho 5. Em seguida, junta-se os dois fios de tamanho 4,
consumindo-se 8x e depois os dois fios de tamanho 5 (original e conectado),
consumindo-se 10x. Neste ponto temos dois fios de tamanho 8 (original e conectado),
que serão unidos, consumindo-se 16x. Finalmente, este fio seria unido com o de
tamanho 10 (conectado), consumindo 26x. No total, seria gasto (5+8+10+16+26)x =65x.

6 14 18 23 26
[1,1,2,2,3,3,4,4,5,5]
[5, -1, 4, 4, 5, 8]
'''

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
            Y[k] = vetorA[i]
            i = i + 1 
        else:
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

def retornaMenor(lista, n):
    menor = lista[x]

    for x in range(n):
        if lista[x] < menor and lista[x] != -1:
            menor = lista[x]
            lista[x] = -1

    return menor 

def conectaFios(lista, n):

    
    if n <= 1:
        return 0

    mergeSort(lista, 0, n-1)
    
    indexAux = 0
    vetorAux = [0] * (n-1)    
    nAux = 2
    mAux = 0
    vetorAux[0] = lista[nAux] + lista[nAux + 1]

    while nAux < n and mAux < n-1:
        if nAux == n-1:
            indexAux = indexAux + 1
            vetorAux[indexAux] = lista[nAux] + vetorAux[mAux]

        elif lista[nAux] + lista[nAux + 1] >= lista[nAux] + vetorAux[mAux]:
            indexAux = indexAux + 1
            vetorAux[indexAux] = lista[nAux] + vetorAux[mAux]
            mAux = mAux + 1
            nAux = nAux + 1
        else:
            indexAux = indexAux + 1
            vetorAux[indexAux] = lista[nAux] + lista[nAux + 1]
            nAux = nAux + 2
            
    while indexAux < n-1:
        indexAux = indexAux + 1
        vetorAux[indexAux] = vetorAux[mAux] + vetorAux[mAux+1]

    print(vetorAux)

lista = [2,3,4,4,5,8]
conectaFios(lista, len(lista))


    

