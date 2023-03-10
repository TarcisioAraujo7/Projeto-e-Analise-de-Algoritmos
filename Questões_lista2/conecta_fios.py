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


def conectaFios(lista, n):

    
    if n <= 1:
        return 0

    mergeSort(lista, 0, n-1)
    
    indexAux = 1
    somas = [-1] * (n-1)    
    nAux = 2
    mAux = 0
    somas[0] = lista[0] + lista[1]

    while nAux < n-1:
        if somas[1] != -1:
            print(lista, nAux)
            somaOriginais = lista[nAux] + lista[nAux + 1]
            print("Soma Originais: ", lista[nAux], " + " ,lista[nAux + 1], " = ", somaOriginais)

            somaFeitos = somas[mAux] + somas[mAux + 1]
            print("Soma Feitos: ", somas[mAux], " + " ,somas[mAux + 1], " = ", somaFeitos)

            somaOriginalFeito = lista[nAux] + somas[mAux]
            print("Soma Original Feito: ", lista[nAux], " + " ,somas[mAux], " = ", somaOriginalFeito)
            

            if somaOriginais <= somaOriginalFeito and somaOriginais <= somaFeitos:
                print('Entrou Originais')
                somas[indexAux] = somaOriginais
                indexAux = indexAux + 1
                nAux = nAux + 2
            elif somaOriginalFeito <= somaOriginais and somaOriginalFeito <= somaFeitos:
                print('Entrou Original Feitos')

                somas[indexAux] = somaOriginalFeito
                mAux = mAux + 1
                nAux = nAux + 1
                indexAux = indexAux + 1
            else:
                print('Entrou Feitos')

                somas[indexAux] = somaFeitos
                indexAux = indexAux + 1
                mAux = mAux + 2
            print('------------------------------------------')
        else:
            somaOriginais = lista[nAux] + lista[nAux + 1]
            print("Soma Originais: ", lista[nAux], " + " ,lista[nAux + 1], " = ", somaOriginais)
            somaOriginalFeito = lista[nAux] + somas[mAux]
            print("Soma Original Feitos: ", lista[nAux], " + " ,somas[mAux], " = ", somaOriginalFeito)


            if somaOriginais <= somaOriginalFeito:
                print('Entrou Originais')
                somas[indexAux] = somaOriginais
                indexAux = indexAux + 1
                nAux = nAux + 2
            else:
                print('Entrou Original Feitos')
                somas[indexAux] = somaOriginalFeito
                mAux = mAux + 1
                nAux = nAux + 1
                indexAux = indexAux + 1
            print('------------------------------------------')


    
    saida = 0
    for x in range(n-1):
        if somas[x] == -1:
            print(somas,somas[x])
            if (nAux == n-1 and lista[nAux] + somas[mAux] <= somas[mAux] + somas[mAux + 1]) or x == n-2 and nAux == n-1:
                print('a')
                somas[indexAux] = lista[nAux] + somas[mAux]
                nAux = nAux + 1
                mAux = mAux + 1
                indexAux = indexAux + 1
            else:
                print('b')
                somas[indexAux] = somas[mAux] + somas[mAux + 1]
                indexAux = indexAux + 1
                mAux = mAux + 2
        
        saida = saida + somas[x]

    print(somas, saida)
    return saida

lista = [2, 4, 8, 4, 5, 3]
conectaFios(lista, len(lista))
