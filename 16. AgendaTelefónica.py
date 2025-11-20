agenda = {}
while True:
    etr=input("Ingrese nombre y teléfono (o 'fin' para terminar): ")
    if etr.lower() == "fin":
        break
    try:
        nombre, telefono = etr.split("-")
        nombre = nombre.strip()
        telefono = telefono.strip()
        agenda[nombre] = telefono
    except ValueError:
        print("Formato incorrecto. Use: Nombre - Teléfono")
print(agenda)
