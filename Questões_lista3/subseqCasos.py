
casos = [1800, 1900, 1850, 1955, 1750, 2100, 2005, 2215, 2155]
casos1 = [1,5,2,3]

def maior_valor(lista):
    if not lista:
        return None
    
    maior = lista[0]
    for i in range( len(lista)):
        if lista[i] > maior:
            maior = lista[i]
    
    return maior

def subsequencia_crescente_infectados(dados):
    n = len(dados)
    memo = [1] * n
    
    for i in range( n):
        for j in range(i):
            if dados[i] > dados[j]:
                if memo[i] <= memo[j]+1:
                    memo[i] = memo[j] + 1
    
    tam_mais_longa_subsequencia = maior_valor(memo)
    indice = 0
    
    for x in range(n):
        if memo[x] == tam_mais_longa_subsequencia:
            indice = x
    
    subsequencia = [0] * tam_mais_longa_subsequencia
    ultimo_valor = dados[indice]

    aux = tam_mais_longa_subsequencia - 1
    subsequencia[aux] = ultimo_valor

    for k in range(indice - 1, -1, -1):
        if memo[k] == tam_mais_longa_subsequencia - 1 and dados[k] < ultimo_valor:
            aux = aux - 1
            subsequencia[aux] = dados[k]
            tam_mais_longa_subsequencia -= 1
            ultimo_valor = dados[k]
    
    print(subsequencia)


subsequencia_crescente_infectados(casos)
