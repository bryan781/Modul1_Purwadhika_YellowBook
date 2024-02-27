import json

def load_contacts():
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

    for contact in contacts:
        if contact["phone"] == phone:
            print("Contact with this phone number already exists.")
            return

    contact = {"name": name, "phone": phone, "email": email, "city": city, "address": address, "user_id": user_id}
    contacts.append(contact)
    save_contacts(contacts)
    print("Contact added successfully!")

def read_contacts():
    if not contacts:
        print("No contacts found.")
    else:
        for index, contact in enumerate(contacts):
            print(f"{index+1}. Name: {contact['name']}")
            print(f" Phone: {contact['phone']}")
            if contact.get("email"):
                print(f" Email: {contact['email']}")
            print(f" City: {contact['city']}")
            print(f" Address: {contact['address']}")
            print(f" User ID: {contact['user_id']}")
            print("--------------------")

def update_contact():
    user_id = input("Enter user id of the contact to update: ")
    for contact in contacts:
        if contact["user_id"] == user_id:
            name = input(f"Enter new name (leave blank to keep current: {contact['name']}): ") or contact["name"]
            new_phone = input(f"Enter new phone number (leave blank to keep current: {contact['phone']}): ") or contact["phone"]
            if new_phone != contact["phone"]:
                for c in contacts:
                    if c["phone"] == new_phone:
                        print("Contact with this phone number already exists.")
                        return
            email = input(f"Enter new email (leave blank to keep current: {contact.get('email', 'N/A')}): ") or contact.get("email", "")
            city = input(f"Enter new city (leave blank to keep current: {contact['city']}): ") or contact["city"]
            address = input(f"Enter new address (leave blank to keep current: {contact['address']}): ") or contact["address"]
            user_id = input(f"Enter new user ID (leave blank to keep current: {contact['user_id']}): ") or contact["user_id"]
            
            updated_contact = {"name": name, "phone": new_phone, "email": email, "city": city, "address": address, "user_id": user_id}
            contacts[contacts.index(contact)] = updated_contact
            save_contacts(contacts)
            print("Contact updated successfully!")
            return
    print("Contact not found.")

def delete_contact():
    phone = input("Enter phone number of the contact to delete: ")
    for contact in contacts:
        if contact["phone"] == phone:
            contacts.remove(contact)
            save_contacts(contacts)
            print("Contact deleted successfully!")
            return
    print("Contact not found.")

def search_contact():
    search_term = input("Enter name or phone number to search: ")
    found = False
    for contact in contacts:
        if search_term.lower() in contact["name"].lower() or search_term == contact["phone"]:
            print("Contact found:")
            print(f" Name: {contact['name']}")
            print(f" Phone: {contact['phone']}")
            if contact.get("email"):
                print(f" Email: {contact['email']}")
            print(f" City: {contact['city']}")
            print(f" Address: {contact['address']}")
            print(f" User ID: {contact['user_id']}")
            print("--------------------")
            found = True
    if not found:
        print("No matching contacts found.")

contacts = load_contacts()

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
