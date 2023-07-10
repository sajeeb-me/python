class Animal:
    def __init__(self, name) -> None:
        self.name = name
    
    def make_sound(self):
        print('animal making sound')

class Cat(Animal):
    def __init__(self, name) -> None:
        super().__init__(name)

    def make_sound(self):
        print('meow meow')

class Dog(Animal):
    def __init__(self, name) -> None:
        super().__init__(name)
    
    def make_sound(self):
        print("bhew bhew")

bilai = Cat("Real Don")
bilai.make_sound()

shepard = Dog("Local Shepard")
shepard.make_sound()

animals = [bilai, shepard]
for animal in animals:
    animal.make_sound()