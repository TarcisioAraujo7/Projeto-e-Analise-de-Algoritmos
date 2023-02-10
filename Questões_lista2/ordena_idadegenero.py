'''
3. Suponha que sua entrada seja um vetor de n registros, contendo informações sobre
indivíduos: nome, ano de nascimento, gênero (que por simplificação, considere F, M,
X). Adapte o Quicksort para ordenar este vetor considerando o ano de nascimento e o
gênero, de acordo com o critério a seguir. Indivíduos serão ordenados de forma
crescente pela idade. Indivíduos com a mesma idade devem ser ordenados de acordo
com o gênero: todos os de gênero feminino (F) precedem todos os de gênero masculino
(M) e estes precedem todos os de demais gêneros (X).
'''

class individuo:
    def __init__(self,nome, anoNasc, gen):
        self.nome = nome
        self.anoNasc = anoNasc
        self.gen = gen

    def __str__(self) -> str:
        return self.nome
    
    def __repr__(self):
        return self.nome

def partition(array, low, high):
 
    # choose the rightmost element as pivot
    pivot = array[high]
 
    # pointer for greater element
    i = low - 1
 
    # traverse through all elements
    # compare each element with pivot
    for j in range(low, high):
        if array[j].anoNasc <= pivot.anoNasc:
 
            # If element smaller than pivot is found
            # swap it with the greater element pointed by i
            i = i + 1
 
            # Swapping element at i with element at j
            (array[i], array[j]) = (array[j], array[i])
 
    # Swap the pivot element with the greater element specified by i
    (array[i + 1], array[high]) = (array[high], array[i + 1])
 
    # Return the position from where partition is done
    return i + 1
 
# function to perform quicksort
 
 
def quickSort(array, low, high):
    if low < high:
 
        # Find pivot element such that
        # element smaller than pivot are on the left
        # element greater than pivot are on the right
        pi = partition(array, low, high)
 
        # Recursive call on the left of pivot
        quickSort(array, low, pi - 1)
 
        # Recursive call on the right of pivot
        quickSort(array, pi + 1, high)


lista = [ individuo("Xesquedela", 2003, 'F'),individuo("Alicia", 2003, 'F'), individuo("Lucas", 2012, 'M'), individuo("Tarcisio", 2002, 'M'), individuo("Julia", 2020, 'F')]
n = len(lista)

quickSort(lista, 0, n -1)

print(lista)