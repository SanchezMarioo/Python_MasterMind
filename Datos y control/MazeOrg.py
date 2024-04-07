import os
import random

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
    while len(map_objects) < NUM_OF_MAP_OBJECTS:
        new_position = [random.randint(0, MAP_WIDTH-1), random.randint(0, MAP_HEIGHT-1)]
        if new_position not in map_objects and new_position != my_position:
            map_objects.append(new_position)


    if os.name == 'nt':  
        os.system('cls')
    else:
        os.system('clear')

    print("+" + "-" * MAP_WIDTH * 3 + "+")

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