
POS_X = 0
POS_Y = 1
my_position = [3, 1]  # Indicates the position of our character

MAP_WIDTH = 20
MAP_HEIGHT = 15

print("+" + "-" * (MAP_WIDTH * 3 + 1 ) + "+")  

for coordinate_y in range(MAP_HEIGHT):
    print("|", end="")  
    for coordinate_x in range(MAP_WIDTH):
        if my_position == [coordinate_x, coordinate_y]:
            print(" @ ", end="")  
        else:
            print(" . ", end="")  
    print(" |")  
print("+" + "-" * (MAP_WIDTH * 3+ 1 ) + "+")  