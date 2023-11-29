class Critter(object):
    """A virtual pet"""
    def __init__(self, name, hunger=0, boredom=0, level=0):
        self.name = name
        self.hunger = hunger
        self.boredom = boredom
        self.level = level

    def __pass_time(self):
        self.hunger += 1
        self.boredom += 1

    @property
    def mood(self):
        unhappiness = self.hunger + self.boredom
        if unhappiness < 5:
            m = "happy"
        elif 5 <= unhappiness <= 10:
            m = "okay"
        elif 11 <= unhappiness <= 15:
            m = "frustrated"
        else:
            m = "mad"
        return m

    def feed(self, food):
        print(f"{food.name}. Thank you.")
        self.hunger -= food.getLevel()
        if self.hunger < 0:
            self.hunger = 0
        self.level += food.getCritterLevel()
        self.__pass_time()

    def play(self, fun=4):
        print("Wheee!")
        self.boredom -= fun
        if self.boredom < 0:
            self.boredom = 0
        self.__pass_time()

    def talk(self):
        print("I'm", self.name, "and I feel", self.mood, "now.\n")
        self.__pass_time()


class Food(object):
    """Food menu"""
    def __init__(self, name, level, critter_level):
        self.name = name
        self.level = level
        self.critter_level = critter_level

    def getLevel(self):
        return self.level

    def getCritterLevel(self):
        return self.critter_level


def main():
    crit_name = input("What is your critter's name?: ")
    crit = Critter(crit_name)

    food_menu = [
        Food("Feed", level=3, critter_level=2),
        Food("Meat", level=5, critter_level=3),
        Food("Gum", level=2, critter_level=1)
    ]

    choice = None
    while choice != "0":
        print(
            """
            Critter Caretaker

            0 - Quit
            1 - Listen to your critter
            2 - Feed your critter
            3 - Play with your critter
            """
        )
        choice = input("Choice: ")
        print()

        if choice == "0":
            print("Good-bye.")
        elif choice == "1":
            crit.talk()
        elif choice == "2":
            print("Food Menu:")
            for i, food in enumerate(food_menu, 1):
                print(f"{i}. {food.name}")
            try:
                food_choice = int(input("Choose a food item (1-3): "))
                if 1 <= food_choice <= 3:
                    crit.feed(food_menu[food_choice - 1])
                else:
                    print("Invalid food choice.")
            except ValueError:
                print("Invalid input. Please enter a number.")
        elif choice == "3":
            crit.play()
        else:
            print("\nSorry,", choice, "isn't a valid choice.")


main()
input("\n\nPress the enter key to exit.")
