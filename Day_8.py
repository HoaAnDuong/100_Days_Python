
# def CanToUse(height, width, coverage = 5):
#     return round((height*width)/coverage)

# test_h = int(input("Enter height: "))
# test_w = int(input("Enter width: "))

# print(f"Here is number of paint cans to use:{CanToUse(test_h, test_w)}")

# def primeCheck(x):
#     x = abs(x)
#     if x == 0 or x == 1: return False
#     else:
#         for i in range(2,int(x ** 0.5)+ 1):
#             if x % i == 0:
#                 return False
#     return True
# a = -29999999993
# print(primeCheck(a),a)

def encrypt(x,shift):
    x = x.lower()
    str = ""
    for letter in x:
        if ord(letter) >= 97 and ord(letter) <= 122:
            char_code = ord(letter) + shift
            if char_code > 122: char_code = 97 + (char_code-122) % 25 - 1
            elif char_code < 97: char_code = 122 - (97-char_code) % 25 + 1
            str += chr(char_code)
        else: 
            str += letter 
    return str

def decrypt(x, shift):
    return encrypt(x,-shift)

def CeasarCipher(x, shift, direction):
    if direction == True or direction == "encode":
        return encrypt(x, shift)
    if direction == False or direction == "decode":
        return decrypt(x, shift)

name = encrypt("hoaan2003",-3)
print(name)
name = decrypt(name,-3)
print(name)








