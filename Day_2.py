import sys

# name = "Hoa An"
# print(name[0],len(name),type(name))
# year = 2003
# try:
#     print(year,type(year))
#     print(len(year))
# except:
#     print(sys.exc_info())
# try:
#     year = str(year)
#     print(year,len(year),type(year)) #u can convert int to string
#     year = float(year)
#     print(year,type(year)) #u can convert string int-like or float-like to float
#     f = "17.2003"
#     f = float(f)
#     print(f)
# except:
#     print(sys.exc_info())
# try:
#     name += str(year)
#     print(name)
#     name = float(name)
#     print(name,len(name),type(name))
# except:
#     print(sys.exc_info()[1])
# finally:
#     print("Dont worry about that *hehe*")

# input_num = input("Gimme a int:")
# try:
#     sum = 0
#     for digit in input_num:
#         sum += int(digit)
#     print("The sum of digits is ",sum)
# except:
#     print(sys.exc_info()[1])

# height = float(input("Enter your height(m):"))
# weight = float(input("Enter your weight(kg):"))
# bmi = weight/(height**2)

# print(f"Here your BMI: {round(bmi)}")

print("One day, you and the boys are going to a cafe.")
print("The owner is a beautiful girl and serves all of you with the best attitude. ")
print("At the payment, you and your friend decided to tip her depend on the percentage of the bill. ")
total_bill = float(input("Enter the total bill:"))
num_people = int(input("How many people are there:"))
percent = float(input("Enter the percentage of the bill y'all want to tip(%):"))
percent /= 100
print("Here is the total bill: ", (total_bill * (1+percent)))
print("Each person should pay: ", (total_bill * (1+percent)/num_people))




