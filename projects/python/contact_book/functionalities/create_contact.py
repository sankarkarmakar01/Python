def create_contact(contacts):
    name = input("Enter your name: ").strip()
    if not name:
        print("Name cannot be empty...")
        return

    if name in contacts:
        print("This contact is already added...")
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
    print("Contact added successfully...")
