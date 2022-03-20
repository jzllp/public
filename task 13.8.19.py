# --- task 13.8.19/

tickets = int(input('Enter the desired number of tickets:'))

price = []

for i in range(tickets):
    age = input('Enter visitor age:').split()
    for age in age:
        age = int(age)
    if age < 18:
        price += [0]
    if 18 <= age < 25:
        price += [990]
    if age >= 25:
        price += [1390]

if tickets > 3:
    discount = sum(price)/100*10
else:
    discount = 0

yor_price = sum(price)-discount

print()     # - /обозначаю отступ в терминале/

print('Number of tickets -', tickets, '\n',
      'The amount of your discount -', int(discount), 'руб.', '\n',
      'The amount of your tickets, taking into account the discount -', int(yor_price), 'руб.')

