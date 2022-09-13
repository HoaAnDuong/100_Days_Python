import os
def strToInt(str):
    return int(str) 

def isLeap(year):
    if year % 400 == 0: return False
    elif year % 100 == 0: return True
    elif year % 4 == 0: return True
    else: return False

dict = {"1":1}

print("I used to spend a lot of time find bugs in my spaghetti-like code. But, finding bugs by looking at the code isn't easy.")
print("I've recently found 2 methods to find bugs, which is called Debugger. Remember, Debuggers wont help you slay the bugs. It's just help you tracking the bugs.")
print("To prevent program ended up with exception, I will put bugged code in try/except. One more thing, when exception is thrown, below code in try block will be ignored.")

print("\nMethods 1: Use VSCode Debugger (best for debug)")
print("To Use VSCode Debugger, you can click Run->Start Debugging or use shortcut F5 or Ctrl+Shift+D")
print("When Running with Debugger, you can access to many features to understand what is going on in the program as well as errors.")
print("Here the VSCode debugger document link:")
print("https://code.visualstudio.com/docs/editor/debugging")
print("Beside VSCode, Many Python IDE like PyCharm,etc. also have its own debugger.")
try:
    print(strToInt("1.23123"))
except:
    pass
try:
    print(strToInt("1"))
except:
    pass
try:
    is_leap = isLeap(2000)
    print(is_leap)
except:
    pass

try:
    print(dict[1])
except:
    pass

print("\nMethod 2: Python Debugger (pythonic)")
print("To use Python debugger, you just need to import pdb")
print("One of the simple way to use Python debugger is use pdb.set_trace()")
print("You can type code in terminal line (Pdb) to excute and debug")
print("When you type \"h\" in terminal line (Pdb), it will print command")
print("When you type \"s\" in terminal line (Pdb), it will start debugging codes below pdb.set_trace()")
print("Here the Python Debugger docs:")
print("https://docs.python.org/3/library/pdb.html")
import pdb
pdb.set_trace()
try:
    print(strToInt("1.23123"))
except:
    pass
try:
    print(strToInt("2"))
except:
    pass
try:
    is_leap = isLeap(2100)
except:
    pass

try:
    print(is_leap)
except:
    pass

try:
    print(dict[2])
except:
    pass

print("To disable Python Debugger, just enter c ")

print("\nBonus Method: Look direcly as output and your code")
print("It's the easiest way to debug code. For example:")

print(("print(strToInt(\"3.14\"))"))
print(strToInt("3.14"))



