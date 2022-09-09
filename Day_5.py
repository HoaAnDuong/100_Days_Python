import sys
import random
# list = input("Enter a list of students's height:").split()
# list_1 = [int(i) for i in list]
# sum = 0
# for i in list_!:
#     sum+=i
# print(f"Total weight {sum}\nAverage weight {sum/len(list)}")

# list_2 = input("Enter a list of students's score:").split()
# list_2 = [int(i) for i in list]
# max = 0
# for i in list_2:
#     if i > max: max = i 
# print(f"Highest score: {max}")

# n = int(input("Enter the final number in sequence:"))
# if n%2 != 0: 
#     print("Because the input number is odd, I'll subtract it by 1")
#     n-=1
# # sum = 0
# # for i in range(0, n+2,2):
# #     sum+=i
# sum = (n/2)*(n/2+1)
# print(sum)

# n1 = int(input("Enter the final number in iteration:"))
# for i in range(1,n1+1):
#     str = ""
#     if i % 3 == 0:
#         str += "Fizz"
#     if i % 5 == 0:
#         str += "Buzz"
#     print(str) if len(str) != 0 else print(i)

length = int(input("Enter length of your password:"))
password = ""
for i in range(length):
    password+=chr(random.randint(33,126))

print(f"Here your password: {password}")




