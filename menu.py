import messages as msg

class Menu:
    def __init__(self):
        self.items = {}

    def add_item(self, key, description, action):
        self.items[key] = {'description': description, 'action': action}

    def action(self, key):
        if key in self.items:
            self.items[key]['action']()

    def show(self):
        """Печать меню"""
        print('*'*50)
        for menu_key, menu_val in self.items.items():
            print(f'{menu_key} - {menu_val["description"]}')
        print('*' * 50)

    def input_choice(self):
        choice = input('\nВыберите действие: ').strip().upper()
        if choice not in self.items:
            raise KeyError(msg.MSG_INCORRECT_INPUT)
        return choice
