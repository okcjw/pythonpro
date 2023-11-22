class Critter:
    total = 0
    
    def __init__(self, name):
        Critter.total += 1
        print("A critter has been born!")

    @staticmethod
    def status():
        print("Accessing the class attribute Critter.total:", Critter.total, "\n")

Critter.status()

print("Creating critters.")
crit1 = Critter("critter 1")
crit2 = Critter("critter 2")
crit3 = Critter("critter 3")

print("\nThe total number of critters is", crit1.total)

print("\nAccessing the class attribute through an object:", crit1.total)

input("\nPress the enter key to exit.")

