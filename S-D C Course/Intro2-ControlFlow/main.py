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

reynolds_number = 100

if 2000 < reynolds_number < 10_000:
    print('flow regime is transitional')

if reynolds_number > 2000 and reynolds_number < 10_000:
    print('flow regime is transitional!')

if reynolds_number <= 2000 or reynolds_number >= 10_000:
    print('flow regime is not transitional')



