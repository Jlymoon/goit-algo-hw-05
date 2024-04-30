
def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Contact not found."
        except ValueError:
            return "Invalid value provided."
        except IndexError:
            return "Missing required arguments."
        except Exception as e:
            return f"An unexpected error occurred: {e}"

    return inner


def parse_input(user_input):
    cmd, *args = user_input.strip().split()
    return cmd.lower(), args


@input_error
def add_contact(contacts, name, phone):
    contacts[name] = phone
    return "Contact added."


@input_error
def change_contact(contacts, name, new_phone):
    if name in contacts:
        contacts[name] = new_phone
        return "Contact updated."
    else:
        return "Contact not found."


@input_error
def show_phone(contacts, name):
    return contacts[name]


@input_error
def show_all(contacts):
    if contacts:
        return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])
    else:
        return "No contacts found."


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            if len(args) == 2:
                name, phone = args
                print(add_contact(contacts, name, phone))
            else:
                print("Give me name and phone please.")
        elif command == "change":
            if len(args) == 2:
                name, new_phone = args
                print(change_contact(contacts, name, new_phone))
            else:
                print("Give me name and new phone number please.")
        elif command == "phone":
            if len(args) == 1:
                name = args[0]
                print(show_phone(contacts, name))
            else:
                print("Enter user name.")
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()

