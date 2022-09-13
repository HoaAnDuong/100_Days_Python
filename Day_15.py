import sys


menu_1 = {
    "espresso": {
        "money": 1.50,

        "water": 50,
        "coffee": 18
    },

    "latte": {
        "money": 2.50,

        "water": 200,
        "milk": 150,
        "coffee": 24
    },

    "cappuccino": {
        "money": 3.50,

        "water": 250,
        "milk": 100,
        "coffee": 24
    }
}



def createStorage():
    return {
        "water" : 0,
        "milk" : 0,
        "coffee": 0
    }
def checkStorage(storage):
    try:
        print("Storage currently have:")
        print("Water(ml):",storage["water"])
        print("Milk(ml):", storage["milk"])
        print("Coffee(g):", storage["coffee"])
    except:
        print("Error: ",sys.exc_info()[1])

def fillStorage(storage,water = 500, milk = 300, coffee = 50):
    try:
        storage["water"] += water
        storage["milk"] += milk
        storage["coffee"] += coffee
    except:
        print("Error: ",sys.exc_info()[1])

storage_1 = createStorage()
fillStorage(storage_1)
checkStorage(storage_1)

def addMoney(customer):
    while True:
        try:
            customer["money"] += int(input("Enter number of Pennies($0.01):")) * 0.01
            break
        except:
            print("Error: ",sys.exc_info()[1])
    while True:
        try:
            customer["money"] += int(input("Enter number of Dimes($0.10):")) * 0.1
            break
        except:
            print("Error: ",sys.exc_info()[1])
    while True:
        try:
            customer["money"] += int(input("Enter number of Nickels($0.05):")) * 0.05
            break
        except:
            print("Error: ",sys.exc_info()[1])
    while True:
        try:
            customer["money"] += int(input("Enter number of Quarters($0.25):")) * 0.25
            break
        except:
            print("Error: ",sys.exc_info()[1])
    customer["money"] = round(customer["money"], 2)
    print("Current Money: $",customer["money"])
    return customer["money"]

def checkCustomer(customer):
    try:
        print("Current Money: ${}".format(customer["money"]))
        print("Current Order: {}".format(customer["order"]))
    except:
        print("Error:",sys.exc_info()[1])

def getMoneyBack(customer):
    try:
        print("You will get ${} back.".format(customer["money"]))
        customer["money"] = 0
    except:
        print("Error: ",sys.exc_info()[1])

def makeDrink(chosen_drink,storage):
    try:
        for i in chosen_drink:
            if i != "money":
                if storage[i] >= chosen_drink[i]:
                    storage[i] -= chosen_drink[i]
                else:
                    print("Not enough {}(Storage: {}, Needed: {})".format(i,storage[i],chosen_drink[i]))
                    return 0
        return 1
    except:
        print("Error:",sys.exc_info())
        return 0


def makeOrder(customer,storage,menu):
    print("Current money: $ ",customer["money"])
    order = input("Would you like to drink(Espresso($1.5)/Latte($2.5)/Cappuccino($3.5)?").lower()
    try:
        chosen_drink = menu[order]
        try:
            if customer["money"] >= chosen_drink["money"]:
                if makeDrink(chosen_drink,storage):
                    customer["money"] -= chosen_drink["money"]
                    print(f"Here's your {order.title()}")
                    return order
                else:
                    print("Sorry for Ingredients Insufficient!!!")
                    return None
            else:
                print("Money insufficient({}'s price: ${}, you have: ${}) !!!".format(order,chosen_drink["money"],customer["money"]))
        except:
            print("Error:",sys.exc_info()[1])

    except:
        print(f"Cannot find {order} in menu")

def getOrder(customer):
    try:
        if customer["order"] == {}: print("You don't have any order yet.")
        else:
            print("Here is your drink:")
            for i in customer["order"]:
                print("{} {}".format(customer["order"][i],i.title()))
            customer["order"] = {}
    except:
        print("Error:",sys.exc_info()[1])


def command(customer,cmd =  input("Commands:  add_money, check_storage, check_customer, end, fill_storage, get_drink, get_money_back, make_order\nWhat do you want to do?").lower(),storage = storage_1,menu = menu_1):
    try:
        match cmd:
            case "check_storage":
                checkStorage(storage)
                cmd = input(
                    "Commands:  add_money, check_storage, check_customer, end, fill_storage, get_drink, get_money_back, make_order\nWhat do you want to do?").lower()
                return command(customer,cmd)
            case "fill_storage":
                if bool(input("Do you want to fill the storage manually(Y/N)?").lower()):
                    try:
                        water = int(input("Enter amount of water(ml) to fill:"))
                        milk = int(input("Enter amount of milk(ml) to fill:"))
                        coffee = int(input("Enter amount of coffee(ml) to fill:"))
                        fillStorage(storage,water = water,milk = milk,coffee = coffee)
                    except:
                        print("Error: ",sys.exc_info()[1])
                cmd = input(
                    "Commands:  add_money, check_storage, check_customer, end, fill_storage, get_drink, get_money_back, make_order\nWhat do you want to do?").lower()
                return command(customer, cmd)
            case "check_customer":
                checkCustomer(customer)
                cmd = input(
                    "Commands:  add_money, check_storage, check_customer, end, fill_storage, get_drink, get_money_back, make_order\nWhat do you want to do?").lower()
                return command(customer, cmd)
            case "add_money":
                addMoney(customer)
                cmd = input(
                    "Commands:  add_money, check_storage, check_customer, end, fill_storage, get_drink, get_money_back, make_order\nWhat do you want to do?").lower()
                return command(customer, cmd)
            case "get_money_back":
                getMoneyBack(customer)
                cmd = input(
                    "Commands:  add_money, check_storage, check_customer, end, fill_storage, get_drink, get_money_back, make_order\nWhat do you want to do?").lower()
                return command(customer, cmd)
            case "make_order":
                drink = makeOrder(customer,storage,menu)
                if drink != None:
                    if drink in customer["order"]:
                        customer["order"][drink] += 1
                    else:
                        customer["order"][drink] = 1
                cmd = input(
                    "Commands:  add_money, check_storage, check_customer, end, fill_storage, get_drink, get_money_back, make_order\nWhat do you want to do?").lower()
                return command(customer, cmd)
            case "get_drink":
                getOrder(customer)
                cmd = input(
                    "Commands:  add_money, check_storage, check_customer, end, fill_storage, get_drink, get_money_back, make_order\nWhat do you want to do?").lower()
                return command(customer, cmd)
            case "end":
                getMoneyBack(customer)
                getOrder(customer)
                print("Thank you for purchasing Coffee!")
                return 0
            case default:
                print("Syntax Error")
                cmd = input(
                    "Commands:  add_money, check_storage, check_customer, end, fill_storage, get_drink, get_money_back, make_order\nWhat do you want to do?").lower()
                return command(customer, cmd)
    except:
        print("Error:",sys.exc_info()[1])
        return -1





customer_1 = {
    "money": 2.5,
    "order": {}
}



command(customer_1)




