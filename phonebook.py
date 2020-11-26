import serializers
import messages as msg
import copy
import json
from contact import Contact


def check_phonenumber(number):
    if not number.isnumeric():
        raise KeyError(msg.MSG_INCORRECT_PHONE)
    return number


def check_email(email):
    if not email:
        raise KeyError(msg.MSG_INCORRECT_EMAIL)
    return email



class PhoneBook:
    """
    phonebook = {
        'BILL': {'name': 'Bill',
                'phone': ['380671111111',],
                'email': ['test@test.ua',],
        }
    }
    """
    def __init__(self, format):
        self._phonebook = {}
        self.format = format
        self.serializer = serializers.Serializers(format=format)

    def __iter__(self):
        for key in self._phonebook:
            yield key

    def __getitem__(self, key):
        return self._phonebook[key]

    def items(self):
        for key, value in self._phonebook.items():
            yield key, value

    def load_data(self, file=None):
        self._phonebook = self.serializer.load(file)

    def save_data(self, file=None):
        self.serializer.save(file, self._phonebook)

    def get_all(self):
        return self._phonebook.copy()

    def get(self, name):
        return self._phonebook.get(name, None)

    def find(self, name):
        return self.get(name)

    def add_contact(self, contact_):
        self._phonebook[contact_.name.upper()] = contact_.copy()

    def delete_contact(self, name):
        if name not in self._phonebook:
            raise KeyError(msg.MSG_CONTACT_NOT_EXISTS)
        self._phonebook.pop(name)

    def update_contact(self, name, contact):
        self._phonebook[name.upper()] = contact.copy()
