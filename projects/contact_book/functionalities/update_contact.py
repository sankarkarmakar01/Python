def update_contact(contacts):
    name = input("Enter the name of the contact to update: ").strip()
    if not name:
        print("Name cannot be empty...")
        return

    email = input("Enter your email: ").strip()

    try:
        age = int(input("Enter your age: "))
    except ValueError:
        print("Age must be an integer...")
        return

    phone = input("Enter your phone number: ").strip()
    if not phone:
        print("Phone number cannot be empty...")
        return

    contacts[name] = {
        "name": name,
        "email": email,
        "age": age,
        "phone": phone
    }
    print("Contact updated successfully...")
