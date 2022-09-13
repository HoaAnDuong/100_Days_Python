import sys

#Spaghetti!!!!

def IngredientDict(water = 0,milk = 0,coffee = 0):
    #why am I still using dict? Because if a new ingredient appears and I decide to use a var to store it, I will need to rewrite entirely all the code.
    #In case a new ingredient appears, I just assign it to exist dict and throw exception if errors occur
    return {
        "water": water,
        "milk": milk,
        'coffee': coffee
    }

class Storage:
    def __init__(self,storage = IngredientDict(water = 500, milk = 300, coffee = 50)):
        self.storage = storage
    def check(self):
        try:
            print("Storage currently have:")
            for i in self.storage:
                print("{}: {}".format(i,self.storage[i]))
        except:
            print("Error: ", sys.exc_info()[1])
    def fill(self,ingredient):
        for i in ingredient:
            if i in self.storage:
                self.storage[i] += ingredient[i]
            else:
                self.storage[i] = ingredient[i]
    def makeDrink(self,drink):
        try:
            backup_storage = self.storage
            for i in drink.ingredient:
                if i != "money":
                    if self.storage[i] >= drink.ingredient[i]:
                        self.storage[i] -= drink.ingredient[i]
                    else:
                        self.storage = backup_storage
                        print("Not enough {}(Storage: {}, Needed: {})".format(i, self.storage[i], drink.ingredient[i]))
                        return 0
            return 1
        except:
            print("Error:", sys.exc_info())
            return 0



class Drink:
    def __init__(self,name = "",cost = 0.,ingredient = IngredientDict()):
        self.name = name.lower()
        self.cost = cost
        self.ingredient = ingredient

class Menu:
    menu = {}
    def addDrink(self,drink):
        try:
            if isinstance(drink,(list,tuple)):
                for i in drink:
                    print(type(i))
                    self.menu[i.name] = i;
            else:
                self.menu[drink.name] = drink
        except:
            print("Error:",sys.exc_info()[1])
    def check(self):
        try:
            for i in self.menu:
                i = self.menu[i]
                print("\nName: {}".format(i.name.title()))
                print("Cost: ${}".format(i.cost))
                print("Ingredients:")
                for j in i.ingredient:
                    print("{}: {}".format(j,i.ingredient[j]))
        except:
            print("Error:",sys.exc_info()[1])



class Customer:
    def __init__(self):
        self.name = input("What's your name?")
        self.order = {}
        self.money = 0
        self.addMoney()
    def check(self):
        try:
            print("{}'s account:".format(self.name))
            print("Current Money: ${}".format(self.money))
            print("Current Order: {}".format(self.order))
        except:
            print("Error:", sys.exc_info()[1])
    def addMoney(self):
        while True:
            try:
                self.money += int(input("Enter number of Pennies($0.01):")) * 0.01
                break
            except:
                print("Error: ", sys.exc_info()[1])
        while True:
            try:
                self.money += int(input("Enter number of Dimes($0.10):")) * 0.1
                break
            except:
                print("Error: ", sys.exc_info()[1])
        while True:
            try:
                self.money += int(input("Enter number of Nickels($0.05):")) * 0.05
                break
            except:
                print("Error: ", sys.exc_info()[1])
        while True:
            try:
                self.money += int(input("Enter number of Quarters($0.25):")) * 0.25
                break
            except:
                print("Error: ", sys.exc_info()[1])
        self.money = round(self.money, 2)
        print("Current Money: $", self.money)
    def getMoneyBack(self):
        try:
            print("You will get ${} back.".format(self.money))
            self.money = 0
        except:
            print("Error: ", sys.exc_info()[1])

    def getOrder(self):
        try:
            if self.order == {}:
                print("You don't have any order yet.")
            else:
                print("Here is your drink:")
                for i in self.order:
                    print("{} {}".format(self.order[i], i.title()))
                self.order = {}
        except:
            print("Error:", sys.exc_info()[1])

    def makeOrder(self, storage, menu):
        print("Current money: $ ", self.money)
        print(menu.check())
        drink = input("Would you like to drink?").lower()
        try:
            chosen_drink = menu.menu[drink]
            try:
                if self.money >= chosen_drink.cost:
                    if storage.makeDrink(chosen_drink):
                        self.money -= chosen_drink.cost
                        print(f"Here's your {drink.title()}")
                        if drink in self.order:
                            self.order[drink] += 1
                        else:
                            self.order[drink] = 1
                    else:
                        print("Sorry for Ingredients Insufficient!!!")
                        return None
                else:
                    print("Money insufficient({}'s price: ${}, you have: ${}) !!!".format(drink, chosen_drink.money,
                                                                                          self.money))
            except:
                print("Error:", sys.exc_info()[1])
        except:
            print(f"Cannot find {drink} in menu")

def getcmd():
    return input("Commands:  add_money, check_storage, check_customer, end, fill_storage, get_drink, get_money_back, make_order\nWhat do you want to do?").lower()

def command(customer,cmd,storage,menu):
    try:
        match cmd:
            case "check_storage":
                storage.check()
                cmd = getcmd()
                return command(customer,cmd,storage,menu)
            case "fill_storage":
                if bool(input("Do you want to fill the storage manually(Y/N)?").lower()):
                    try:
                        water = int(input("Enter amount of water(ml) to fill:"))
                        milk = int(input("Enter amount of milk(ml) to fill:"))
                        coffee = int(input("Enter amount of coffee(ml) to fill:"))
                        storage.fill(storage,IngredientDict(water = water,milk = milk,coffee = coffee))
                    except:
                        print("Error: ",sys.exc_info()[1])
                cmd = getcmd()
                return command(customer,cmd,storage,menu)
            case "check_customer":
                customer.check()
                cmd = getcmd()
                return command(customer,cmd,storage,menu)
            case "add_money":
                customer.addMoney()
                cmd = getcmd()
                return command(customer,cmd,storage,menu)
            case "get_money_back":
                customer.getMoneyBack()
                cmd = getcmd()
                return command(customer,cmd,storage,menu)
            case "make_order":
                customer.makeOrder(storage,menu)
                cmd = getcmd()
                return command(customer,cmd,storage,menu)
            case "get_drink":
                customer.getOrder()
                cmd = getcmd()
                return command(customer,cmd,storage,menu)
            case "end":
                customer.getMoneyBack()
                customer.getOrder()
                print("Thank you for purchasing Coffee!")
                return 0
            case default:
                print("Syntax Error")
                cmd = getcmd()
                return command(customer,cmd,storage,menu)
    except:
        print("Error:",sys.exc_info()[1])
        return -1
storage = Storage()
menu = Menu()
menu.addDrink([Drink("espresso",1.5,{
                    "water": 200,
                    "milk": 150,
                    "coffee": 24
                }),
               Drink("latte", 2.5, {
                   "water": 200,
                   "milk": 150,
                   "coffee": 24
               }),
               Drink("cappuccino", 2.5, {
                   "water": 200,
                   "milk": 150,
                   "coffee": 24
               }),
               ])
customer = Customer()
cmd =  getcmd()
command(customer,cmd,storage,menu)

