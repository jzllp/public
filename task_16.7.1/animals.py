from class_form import Form

animal_01 = Form('Кошка', 'Барон', 'M', 7)
animal_02 = Form('Собака', 'Феликс', 'M', 3)

print(animal_01.kind,':', '\n', animal_01.name, ':', animal_01.gender, ':', animal_01.age)
print()
print(animal_02.kind,':', '\n', animal_02.name, ':', animal_02.gender, ':', animal_02.age)