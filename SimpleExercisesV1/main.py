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

#lambda
calc = lambda num: "Even number" if num % 2 == 0 else "Odd number"
print(calc(12))