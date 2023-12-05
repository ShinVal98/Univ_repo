contacts = {}

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def change_contact(name, new_phone_number):
    if name in contacts:
        contacts[name] = new_phone_number
        print("Contact updated.")

def show_phone(name):
    if name in contacts:
        print(f"Phone Number for {name}: {contacts[name]}")

def main():
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)
        
        if command in ['hello', 'hi']:
            print("How can I help you?")

        elif command == 'add':
            print(add_contact(args, contacts))

        elif command == 'change':
            name = input("Enter the contact's name: ")
            new_phone_number = input("Enter the new phone number: ")
            change_contact(name, new_phone_number)

        elif command == 'phone':
            name = input("Enter the contact's name: ")
            show_phone(name)

        elif command == 'all':
            print("All Contacts:")
            for name, phone_number in contacts.items():
                print(f"Name: {name}, Phone Number: {phone_number}")

        elif command in ['exit', 'close']:
            print("Goodbye!")
            break

        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
