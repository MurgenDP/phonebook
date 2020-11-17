import configparser
import phonebook as ph
import messages as msg
import menu

config = configparser.ConfigParser()
config.read(".\\phonebook.conf")
FORMAT_PHONEBOOK = config['MAIN']['phonebook_format'].upper()

PHONEBOOK_DATA_JSON = 'phonebook.json'
PHONEBOOK_DATA_PICKLE = 'phonebook.pickle'
PHONEBOOK_DATA_CSV = 'phonebook.csv'


# def menu_print():
#     """Печать меню"""
#     print(2 * '\n')
#     for menu_key, menu_val in MENU_STR.items():
#         print(f'{menu_key} - {menu_val["description"]}')


# def menu_input_action():
#     """Выбор пункта меню.
#         В случае если введенный символ не соответствует ни одному из пунктов, то возвращается None
#     """
#     menu_print()
#     input_str = input('\nВыберите действие: ').strip().upper()
#     if input_str not in MENU_STR:
#         raise KeyError(msg.MSG_INCORRECT_INPUT)
#     return input_str


def input_name():
    """Ввод и проверка имени абонента
        В случае некорректного имени возвращается None
    """
    _input_name = input('Введите имя: ')
    if not _input_name.isalpha():
        raise KeyError(msg.MSG_INCORRECT_NAME)
    return _input_name
#
# def contact_input_number():
#     input_number = input('Введите телефон: ')
#     if not input_number.isnumeric():
#         raise KeyError(msg.MSG_INCORRECT_PHONE)
#     return input_number

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
book.load_data(filename)


# MENU_STR = {
#     '1': {'description': 'Создать запись', 'action': phonebook_new_item},
#     '2': {'description': 'Найти по имени', 'action': phonebook_find_item},
#     '3': {'description': 'Изменить номер', 'action': phonebook_update_item},
#     '4': {'description': 'Удалить абонента', 'action': phonebook_delete_item},
#     '5': {'description': 'Просмотр справочника', 'action': phonebook_print_all},
#     'Q': {'description': 'Выход', 'action': exit_},
# }

menu = menu.Menu()
menu.add_item('1', 'Add', book.add)
menu.add_item('2', 'Find', book.find)
menu.add_item('3', 'Update', book.update)
menu.add_item('4', 'Delete', book.delete)
menu.add_item('5', 'View all', book.view_all)
menu.add_item('6', 'Load data', book.load_data)
menu.add_item('7', 'Save data', book.save_data)
menu.add_item('Q', 'Quit', exit)

while True:
    try:
        menu.show()
        choice = menu.input_choice()
        contact_name = ''
        contact_number = ''
        if choice not in ('Q', '5', '6', '7'):
            contact_name = input_name()
            if choice in ('1', '3'):
                contact_number = input('Input phone number: ')

        if choice == '1':
            book.add(contact_name, contact_number)
        elif choice == '2':
            book.find(contact_name)
        elif choice == '3':
            book.update(contact_name, contact_number)
        elif choice == '4':
            book.delete(contact_name)
        elif choice == '5':
            book.view_all()
        elif choice == '6':
            book.load_data(filename)
        elif choice == '7':
            book.save_data(filename)
        elif choice == 'Q':
            exit()

    except KeyError as e:
        print(e)



