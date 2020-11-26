import messages as msg
import copy

def check_phonenumber(number):
    if not number.isnumeric():
        raise KeyError(msg.MSG_INCORRECT_PHONE)
    return number


def check_email(email):
    if not email:
        raise KeyError(msg.MSG_INCORRECT_EMAIL)
    return email


class Contact:
    def __init__(self, name, **attr):
        self.name = name
        self.phone = []
        self.email = []
        for a, value in attr.items():
            if a == 'phone':
                self.add_phone(value)
            elif a == 'email':
                self.add_email(value)

    def __str__(self):
        return f'name: {self.name}; phone: {self.phone}; email: {self.email}'

    def to_dict(self):
        return dict(name=self.name, phone=self.phone, email=self.email)

    def copy(self):
        return copy.copy(self)

    def add_phone(self, number):
        if check_phonenumber(number):
            self.phone.append(number)

    def delete_phone(self, number):
        if number not in self.phone:
            raise KeyError(msg.MSG_INCORRECT_PHONE)
        self.phone.remove(number)

    def update_phone(self, old_number, new_number):
        if check_phonenumber(new_number) and old_number in self.phone:
            for idx, value in enumerate(self.phone):
                if value == old_number:
                    self.phone[idx] = new_number
        else:
            raise KeyError(msg.MSG_INCORRECT_PHONE)

    def add_email(self, email):
        if check_email(email):
            self.email.append(email)

    def delete_email(self, email):
        if email not in self.email:
            raise KeyError(msg.MSG_INCORRECT_EMAIL)

    def update_email(self, old_email, new_email):
        if check_email(new_email) and old_email in self.email:
            for idx, value in enumerate(self.email):
                if value == old_email:
                    self.email[idx] = new_email

    def show(self):
        return f'name: {self.name}; phone: {self.phone}; email: {self.email}'

