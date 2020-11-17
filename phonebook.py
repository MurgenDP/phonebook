import serializers
import messages as msg


class PhoneBook:
    '''
    phonebook = {
        'ПУПКИН': {'Пупкин': '380670671010'},
        'ИВАНОВ1': {'Иванов1': '380671111111'},
        'АБОНЕНТ': {'Абонент': '380672222222'},
    }
    '''
    def __init__(self, format):
        self._phonebook = {}
        self.format = format
        self.serializer = serializers.Serializers(format=format)

    def _check_phonenumber(self, number):
        if not number.isnumeric():
            raise KeyError(msg.MSG_INCORRECT_PHONE)
        return number

    def load_data(self, file=None):
        self._phonebook = self.serializer.load(file)

    def save_data(self, file=None):
        self.serializer.save(file, self._phonebook)

    def view_all(self):
        """Печать всего содержимого справочника"""
        for key, val in self._phonebook.items():
            print(key, val)

    def add(self, name, number):
        if self._check_phonenumber(number):
            self._phonebook[name.upper()] = {name: number}

    def find(self, name):
        for name, phone in self._phonebook[name].items():
            print(name, phone)

    def update(self, name, number):
        """Обновление номера телефона по имени абонента"""
        contact_name_upper = name.upper()
        if contact_name_upper not in self._phonebook:
            raise KeyError(msg.MSG_CONTACT_NOT_EXISTS)

        number = self._check_phonenumber(number)
        self._phonebook[contact_name_upper][name] = number

    def delete(self, name):
        if name not in self._phonebook:
            raise KeyError(msg.MSG_CONTACT_NOT_EXISTS)
        self._phonebook.pop(name)
