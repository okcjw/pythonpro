my_inventory = ()

def wait_for_enter():
        user_input = input("Press the enter key to continue.")
        while user_input != "":
            print("Press the enter key to continue.")

print("Your items:")
for i in range(4):
    user_input = input()
    my_inventory += (user_input,)

print("")
wait_for_enter()
print("You have", len(my_inventory), "items in your possession.")

print("")
wait_for_enter()
if "healing potion" in my_inventory:
    print("You will live to fight another day.")

print("")
slice_index = int(input("Enter the index number for an item in inventory : "))
print("At index", slice_index, "is", my_inventory[slice_index])

print("")
slice_begin = int(input("Enter the index number to begin a slice : "))
slice_end = int(input("Enter the index number to end the slice : "))
print("inventory[", slice_begin, ":", slice_end, "]", end = "\t\t")
print(my_inventory[slice_begin:slice_end])

print("")
wait_for_enter()
chest = ('gold', 'gems')
print("You find a chest. It contains:")
print(chest)

my_inventory += chest
print("You add the contents of the chest to your inventory.")
print("Your inventory is now:")
print(my_inventory)

print("")
user_input = input("Press the enter key to exit.")
while user_input != "":
    print("Press the enter key to exit.")
