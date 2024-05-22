print("\n#####PROTECTED-MEMBER#####\n")
class Base: 
	def __init__(self): 
		# Protected member 
		self._a = 2

class Derived(Base): 
	def __init__(self): 

		Base.__init__(self) 
		print("Calling protected member of base class: ", 
			self._a) 

		self._a = 3
		print("Calling modified protected member outside class: ", 
			self._a) 


obj1 = Derived() 

obj2 = Base() 

print("Accessing protected member of obj1: ", obj1._a) 

print("Accessing protected member of obj2: ", obj2._a) 

print("\n#################################################\n")


print("\n#####PRIVATE-MEMBER#####\n")
# class Animal:
#     def __init__(self):
#         self.__age = 20
	
	# def getPvtData(self):
	# 	print("The private data is: ", self.__age)
			

class Animal:
    def __init__(self):    
        self.__age = 20    
    
    def getPvtData(self):  
        print("The private data is: ", self.__age)  



a1 = Animal()
a1.getPvtData()
# print("The age of animal is: ", a1.__age) # This line will cause error
	

