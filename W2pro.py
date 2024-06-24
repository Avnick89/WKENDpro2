
contact ={}

def menu():
    print(           "**MENU**")
   
    print("Enter 0 to look up an existing number.")
    print("Enter 1 to add contact .")
    print("Enter 2 to update an contact")
    print("Enter 3 delete an contact")
    print("press 4 to Exit.")
    print("press 5 to print all contacts")
    print("press 6 to display Menu")
    
    
menu()
def display():
    for key, value1 in contact.items():
        print(key, ":", value1)

while True:
    choice = int(input("Enter Option:"))

    if choice == 0:
        look = input("Name of number owner:").upper()
        keys = list(contact.keys())
        values1 = list(contact.values())

        print("Number of ", look, ":", values1[keys.index(look)])
    elif choice == 1:
        Name = input("Name of new contact: ").upper()
        Number = input("Enter 11 or 8 digit number: ")
        if len(Number) == 11:
            contact.update({Name: [Number, "Mobile"]})
            print("CONTACTS")
            display()

    elif choice == 2:
        Name = input("Name of person to update contact:").upper()
        Number = input("New contact number:")
        if len(Number) == 11:
            contact[Name] = [Number, "Mobile"]
            print("CONTACTS")
            display()

        else:
            print("Number is invalid.Please try again.")

    elif choice == 3:
        delete = input("Name of contact to remove:").upper()
        del contact[delete]
        print("CONTACTS")
        display()
    elif choice == 4:
        print("Thank you!")
        break
    elif choice == 5:
        print("CONTACTS")
        display()
    else:
        menu()