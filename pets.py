import time
import random
class pet:
    def __init__(self, name, happiness, entertainment, hunger):
        self.name = name
        self.happiness = happiness
        self.entertainment = entertainment
        self.hunger = hunger
    def terminal(self):
        print("Pet name: ", self.name)
        print("Commands:")
        print("\"stats\"")
        print("\"feed\"")
        print("\"play\"")
Charlie = pet("Charlie", 100, 100, 100)
while Charlie.hunger > 0 or Charlie.happiness > 0:
    Charlie.terminal()
    command = input().lower()
    if command == "stats":
        print("Name", Charlie.name)
        print("Happiness", Charlie.happiness)
        print("Entertainment", Charlie.entertainment)
        print("Hunger", Charlie.hunger)
    elif command == "feed":
        if Charlie.hunger > 90:
            print("He's full.")
        else:
            Charlie.hunger += randint(5, 15)
    elif command == "play":
        Charlie.happiness += (20/(Charlie.happiness))//1