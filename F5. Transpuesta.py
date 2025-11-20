matriz=[[1, 2, 3],[4, 5, 6]]
trp = [[fila[i] for fila in matriz] for i in range(len(matriz[0]))]
print("Matriz transpuesta:", trp)