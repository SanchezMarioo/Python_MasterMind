import  string

presentacion = input("¿Cual es el texto que quieres contar?: ")
espacios = 0
puntos = 0
comas = 0

for letras in presentacion:
    if letras == " ":
        espacios+= 1
    elif letras == ".":
        puntos += 1
    elif letras == ",":
        comas += 1
print("En este texto hay, {} espacios, {} puntos y {} comas".format(espacios, puntos, comas ))