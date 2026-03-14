def list_contacts(contacts):
    if not contacts:
        print("No contacts found...")
        return

    print("\nAll Contacts:")
    for name, info in contacts.items():
        print(f"Name: {info['name']}, Email: {info['email']}, Age: {info['age']}, Phone: {info['phone']}")
