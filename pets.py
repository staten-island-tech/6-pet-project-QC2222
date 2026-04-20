import time
import random
class pet:
    def __init__(self, name, hapyns, hngr, thrs):
        self.name = name
        self.hapyns = hapyns
        self.hngr = hngr
        self.thrs = thrs
    def terminal(self):
        print("")
        print("Pet name: ", self.name)
        print("Happiness:", (round(self.hapyns), 1))
        print("Hunger:", self.hngr)
        print("Thirst:", self.thrs)
        print("Commands:")
        print("\"feed\"")
        print("\"play\"")
        print("\"give water\"")
        print("\"do nothing\"")
        print("")
Charlie = pet("Charlie", 100, 100, 100)
print(Charlie.hapyns)
while Charlie.hngr >= 0 and Charlie.thrs >= 0 and Charlie.hapyns >= 0:
    Charlie.terminal()
    command = input().lower()
    if command == "feed":
        if Charlie.hngr > 95:
            print("He's full.")
        else:
            Charlie.hngr += random.randint(20, 35)
            print("Charlie fed.")
        time.sleep(2)
    elif command == "play":
        Charlie.hapyns += round((20 - (5 * (1 + (1 - (Charlie.hngr / 100))))), 1)
        Charlie.hngr -= random.randint(2, 7)
        Charlie.thrs -= random.randint(2, 7)
        print("Playing with Charlie...")
        time.sleep(2)
    elif command == "give water":
        if Charlie.thrs > 95:
            print("He's not thirsty.")
        else:
            Charlie.thrs += random.randint(20, 30)
            print("Charlie drank.")
        time.sleep(2)
    elif command == "do nothing":
        print("Doing nothing...")
        time.sleep(2)
    else:
        print("Invalid command, input something else.")
        time.sleep(2)
    Charlie.hngr -= random.randint(3, 5)
    Charlie.thrs -= random.randint(3, 5)
    Charlie.hapyns -= round((random.randint(2, 3) * ((1 + (1 - (Charlie.hngr / 100)))**2)), 1)
    if Charlie.hapyns > 100:
        Charlie.hapyns = 100
if Charlie.hngr <= 0:
    print("Charlie died of starvation, this is all your fault, you didn't feed him, what is wrong with you.")
elif Charlie.thrs <= 0:
    print("Charlie died of thirst, why would you not take care of him, how could you do this to him, he's literally dead.")
else:
    print("Charlie ran away because you were a terrible owner, you couldn't even keep him happy")