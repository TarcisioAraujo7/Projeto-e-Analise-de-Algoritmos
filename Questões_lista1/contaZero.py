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

# Returns index of x in arr if present, else -1
def binary_search(arr, low, high, x):
 
    # Check base case
    if high >= low:
 
        mid = (high + low) // 2
 
        # If element is present at the middle itself
        if arr[mid] == 1 and arr[mid-1] == 0 :
            return mid
        elif arr[mid] == 0 and arr[mid+1] == 1:
            return mid+1
        elif arr[high] == 0:
            return high + 1
        elif arr[low] == 0 and arr[low+1]== 1:
            return low + 1
        # If element is smaller than mid, then it can only
        # be present in left subarray
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
 
        # Else the element can only be present in right subarray
        else:
            return binary_search(arr, mid + 1, high, x)
 
    else:
        # Element is not present in the array
        return -1
 
# Test array
arr = [ 2, 3, 4, 10, 40 ]
x = 10
 
# Function call
result = binary_search(arr, 0, len(arr)-1, x)