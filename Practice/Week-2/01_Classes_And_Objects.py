print("\n#################################################\n")


class Dog:
    name="Puppy"
    age=12

d1 = Dog()
print(f'Dog name is {d1.name} and its age is {d1.age}')


print("\n#################################################\n")

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    
c1 = Animal("Catty", 3)
print(f'Animal name is {c1.name} and its age is {c1.age}')



print("\n#################################################\n")

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"Animal name is {self.name} and its age is {self.age}"
    
    
c2 = Animal("Billu", 2)
print(c2)


print("\n#################################################\n")

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def getDetails(self):
        print(f"Animal name is {self.name} and its age is {self.age}")

    
    
c3 = Animal("Mini", 1)
c3.getDetails()







print("\n#################################################\n")
print("\n#################################################\n")

print("\n#################################################\n")
print("\n#################################################\n")