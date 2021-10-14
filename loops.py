# we can loop over anything that has a collection of items

# string
for letter in 'WhatEver':
    print(letter)

# list
for number in [1, 2, 3, 4, 5]:
    print(number)

# set
for set_item in {1, 2, 3, 4, 5}:
    print(set_item)

# tuple
for tuple_item in (1, 2, 3, 4, 5):
    print(tuple_item)

# nested loops
for tuple_item in (1, 2, 3, 4, 5):
    for array_item in ['a', 'b', 'c']:
        print(tuple_item, array_item)
