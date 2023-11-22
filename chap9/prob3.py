class Critter:
    def __init__(self, name):
        print("A new critter has been born!")
        self.name = name
    
    def talk(self):
        print("Hi. I'm", self.name, "\n")
    
    def __str__(self):
        rep = "Critter object\n"
        rep += "name: " + str(self.name) + "\n"
        return rep
    
crit1 = Critter("Poochie")
crit1.talk()

crit2 = Critter("Randolph")
crit2.talk()

print("Printing crit1:")
print(crit1)

print("Directly accessing crit1.name:")
print(crit1.name)

print("")

input("Press the enter key to exit.")

