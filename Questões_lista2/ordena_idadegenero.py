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
        return str(self.anoNasc) + ' - ' + self.gen

def primeiro_menor(ind1, ind2):
    gen1 = ind1.gen
    gen2 = ind2.gen
    
    # F < M < X

    if gen1 == 'M' and gen2 == 'X':
        return True
    elif gen1 == 'F' and (gen2 == 'X' or gen2 == 'M'):
        return True
    else: 
        return False

def particao(lista, inicio, fim):

    pivot = lista[fim]
    i = inicio

    for j in range(inicio, fim):
        if lista[j].anoNasc < pivot.anoNasc:
            lista[j], lista[i] = lista[i], lista[j]
            # incrementa-se o limite dos elementos menores que o pivô
            i = i + 1
        if  lista[j].anoNasc == pivot.anoNasc and primeiro_menor(lista[j], pivot):
            lista[j], lista[i] = lista[i], lista[j]
            # incrementa-se o limite dos elementos menores que o pivô
            i = i + 1

    lista[i], lista[fim] = lista[fim], lista[i]
    
    return i

def quicksort(lista, inicio, fim):
    
    if inicio < fim:
        p = particao(lista, inicio, fim)
        # recursivamente na sublista à esquerda (menores)
        quicksort(lista, inicio, p-1)
        # recursivamente na sublista à direita (maiores)
        quicksort(lista, p+1, fim)

# F < M < X
lista = [ individuo("Xesquedela", 2003, 'X'),individuo("Alicia", 2003, 'X'),individuo("Xesquedele", 2003, 'M'),
          individuo("Tarcisio", 2002, 'X'), individuo("Julia", 2002, 'F'), individuo("Lucas", 2002, 'M') ]
n = len(lista)

quicksort(lista, 0, n -1)

# F < M < X
print(primeiro_menor(individuo("Xesquedela", 2003, 'M'), individuo("Alicia", 2003, 'F')))
print(lista)