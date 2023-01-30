'''
Elabore dois algoritmos para calcular o maior elemento de um vetor X de n elementos,
um deles usando indução fraca e o outro usando indução forte.

'''
# Indução forte

lista = [2,3,5,7,2,3,6,2,7,5]

def maiorForte(X, n):
    if n == 0:
        return X[n]
    else:
        maiorNum = maiorForte(X, n-1)
        if X[n-1] >= maiorNum:
            return X[n-1]
        else:
            return maiorNum

print(maiorForte(lista,10))

# Indução fraca

def maiorFraco(X, n, maior):
    if n == 0:
        return maior
    else:
        if X[n-1] >= maior:
            maior = X[n-1]
            return maiorFraco(X,n-1,maior)
        else:
            return maiorFraco(X,n-1,maior)

print(maiorFraco(lista,10,lista[0]))
