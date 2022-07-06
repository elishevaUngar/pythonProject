from Contacts.contactsFunctions import *


def menu():
    choice = 101
    while choice != '0':
        print("\n**Welcome**\n")
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
                displayAllContacts()
            case "2":
                firstName = input("Please enter first name: ")
                lastName = input("Please enter last name: ")
                phoneNumber = input("Please enter phone number: ")
                contactToAdd = Contact(firstName, lastName, phoneNumber)
                addContact(contactToAdd)
            case "3":
                contactToSearch = input("Please enter name for search: ")
                print(search1(contactToSearch))
            case "4":
                contactToSearch = input("Please enter name for update: ")
                attribute = input("Please enter attribute for update: ")
                newValue = input("Please enter a new value to update: ")
                updateContact(attribute, contactToSearch, newValue)
            case "5":
                contactToSearch = input("Please enter name for search: ")
                deleteContact(contactToSearch)
            case "6":
                deleteAllContacts()
            case "7":
                print("\nbye-bye")
                return 0


menu()
