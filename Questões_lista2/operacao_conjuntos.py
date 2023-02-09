'''
1. Dados dois conjuntos A de n elementos e B de m elementos, implementados como
vetores, elabore um algoritmo para determinar dois conjuntos: união (U) e diferença
simétrica (I) dos conjuntos A e B. Soluções quadráticas não serão aceitas. Você não
pode usar espaço adicional na solução a menos de variáveis e dos vetores de entrada e
saída acima mencionados. Lembrete: Conjuntos não admitem números repetidos. Logo,
o vetor de saída, por representar um conjunto, não pode ter elementos repetidos.
'''

def max_heapify(A,n,i):
    l = left(i)
    r = right(i)
    
    if l < n and A[l] > A[i]:
        largest = l
    else:
        largest = i
    if r < n and A[r] > A[largest]:
        largest = r
    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        max_heapify(A,n, largest)


def left(i):
    return 2 * i + 1


def right(i):
    return 2 * i + 2


def build_max_heap(A):
    n = len(A)
    for i in range(n, -1,-1):
        max_heapify(A,n, i)
    for i in range(n-1,0,-1):
        A[0],A[i]=A[i],A[0]
        max_heapify(A,i,0)


def uniao_difsimetrica(conjA, conjB, n, m):
    auxA = 0
    auxB = 0

    uniao = []
    dif_simetrica = []

    build_max_heap(conjA)
    build_max_heap(conjB)

    while auxA != n and auxB != m :

        if conjA[auxA] < conjB[auxB]:
            uniao.append(conjA[auxA])
            dif_simetrica.append(conjA[auxA])

            auxA = auxA + 1

        elif conjB[auxB] < conjA[auxA]:
            uniao.append(conjB[auxB])
            dif_simetrica.append(conjB[auxB])

            auxB = auxB + 1
        
        elif conjA[auxA] == conjB[auxB]:
            uniao.append(conjA[auxA])
            auxA = auxA + 1
            auxB = auxB + 1
    
    
    while auxA != n:
        
        uniao.append(conjA[auxA])
        dif_simetrica.append(conjA[auxA])
        auxA = auxA + 1
    
    while auxB != m:
        uniao.append(conjB[auxB])
        dif_simetrica.append(conjB[auxB])
        auxB = auxB + 1


    return uniao, dif_simetrica






cjA = [8,7,23,4,2,1]
cjB = [1,2,23,6,124,7,9]

n = len(cjA) 
m = len(cjB) 

print(uniao_difsimetrica(cjA,cjB,n,m))
