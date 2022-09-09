# def isLeap(year):
#     if year % 400 == 0:
#         return True
#     elif year % 100 == 0:
#         return False
#     elif year % 4 == 0:
#         return True
#     return False
# def daysInMonth(month,year):
#     day_list = [31,28,31,30,31,30,31,31,30,31,30,31]
#     if month !=2:
#         return day_list[month-1]
#     else:
#         return 28 + isLeap(year)
# print(daysInMonth(12,2001))

# print("HoaAn".title())


def add(n1,n2):
    return n1 + n2
def subtract(n1,n2):
    return n1 - n2
def multiply(n1,n2):
    return n1 * n2
def divide(n1,n2):
    return n1 / n2
def mod(n1,n2):
    return n1 % n2
def power(n1,n2):
    return n1 ** n2


def calculateStr(str): #only accept syntax: n1 <operator> n2
    operator_dict = {
        "+":add,
        "-":subtract,
        "*":multiply,
        "/":divide,
        "%":mod,
        "^":power,
        "**":power
    }

    str = str.split(" ")
    
    try:
        n1 = float(str[0])
        operator = str[1]
        n2 = float(str[2])
        return operator_dict[operator](n1,n2)
    except:
        return 0
print(calculateStr("13 ** 13"))


