def mochila_backtracking(s, k,n):
    
    incluir = [False] * n

    def backtrack(i, soma):

        if soma == k:
            return True
        
        if i == n or soma > k:
            return False
        incluir[i] = True
        if backtrack(i+1, soma+s[i]):
            return True
        incluir[i] = False
        return backtrack(i+1, soma)

    if backtrack(0, 0):
        for i in range(n):
            if incluir[i]:
                print(s[i])
        
    else:
        print("Não há solução")

s = [4,2,5,8,3]
k = 11
n = len(s)
mochila_backtracking(s, k, n)
