class Cat:
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age

    def print(self):
        return f"Имя: {self.name}\nПол: {self.gender}\nВозраст: {self.age}"
