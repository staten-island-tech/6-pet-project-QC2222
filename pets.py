class pet:
    def __init__(self, name, specimen, happiness, entertainment, hunger):
        self.name = name
        self.specimen = specimen
        self.inventory = inventory
        self.happiness = happiness
        self.entertainment = entertainment
        self.hunger = hunger
    def showstats(self, name, specimen, happiness, entertainment, hunger):
        print("Name", name)
        print("Specimen", specimen)
        print("Happiness", happiness)
        print("Entertainment", entertainment)
        print("Hunger", hunger)
availablepets = ["dog", "cat", "turtle", "fish", "bird", "komodo dragon"]
while x != 1:
    for i in availablepets:
        petselec = input("Choose your pet: Dog, cat, turtle, fish, bird or komodo dragon.")
