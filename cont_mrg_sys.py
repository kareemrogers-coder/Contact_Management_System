


###### MODULE 3: MINI-PROJECT| CONTACT MANAGEMENT SYSTEMS





import re

def con_database(contacts):
    with open("Contacts_list.txt", "w") as file:
        for contact in contacts:
            file.write(f"{contact["Name"]}, {contact["Phone Number"]}, {contact["Email Address"]}\n")

def add_on(contacts):
    name = input ("Please enter your full name: ")
    phone_num = input("Please enter your Phone Number: ")
    if len(phone_num) == 10:
        formatted_phone_num = f"{phone_num[:3]}-{phone_num[3:6]}-{phone_num[6:]}"
    else:
        return "invlaid entry"
    email_info = input("Please enter your email address: ")
    contacts.append({"Name": name, "Phone Number": formatted_phone_num, "Email Address": email_info})
    con_database(contacts)

def back_up():
    contact_list =[]
    with open('Contacts_list.txt', 'r') as file:
        for line in file:
            line = line.strip()
            parts = line.split(", ")
            if len(parts) == 3:
                name, phone_num, email_info = parts
                contact_list.append({"Name": name, "Phone Number": phone_num, "Email Address": email_info})
            else:
                print(f"Skipping invalid line: {line}")
    return contact_list

def modify_contact(contacts):
    view_contacts(contacts)
    pass


def rem_contact(contacts):
    view_contacts(contacts)
    option = int(input("Please select contact you would like to remove? "))
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
4 - Display all contacts.
5 - Quit.
    ''')
    

        if ans == "1":
            add_on(contact_list)
        elif ans == "2": 
            modify_contact(contact_list)
        elif ans == "3":
            rem_contact(contact_list)
        elif ans == "4": 
            view_contacts(contact_list)
        elif ans == "5":
            print("Exiting System")
            break
        else:
            print("Invalid entry. Please try again.")


main_menu()