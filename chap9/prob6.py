class Critter:
    def __init__(self, name):
        print("A new critter has been born!")
        self.__name = name

    def set_name(self, new_name):
        if new_name == "":
            print("A critter's name can't be the empty string.")
        else:
            self.__name = new_name
            print("Name change successful.")

    def get_name(self):
        return self.__name

    name = property(get_name, set_name)

crit = Critter("Poochie")

print("\nHi, I'm", crit.get_name())

print("\nMy critter's name is:", crit.get_name())

print("\nAttempting to change my critter's name.")

crit.set_name("")

print("\nAttempting to change my critter's name again.")

crit.set_name("Randolph")

print("\nHi, I'm", crit.get_name())

print()

input("Press the enter key to exit.")

