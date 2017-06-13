#! /usr/local/bin/python3

# Parameters
print('Parameters:')

def add_numbers(x, y, z=0):
    return x + y + z

print(add_numbers(1, 2))
print(add_numbers(1, 2, 3))

print()


# Assign function to variable
print('Assign function to variable:')

my_func = add_numbers

print(type(my_func))
print(my_func(1, 2, 3))

print()


# Flag parameters
print('Flag parameters:')

def do_math(a, b, kind='add'):
    if (kind == 'add'):
        return a + b
    else: 
        return a - b

print(do_math(1, 2))
print(do_math(1, 2, 'add'))
print(do_math(1, 2, 'something else'))

print()

