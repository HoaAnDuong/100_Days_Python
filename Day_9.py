# def addNewCountry(travel_log,country,visits,cities):
#     travel_log.append({
#         "country":country,
#         "visits":visits,
#         "cities":cities
#     })
#     return travel_log
# travel_log_1 = [{"country":"Maldives",
#                 "visits":1,
#                 "cities":["Malé"]}]
# addNewCountry(travel_log_1,"Russia",2,["Moscow","Saint Petersburg"])
# print(travel_log_1)

import os # sorry i dont have replit
import platform
import sys

os_name = platform.system()

# os_name  = None
if os_name != "Darwin":
    print(f"\nYou're using {os_name}\n")
else:
    print("\nYou're using MacOS\n")

def blindAution(item):
    have_others_bidders = True
    max_bidders = {
        "name": "",
        "money": 0
    }
    while have_others_bidders:
        print("Welcome to the blind auction!!!")
        print(f"You are bidding for a(an) {item}.")
        try:
            name = input("What is your name?")
            money = int(input("How much money(in USD) you want to bid?")) 
            if money > max_bidders["money"]:
                max_bidders["name"] = name
                max_bidders["money"] = money
            have_others_bidders = bool(input("Are there any others bidders(yes/no)?").lower() == "yes")
        except:
            print(f"Error Occured: {sys.exc_info()[1]}")
        
        
        if os_name == "Windows":
            if os.system("cls"):
                if bool(input("So sorry, we cannot clear the screen. If you think the aution is unfair, press \"e\" of \"E\" to exit:").lower() == "e"):
                    return {
                        "item": item,
                        "name": "No One",
                        "money": 0
                    } 
        elif os_name == "Darwin" or os_name == "Linux":
            if os.system("clear"):
                if bool(input("So sorry, we cannot clear the screen. If you think the aution is unfair, press \"e\" of \"E\" to exit:").lower() == "e"):
                    return {
                        "item": item,
                        "name": "No One",
                        "money": 0
                    }
        else:
                if os.system("clear"):
                    if bool(input("So sorry, we cannot clear the screen. If you think the aution is unfair, press \"e\" of \"E\" to exit:").lower() == "e"):
                        return {
                            "item": item,
                            "name": "No One",
                            "money": 0
                        }
    return {
        "item" :item,
        "name" : max_bidders["name"],
        "money" : max_bidders["money"]
    }
winner_bidder = blindAution("Gaming Keyboard(best for playing Geometry Dash)")



try:
    if winner_bidder["money"] == 0:
        print("No one win the {}.An Unexpected Error Occured".format(winner_bidder["item"]))
    else: print("The winner bidder of {} is {}. He/She bidded {} USD".format(winner_bidder["item"],winner_bidder["name"],winner_bidder["money"]))
except:
    print(f"Error Occured: {sys.exc_info()[1]}")
            

