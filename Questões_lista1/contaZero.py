'''
Dado um vetor cujos elementos só podem assumir os valores 0 ou 1, ordenados em 
ordem crescente, encontre a quantidade de 0s que o vetor possui em tempo O(log n). 
Ex: Para A = [0,0,1,1,1] a resposta seria 2. Para A = [1,1,1] a resposta seria 0. 

algoritmo contarZeros(X, n, pivo)
início
	pivo:= n/2
	se pivo = 1
	então retorne 1
	senão
	    se X[pivo] < X[pivo+1]
	    então retorne pivo + contarZeros(X, 2, 0)
	    se X[pivo-1] < X[pivo]
	    então retorne pivo-1 + contarZeros(X, 2, 0)
    senão
        se X[pivo]= 0 && X[pivo +1]= 0
	  então retorne contarZeros(X,n*2 - pivo,0)
	  se X[pivo]= 1 && X[pivo-1]= 1
	  então retorne contarZeros(X,n/2,0)


fim

'''

def contaZeros(X,n):
    pivo = n // 2
    print(pivo, X[pivo])
    if pivo == 1:
        return 1
    else:
        if X[pivo-1] < X[pivo]:
            return (pivo-1) + contaZeros(X,2)
        if X[pivo] < X[pivo+1]:
            return pivo + contaZeros(X, 2)
        else:
            if X[pivo] == 0 and X[pivo +1] == 0:
                return contaZeros(X, (n*2) - pivo)
            if X[pivo] == 1 and X[pivo-1] == 1:
                return contaZeros(X, n//2)

lista = [0,0,0,0,0,0,0,0,0,1]

print(contaZeros(lista,len(lista)))