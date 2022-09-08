# num = int(input("Enter a number: "))

# num = str(num)
# if int(num[-1]) % 2 == 0:
#     print(f"{num} is Even")
# else:
#     print(f"{num} is Odd")

# height = float(input("Enter height(m):"))
# weight = float(input("Enter weight(m):"))
# bmi = weight/height ** 2
# if bmi < 18.5:
#     print(f"Your BMI: {bmi} (underweight)")
# elif bmi < 25:
#     print(f"Your BMI: {bmi} (normal weight)")
# elif bmi < 30:
#     print(f"Your BMI: {bmi} (overweight)")
# elif 35:
#     print(f"Your BMI: {bmi} (obese)")
# else:
#     print(f"Your BMI: {bmi} (clinically obese)")

# year = int(input("Enter the year:"))

# if year % 100 == 0:
#     if year % 400 == 0:
#         print(f"{year} is a leap year")
#     else:
#         print(f"{year} is not a leap year")
# elif year % 4 == 0:
#     print(f"{year} is a leap year")
# else:
#     print(f"{year} is not a leap year")

# size = input("Enter the size(S, M, L):")
# add_pepperoni = bool(input("Add pepperoni(Y/N):") == "Y")
# extra_cheese = bool(input("Extra cheese(Y/N):") == "Y")
# print(size,add_pepperoni,extra_cheese)

# bill = 0
# if size == "S":
#     bill+=15
#     if add_pepperoni:
#         bill+=2
# else:
#     if size == "M":
#         bill+=20
#     if size == "L":
#         bill+=25
#     if add_pepperoni:
#         bill+=3
# if extra_cheese:
#     bill+=1

# print(f"Here the bill: {bill}")

# name_1 = input("Enter your name:")
# name_2 = input("Enter your crush name:")
# name_1 = name_1.lower()
# name_2 = name_2.lower()
# dict = {"t":0, "r":0, "u":0, "e":0, "l":0, "o":0, "v":0}
# for i in name_1:
#     for j in dict:
#         if i == j: dict[j]+= 1
# for i in name_2:
#     for j in dict:
#         if i == j: dict[j]+= 2
# chance = dict["l"] + dict ["o"] + dict ["v"] + dict ["e"]
# chance += (dict["t"] + dict ["r"] + dict ["u"] + dict ["e"])*10   
# print(f"Chance of \"cưa đổ\" your crush: {chance}%")
#this algorithm is stronger than any ML models i trained

print("Welcome to the island, you mission is find the hidden treasure here")

is_alive = bool(input("Hehe, there is a two-way lanes decision. Which's way you will turn?(left/right)").lower() == "left")

if is_alive:
    is_alive = bool(input("Damn, there is a river ahead. Would you swim?(swim/wait)").lower() == "wait")
else:
    print("You picked the wrong way and died")
if is_alive:
    choosen_door = str(input("Luckily, the tide is lower and you can walk to the otherside. OMG!!! There is so many door here. Which's door open to the treasure room?(red/yellow/blue)").lower())
else:
    print("Because the river's flow is so strong, you wiped away and drowned")

try:
    if choosen_door == "yellow":
        print("Yay,you win the treasure.But how to bring them back to home???")
    elif choosen_door == "red":
        print("You suddenly burn to ashes, and...")
    elif choosen_door == "blue":
        print("You suddenly fronzen and died like many people here.")
except:
    pass
finally:
    print("There is 5 ending here.")