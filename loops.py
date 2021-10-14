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


#iterable - list, dictionary, tuple, set, string
# iterate -> go one by one checking each item in the collection

# dictionary:

user = {
    'name': 'Golem',
    'age': 5006,
    'can_swim': False
}


for x in user:
    print(x)  # name, age, can_swim

for key in user.keys():
    print(key)  # name, age, can_swim

for value in user.values():
    print(value)  # Golem, 5006, False

for item in user.items():
    print(item)  # ('name', 'Golem'), ('age', 5006), ('can_swim', False)

for item in user.items():
    key, value = item
    print(key, value)  # name Golem, age 5006, can_swim False

for key, value in user.items():
    print(key, value)  # name Golem, age 5006, can_swim False
