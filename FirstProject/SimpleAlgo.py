def sum_of_even_numbers(n):
    total = 0
    for i in range(2, n+1, 2):
        total += i
        a = 5
    return total

# Example usage
#n = int(input("Enter a positive integer: "))
n = 4
result = sum_of_even_numbers(n)
print(f"The sum of even numbers from 1 to {n} is {result}.")

mytext = "hello this is my text"

print('----------------------------------------------------------------')

for i in range(5):
    if i % 2 == 0:
        print("Even:", i)
        for j in range(3):
            if j == 1:
                print("  Middle loop:", j)
    else:
        print("Odd:", i)

