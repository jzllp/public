from class_form import Rectangle, Square, Circle, Circle_d

rect_1 = Rectangle(3,4)
rect_2 = Rectangle(12,5)

print(rect_1.get_area())
print(rect_2.get_area())

square_1 = Square(5)
square_2 = Square(10)

print()
print(square_1.get_area(), square_2.get_area())

circle_1 = Circle(3.14, 20)

print()
print(circle_1.get_area())

circle_2 = Circle_d(3.14, 40)

print()
print(circle_2.get_area())

figures = [rect_1, rect_2, square_1, square_2, circle_1, circle_2]
for figures in figures:
    if isinstance(figures, Square):
        print(figures.get_area())
    else:
        print(figures.get_area())