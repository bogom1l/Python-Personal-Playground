
# age, name, gender = 25, 'Jane', 'Female'
# print(age, name, gender)
#
# blood_type = 'AB'
# print(blood_type)
#
# age = 25
# print(age)
#
# age += 5
# print(age)
#
# age -= 5
# print(age)

# x = 7
# y = 3
# z = x/y
# print(z)
# print(type(x))
# print(type(z))
# print(type(int(7/3.5)))
#
# w = int(3.7)
# print(w)
# print(type(w))
#
# v = float(4)
# print(v)
# print(type(v))

# dialogue = 'alex said "hello"'
# print(dialogue)

# segment_one = "I\'am 25"
# segment_two = "years old"
# full_sentence = segment_one + " " + segment_two
# print(full_sentence)
# print(len(full_sentence))
#
# this_crash_course_is_awesome = True
# this_crash_course_is_not_awesome = False
#
# comparison_operation = not 5 > 3
# print(comparison_operation)

# movie_title = 'Harry Potter and the Prisoner of Askaban'
# print(movie_title)
# print(movie_title.upper())
# print(movie_title.lower())
# print(movie_title.count('a'))

# list1 = [1,2,3,4]
# tuple1 = (5,6,7,8)
#
# print(f"{type(list1)} : {list1}")
# print(f"{type(tuple1)} : {tuple1}")
#
# for i in list1:
#     if(i <= len(list1)-1):
#         print(f"{type(list1[i])}")

# ordered_numbers = [0,1,2,3,4,5,6,7,8,9,10]
# print(ordered_numbers[2:10])
# print(ordered_numbers[:10])
# print(ordered_numbers[4:])
#
# new_numbers = list(range(5,15))
# print(new_numbers)
#
# new_numbers2 = list(range(4, 87, 5))
# print(new_numbers2)
#
# show_title = 'game of thrones'
# print(show_title[2])
# print(show_title[2:5])
# print(show_title[2:])

# months = ['January', 'February', 'March']
# print('June' in months)
# print('March' in months)
# print('August' not in months)
# print('February' not in months)
# print('-------------')
#
# course = 'python crash course'
# print('crash' in course)
#
# ans = 'rash' in course
# print(ans)
#
# print('abc' not in course)

# grocery_list = ['bananas', 'apples', 'cauliflower']
# print(grocery_list)
# grocery_list[2] = 'strawberries'
# print(grocery_list)
#
# misspelled_vegetable = 'cucomber'
# print(misspelled_vegetable)
#
# #error
# misspelled_vegetable[3] = 'u'
# print(misspelled_vegetable)

# fruit = 'applle'
# new_fruit = fruit[:4] + fruit[-1]
# new_fruit2 = fruit.replace("applle", "apple")
# print(new_fruit)
# print(new_fruit2)

# name = 'Ameer'
# other_name = name
# name = 'John'
# print(name)
# print(other_name)
#
# books = ['Book1', 'Book2', 'Book3']
# more_books = books
# books[0] = 'Book5'
# print(books)
# print(more_books)
#
# more_books[0] = 'Book7'
# print(books)
# print(more_books)

numbers = [4, 3, 7, 4]
print(numbers)
print(len(numbers))
print(max(numbers))
print(min(numbers))
print(sorted(numbers))
print(sorted(numbers, reverse=True))

names = ['Thomas', 'Alex', 'Zack']
print(names)
print(len(names))
print(max(names))
print(min(names))
print(sorted(names))
print(sorted(names, reverse=True))


months1 = '-'.join(['January', 'February', 'March'])
print(months1)
months2 = ' '.join(['January', 'February', 'March'])
print(months2)

months_list = ['January', 'February', 'March']
months_list.append('April')
print(months_list)

print('This person is {}, {}, and {}'.format('tall', 'slim', 'strong'))



