def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts: dict):
    name, phone = args
    if name in contacts:
        return "Contact already added, change it"
    contacts[name] = phone
    return "Contact added"

def change_contact(args, contacts: dict):
    name, phone = args
    if not name in contacts:
        return "Contact not exist, add it"
    contacts[name] = phone
    return "Contact changed"

def single_phone(args, contacts: dict):
    name = args[0]
    if name not in contacts:
        return "Contact not exist"
    return name + " number is " + contacts[name]

def all_phones(contacts: dict):
    if not contacts:
        return ["Contacts is empty"]
    result = []
    for name, phone in contacts.items():
        result.append(name + " number is " + phone)
    return result

def main():
    contacts = {}
    commands = [
        "close", 
        "exit", 
        "hello", 
        "add [username] [phone]", 
        "change [username] [phone]", 
        "phone [username]", 
        "all"
    ]
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(single_phone(args, contacts))
        elif command == "all":
            print("\n".join(all_phones(contacts)))
        else:
            print("Invalid command. Available commands:\n   ", "\n    ".join(commands))

if __name__ == "__main__":
    main()