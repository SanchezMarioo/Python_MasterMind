import random
nelegido = random.randint(1,10)
nrandom= int(input("Dime un numero: "))

if nrandom != nelegido:
    print("No lo has adivinado. Vuelve a intentarlo")
if nrandom == nelegido:
    print("Has adivinado el numero.¡Felicidades!")
if nrandom > 10:
    print("Te has pasado el numero de numero es entre el 1 y el 10")
if nrandom < -1:
    print("Te has quedado corto el numero es entre el 1 y el 10")
print("El numero ganador era: {}".format(nelegido))
