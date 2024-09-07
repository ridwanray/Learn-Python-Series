                    #Python Mixin
class MoveMixin:
    def move(self):
        print(f"{self.__class__.__name__} is moving")

class Animal:

    def eat(self):
        print("Animal is  eating")

class Cat(MoveMixin, Animal):
    ...


class Dog(MoveMixin, Animal):
    ...


class Car(MoveMixin): ...

Cat().move()
Dog().move()
Car().move()
