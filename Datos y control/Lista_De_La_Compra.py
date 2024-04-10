
lista_compra = []
print("Lista de la compra")

while True:
    item = input("¿Qué deseas comprar? [Q] para salir:  ")
    if item == "Q":
        break  # Salir del bucle si el usuario ingresa "Q"
    elif item in lista_compra:
        print("{} ya está en la lista de la compra".format(item))
    else:
        lista_compra.append(item)



pregunta = None
while pregunta not in ["S", "N"]:
    pregunta = input("Seguro que quieres añadir estos elementos a la lista de la compra (S/N): ")

if pregunta == "N" and lista_compra:
    lista_compra.pop()  # Eliminar el último elemento si la respuesta es "N" y la lista no está vacía
    print("No se han añadido los elementos a la lista de la compra.")
elif pregunta == "S":
    print("Se han añadido los items {} a la lista de la compra".format(lista_compra))
