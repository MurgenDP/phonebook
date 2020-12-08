import messages as msg
import copy


class Attribute:
    # def __init__(self):
    #     self.value = []

    def __init__(self, val=None):
        if not val:
            self.value = []
        self.value = list(val)

    def __iter__(self):
        for val in self.value:
            yield val

    def validate(self, value):
        return value

    def add(self, value):
        if self.validate(value):
            self.value.append(value)

    def delete(self, value):
        if self.validate(value):
            self.value.remove(value)

    def update(self, value, new_value):
        if self.validate(value) and self.validate(new_value):
            for idx, val in enumerate(self.value):
                if val == value:
                    self.value[idx] = new_value

    def __repr__(self):
        return repr(self.value)


class PhoneAttribute(Attribute):
    def validate(self, value):
        if not value.isnumeric():
            raise KeyError(msg.MSG_INCORRECT_PHONE)
        return value


class EMailAttribute(Attribute):
    def validate(self, value):
        if not value:
            raise KeyError(msg.MSG_INCORRECT_EMAIL)
        return value


class Contact:
    def __init__(self, name, **attr):
        self.name = name
        self.phone = PhoneAttribute()
        self.email = EMailAttribute()
        for a, value in attr.items():
            if a == 'phone':
                # self.add_phone(value)
                self.phone.add(value)
            elif a == 'email':
                # self.add_email(value)
                self.email.add(value)

    def __str__(self):
        return f'name: {self.name}; phone: {self.phone}; email: {self.email}'

    def __setstate__(self, state):
        if 'phone' in state:
            state['phone'] = PhoneAttribute(state['phone'])
        if 'email' in state:
            state['email'] = EMailAttribute(state['email'])
        self.__dict__ = state

    def to_dict(self):
        return dict(name=self.name, phone=self.phone, email=self.email)

    def copy(self):
        return copy.copy(self)

    def add_phone(self, number):
        self.phone.add(number)

    def delete_phone(self, number):
        if number not in self.phone:
            raise KeyError(msg.MSG_INCORRECT_PHONE)
        self.phone.delete(number)

    def update_phone(self, old_number, new_number):
        self.phone.update(old_number, new_number)

    def add_email(self, email):
        self.email.add(email)

    def delete_email(self, email):
        if email not in self.email:
            raise KeyError(msg.MSG_INCORRECT_EMAIL)
        self.email.delete(email)

    def update_email(self, old_email, new_email):
        self.email.update(old_email, new_email)

    def show(self):
        return f'name: {self.name}; phone: {self.phone}; email: {self.email}'

