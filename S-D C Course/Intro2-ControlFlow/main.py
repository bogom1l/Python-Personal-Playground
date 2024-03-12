# grocery_items = {'bananas': 2.99, 'apples': 1.29,
#                  'papayas': 2.39}
#
# item = 'brussel sprouts'
#
# if item in grocery_items:
#     print(f'found the {item}')
# else:
#     print(f'could not find the {item}')
#     grocery_items.update({item: 5.49})
#     print('just added the item. updated groceries:', grocery_items)

# grocery_items = {'bananas': 2.99, 'apples': 1.29,
#                  'papayas': 2.39}
#
# item_name, item_price = 'rutabagas', 7.49
#
# if item_name in grocery_items:
#     print(f'found the {item_name}')
# elif item_price > 2.99:
#     print('too expensive for inventory!')
# else:
#     print(f'could not find the {item_name}')
#     grocery_items.update({item_name: item_price})
#     print('just added the item. updated groceries:', grocery_items)

# reynolds_number = 100
#
# if 2000 < reynolds_number < 10_000:
#     print('flow regime is transitional')
#
# if reynolds_number > 2000 and reynolds_number < 10_000:
#     print('flow regime is transitional!')
#
# if reynolds_number <= 2000 or reynolds_number >= 10_000:
#     print('flow regime is not transitional')
#

# months = ['January', 'February', 'March']
#
# for month in months:
#     print(month, end=' ')
#
# for number in range(0, 100):
#     print(number, end=' ')

# names = ['hillAry', 'diaNa', 'brian']
# print(names)
#
# for i in range(len(names)):
#     names[i] = names[i].title()
#
# print(names)

# movies = {'Titanic': 1997, 'Finding Nemo': 2003, 'The Matrix': 1999}
#
# for key in movies:
#     print(key)
#
# for value in movies.values():
#     print(value)
#
# for (key, value) in movies.items():
#     print(f"{key} - {value}")

# count = 0
#
# while count < 5:
#     print(f"Count is: {count}")
#     count += 1
#

# numbers = list(range(0, 10))
# print(numbers)
#
# for number in numbers:
#     if number % 2 != 0:
#         continue
#     print(number)


#----------------------------------------------------------------
# import random
# target_number = random.randint(1, 100)
#
# guess = 0
# attempts = 0
#
# while guess != target_number:
#     guess = int(input("Guess the number (between 1 and 100): "))
#     attempts += 1
#
#     if guess < target_number:
#         print("Too low!")
#     elif guess > target_number:
#         print("Too high!")
#     else:
#         print(f"Congratulations! You've guessed the number {target_number} correctly!")
#         print(f"It took you {attempts} attempts.")
#----------------------------------------------------------------

print("Finished")
