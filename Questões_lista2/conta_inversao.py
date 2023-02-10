'''
2. O número de inversões de um vetor V de n elementos é o número de pares ordenados
(i,j) tais que 1 ≤ i < j ≤ n e V[i] > V[j]. Adapte o Mergesort para calcular o número
de inversões de um vetor dado. O consumo de tempo de sua função deve ser O(n log n)
no pior caso. Por exemplo, o vetor [1, 3, 4, 2] tem duas inversões pois possui dois pares
(i,j) que obedecem à restrição, que são, (2,4) e (3,4).
'''

def merge(A, aux, comeco, meio, fim):
 
    k = comeco
    i = comeco
    j = meio + 1
    contador = 0
    
    while i <= meio and j <= fim:

        if A[i] <= A[j]:
            aux[k] = A[i]
            i = i + 1
        else:
            aux[k] = A[j]
            j = j + 1
            contador = contador + (meio - i + 1)        
 
        k = k + 1
 
    while i <= meio:
        aux[k] = A[i]
        k = k + 1
        i = i + 1
 
    for i in range(comeco, fim + 1):
        A[i] = aux[i]
    
    return contador
 
 
def mergesort(A, aux, comeco, fim):
     
    if fim <= comeco:        
        return 0
 
    meio = comeco + (fim - comeco) // 2
    contador = 0
 
    contador = contador + mergesort(A, aux, comeco, meio)     
    contador = contador + mergesort(A, aux, meio + 1, fim)  
    contador = contador + merge(A, aux, comeco, meio, fim)   
 
    return contador

lista = [9,3,0,5,8,4]


f = len(lista)

aux = [0] * f

print(mergesort(lista, aux, 0, f-1))
