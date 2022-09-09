import random, sys
from re import T
# seed = int(input("Enter seed:"))
# random.seed(seed)
# roll_time = int(input("How many time do you want to roll? "))
# for i in range(roll_time):
#     print("Heads" if random.randint(0,1) else "Tails")

# input = input("Who did have meal here?\n")
# list = input.split(", ")
# the_winner = random.choice(list)
# print(f"{the_winner} is going to pay the food bill")

# def createMap():
#     num_rows = 0
#     num_cols = 0
#     try:
#         num_cols = int(input("Enter the number of columns:"))
#         num_rows = int(input("Enter the number of rows:"))
#     except:
#         print(sys.exc_info())
#         return createMap()
#     else:
#         map = []

#         for i in range(num_cols):
#             map.append([])
#             for j in range(num_rows):
#                 map[i].append("O") 
#         return map

# I will make my customer suffered from theirs incorrect inputs
# def putTreasureOnMap(map):
#     x_pos = 0
#     y_pos = 0
#     try:
#         if bool(input("Would you like to randomize treasure's location???(Y/N) ") == "Y"):
#             x_pos = random.randint(0, len(map[0])-1)
#             y_pos = random.randint(0, len(map)-1)
#         else:
#             x_pos = int(input("Enter the columns pos: "))
#             y_pos = int(input("Enter the rows pos: "))
#     except:
#         print(sys.exc_info())
#         putTreasureOnMap(map)
#     else:
#         try:
#             map[y_pos][x_pos] = "X"
#         except:
#             print(sys.exc_info())
#             putTreasureOnMap(map)
# map_1 = createMap()           
# putTreasureOnMap(map_1)
# for r in map_1:
#     print(r)

dict = {"rock":0, "paper":1, "scissors":2}
rev_dict = {0:"Rock",1:"Paper",2:"Scissors"}
winner_dict = {-2:"Syntax Error",-1:"Tie",0:"You win",1:"Computer wins"}

def whoWin(move_1,move_2):
    list = [0,1,2,0]
    try:
        move_1 = dict[move_1.lower()]
    except:
        pass
    try:
        move_2 = dict[move_2.lower()]
    except:
        pass
        
    try:
        if move_1 == move_2:
            return -1
        elif list[move_1+1] == list[move_2]:
            return 1
        elif list[move_1] == list[move_2+1]:
            return 0
        return -2
    except:
        return -2

your_move = input("Enter your move:")
computer_move = random.randint(0,2)

try:
    your_move = int(your_move)
except:
    pass


try:
    print(rev_dict[your_move])
except:
    print(your_move)         

try:
    print(rev_dict[computer_move])
except:
    print(computer_move) 

print(winner_dict[whoWin(your_move, computer_move)])





            
