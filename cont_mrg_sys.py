
import re

def con_database(contacts):
    with open("Contacts_list.txt", "w") as file:
        for contact in contacts:
            file.write(f"{contact["Name"]}, {contact["Phone Number"]}, {contact["Email Address"]}\n")

def add_on(contacts):
    name = input ("Please enter your full name: ")
    phone_num = int(input("Please enter your Phone Number: "))
    email_info = input("Please enter your email address: ")
    contacts.append({"Name": name, "Phone Number": phone_num, "Email Address": email_info})
    con_database(contacts)
    # print(contacts)

def back_up():
    contact_list =[]
    with open('Contacts_list.txt', 'r') as file:
        for line in file:
            # data = re.search(r"([\w\s]+), ([\d{3}]-[\d{3}]-[\d{4}]), ([\w.]+@[\w]+\.[\w]+)",line)
            name, phone_num, email_info = line.split(", ") # only take one argument
            contact_list.append({"Name": name, "Phone Number": phone_num, "Email Address": email_info})
    return contact_list

def modify_contact(contacts):
    pass

def rem_contact(contacts):
    view_contacts(contacts)
    option = int(input("Please select contact you would like to remove "))
    contact = contacts.pop(option-1)
    print(f"{contact['Name']} was removed! ")
    con_database(contacts)

def view_contacts(contacts):
    for index, contact in enumerate(contacts):
        print(f"{index + 1} {contact['Name']} {contact['Phone Number']} {contact['Email Address']}")



def main_menu():
    flag = True
    while True:
        contact_list = back_up()
        ans = input(''' 

Welcome your Contact Management System
Select from the following features:
                
1 - Add a new contact. 
2 - Edit an existing contact.
3 - Delete a contact.
4 - Search for a contact. 
5 - Display all contacts.
6 - Export contacts to a text file.
7 - Import contacts from a text file.
8 - Quit.
    ''')
    

        if ans == "1": # this can be join with 7 (I can add a contact and have it import from a text file)
            add_on(contact_list)
        elif ans == "2":
            pass
        elif ans == "3":
            rem_contact(contact_list)
        elif ans == "4": # bonus question
            pass
        elif ans == "5": # this can be join with 6 (I can display the contact and have it export from a text file)
            view_contacts(contact_list)
        # elif ans == "6":
        #     pass
        # elif ans == "7":
            # pass
        elif ans == "8":
            print("Exiting System")
            break
        else:
            print("Invalid entry. Please try again.")


main_menu()