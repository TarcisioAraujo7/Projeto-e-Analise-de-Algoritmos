'''
Elabore dois algoritmos para calcular o maior elemento de um vetor X de n elementos,
um deles usando indução fraca e o outro usando indução forte.

'''
# Indução fraca

lista = [9,3,5,2,3,2,5]

def maiorFraca(X, n):
    
    if n == 0:
        return X[n]
    else:
        maiorNum = maiorFraca(X, n-1)
        print(n)
        if X[n-1] >= maiorNum:
            return X[n-1]
        else:
            return maiorNum

print(maiorFraca(lista,7))

# Indução forte

def maiorIndForte(X, comeco, final):
    if comeco < final:
        pivo = comeco + (final-comeco)//2

        esq = maiorIndForte(X, comeco, pivo)
        dir = maiorIndForte(X, pivo + 1, final)

        if esq > dir:
            return esq
        else:
            return dir

    return X[comeco]

print(maiorIndForte(lista,0,6))
