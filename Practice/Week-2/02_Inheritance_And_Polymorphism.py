class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, name, age, year):
        super().__init__(name, age)
        self.year = 3
    
    def getDetails(self):
        print(f"The name of Student is {self.name} and his/her age is {self.age} and he/she's is in {self.year} year of graduation")

    
s1 = Student("Aman", 22, 3)
s1.getDetails()



print("\n######--Duck Typing Polymorphism--######\n")
class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"

def make_animal_speak(animal):
    return animal.speak()

dog = Dog()
cat = Cat()
print(make_animal_speak(dog))  
print(make_animal_speak(cat))  



print("\n######--Operator Overloading Polymorphism--######\n")
print(1 + 2)
print("a" + "b")   
print([1, 2] + [3, 4])  



print("\n######--Method Overloading--######\n")
def greet(name=None):
    if name:
        return f"Hello, {name}!"
    else:
        return "Hello!"

print(greet())       
print(greet("Alice"))  




print("\n######--Method Overriding--######\n")
class Animal:
    def speak(self):
        return "Some sound"

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

animals = [Dog(), Cat(), Animal()]
for animal in animals:
    print(animal.speak())

