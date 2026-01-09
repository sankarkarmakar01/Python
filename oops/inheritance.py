class Animal:
    def eat(self):
        print("Animal is eating")

class Dog(Animal):
    def eat(self):
        print("Dog is eating")

animal = Animal()
dog = Dog()

animal.eat()
dog.eat()