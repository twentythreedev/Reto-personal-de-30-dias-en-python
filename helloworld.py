from itertools import pairwise


print("¡hola mundo!")

print(2 + 3)
print(2 - 3)
print(2 * 3)
print(2 / 3)
print(2 ** 3)
print(2 % 3)
print(2 // 3)

print(type(10))          # Int
print(type(3.14))        # Float
print(type(1 + 3j))      # Complex number
print(type('Asabeneh'))  # String
print(type([1, 2, 3]))   # List
print(type({'name':'Asabeneh'})) # Dictionary
print(type({9.8, 3.14, 2.7}))    # Set
print(type((9.8, 3.14, 2.7)))    # Tuple


nombre = ("ivan ")
familia = ("Gonzalez ")
pais = ("Colombia")

variable_completa = nombre + familia  + pais

print(variable_completa)
