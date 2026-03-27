import time
class pet:
    def __init__(self, name, happiness, entertainment, hunger):
        self.name = name
        self.happiness = happiness
        self.entertainment = entertainment
        self.hunger = hunger
    def showstats(self, name, happiness, entertainment, hunger):
        print("Name", name)
        print("Happiness", happiness)
        print("Entertainment", entertainment)
        print("Hunger", hunger)
availablepets = ["dog", "cat", "turtle", "fish", "bird", "komodo dragon"]
Charlie = pet("Charlie", 100, 100, 100)
while 0 != 1:
    time.sleep(5)
    Charlie.showstats("Charlie", 100, 100, 100)