'''
Elabore dois algoritmos para calcular o maior elemento de um vetor X de n elementos,
um deles usando indução fraca e o outro usando indução forte.

algoritmo maiorIndFraca(X, n)
inicio
	se n = 0
	então
	    return X[n]
	senão
	    maior := maiorIndFraca(X, n-1)
	    se X[n] >= maior
	    então
	        return X[n]
	    senão
	        return maior
	    

fim

'''

def maior(X, n):
    if n == 0:
        return X[n]
    else:
        maiorNum = maior(X, n-1)
        if X[n] >= maiorNum:
            return X[n]
        else:
            retur maiorNum

print(maior([1,2,3,1,4,2,41,1,2,4,6],11))
