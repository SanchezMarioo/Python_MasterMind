lista_compra = []

print("La Lista de la compra")
while True:
    item = input("¿Qué deseas comprar? Para salir, teclea [Q]: ")
    if item != "Q":
        item = item.capitalize()  # Convertir la primera letra a mayúscula
        if item in lista_compra:
            print("{} ya está en la lista de la compra.".format(item))
        else:
            lista_compra.append(item)
            respuesta = input("¿Deseas añadir {} a la lista de la compra? [S] / [N]: ".format(item))
            while respuesta not in ["S", "N"]:
                respuesta = input("¿Deseas añadir {} a la lista de la compra? [S] / [N]: ".format(item))
            if respuesta == "N":
                lista_compra.remove(item)
                print("No se ha añadido {} a la lista de la compra.".format(item))
            elif respuesta == "S":
                print("Se ha añadido {} a la lista de la compra.".format(item))
    else:
        print("La lista de la compra es: {} ".format(lista_compra))
        break
