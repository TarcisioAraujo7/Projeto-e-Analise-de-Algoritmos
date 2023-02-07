'''
1. Dados dois conjuntos A de n elementos e B de m elementos, implementados como
vetores, elabore um algoritmo para determinar dois conjuntos: união (U) e diferença
simétrica (I) dos conjuntos A e B. Soluções quadráticas não serão aceitas. Você não
pode usar espaço adicional na solução a menos de variáveis e dos vetores de entrada e
saída acima mencionados. Lembrete: Conjuntos não admitem números repetidos. Logo,
o vetor de saída, por representar um conjunto, não pode ter elementos repetidos.
'''

def uniao_difsimetrica(conjA, conjB, n, m):
    auxA = 0
    auxB = 0

    uniao = []
    dif_simetrica = []

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


cjA = [1,2,4,6,7,8]
cjB = [1,2,4,6,7,9]

n = len(cjA) 
m = len(cjB) 

print(uniao_difsimetrica(cjA,cjB,n,m))
