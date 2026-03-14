from functionalities.create_contact import create_contact
from functionalities.list_contacts import list_contacts
from functionalities.update_contact import update_contact
from functionalities.delete_contact import delete_contact
from functionalities.search_contact import search_contact
from functionalities.count_contacts import count_contacts

contacts = {}

def main():
    while True:
        print("""
                1. Create Contact
                2. List Contacts
                3. Update Contact
                4. Delete Contact
                5. Search Contact
                6. Count Contacts
                7. Exit
                """)
        try:
            choice = int(input("Enter your choice: ").strip())
        except ValueError:
            print("Please enter a valid number...")
            continue

        if choice == 1:
            create_contact(contacts)
        elif choice == 2:
            list_contacts(contacts)
        elif choice == 3:
            update_contact(contacts)
        elif choice == 4:
            delete_contact(contacts)
        elif choice == 5:
            search_contact(contacts)
        elif choice == 6:
            count_contacts(contacts)
        elif choice == 7:
            print("Exiting...")
            break
        else:
            print("Invalid choice...")


if __name__ == '__main__':
    main()
