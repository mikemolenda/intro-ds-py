#! /usr/local/bin/python3

# Check Types
print('Check Types:')
print()

def my_func():
    return None

print(str(type('string')))
print(str(type(None)))
print(str(type(1)))
print(str(type(1.0)))
print(str(type(my_func)))
print(str(type([1, 2, 3])))
print(str(type((1, 2, 3))))
print(str(type({1, 2, 3})))

print()


# Sequences: Iterate, Index, Concatenate, and Repeat
print('Sequences: Iterate, Index, Concatenate, and Repeat')
print()

my_list = list(range(0,10))

for item in my_list:
    print(item)

print()

print('my_list[3]:', my_list[3])
print('len(my_list):', len(my_list))
print()

print(my_list)
print(my_list + [10, 11, 12])
print(my_list * 2)
print([5] * 5)
print()

print('1 in (1, 2, 3)?', 1 in (1, 2, 3))
print('4 in [1, 2, 3]?', 4 in [1, 2, 3])
print()

# String Operations
print('String Operations:')
print()

s = 'A string in Python is a list of characters'
print(s)
print('s[2:8]:', s[2:8])
print('s[-30:-24]:', s[-30:-24])
print('s[:18]:', s[:18])
print('s[-23:]:', s[-23:])
print('\Py\' in s:', 'Py' in s)
print('s.split(\' \'):', s.split(' '))
print('s.split(\' \')[3]:', s.split(' ')[3])
print()

print()

# Dictionaries
print('Dictionaries:')
print()

temperatures = {'Chicago': 67, 'Miami': 91, 'Anchorage': 46}
print(temperatures)
print('temperatures[\'Chicago\']:', temperatures['Chicago'])
print('temperatures[\'Chicago\'] > temperatures[\'Anchorage\']):', temperatures['Chicago'] > temperatures['Anchorage'])
print()

temperatures['Los Angeles'] = 77
print('temperatures[\'Los Angeles\'] = 77')
print(temperatures)
print()

for temperature in temperatures.values():
    print(temperature)

print()

for city, temperature in temperatures.items():
    print(city, temperature, sep=': ')
print()

print()

# Unpacking Collections to Variables
print('Unpacking Collections to Variables:')
print()

tuple = ('Incognito', 'Guy', 36)
l_name, f_name, age = tuple
print(tuple)
print(l_name)
print(f_name)
print(age)
print('{} {} is {} years old'.format(f_name, l_name, age))
