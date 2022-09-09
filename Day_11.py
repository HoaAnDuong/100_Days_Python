from dis import dis
import random
import time
import os
import platform

os_name = platform.system()

dict = {"A":[1,10,11],"J":10,"Q":10,"K":10,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"10":10}

cards = []
random.seed(time.time())
for i in range(2,11):
    for j in range(4):
        cards.append(str(i))
for i in ["A","J","Q","K"]:
    for j in range(4):
        cards.append(i)
print(cards)


def clearscreen():
    if os_name == "Windows":
        if os.system("cls"):
            if bool(input("So sorry, we cannot clear the screen. If you think the game is unfair, press \"e\" of \"E\" to end the game:").lower() == "e"):
                return -1
    else:
        if os.system("clear"):
            if bool(input("So sorry, we cannot clear the screen. If you think the game is unfair, press \"e\" of \"E\" to end the game:").lower() == "e"):
                return -1 
    return 0
def createPlayer(num_player):
    list = []
    for i in range(num_player):
        list.append({
            "cards": [],
            "point": 0,
            "status": ""
        })
    return list
def display(player,player_name,show = False):
    print(f"Player {player_name} currently have:")
    if show:
        print("Cards:{}".format(player["cards"]))
        print("Points: {}".format(player["point"]))
    else:
        message = "Cards: "
        if len(player["cards"]) != 0:
            message += player["cards"][0]
            for i in range(1,len(player["cards"])):
                message += " ?"
        print(message)
    try:
        print("Status: {}".format(player["status"]))
    except:
        pass


def pick(player,player_name):
    for i in range(2,5):
        print(f"It's player {player_name} turn.")
        display(player,player_name,show = True)
        if player["point"] < 16: print("Warning!!! Your point is less than 16")
        if bool(input("Would you like to pick a card(Y/N)?") == "Y") and len(cards) > 0 and player["status"] == "" : 
            player["cards"].append(cards.pop(random.randrange(len(cards))))
            if player["cards"][i] != "A":
                player["point"] += dict[player["cards"][i]]
            else:
                temp_point = player["point"] + 1
                for l in [10,11]:
                    if player["point"] + l <=21:
                        temp_point = player["point"] + l
                player["point"] = temp_point    
        elif len(cards) == 0:
            print("Sorry, we ran out of cards :'))")
            display(player,player_name,show = True)
            print(f"Player {player_name} turn's ended")
            break
        else: 
            display(p,player_name, show = True)
            print(f"Player {player_name} turn's ended")
            break
    
    clearscreen()

def bust(players,boss,picked):
    boss_want_bust = True
    for p1 in players:
        display(p1,players.index(p1))
    if boss["point"] < 15:
        print("Boss!!! Your point is less than 15, so you cannot bust anyone")    
    else:
        while(boss_want_bust):
            display(boss,"Boss",show=True)
            boss_want_bust = bool(input(f"Boss!!!Do you want to bust someone(from 0 to {picked}) (Y/N)?").lower() == "y")
            if boss_want_bust:
                try:
                    busting_id = int(input(f"Boss!!! Enter the player ID(from 0 to {picked}) to bust:"))
                    
                    if players[busting_id]["status"] != "":
                        print("Sorry, player {} is already {}".format(busting_id, players[busting_id]["status"]))
                    elif busting_id < picked:
                        print("Sorry, this player is not picked yet")
                    elif boss["point"] > 21:
                        if players[busting_id]["point"] > 21 or players[busting_id]["point"] < 16:
                            players[busting_id]["status"] = "tie"
                        else:
                            players[busting_id]["status"] = "win"
                    else:
                        if players[busting_id]["point"] > 21:
                            players[busting_id]["status"] = "lose"
                        else:
                            if len(players[busting_id]["cards"]) == 5:
                                players[busting_id]["status"] = "win"
                            elif players[busting_id]["point"] > boss["point"]:
                                players[busting_id]["status"] = "win"
                            elif players[busting_id]["point"] == boss["point"]:
                                players[busting_id]["status"] = "tie"
                            else:
                                players[busting_id]["status"] = "lose"
                        print("Player {} is {}".format(busting_id, players[busting_id]["status"]))
                        display(boss,"Boss",show = True)
                        display(players[busting_id],busting_id,show=True)
                except:
                    print("Sorry, an error occurred!!!")
    clearscreen() 
    
def boss_turn(boss):
    for i in range(2,5):
        print(f"It's Boss turn.")
        display(boss,"Boss",show = True)
        if bool(input("Would you like to pick a card(Y/N)?") == "Y") and len(cards) > 0 and boss["status"] == "":
            boss["cards"].append(cards.pop(random.randrange(len(cards))))
            if boss["cards"][i] != "A":
                boss["point"] += dict[boss["cards"][i]]
            else:
                temp_point = boss["point"] + 1
                for l in [10,11]:
                    if boss["point"] + l <=21:
                        temp_point = boss["point"] + l
                boss["point"] = temp_point   
                   
        elif len(cards) == 0:
            print("Sorry, we ran out of cards :'))")
            if bust(players,boss,players.index(p)) == -1:
                return -1
            display(boss,"Boss",show = True)
            print(f"Boss turn's ended")
            break
        else: 
            print("If you cancel Bust, Mass Bust will carry on")
            if bust(players,boss,players.index(p)) == -1:
                return -1
            display(boss,"Boss",show = True)
            print(f"Boss turn's ended")
            break
    clearscreen()

def mass_bust(players,boss):
    print("Mass Busts is coming!!!")
    for p in players:
        if p["status"] != "":
            print("Player {} is already {}".format(players.index(p), p["status"]))
        elif boss["point"] > 21:
            if p["point"] > 21:
                p["status"] = "tie"
            else:
                p["status"] = "win"
        else:
            if p["point"] > 21 or p["point"] < 16:
                p["status"] = "lose"
            else:
                if len(p["cards"]) == 5:
                    p["status"] = "win"
                elif p["point"] > boss["point"]:
                    p["status"] = "win"
                elif p["point"] == boss["point"]:
                    p["status"] = "tie"
                else:
                    p["status"] = "lose"
        print("Player {} is {}".format(players.index(p), p["status"]))
        display(boss,"Boss",show=True)
        display(p,players.index(p), show=True)




def checkBlackjack(players,boss):
    if boss["cards"].count("A") == 2:
        print("Boss is Aced!!!")
        for p in players:
            if p["cards"].count("A") == 2:
                print(f"And player {players.index(p)} is Aced too!!!")
                p["status"] = "tie"
            else:
                p["status"] = "lose"
            return -1
    elif boss["cards"].count("A") == 1 and (boss["cards"].count("J") == 1 or boss["cards"].count("Q") == 1 or boss["cards"].count("K") == 1):
        print("Boss is Blackjack!!") 
        for p in players:
            if p["cards"].count("A") == 2:
                print(f"But player {players.index(p)} is Aced!!!")
                p["status"] = "win"
            elif p["cards"].count("A") == 1 and (p["cards"].count("J") == 1 or p["cards"].count("Q") == 1 or p["cards"].count("K") == 1):
                print(f"Player {players.index(p)} is Backjack too!!!")
                p["status"] = "tie"
            else:
                p["status"] = "lose"
        return -1
    else:
        for p in players:
            if p["cards"].count("A") == 2:
                print(f"Player {players.index(p)} is Aced !!!")
                p["status"] = "win"
            elif p["cards"].count("A") == 1 and (p["cards"].count("J") == 1 or p["cards"].count("Q") == 1 or p["cards"].count("K") == 1):
                print(f"Player {players.index(p)} is Blackjack !!!")
                p["status"] = "win"
    return 0



boss = {
    "cards": [],
    "point": 0
    }

num_player = int(input("Enter number of players:"))

players = createPlayer(num_player)

print("The game begin.")

if checkBlackjack(players,boss) != -1:
    for p in players:
        for i in range(2):
            if len(cards) > 0:
                p["cards"].append(cards.pop(random.randrange(len(cards))))
                if p["cards"][i] != "A":
                    p["point"] += dict[p["cards"][i]]
                else:
                    temp_point = p["point"] + 1
                    for l in [10,11]:
                        if p["point"] + l <=21:
                            temp_point = p["point"] + l
                    p["point"] = temp_point 
            else:
                print("Sorry, we ran out of cards :'))")
                break    
        
    for i in range(2):
            if len(cards) > 0:
                boss["cards"].append(cards.pop(random.randrange(len(cards))))
                if boss["cards"][i] != "A":
                    boss["point"] += dict[boss["cards"][i]]
                else:
                    temp_point = boss["point"] + 1
                    for l in [10,11]:
                        if boss["point"] + l <=21:
                            temp_point = boss["point"] + l
                    boss["point"] = temp_point
            else:
                print("Sorry, we ran out of cards :'))")
                break 

    checkBlackjack(players,boss)

    print("It's turn for picking more cards and busting.")

    

    for p in players:
        clearscreen()
        input(f"Player {players.index(p)}, Press Enter to start:")
        for p1 in players:
            display(p1,players.index(p1))
        display(boss,"Boss")

        pick(p,players.index(p))
            

        clearscreen()

        bust(players,boss,players.index(p))

        clearscreen()
        
    boss_turn(boss)    

    mass_bust(players,boss)

print("The game ended.")

display(boss,"Boss",show = True)
for p in players:
    display(p,players.index(p),show = True)






            

            

