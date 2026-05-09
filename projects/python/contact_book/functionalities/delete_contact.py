def delete_contact(contacts):
    name = input("Enter the name to delete: ").strip()

    if name in contacts:
        del contacts[name]
        print("Contact delected successfully...")
    else:
        print("Contact not found...")
