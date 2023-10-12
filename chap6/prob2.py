scores = {}

while True: 
    print("\tHigh Scores Keeper\n")
    print("\t0 - Quit")
    print("\t1 - List Scores")
    print("\t2 - Add a Score")
    print("")
    
    choice = int(input("Choice: ")) 
    print("")

    if choice == 0:
        break
    elif choice == 1:
        print("High Scores\n")
        print("NAME\tSCORE")
        for name,score in sorted(scores.items(), key=lambda item: item[1], reverse=True):
            print(name + "\t" + str(score))
        print("")
    elif choice == 2:
        name = input("What is the player's name?: ")
        score = int(input("What score did the player get?: "))
        scores[name] = score
    else:
       print("Enter 0 or 1 or 2")
