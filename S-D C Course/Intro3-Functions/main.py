# def get_rectangle_area(length, width):
#     """ calculates area of rectangle """
#     return length * width
#
#
# length, width = map(int, (input("Please enter length and width:").split()))
# area = get_rectangle_area(length, width)
# print(f"Rectangle area = {area}")


def is_number_even(number):
    return number % 2 == 0


numbers = list(range(1, 6)) # [1, 2, 3, 4, 5]

even_numbers = list(filter(is_number_even, numbers))
print(even_numbers)

even_numbers2 = list(filter(lambda number: number % 2 == 0, numbers))
print(even_numbers2)

