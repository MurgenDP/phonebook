import configparser
import phonebook as ph
import messages as msg
import menu as m
import contact as cn
import argparse

config = configparser.ConfigParser()
config.read(".\\phonebook.conf")
FORMAT_PHONEBOOK = config['MAIN']['phonebook_format'].upper()
MODE_INPUT = config['MAIN']['mode_input'].upper()       # console, keyboard

PHONEBOOK_DATA_JSON = 'phonebook.json'
PHONEBOOK_DATA_PICKLE = 'phonebook.pickle'
PHONEBOOK_DATA_CSV = 'phonebook.csv'


def input_name(text=None):
    if text:
        name = text
    else:
        name = input('Input name: ')
    if not name.isalpha():
        raise KeyError(msg.MSG_INCORRECT_NAME)
    return name


def input_number(text=None):
    if text:
        number = text
    else:
        number = input('Input phone number: ')
    if not number.isnumeric():
        raise KeyError(msg.MSG_INCORRECT_PHONE)
    return number


def input_email(text=None):
    if text:
        email = text
    else:
        email = input('Input email: ')
    if not email.isprintable():
        raise KeyError(msg.MSG_INCORRECT_EMAIL)
    return email


def add_contact(book, **kwargs):
    print('add_contact.kwargs: ', kwargs)
    name = input_name(text=kwargs.get('name', None))
    phone = input_number(text=kwargs.get('phone', None))
    email = input_email(text=kwargs.get('email', None))
    contact = cn.Contact(name=name, phone=phone, email=email)
    book.add_contact(contact)


def add_phonenumber(book, **kwargs):
    name = input_name(text=kwargs.get('name', None)).upper()
    contact = book.get(name)
    if contact:
        phone = input_number(text=kwargs.get('phone', None))
        contact.add_phone(phone)
        book.update_contact(name, contact)


def add_email(book, **kwargs):
    print('add_email.kwargs: ', kwargs)
    name = input_name(text=kwargs.get('name', None)).upper()
    contact = book.get(name)
    if contact:
        email = input_email(text=kwargs.get('email', None))
        contact.add_email(email)
        book.update_contact(name, contact)


def delete_contact(book, **kwargs):
    name = input_name(text=kwargs.get('name', None)).upper()
    book.delete_contact(name)


def delete_phonenumber(book, **kwargs):
    name = input_name(text=kwargs.get('name', None)).upper()
    print(type(book))
    if name not in book:
        raise KeyError(msg.MSG_CONTACT_NOT_EXISTS)
    number = input_number(text=kwargs.get('phone', None))
    book[name].delete_phone(number)


def delete_email(book, **kwargs):
    name = input_name(text=kwargs.get('name', None)).upper()
    if name not in book:
        raise KeyError(msg.MSG_CONTACT_NOT_EXISTS)
    email = input_email(text=kwargs.get('email', None))
    book[name].delete_email(email)


def update_phonenumber(book, **kwargs):
    name = input_name().upper()
    if name not in book:
        raise KeyError(msg.MSG_CONTACT_NOT_EXISTS)
    number_old = input_number('Input old number: ')
    number_new = input_number('Input new number: ')
    book[name].update_phone(number_old, number_new)


def update_email(book, **kwargs):
    name = input_name().upper()
    if name not in book:
        raise KeyError(msg.MSG_CONTACT_NOT_EXISTS)
    email_old = input_email('Input old email: ')
    email_new = input_email('Input new email: ')
    book[name].update_email(email_old, email_new)


def find(book, **kwargs):
    name = input_name(text=kwargs.get('name', None)).upper()
    if name not in book:
        raise KeyError(msg.MSG_CONTACT_NOT_EXISTS)
    print(book.find(name).show())


def view_all(book, **kwargs):
    for key, contact in book.items():
        print(key, contact.show())


def load_data(book, **kwargs):
    if 'filename' not in kwargs:
        raise KeyError(msg.MSG_INCORRECT_FILE_NAME)
    filename = kwargs['filename']
    book.load_data(file=filename)


def save_data(book, **kwargs):
    if 'filename' not in kwargs:
        raise KeyError(msg.MSG_INCORRECT_FILE_NAME)
    filename = kwargs['filename']
    book.save_data(file=filename)


def exit_(book, **kwargs):
    exit()


def dummy(book, **kwargs):
    pass


print(FORMAT_PHONEBOOK)


filename = ''
if FORMAT_PHONEBOOK == 'JSON':
    filename = PHONEBOOK_DATA_JSON
elif FORMAT_PHONEBOOK == 'PICKLE':
    filename = PHONEBOOK_DATA_PICKLE
elif FORMAT_PHONEBOOK == 'CSV':
    filename = PHONEBOOK_DATA_CSV
else:
    raise KeyError(msg.MSG_INCORRECT_DATA_FORMAT)


book = ph.PhoneBook(FORMAT_PHONEBOOK)

menu = m.Menu()
menu.add_item('1', 'Add')
menu.add_item('2', 'Find', find)
menu.add_item('3', 'Update')
menu.add_item('4', 'Delete')
menu.add_item('5', 'View all', view_all)
menu.add_item('6', 'Load data', load_data)
menu.add_item('7', 'Save data', save_data)
menu.add_item('Q', 'Quit', exit_)

menu.items['1']['menu'] = m.Menu()
menu.items['1']['menu'].add_item('1', 'Contact', add_contact)
menu.items['1']['menu'].add_item('2', 'Phone', add_phonenumber)
menu.items['1']['menu'].add_item('3', 'Email', add_email)
menu.items['1']['menu'].add_item('4', 'Return', dummy)

menu.items['3']['menu'] = m.Menu()
menu.items['3']['menu'].add_item('1', 'Phone', update_phonenumber)
menu.items['3']['menu'].add_item('2', 'Email', update_email)
menu.items['3']['menu'].add_item('3', 'Return', dummy)

menu.items['4']['menu'] = m.Menu()
menu.items['4']['menu'].add_item('1', 'Contact', delete_contact)
menu.items['4']['menu'].add_item('2', 'Phone', delete_phonenumber)
menu.items['4']['menu'].add_item('3', 'Email', delete_email)
menu.items['4']['menu'].add_item('4', 'Return', dummy)


parser = argparse.ArgumentParser()
parser.add_argument("--mode", action="store", help="input mode", required=True)
parser.add_argument("--action", action="store", help="action [add, find, delete]", nargs='+')
parser.add_argument("--name", action="store", help="contact name")
parser.add_argument("--phone", action="store", help="contact phone")
parser.add_argument("--email", action="store", help="contact email")
args = parser.parse_args()

arguments = dict(vars(args))
print('arguments: ', arguments)
if "mode" in arguments and arguments["mode"] == "interactive":
    while True:
        try:
            menu.show()
            choice = menu.input_choice()

            if choice not in menu.items:
                continue
            submenu = menu.items[choice].get('menu', None)
            if submenu is None:
                action = menu.get_action(choice)
            else:
                submenu.show()
                choice_1 = submenu.input_choice()
                action = submenu.get_action(choice_1)

            action(book, filename=filename)

        except KeyError as e:
            print(e)
elif "mode" in arguments and arguments["mode"] == "console":
    load_data(book, filename=filename)
    view_all(book)
    print(100*'*')
    if 'action' not in arguments:
        raise AttributeError("Action attribute is required")
    # if len(arguments['action']) != 2:
    #     raise AttributeError("Action attribute incorrect")
    if 'name' not in arguments:
        raise AttributeError("Name attribute is required")

    param = {}
    param['name'] = arguments.get("name", None)
    param['phone'] = arguments.get("phone", None)
    param['email'] = arguments.get("email", None)

    if args.action[0] == "add":
        if args.action[1] == "contact":
            add_contact(book, **param)
            add_email(book, name=param['name'], email='zzz')
        if args.action[1] == "phone":
            add_phonenumber(book, **param)
        if args.action[1] == "email":
            add_email(book, **param)
    elif args.action[0] == "delete":
        if args.action[1] == "contact":
            delete_contact(book, **param)
        if args.action[1] == "phone":
            delete_phonenumber(book, **param)
        if args.action[1] == "email":
            delete_email(book, **param)

    elif args.action[0] == "delete":
        pass
    elif args.action[0] == "find":
        find(book, **param)

    view_all(book)

# python main.py --mode=console --action=add --name test --phone 123321 --email qwe
# python main.py --mode=console --action=delete contact --name bill --phone 123321 --email qwe

