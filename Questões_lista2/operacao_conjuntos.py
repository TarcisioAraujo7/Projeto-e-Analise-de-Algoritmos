'''
1. Dados dois conjuntos A de n elementos e B de m elementos, implementados como
vetores, elabore um algoritmo para determinar dois conjuntos: união (U) e diferença
simétrica (I) dos conjuntos A e B. Soluções quadráticas não serão aceitas. Você não
pode usar espaço adicional na solução a menos de variáveis e dos vetores de entrada e
saída acima mencionados. Lembrete: Conjuntos não admitem números repetidos. Logo,
o vetor de saída, por representar um conjunto, não pode ter elementos repetidos.
'''

def max_heap(A,n,i):
    l = esquerda(i)
    r = direita(i)
    
    if l < n and A[l] > A[i]:
        maior = l
    else:
        maior = i
    if r < n and A[r] > A[maior]:
        maior = r
    if maior != i:
        A[i], A[maior] = A[maior], A[i]
        max_heap(A,n, maior)


def esquerda(i):
    return 2 * i + 1


def direita(i):
    return 2 * i + 2


def faz_maxHeap(A):
    n = len(A)
    for i in range(n, -1,-1):
        max_heap(A,n, i)
    for i in range(n-1,0,-1):
        A[0],A[i]=A[i],A[0]
        max_heap(A,i,0)


def uniao_difsimetrica(conjA, conjB, n, m):
    auxA = 0
    auxB = 0
    indexUniao = 0
    indexDif = 0

    uniao = [-1] * (n + m)
    dif_simetrica = [-1] * (n + m)

    faz_maxHeap(conjA)
    faz_maxHeap(conjB)

    while auxA != n and auxB != m :

        if conjA[auxA] < conjB[auxB]:
            uniao[indexUniao] = conjA[auxA]
            indexUniao = indexUniao + 1

            dif_simetrica[indexDif] = conjA[auxA]
            indexDif = indexDif + 1

            auxA = auxA + 1

        elif conjB[auxB] < conjA[auxA]:
            uniao[indexUniao] = conjB[auxB]
            indexUniao = indexUniao + 1

            dif_simetrica[indexDif] = conjB[auxB]
            indexDif = indexDif + 1

            auxB = auxB + 1
        
        elif conjA[auxA] == conjB[auxB]:
            uniao[indexUniao] = conjA[auxA]
            indexUniao = indexUniao + 1
            
            auxA = auxA + 1
            auxB = auxB + 1
    
    
    while auxA != n:
        
        uniao[indexUniao] = conjA[auxA]
        indexUniao = indexUniao + 1
        
        dif_simetrica[indexDif] = conjA[auxA]
        indexDif = indexDif + 1
        
        auxA = auxA + 1
    
    while auxB != m:
        uniao[indexUniao] = conjB[auxB]
        indexUniao = indexUniao + 1
        
        dif_simetrica[indexDif] = conjB[auxB]
        indexDif = indexDif + 1
        
        auxB = auxB + 1


    return uniao, dif_simetrica






cjA = [8,7,23,4,2,1]
cjB = [1,2,23,6,124,7,9]

n = len(cjA) 
m = len(cjB) 

print(uniao_difsimetrica(cjA,cjB,n,m))
