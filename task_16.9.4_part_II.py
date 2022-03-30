class Users:
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


form_list = {}

for i in range(1):
    form_list['name'] = input('Введите имя посетителя:')
    form_list['surname'] = input('Введите фамилию посетителя:')
    form_list['city'] = input('Введите город посетителя:')
    form_list['status'] = input('Введите статус посетителя:')

user_list = [form_list]

for user_list in user_list:
    user_1 = Users(name=user_list.get('name'),
                   surname=user_list.get('surname'),
                   city=user_list.get('city'),
                   status=user_list.get('status'))
    print()
    print(user_1.name,
          user_1.surname,
          user_1.city,
          user_1.status)

all_form = Users(user_1.name,
                 user_1.surname,
                 user_1.city,
                 user_1.status)

all_form.form()
