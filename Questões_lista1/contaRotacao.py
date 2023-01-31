def checarCasos(X,n):
    if n==1 or n == 0 or X[n-1] > X[0]:
        return 0
    if X[0] > X[1]:
        return 1
    else:
        return -1


def buscaBinariaRota(X, inicio, fim):
    metade = inicio  + (fim - inicio)//2
    print(X, inicio, fim, metade)
    if X[metade] > X[metade+1]:
        return metade + 1
    if X[metade] < X[metade-1]:
        return metade 
    if X[metade] == 1 and X[metade-1] == 1:
        return buscaBinariaRota(X, inicio, metade-1)

    if X[metade] == 0 and X[metade+1] == 0:
        return buscaBinariaRota(X, metade+1, fim)

def contarRota(X,n):
    checagem = checarCasos(X,n)
    if checagem != -1:
        return checagem
    else:
        return buscaBinariaRota(X,0,n)


lista = [7,9,2,3,5,6]
n= len(lista)

print(contarRota(lista,n))