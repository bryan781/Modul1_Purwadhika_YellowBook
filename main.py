# Initialize an empty list to store contacts
contacts = []

# Function to create (insert) a contact into the list
def create_contact(name, number):
    contact = {"name": name, "number": number}
    contacts.append(contact)
    print("Contact added successfully!")

# Function to read (retrieve) all contacts from the list
def read_contacts():
    if contacts:
        print("Contacts in the phone book:")
        for index, contact in enumerate(contacts, start=1):
            print(f"{index}. Name: {contact['name']}, Number: {contact['number']}")
    else:
        print("The phone book is empty.")

# Function to update a contact in the list
def update_contact(index, new_name, new_number):
    if 1 <= index <= len(contacts):
        contacts[index - 1]["name"] = new_name
        contacts[index - 1]["number"] = new_number
        print("Contact updated successfully!")
    else:
        print("Invalid index. Please enter a valid index.")

# Function to delete a contact from the list
def delete_contact(index):
    if 1 <= index <= len(contacts):
        deleted_contact = contacts.pop(index - 1)
        print(f"Contact '{deleted_contact['name']}' deleted successfully!")
    else:
        print("Invalid index. Please enter a valid index.")

# Main program loop
while True:
    print("\nCRUD Operations for Phone Book:")
    print("1. Add a contact")
    print("2. View all contacts")
    print("3. Update a contact")
    print("4. Delete a contact")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        name = input("Enter the contact's name: ")
        number = input("Enter the contact's number: ")
        create_contact(name, number)
    elif choice == '2':
        read_contacts()
    elif choice == '3':
        index = int(input("Enter the index of the contact to update: "))
        new_name = input("Enter the new name: ")
        new_number = input("Enter the new number: ")
        update_contact(index, new_name, new_number)
    elif choice == '4':
        index = int(input("Enter the index of the contact to delete: "))
        delete_contact(index)
    elif choice == '5':
        print("Exiting program...")
        break
    else:
        print("Invalid choice. Please enter a valid option (1-5).")
