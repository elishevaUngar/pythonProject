def menu():
    choice = '0'
    while choice == '0':
        print("Main Choice: Choose 1 of 7 choices")
        print("Choose 1 for display all contacts")
        print("Choose 2 for add new contact")
        print("Choose 3 for search contact")
        print("Choose 4 for update an attribute")
        print("Choose 5 for delete contact")
        print("Choose 6 for clear all list")
        print("Choose 7 for exit")
        choice = input("Please make a choice: ")
        match choice:
            case "1":
               return 1
            case "2":
                return 2
            case "3":
                return 3
            case "4":
                return 4
            case "5":
                return 5
            case "6":
                return 6
            case "7":
                return 7
            case _:
                print(0)
menu()



