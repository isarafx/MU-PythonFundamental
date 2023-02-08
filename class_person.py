class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_name(self):
        print(f"My name {self.name}")

    def show_age(self):
        print(f"I'm {self.age} year old")