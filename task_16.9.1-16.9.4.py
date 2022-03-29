# - task 16.9.1

class Square:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'Square({self.x}, {self.y})'


square = Square(50, 50)

print(square)


# - task 16.9.2

class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def rectangle_area(self):
        return self.a * self.b


rectangle = Rectangle(20, 60)

print("Rectangle S=", rectangle.rectangle_area())


# - task 16.9.3

class Users:
    def __init__(self, user_name, user_surname, cash):
        self.user_name = user_name
        self.user_surname = user_surname
        self.cash = cash

    def form(self):
        print(f'{self.user_name} {self.user_surname}. Баланс: {self.cash} $.')


new_user = Users('Илья', 'Иванов', 90)

new_user.form()

# - task 16.9.4

print()

invitation = input('Enter visitor name:'), \
             input("Enter visitor's last name:"), \
             input("Enter visitor's city:"), \
             input("Enter visitor status:")


class Invitation:
    def __init__(self, name, surname, city, status):
        self.name = name
        self.surname = surname
        self.city = city
        self.status = status

    def form(self):
        print()
        print('Список приглашенных:')
        print(f'{self.name} '
              f'{self.surname}' '\n'
              'г.' f'{self.city}' '\n'
              'статус ' f'{self.status}')

user_list = Invitation(invitation[0], invitation[1], invitation[2], invitation[3])

user_list.form()