clf={}
while True:
    entrada=input("Ingrese nombre y nota (o 'fin' para terminar): ")
    if entrada.lower()=="fin":
        break
    try:
        nombre, nota=entrada.split(":")
        nombre=nombre.strip()
        nota=float(nota.strip())
        clf[nombre]=nota
    except ValueError:
        print("Formato incorrecto. Use: Nombre: Nota")
prom=sum(clf.values())/len(clf)
print("Promedio general:", prom)
