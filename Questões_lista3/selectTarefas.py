class Tarefa:
    def __init__(self, valor, inicio, duracao):
        self.valor = valor
        self.inicio = inicio
        self.duracao = duracao
        self.fim = str(int(inicio) + int(duracao))

def selecionar_tarefas(tarefas):
    tarefas.sort(key=lambda x: x.fim)  # ordena as tarefas por data de fim
    n = len(tarefas)
    V = [tarefa.valor for tarefa in tarefas]  # inicializa o vetor V com os valores de avanço das respectivas tarefas

    for i in range(1, n):
        for j in range(i):
            if tarefas[j].fim <= tarefas[i].inicio:
                V[i] = max(V[i], V[j] + tarefas[i].valor)

    return max(V)

tarefas = [Tarefa(2, "01/10/2021", 4), Tarefa(4, "02/10/2021", 6), Tarefa(4, "06/10/2021", 3), 
           Tarefa(7, "03/10/2021", 9), Tarefa(2, "10/10/2021", 3), Tarefa(1, "11/10/2021", 3)]

max_valor = selecionar_tarefas(tarefas)
print(max_valor)  # saída: 8
