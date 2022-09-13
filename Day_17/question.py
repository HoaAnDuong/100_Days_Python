import pandas
import random
import time

random.seed(time.time())

data = pandas.read_csv("imdb-videogames_2.csv")

described_data = data.describe()

class BaseQuestion:
    def __init__(self):
        self.question = ""
        self.answers = {}
        self.correct_answer = ""
    def set(self,question,answers,correct_answer):
        self.question = question
        self.answers = answers
        self.correct_answer = correct_answer
    def ask(self):
        print("\n{}".format(self.question))
        print("Answer:")
        for i in sorted(self.answers):
            print("{}. {}".format(i.upper(),self.answers[i]))

        if input("Enter Your Answers:").lower() == self.correct_answer:
            print("Correct Answer!!!")
            return True
        else:
            print("Incorrect!!!The correct answer is {}. {}".format(self.correct_answer.upper(),self.answers[self.correct_answer]))
            return False

class YearQuestion(BaseQuestion):
    def __init__(self):
        super().__init__()
        self.data = data.loc[random.randint(0,727)][["name","year"]]

        self.question = "When was {} released?".format(self.data["name"])

        self.correct_answer = random.choice(["a","b","c"])
        self.answers[self.correct_answer] = self.data["year"]

        for i in ["a","b","c"]:
            if not i in self.answers:
                self.answers[i] = random.randint(self.data["year"]-5,self.data["year"]+5)
                for j in self.answers:
                    while self.answers[i] == self.answers[j] and i != j:
                        self.answers[i] = random.randint(self.data["year"] - 5, self.data["year"] + 5)
class RatingQuestion(BaseQuestion):
    def __init__(self):
        super().__init__()
        self.data = []
        for i in range(4):
            self.data.append(data.loc[random.randint(0,727)][["name","rating","votes"]])
            for j in range(i):
                while self.data[i]["rating"] == self.data[j]["rating"]:
                    self.data[i] = data.loc[random.randint(0, 727)][["name","rating","votes"]]
                    j = 0
        for i,j in enumerate(["a", "b", "c", "d"]):
            self.answers[j] = self.data[i]["name"]
        if random.random() > 0.5:
            self.question = "Which game has the highest rating(in IMDB)?"
            max = 0
            for i,j in enumerate(["a", "b", "c", "d"]):
                if self.data[i]["rating"] > max:
                    max = self.data[i]["rating"]
                    self.correct_answer = j
        else:
            self.question = "Which game has the lowest rating(in IMDB)?"
            min = 10
            for i, j in enumerate(["a", "b", "c", "d"]):
                if self.data[i]["rating"] < min:
                    min = self.data[i]["rating"]
                    self.correct_answer = j

    def ask(self):
        print("\n{}".format(self.question))
        print("Answer:")
        for i in sorted(self.answers):
            print("{}. {}".format(i.upper(), self.answers[i]))

        if input("Enter Your Answers:").lower() == self.correct_answer:
            print("Correct Answer!!!The correct answer is {}. {}(rating: {})".format(self.correct_answer.upper(),
                                                                                  self.answers[self.correct_answer],
                                                                                  self.data[ord(self.correct_answer) - ord("a")]["rating"]))
            self.getInformation()
            return True
        else:
            print("Incorrect!!!The correct answer is {}. {}(rating: {})".format(self.correct_answer.upper(),
                                                                            self.answers[self.correct_answer],
                                                                            self.data[ord(self.correct_answer) - ord("a")]["rating"]))
            self.getInformation()
            return False
    def getInformation(self):
        print("\nHere the rating:")
        for i in range(4):
            print("{}: {}(Based on {} votes)".format(self.data[i]["name"],self.data[i]["rating"],self.data[i]["votes"]))



