import pandas as pd

try:
    con_data = pd.read_csv("con_list.csv")
except FileNotFoundError:
    con_data = pd.DataFrame(columns=["Name", "Phone Number", "Email", "Address"])

def meanu():
    print("Enter 1 for Add Contact")
    print("Enter 2 for View Contact List")
    print("Enter 3 for Search Contact")
    print("Enter 4 for Update Contact")
    print("Enter 5 for Delete Contact")
    print("Enter 6 for Exist")

def  meanu2():
    print("Enter 1 for Name")
    print("Enter 2 for Phone Number")
    print("Enter 3 for Email")
    print("Enter 4 for Address")

def add():
    name=input("Enetr your Name:")
    phone_nm =input("Enetr your Phone number:")
    email=input("Enetr your Email:")
    address=input("Enetr your Address:")

    teamp_contact = pd.DataFrame([{"Name": name, "Phone Number": phone_nm, "Email": email, "Address": address}])
    global con_data
    con_data = pd.concat([con_data, teamp_contact], ignore_index=True)

    con_data.to_csv("contacts.csv", index=False)
    print("New Contact added successfully!")

def view():
    global con_data
    if con_data.empty:
        print("Contacts are not found.")
    else:
        print("\nContact List:\n")
        print(con_data)

def search():
    s_name=input("Enter name for search a contact details:")
    phone=input("Enter phone number for search a contact details:")
    #use both phone_number and name for uniqe search
    info=con_data[(con_data["Phone Number"]==phone) & (con_data["Name"]== s_name)]
    if not info.empty:
       print("Contact details:")
       print(info)
    else:
        print("Contact details not macth try again!!")    

def  update():
    s_name=input("Enter name for update a contact details:")
    phone=input("Enter phone number for update a contact details:")
    info=con_data[(con_data["Phone Number"]==phone) & (con_data["Name"]== s_name)]
    info_ind=con_data[(con_data["Phone Number"]==phone) & (con_data["Name"]== s_name)].index
    if not info.empty:
       print("Here your Contact details:")
       print(info)
       print("What do you want to update!!")
       print("\nPlease select your option from following:")
       meanu2()
       choice=int(input("Enter your choice:"))

    else:
        print("Contact details not macth try again!!")    
    
    if choice == 1:
        new_name = input("Enter new name: ")
        con_data.loc[info_ind, "Name"] = new_name
    if choice == 2:
        new_phone = input("Enter new phone number: ")
        con_data.loc[info_ind, "Phone Number"] = new_phone
    if choice == 3:
        new_email = input("Enter new email: ")
        con_data.loc[info_ind, "Email"] = new_email
    if choice == 4:
        new_address = input("Enter new address: ")
        con_data.loc[info_ind, "Address"] = new_address
    else:
        print("Invalid choice. Update canceled.")
        return

    con_data.to_csv("contacts.csv", index=False)
    print("Contact updated successfully!")

def  delete():
    phone=input("Enter phone number for update a contact details:")
    info=con_data[con_data["Phone Number"]==phone]
    info_ind=con_data[con_data["Phone Number"]==phone].index

    if not info.empty:
        print("Here your Contact details:")
        print(info)

        con_data.drop(info_ind, inplace=True)
        con_data.to_csv("contacts.csv", index=False)
        print("Contact deleted successfully!")
    else:
        print("Contact not found!")


def main():
    while True:
        print("Chose any one option from List:")
        meanu()

        option=int(input("Enter your choice:"))
        if option == 1:
            add()
        if option == 2:
            view()
        if option == 3:
            search()
        if option == 4:
            update()
        if option == 5:
            delete()
        if option == 6:
            print("Contact Book closed successfully. All changes have been saved. Goodbye!")
            break
        if option > 6:
            print("Invalid choice. Please try again!!")   

main()             