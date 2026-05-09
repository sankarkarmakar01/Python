def search_contact(contacts):
    name = input("Enter the name to search: ").strip()
    contact = contacts.get(name)

    if contact:
        print(
            f"Found - Name: {contact['name']}, Email: {contact['email']}, Age: {contact['age']}, Phone: {contact['phone']}")
    else:
        print("Contact not found...")
