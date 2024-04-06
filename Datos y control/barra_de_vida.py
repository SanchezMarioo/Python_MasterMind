import random
import os

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

vida_incial_pikachu = 80
vida_incial_squirtle = 90
vida_pikachu = vida_incial_pikachu
vida_squirtle = vida_incial_squirtle
TAMANIO_BARRA_VIDA = 10

while vida_pikachu > 0 and vida_squirtle > 0:
    input("Enter para continuar : ")
    print("Turno de Pikachu")
    clear()

    ataque_pikachu = random.randint(1, 2)
    if ataque_pikachu == 1:
        print("Pikachu ataca con bola voltio")
        vida_squirtle -= 10
    else:
        print("Pikachu ataca con onda truena")
        vida_squirtle -= 20
    barra_vida_pikachu = int(vida_pikachu * TAMANIO_BARRA_VIDA / vida_incial_pikachu)
    print("VIDA DE PIKACHU:  [{}{}] ({}/{})".format("*" * barra_vida_pikachu, " " * (TAMANIO_BARRA_VIDA - barra_vida_pikachu),
                                                   vida_pikachu, vida_incial_pikachu))

    barra_vida_squirtle = int(vida_squirtle * TAMANIO_BARRA_VIDA / vida_incial_squirtle)
    print("VIDA DE SQUIRTLE:  [{}{}] ({}/{})".format("*" * barra_vida_squirtle, " " * (TAMANIO_BARRA_VIDA - barra_vida_squirtle),
                                                   vida_squirtle, vida_incial_squirtle))
    print("Turno Squirtle")
    input("Enter para continuar : ")
    clear()
    ataque_squirtle = None
    while ataque_squirtle != "P" and ataque_squirtle != "A" and ataque_squirtle != "B" and ataque_squirtle != "N":
        ataque_squirtle = input("¿Qué ataque deseas utilizar [P] Placaje Pistola [A]gua [B]urbuja  [N]ada: ")
    if ataque_squirtle == "A":
        vida_pikachu -= 10
    elif ataque_squirtle == "P":
        vida_pikachu -= 12
    elif ataque_squirtle == "B":
        vida_pikachu -= 9
    elif ataque_squirtle == "N":

        vida_pikachu -= 0
        print("Has decidido no hacer nada")
    barra_vida_pikachu = int(vida_pikachu * TAMANIO_BARRA_VIDA / vida_incial_pikachu)
    print("VIDA DE PIKACHU:  [{}{}] ({}/{})".format("*" * barra_vida_pikachu, " " * (TAMANIO_BARRA_VIDA - barra_vida_pikachu),
                                                   vida_pikachu, vida_incial_pikachu))

    barra_vida_squirtle = int(vida_squirtle * TAMANIO_BARRA_VIDA / vida_incial_squirtle)
    print("VIDA DE SQUIRTLE:  [{}{}] ({}/{})".format("*" * barra_vida_squirtle, " " * (TAMANIO_BARRA_VIDA - barra_vida_squirtle),
                                                   vida_squirtle, vida_incial_squirtle))

if vida_squirtle <= 0 and vida_pikachu <= 0:
    print("Ambos Pokémon quedaron fuera de combate. ¡Es un empate!")
elif vida_squirtle <= 0:
    print("¡Gana Pikachu!")
else:
    print("¡Gana Squirtle!")

