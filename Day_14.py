# install pandas and numpy before executing (enter pip install pandas numpy in terminal)
import pandas 
import random
world_population = pandas.read_csv("WorldPopulation/world_population.csv")


def HigherLowerGame():
    
    score = 0

    print("\nWelcome to Higher Lower game!!!")
    print("You will be given you a country's population(in 2022) and another country name.")
    print("Your mission is guessed if that country's population is higher or lower than given one. ")
    print("If you guessed right, I'll show that country's population(in 2022) and give you another one to guess.")

    input("\nPress Enter to ready.")

    print("Let's go!!!")
    country_1_id = random.randint(0,233)

    while True:
        print(f"Score: {score}")
        
        country_2_id = random.randint(0,233)
        country_1 = {
            "name": world_population.loc[country_1_id][["Country"]].values[0],
            "population": world_population.loc[country_1_id][["2022 Population"]].values[0]
        }
        country_2 = {
            "name": world_population.loc[country_2_id][["Country"]].values[0],
            "population": world_population.loc[country_2_id][["2022 Population"]].values[0]
        }
        while(country_1 == country_2):
            country_2 = random.randint(0,233)
        guess =  input("{} has a population of {} in 2022. What's about {} (Higher/Lower)?".format(country_1["name"],country_1["population"],country_2["name"])).lower()

        if country_2["population"] >= country_1["population"]  and guess == "higher":
            print("You guessed right!!! {}'s population is {}".format(country_2["name"],country_2["population"]))
            print("You gained 1 point.")
            score += 1
            country_1_id = country_2_id
            print("Let's go to next country.")
        elif country_2["population"] <= country_1["population"]  and guess == "lower":
            print("You guessed right!!! {}'s population is {}".format(country_2["name"],country_2["population"]))
            print("You gained 1 point.")
            score += 1
            country_1_id = country_2_id
            print("Let's go to next country.")
        else:
            print("You guessed wrong!!! {}'s population is {}".format(country_2["name"],country_2["population"]))
            break
    print("You ended the game with a score of {}".format(score))
    return score
highscore = HigherLowerGame()
while True:
    if bool(input("Do you want to play again(Y/N)?").lower() == "Y"):
        highscore = max(highscore,HigherLowerGame())
    else:
        break
print("Best score: ",highscore)

            



