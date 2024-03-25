"""
#reverse numbers
numbers = input().split()

while numbers:
    last_element = numbers.pop()
    print(last_element, end=' ')
"""
import sys

"""
#reverse numbers v2
numbers = input().split()
reversed_array = []

while numbers:
    last_element = numbers.pop()
    reversed_array.append(last_element)

print(reversed_array)
"""

"""
#lambda
calc = lambda num: "Even number" if num % 2 == 0 else "Odd number"
print(calc(12))
"""

"""
#var = [(x, y) for x in range(1, 4) for y in range(10, 14)]
#var = [x for x in range(10) if x % 2 == 0]
var = {x: x**2 for x in range(5)}

print(var)
"""

"""
vowels = "aeiou"
word = "PythonABC"

result = [symbol for symbol in word if symbol.lower() in vowels]
print(result)
"""

"""
squared = map(lambda x: x**2, range(1, 5))
print(type(squared))
print(list(squared))

result = [str(x) for x in [1, 2, 3]]
print(type(result))
print(result)

result = map(str, [1, 2, 3])
print(type(result))
print(result)
print(list(result))
"""

"""
result = [x for x in [1, 2, 3]]
print(type(result))
print(result)

[print(x) for x in [1, 2, 3]]
[print(x, end=" ") for x in [1, 2, 3]]
"""

"""
b = (x for x in range(101))
print(type(b))
print(b)
print(sys.getsizeof(b))

a = list(b)
print(type(a))
print(sys.getsizeof(a))
print(a)
"""

"""
my_list = []

if my_list:
    print("not empty")
else:
    print("empty")

my_list.append(1)

if my_list:
    print("not empty")
else:
    print("empty")

my_list.clear()

if my_list:
    print("not empty")
else:
    print("empty")
"""



