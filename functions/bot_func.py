# error handling decorator
def input_error(func):
    def inner_func(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        # check for different types of errors
        except ValueError:
            return 'Enter the right amount of arguments for the command'
        except IndexError:
            return 'Missing or invalid number of arguments.'
        except KeyError:
            return 'Key was not found.'
    return inner_func


# input processing
@input_error
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


# add contact cmd
@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."


# change contact cmd
@input_error
def change_contact(args, contacts):
    name, new_phone = args
    contacts[name]
    contacts[name] = new_phone
    return 'Contact updated.'


# show phone cmd
@input_error
def show_phone(args, contacts):
    name = args[0]

    # checking for contact
    if name in contacts and len(args) == 1:
        return contacts[name]
    else:
        return 'Contact not found.'


# show all cmd
@input_error
def show_all(contacts):
    return contacts