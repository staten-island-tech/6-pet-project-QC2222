import time
import random
class pet:
    def __init__(self, name, hapyns, hngr):
        self.name = name
        self.hapyns = hapyns
        self.hngr = hngr
    def terminal(self):
        print("Pet name: ", self.name)
        print("Commands:")
        print("\"stats\"")
        print("\"feed\"")
        print("\"play\"")
Charlie = pet("Charlie", 100, 100)
print(Charlie.hapyns)
while Charlie.hngr > 0 or Charlie.hapyns > 0:
    Charlie.terminal()
    command = input().lower()
    if command == "stats":
        print("Name:", Charlie.name)
        print("Happiness:", Charlie.hapyns)
        print("Hunger:", Charlie.hngr)
        time.sleep(5)
    elif command == "feed":
        if Charlie.hngr > 95:
            print("He's full.")
        else:
            Charlie.hngr += random.randint(20, 35)
            print("Charlie fed.")
        time.sleep(5)
    elif command == "play":
        Charlie.hapyns += round(20 / (Charlie.hapyns * (1 + (Charlie.hngr / 100)) // 1), 1)
        Charlie.hngr -= random.randint(2, 6)
        print("Playing with Charlie...")
        time.sleep(5)
    else:
        print("Invalid action")
    Charlie.hngr -= random.randint(3, 9)
    if Charlie.hapyns > 100:
        Charlie.hapyns = 100
    Charlie.hapyns -= round((random.randint(2, 3) * ((1 + (1 - (Charlie.hngr / 100)))**2)), 1)