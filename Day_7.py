import random
word = ""
length = int(input("Enter the word's length:"))

for i in range(length):
    word += chr(random.randint(97,122))
prediction = ""
i=0
while(prediction != word):
    i += 1
    hint_letter = input("Choose a letter(from a to z) to get a hint:")[0].lower()
    hint_word = ""
    for letter in word:
        if letter == hint_letter: 
            hint_word += "1"
        else: hint_word += "0"
    if i > 30:
        print("You are DEAD...inside")
    elif i > 25:
        print("You spent more than 25 attempts (the number of alphabet) and still suffered from that word *haha*")
    elif i == 10:
        print("10 attempts passed and you're still guessing")
    elif i == 20:
        print("20 attempts passed and (maybe) you gonna guest all the letters *and tired*")
    print("Here the hint: ", hint_word)
    prediction = input(f"Attempt {i}:")
    

print(f"Let's go!!!Here the word: {word}")