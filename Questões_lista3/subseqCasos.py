def maior_subsequencia_crescente(casos):
    n = len(casos)
    dp = [1] * n
    pred = [-1] * n
    for i in range(n):
        for j in range(i):
            if casos[i] > casos[j]:
                dp[i] = max(dp[i], dp[j] + 1)
                pred[i] = j
    return pred

casos = [1800, 1900, 1850, 1955, 1750, 2100, 2005, 2215, 2155]
# print(maior_subsequencia_crescente(casos)) # saída: 5

# [1,5,2,3]
def lcs_infectados(casos):
    n = len(casos)
    # inicializa a lista de tamanho das subsequências crescentes e a lista de predecessores
    lcs = [1] * n
    pred = [-1] * n
    # encontra a mais longa subsequência crescente
    for i in range(n):
        for j in range(i):
            if casos[j] < casos[i]:
                if lcs[j] + 1 > lcs[i]:
                    lcs[i] = lcs[j] + 1
                    pred[i] = j
    # encontra o índice do elemento final da lcs
    max_idx = 0
    for i in range(n):
        if lcs[i] > lcs[max_idx]:
            max_idx = i
    # encontra a lcs
    lcs_infectados = []
    while max_idx != -1:
        lcs_infectados.append(casos[max_idx])
        max_idx = pred[max_idx]
    lcs_infectados.reverse()
    return lcs_infectados

print(lcs_infectados(casos))

def maior_valor(lista):
    if not lista:
        return None
    
    maior = lista[0]
    for i in range(1, len(lista)):
        if lista[i] > maior:
            maior = lista[i]
    
    return maior

def subsequencia_crescente_infectados(dados):
    n = len(dados)
    memo = [1] * n
    
    for i in range(1, n):
        for j in range(i):
            if dados[i] > dados[j]:
                memo[i] = max(memo[i], memo[j] + 1)
    
    tam_mais_longa_subsequencia = maior_valor(memo)
    indice = memo.index(tam_mais_longa_subsequencia)
    
    subsequencia = [dados[indice]]
    for k in range(indice - 1, -1, -1):
        if memo[k] == tam_mais_longa_subsequencia - 1 and dados[k] < subsequencia[-1]:
            subsequencia.append(dados[k])
            tam_mais_longa_subsequencia -= 1
    
    return list(reversed(subsequencia))

print(subsequencia_crescente_infectados(casos))
