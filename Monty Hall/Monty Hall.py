import random
import sys

# Ascii art - made of ascii characters

ALL_CLOSED = """
+------+  +------+  +------+
|      |  |      |  |      |
|   1  |  |   2  |  |   3  |
|      |  |      |  |      |
|      |  |      |  |      |
|      |  |      |  |      |
+------+  +------+  +------+"""


FIRST_GOAT = """
+------+  +------+  +------+
|  ((  |  |      |  |      |
|  oo  |  |   2  |  |   3  |
| /_/|_|  |      |  |      |
|    | |  |      |  |      |
|GOAT|||  |      |  |      |
+------+  +------+  +------+"""

SECOND_GOAT = """
+------+  +------+  +------+
|      |  |  ((  |  |      |
|   1  |  |  oo  |  |   3  |
|      |  | /_/|_|  |      |
|      |  |    | |  |      |
|      |  |GOAT|||  |      |
+------+  +------+  +------+"""

THIRD_GOAT = """
+------+  +------+  +------+
|      |  |      |  |  ((  |
|   1  |  |   2  |  |  oo  |
|      |  |      |  | /_/|_|
|      |  |      |  |    | |
|      |  |      |  |GOAT|||
+------+  +------+  +------+"""


FIRST_CAR_OTHERS_GOAT = """
+------+  +------+  +------+
| CAR! |  |  ((  |  |  ((  |
|    __|  |  oo  |  |  oo  |
|  _/  |  | /_/|_|  | /_/|_|
| /_ __|  |    | |  |    | |
|   O  |  |GOAT|||  |GOAT|||
+------+  +------+  +------+"""

SECOND_CAR_OTHERS_GOAT = """
+------+  +------+  +------+
|  ((  |  | CAR! |  |  ((  |
|  oo  |  |    __|  |  oo  |
| /_/|_|  |  _/  |  | /_/|_|
|    | |  | /_ __|  |    | |
|GOAT|||  |   O  |  |GOAT|||
+------+  +------+  +------+"""

THIRD_CAR_OTHERS_GOAT = """
+------+  +------+  +------+
|  ((  |  |  ((  |  | CAR! |
|  oo  |  |  oo  |  |    __|
| /_/|_|  | /_/|_|  |  _/  |
|    | |  |    | |  | /_ __|
|GOAT|||  |GOAT|||  |   O  |
+------+  +------+  +------+"""


One_door_open = [FIRST_GOAT, SECOND_GOAT, THIRD_GOAT ]
All_open_doors = [ FIRST_CAR_OTHERS_GOAT, SECOND_CAR_OTHERS_GOAT, THIRD_CAR_OTHERS_GOAT]

swapWin =0
swapLose=0
ogWin=0
ogLose=0

#main game loop
while True:
    door_with_car = random.randint(1,3)
    print(ALL_CLOSED)

    while True:
        user_input = int(input("Enter door number (press 0 for quitting): "))
        if user_input in range (1,4):
            break
        elif user_input==0:
            print("Thanks for playing")
            sys.exit()
        else:
            print("Wrong Input! Enter again")


    #if-else loop to show goat door

    if door_with_car != user_input:
        door_shown = 6 - door_with_car - user_input

    else:
        temp_list = [1,2,3]
        temp_list.remove(user_input)
        door_shown= random.choice(temp_list)

    print(One_door_open[door_shown-1])


    swap= input("Do you want to swap the door (Y/N)? ")
    if( swap.upper == 'Y' ):
          user_input = 6 - door_shown - user_input



    print(All_open_doors[door_with_car - 1])

    if door_with_car == user_input and swap.upper()=='Y':
          swapWin += 1
          print("Congrats! You won")
          
    elif door_with_car == user_input and swap.upper()=='N':
          ogWin += 1
          print("Congrats! You won")

    elif user_input != door_with_car and swap.upper() == 'Y':
        swapLose += 1
        print("Better Luck Next time")

    else:
        ogLose +=1
        print("Better Luck Next time")


    print(""" Thanks for playing!
Wins after swapping: {}
Wins without swapping: {}
Losses after swapping: {}
Losses without swapping: {}""".format(swapWin, ogWin, swapLose, ogLose))


    #success = round(Wins/total *100,1)
    try:
        successRate_swap = round(swapWin/(swapWin+swapLose) *100,1)
    except ZeroDivisionError:
        successRate_swap=0

    try:
        successRate_og = round(ogWin/(ogWin+ogLose) *100,1)
    except ZeroDivisionError:
        successRate_og =0

    print("""\nSuccess Rate if you swap: {}%
Success rate if you dont swap: {}%""".format(successRate_swap, successRate_og))
    
    
            
                               
