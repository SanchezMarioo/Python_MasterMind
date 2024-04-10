
# No consegui depurar al 100% el codigo, por  ejemplo cuando entras en una pelea despues de perderla no se muestra bien el mapa


import os
import random
def clear():
    # Clear the console
    os.system('cls' if os.name == 'nt' else 'clear')
my_position = [6, 3]
tail_lenght = 0
tail = []
map_objects = []
fight_objects = []
fight = False
end_game = False

map = """\
###########################
#                           # 
# ############  #### #    ### 
#         ###        ###    # 
#   ##### ### ##     ###    # 
#       # ### #    #####    # 
#     # # ### #     ######### 
#  ##   # ### # #     # ##### 
#   #   # ### # ####    ##### 
### #   # ### # ####    ##### 
### #   # ##            ##### 
###     #  ## #     # # ##### 
### ### #  ## #         ##### 
#######   ### # # # #         
#############################\
"""
map = [list(row) for row in map.split("\n")]

POS_X = 0
POS_Y = 1
MAP_WIDTH = len(map)
MAP_HEIGHT = len(map)
NUM_OF_MAP_OBJECTS = 11
NUM_OF_MAP_FIGHT_OBJECTS = 10


while len(fight_objects) < NUM_OF_MAP_FIGHT_OBJECTS:
    new_position = [random.randint(0, MAP_WIDTH-1), random.randint(0, MAP_HEIGHT-1)]
    if new_position not in fight_objects and new_position != my_position:
        fight_objects.append(new_position)
while not end_game:
    vida_incial_pikachu = 80
    vida_incial_squirtle = 90
    vida_pikachu = vida_incial_pikachu
    vida_squirtle = vida_incial_squirtle
    while len(map_objects) < NUM_OF_MAP_OBJECTS:
        new_position = [random.randint(0, MAP_WIDTH-1), random.randint(0, MAP_HEIGHT-1)]
        if new_position not in map_objects and new_position != my_position:
            map_objects.append(new_position)
    if os.name == 'nt':  
        os.system('cls')
    else:
        os.system('clear')

    print("+" + ("-" * MAP_WIDTH * 3) + "+")

    tail_piece = None      
    for coordinate_y in range(MAP_HEIGHT):
        print("|", end="")
        for coordinate_x in range(MAP_WIDTH):

            char_to_draw = " "
            object_in_celd = None

            for map_object in map_objects:
                if map_object[POS_X] == coordinate_x and map_object[POS_Y] == coordinate_y:
                    char_to_draw = "*"
                    object_in_celd = map_object
            
                for fight_object in fight_objects:
                    if fight_object[POS_X] == coordinate_x and fight_object[POS_Y] == coordinate_y:
                        char_to_draw = "I"  
                        object_in_celd = fight_object
            for tail_piece in tail:
                if tail_piece[POS_X] == coordinate_x and tail_piece[POS_Y] == coordinate_y:
                    char_to_draw = "@"

            tail_in_cell = my_position in tail
            if map[coordinate_y][coordinate_x] == "#":
                char_to_draw = "#"

            if my_position[POS_X] == coordinate_x and my_position[POS_Y] == coordinate_y:
                char_to_draw = "@"
                if object_in_celd in map_objects:
                    map_objects.remove(object_in_celd)
                    tail_lenght += 1
                if tail_in_cell:
                    print("Perdiste")
                    tail_piece= True
                if object_in_celd in fight_objects:
                    fight_objects.remove(object_in_celd)
                    fight = True
                while fight == True:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        TAMANIO_BARRA_VIDA = 10
                        input("Enter para continuar : ")
                        print("Turno de Pikachu")
                        os.system('cls' if os.name == 'nt' else 'clear')

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
                        os.system('cls' if os.name == 'nt' else 'clear')
                        ataque_squirtle = None
                        while ataque_squirtle != "P" and ataque_squirtle != "A" and ataque_squirtle != "B" and ataque_squirtle != "N":
                            ataque_squirtle = input("¿Qué ataque deseas utilizar [P] Placaje Pistola [A]gua [B]urbuja  [N]ada: ")
                        if ataque_squirtle == "A":
                            vida_pikachu = max(0, vida_pikachu - 10)
                        elif ataque_squirtle == "P":
                            vida_pikachu = max(0, vida_pikachu - 12)
                        elif ataque_squirtle == "B":
                            vida_pikachu = max(0, vida_pikachu - 9)
                        elif ataque_squirtle == "N":
                            print("Has decidido no hacer nada")
                        print("Has decidido no hacer nada")
                        barra_vida_pikachu = int(vida_pikachu * TAMANIO_BARRA_VIDA / vida_incial_pikachu)
                        print("VIDA DE PIKACHU:  [{}{}] ({}/{})".format("*" * barra_vida_pikachu, " " * (TAMANIO_BARRA_VIDA - barra_vida_pikachu),
                                                                            vida_pikachu, vida_incial_pikachu))

                        barra_vida_squirtle = int(vida_squirtle * TAMANIO_BARRA_VIDA / vida_incial_squirtle)
                        print("VIDA DE SQUIRTLE:  [{}{}] ({}/{})".format("*" * barra_vida_squirtle, " " * (TAMANIO_BARRA_VIDA - barra_vida_squirtle),
                                                                            vida_squirtle, vida_incial_squirtle))
                        
                        if vida_pikachu <= 0:
                            print("Squirtle gana la batalla")
                            vida_pikachu = 0
                            fight = False

                        elif vida_squirtle <= 0:
                            print("Pikachu gana la batalla")
                            vida_squirtle = 0
                            fight = False

                        os.system('cls' if os.name == 'nt' else 'clear')


            print(" {} ".format(char_to_draw), end="")
        print("|")

    print("+" + "-" * MAP_WIDTH * 3 + "+")

    direction = input("A donde te quieres mover? (w,a,s,d) ")
    direction = direction.lower().strip()

    # MOVE
    if direction == "w":
        tail.insert(0, my_position.copy())
        tail = tail[:tail_lenght]
        my_position[POS_Y] -= 1
        my_position[POS_Y] %= MAP_HEIGHT

    elif direction == "s":
        tail.insert(0, my_position.copy())
        tail = tail[:tail_lenght]
        my_position[POS_Y] += 1
        my_position[POS_Y] %= MAP_HEIGHT

    elif direction == "a":
        tail.insert(0, my_position.copy())
        tail = tail[:tail_lenght]
        my_position[POS_X] -= 1
        my_position[POS_X] %= MAP_WIDTH
    elif direction == "d":
        tail.insert(0, my_position.copy())
        tail = tail[:tail_lenght]
        my_position[POS_X] += 1
        my_position[POS_X] %= MAP_WIDTH
    elif direction == "q":
        end_game = True

    if my_position in tail:
     break
    if tail_in_cell: 
        print("Perdiste")
    
    if map[my_position[POS_Y]][my_position[POS_X]] == '#':
        print("Has perdido")
        end_game = True
    
