import json

def load_contacts():
    # Load contacts from a dictionary
    return contacts

def load_contacts_json():
  try:
    with open("contacts.json", "r") as file:
      return json.load(file)
  except FileNotFoundError:
    return []

def save_contacts(contacts):
    with open("contacts.json", "w") as file:
        json.dump(contacts, file)

def create_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email (optional): ")
    city = input("Enter city: ")
    address = input("Enter address: ")
    user_id = input("Enter user ID: ")
    category = input("Enter category (personal or organization): ")

    for contact in contacts:
        if contact["phone"] == phone:
            print("Contact with this phone number already exists.")
            return

    contact = {"name": name, "phone": phone, "email": email, "city": city, "address": address, "user_id": user_id, "category": category}
    contacts.append(contact)
    choice = input("Save to JSON? (1.Yes, 2.No): ")
    if choice == "1":
        save_contacts(contacts)
        print("Contact added successfully and saved to JSON!")
    elif choice == "2":
        print("Contact added successfully!")
    else:
        print("Invalid choice. Contact not saved to JSON.")

def read_contacts():
    if not contacts:
        print("No contacts found in local dictionary.")
    else:
        for index, contact in enumerate(contacts):
            print(f"{index+1}. Name: {contact['name']}")
            print(f" Phone: {contact['phone']}")
            if contact.get("email"):
                print(f" Email: {contact['email']}")
            print(f" City: {contact['city']}")
            print(f" Address: {contact['address']}")
            print(f" User ID: {contact['user_id']}")
            print(f" Category: {contact['category']}")
            print("--------------------")

def update_contact():
    user_id = input("Enter user ID of the contact to update: ")
    for contact in contacts:
        if contact["user_id"] == user_id:
            name = input(f"Enter new name (leave blank to keep current: {contact['name']}): ") or contact["name"]
            new_phone = input(f"Enter new phone number (leave blank to keep current: {contact['phone']}): ") or contact["phone"]
            
            # Check for duplicate phone number
            if new_phone != contact["phone"]:
                for c in contacts:
                    if c["phone"] == new_phone:
                        print("Contact with this phone number already exists.")
                        return
            
            email = input(f"Enter new email (leave blank to keep current: {contact.get('email', 'N/A')}): ") or contact.get("email", "")
            city = input(f"Enter new city (leave blank to keep current: {contact['city']}): ") or contact["city"]
            address = input(f"Enter new address (leave blank to keep current: {contact['address']}): ") or contact["address"]
            user_id = input(f"Enter new user ID (leave blank to keep current: {contact['user_id']}): ") or contact["user_id"]
            category = input(f"Enter new category (personal or organization, leave blank to keep current: {contact['category']}): ") or contact["category"]
            
            updated_contact = {"name": name, "phone": new_phone, "email": email, "city": city, "address": address, "user_id": user_id, "category": category}
            contacts[contacts.index(contact)] = updated_contact
            choice = input("Save to JSON? (1.Yes, 2.No): ")
            if choice == "1":
                save_contacts(contacts)
                print("Contact updated successfully and saved to JSON!")
            elif choice == "2":
                print("Contact updated successfully!")
            else:
                print("Invalid choice. Contact not saved to JSON.")
            return
    print("Contact not found.")

def delete_contact():
    delete_choice=input("From where do you want to delete? 1.JSON, 2.Local      ")

    if delete_choice=="1":
        con_del=load_contacts_json()
        phone = input("Enter phone number of the contact to delete: ")
    elif delete_choice=="2":
        con_del=contacts
        phone = input("Enter phone number of the contact to delete: ")
    for contact in con_del:
        if contact["phone"] == phone:
            contacts.remove(contact)
            choice = input("Save to JSON? (1.Yes, 2.No): ")
            if choice == "1":
                save_contacts(contacts)
                print("Contact deleted successfully and saved to JSON!")
            elif choice == "2":
                print("Contact deleted successfully!")
            else:
                print("Invalid choice. Contact not saved to JSON.")
            return
    print("Contact not found.")

def search_contact():
    search_choice=input("Search in json file or locally? 1. JSON, 2.Local Dictionary   ")
    if search_choice=="1":
        search_term = input("Enter name or phone number to search: ")
        found = False
        json_contacts=load_contacts_json()
    elif search_choice=="2":
        search_term = input("Enter name or phone number to search: ")
        found = False
        json_contacts=load_contacts()
    for contact in json_contacts:
        if search_term.lower() in contact["name"].lower() or search_term == contact["phone"]:
            print("Contact found:")
            print(f" Name: {contact['name']}")
            print(f" Phone: {contact['phone']}")
            if contact.get("email"):
                print(f" Email: {contact['email']}")
            print(f" City: {contact['city']}")
            print(f" Address: {contact['address']}")
            print(f" User ID: {contact['user_id']}")
            print(f" Category: {contact['category']}")
            print("--------------------")
            found = True
    if not found:
        print("No matching contacts found.")

# Example contacts data as a dictionary
contacts = [
    {"name": "Bob", "phone": "08123123123", "email": "bob123@gmail.com", "city": "Jakarta", "address": "Menteng", "user_id": "00001", "category": "personal"},
    {"name": "Brian", "phone": "08123456789", "email": "brian456@mail.com", "city": "Surabaya", "address": "Wiyung", "user_id": "00002", "category": "personal"},
    {"name": "Alfred", "phone": "08199998888", "email": "alfred111@gmail.com", "city": "Sidoarjo", "address": "Waru", "user_id": "00003", "category": "personal"},
    {"name": "Rena", "phone": "08112225555", "email": "ren123@mail.com", "city": "Tangerang", "address": "BSD", "user_id": "00004", "category": "personal"},
    {"name": "Mely", "phone": "08133377888", "email": "melmel@mail.com", "city": "Surabaya", "address": "Kenjeran", "user_id": "00005", "category": "personal"}
]
# contacts = load_contacts()

while True:
    print("\nPhone Book CRUD Menu:")
    print("1. Create Contact")
    print("2. Read Contacts")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. Search Contact")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        create_contact()
    elif choice == "2":
        read_contacts()
    elif choice == "3":
        update_contact()
    elif choice == "4":
        delete_contact()
    elif choice == "5":
        search_contact()
    elif choice == "6":
        break
    else:
        print("Invalid choice.")
