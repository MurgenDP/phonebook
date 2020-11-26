import messages as msg

class Menu:
    def __init__(self):
        self.items = {}

    def add_item(self, key, description, action=None):
        self.items[key] = {'description': description, 'action': action, 'menu': None}

    def action(self, key):
        if key in self.items:
            self.items[key]['action']()

    def get_action(self, key):
        if key in self.items:
            return self.items[key]['action']

    def show(self):
        print('*'*50)
        for menu_key, menu_val in self.items.items():
            print(f'{menu_key} - {menu_val["description"]}')
        print('*' * 50)

    def input_choice(self):
        choice = input('\nYour choice: ').strip().upper()
        if choice not in self.items:
            raise KeyError(msg.MSG_INCORRECT_INPUT)
        return choice
