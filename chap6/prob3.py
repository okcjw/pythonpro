geek_terms = {"uninstalled": "Uninstalled means being fired. Especially popular during the dot-bomb era.",}

while True:
    print("Geek Translator")
    print("0 - Quit")
    print("1 - Look Up a Geek Term")
    print("2 - Add a Geek Term")
    print("3 - Redefine a Geek Term")
    print("4 - Delete a Geek Term")

    choice = input("Choice: ")

    if choice == "0":
        break
    elif choice == "1":
        term = input("What term do you want me to translate?: ")
        if term in geek_terms:
            definition = geek_terms[term]
            print(definition)
        else:
            print("Term not found.")
    elif choice == "2":
        term = input("Enter the new Geek term: ")
        definition = input("Enter the definition: ")
        geek_terms[term] = definition
        print("Term added.")
    elif choice == "3":
        term = input("Enter the Geek term to redefine: ")
        if term in geek_terms:
            definition = input("Enter the new definition: ")
            geek_terms[term] = definition
            print("Term redefined.")
        else:
            print("Term not found.")
    elif choice == "4":
        term = input("Enter the Geek term to delete: ")
        if term in geek_terms:
            del geek_terms[term]
            print("Term deleted.")
        else:
            print("Term not found.")
    else:
        print("Invalid choice. Please enter a valid option.")

