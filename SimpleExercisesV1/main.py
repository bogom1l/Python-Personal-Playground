"""
#reverse numbers
numbers = input().split()

while numbers:
    last_element = numbers.pop()
    print(last_element, end=' ')
"""

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

#var = [(x, y) for x in range(1, 4) for y in range(10, 14)]
#var = [x for x in range(10) if x % 2 == 0]
var = {x: x**2 for x in range(5)}


print(var)