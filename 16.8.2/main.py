from figures import Rectangle, Sqare, Circle

rectangle1 = Rectangle(5, 10)
rectangle2 = Rectangle(7, 15)
sqare1 = Sqare(20)
circle1 = Circle(15)

figures = [rectangle1, rectangle2, sqare1, circle1]

for figur in figures:
    print(figur.get_area())
