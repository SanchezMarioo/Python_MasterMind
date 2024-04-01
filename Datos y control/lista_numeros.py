
lista_numeros = []
lista_limpia= []

while True:
    item = input("Ponga aquí su numero: ")
    item.capitalize()
    if item == "Q":
        break
    if item in lista_numeros:
        print("El {} ya esta en la lista.".format(item))
    else:
        pregunta = input("¿Quieres que el numero {} se añada a la lista [S/N] ".format(item))
        if pregunta == "S":
            lista_numeros.append(item)
        elif pregunta == "N":
            print("El numero {} no se ha añadido a la lista.")
        else:
            print("No has elegido ninguna opcion")
        print(lista_numeros)
for numero in lista_numeros:
    lista_limpia.append(int(numero))
print("El maximo de esta lista es ", max(lista_limpia))


