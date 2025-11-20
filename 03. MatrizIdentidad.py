num=int(input("Ingrese el tamaño de la matriz: "))
MaI=[]
for i in range(num):
    fila=[]
    for j in range(num):
        if i==j:
            fila.append(1)
        else:
            fila.append(0)
    MaI.append(fila)
for fila in MaI:
    print(fila)
