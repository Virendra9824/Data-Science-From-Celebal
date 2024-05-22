print("\n#################################################\n")

str1 = "Hello-World"
str2 = '''"Joy" is rich guy!'''
str3 = "Warning-Message"

print(str1)
print(str2)
print(str3)


print("\n#################################################\n")

print(str1[0:5])


print("\n#################################################\n")
print(str1[-1])


print("\n#################################################\n")

print(str1.upper())
print(str1.lower())
print(str2.count('i'))
print(str2.replace('J','R'))

print("\n#################################################\n")
greeting = "Hello"
name = "Archit"

message1 = greeting + " " + name + ", " +  "Welcome!"
print(message1)

message2 = '{} {}, Welcome!'.format(greeting, name)
print(message2)

message3 = f'{greeting} {name}, Welcome!'
print(message3)

print("\n#################################################\n")

print(dir(name))

print("\n#################################################\n")

print(help(str))

