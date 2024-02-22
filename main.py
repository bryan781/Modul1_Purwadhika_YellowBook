
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
  contact = {"name": name, "phone": phone, "email": email}
  contacts.append(contact)
  save_contacts(contacts)
  print("Contact added successfully!")

def read_contacts():
  if not contacts:
    print("No contacts found.")
  else:
    for index, contact in enumerate(contacts):
      print(f"{index+1}. Name: {contact['name']}")
      print(f"  Phone: {contact['phone']}")
      if contact.get("email"):
        print(f"  Email: {contact['email']}")
      print("--------------------")

def update_contact():
  contact_index = int(input("Enter the index of the contact to update: ")) - 1
  if 0 <= contact_index < len(contacts):
    contact = contacts[contact_index]
    name = input("Enter new name (leave blank to keep current): ") or contact["name"]
    phone = input("Enter new phone number (leave blank to keep current): ") or contact["phone"]
    email = input("Enter new email (leave blank to keep current): ") or contact.get("email")
    contact = {"name": name, "phone": phone, "email": email}
    contacts[contact_index] = contact
    save_contacts(contacts)
    print("Contact updated successfully!")
  else:
    print("Invalid contact index.")

def delete_contact():
  contact_index = int(input("Enter the index of the contact to delete: ")) - 1
  if 0 <= contact_index < len(contacts):
    del contacts[contact_index]
    save_contacts(contacts)
    print("Contact deleted successfully!")
  else:
    print("Invalid contact index.")

contacts = load_contacts()

while True:
  print("\nPhone Book CRUD Menu:")
  print("1. Create Contact")
  print("2. Read Contacts")
  print("3. Update Contact")
  print("4. Delete Contact")
  print("5. Exit")

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
    break
  else:
    print("Invalid choice.")
