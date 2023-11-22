class Critter(object):
    def __init__(self, name):
        print("A new critter has been born!")
        self.__name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if new_name == "":
            print("A critter's name can't be the empty string.")
        else:
            self.__name = new_name
            print("Name change successful.")

    def talk(self):
        print("\nHi, I'm", self.name)

critter = Critter("Poochie")

critter.talk()

print("\nMy critter's name is:", critter.name)

print("\nAttempting to change my critter's name.")
critter.name = ""

print("\nAttempting to change my critter's name again.")
critter.name = "Randolph"

critter.talk()

input("\nPress the enter key to exit.")

