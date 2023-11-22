class Critter:
    def __init__(self):
        print("A new critter has been born!")
    
    def talk(self):
        print("Hi. I'm an instance of class Critter.\n")

crit1 = Critter()
crit2 = Critter()

print()

crit1.talk()
crit2.talk()

input("Press the enter key to exit.")

