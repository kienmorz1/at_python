class Animal:
    def speak(self):
        return "ooo"

class Dog(Animal):
    def speak(self):
        return "Woof"

class Cat(Animal):
    def speak(self):
        return "Meow"

class Wolf(Animal):
    pass
    
dog = Dog()
cat = Cat()
wolf = Wolf()
print(dog.speak())
print(cat.speak())
print(wolf.speak())


def say_quack(duck):
    duck.quack()
    
class Duck():
    def quack(self):
        print("Quack Quack")

class Bird():
    def quack(self):
        print("Tweet Tweet")
duck = Duck()
say_quack(duck)
bird = Bird()
say_quack(bird)