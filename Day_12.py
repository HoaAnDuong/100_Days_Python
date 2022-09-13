

import random
import time
import math

random.seed(time.time())

print("Welcome to the Number Guessing game!!!")
max = int(input("Enter the max number to guest:"))


print("There're 3 difficulty:")
print(f"Hard: {math.ceil(math.log(max,2))}")
print(f"Medium: {2 * math.ceil(math.log(max,2))}")
print(f"Easy: {8 * math.ceil(math.log(max,2))}")

difficulty = input("Enter the difficulty:").lower()
num_of_guesses = 0
if difficulty == "hard":
    num_of_guesses = math.ceil(math.log(max,2))
elif difficulty == "medium":
    num_of_guesses = 2 * math.ceil(math.log(max,2))
else:
    num_of_guesses = 10 * math.ceil(math.log(max,2))

print(f"You choose {difficulty.title()} .You will guess a number between 0 and {max}. You will have {num_of_guesses} attempts.")
chosen_num = random.randint(0,max)

input("The number was chosen. Press Enter to ready.")

guessed_num = 0

for i in range(num_of_guesses):
    try:
        guessed_num = int(input(f"Attempt {i} (You have {num_of_guesses-i-1} attempts less):"))
        if guessed_num == chosen_num:
            print(f"Congratulations! The number is {chosen_num}.")
            break
        elif guessed_num > chosen_num:
            print(f"{guessed_num} is bigger than chosen number.")
        else:
            print(f"{guessed_num} is smaller than chosen number.")
    except:
        print(f"Sorry, you guessed wrong.Please try again (You have {num_of_guesses-i-1} attempts less)")
if guessed_num != chosen_num:
    print(f"After {num_of_guesses} attempts,you are still not guessing that number. The number is {chosen_num}")

print("\nTip: Use Binary Search. For example, from 0 to 1000, you can guess 500, then 750 if bigger or 250 if smaller.\n")
    
