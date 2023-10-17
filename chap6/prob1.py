inventory = ['sword', 'armor', 'shield', 'healing potion', 'gold', 'gems']

def wait_for_enter():
    user_input = input("Press the enter key to continue.")
    while user_input != "":
        print("Press the enter key to continue.")

wait_for_enter()
print("You trade your sword for a crossbow.")
inventory.remove('sword')
inventory.insert(0,'crossbow')
print("Your inventory is now:")
print(inventory)
print("")

wait_for_enter()
print("You use your gold and gems to buy an orb of future telling.")
inventory.remove('gold')
inventory.remove('gems')
inventory.append('orb of future telling')
print("Your inventory is now:")
print(inventory)
print("")

wait_for_enter()
print("In a great battle, your shield is destroyed.")
inventory.remove('shield')
print("Your inventory is now:")
print(inventory)
print("")

wait_for_enter()
print("Your crossbow and armor are stolen by thieves.")
inventory.remove('crossbow')
inventory.remove('armor')
print("Your inventory is now:")
print(inventory)
print("")

user_input = input("Press the enter key to exit.")
while user_input != "":
    print("Press the enter key to exit.")
