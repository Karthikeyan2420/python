class cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"I am a cat. My name is {self.name}. I am {self.age} years old.")

    def make_sound(self):
        print("Meow")


class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"I am a dog. My name is {self.name}. I am {self.age} years old.")

    def make_sound(self):
        print("Bark")

class cow:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def info(self):
        print(f"I am a cow.my name is{self.name}.I am {self.age} years old.")

    def make_sound(self):
        print("mmaaa") 



cat1 = cat("Kitty", 2)
dog1 = Dog("Fluffy", 4)
cow1=cow("pinkyy",4)
for animal in (cat1, dog1,cow1):
    animal.make_sound()
    animal.info()