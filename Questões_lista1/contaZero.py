'''
Dado um vetor cujos elementos só podem assumir os valores 0 ou 1, ordenados em 
ordem crescente, encontre a quantidade de 0s que o vetor possui em tempo O(log n). 
Ex: Para A = [0,0,1,1,1] a resposta seria 2. Para A = [1,1,1] a resposta seria 0. 

'''


def checarCasos(X,n):
    if n == 0 or X[0] == 1:
        return 0
    if X[n-1] == 0:
        return n
    return -1


def buscaBinaria01(X, inicio, fim):
    metade = inicio  + (fim - inicio)//2
    if X[metade] == 0 and X[metade+1] == 1:
        return metade +1
    if X[metade] == 1 and X[metade-1] == 0:
        return metade
    if X[metade] == 1 and X[metade-1] == 1:
        return buscaBinaria01(X, inicio, metade-1)
    if X[metade] == 0 and X[metade+1] == 0:
        return buscaBinaria01(X, metade+1, fim)

def contarZeros(X,n):
    checagem = checarCasos(X,n)
    if checagem != -1:
        return checagem
    else:
        return buscaBinaria01(X,0,n)


lista = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1]
n = len(lista)

print(contarZeros(lista,n))