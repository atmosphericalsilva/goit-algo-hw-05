# imorting modules and other libraries
from functions import bot_func


# bot function
def main():
    contacts = {}
    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ")
        command, *args = bot_func.parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")

        elif command == "add":
            print(bot_func.add_contact(args, contacts))

        elif command == "change":
            print(bot_func.change_contact(args, contacts))

        elif command == "phone":
            print(bot_func.show_phone(args, contacts))

        elif command == "all":
            print(bot_func.show_all(contacts))

        else:
            print("Invalid command.")


if __name__ == '__main__':
    # calling bot function
    main()