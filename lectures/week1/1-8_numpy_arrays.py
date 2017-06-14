#! /usr/local/bin/python3

import numpy as np

# Creating Arrays
print('Creating Arrays:')
print()

my_list = [1, 2, 3]
list_reference_conversion = np.array(my_list)
print(list_reference_conversion)
print()

list_constant_conversion = np.array([4, 5, 6])
print(list_constant_conversion)
print()

range_array = np.arange(0, 30, 2)
print('np.arange generates an array from passed start, stop, and step args')
print(range_array)
print()

linspace_array = np.linspace(0, 4, 9)
print('np.linspace generates n indexes that are an even dispersion of values')
print('from the passed start, stop and n divisions arguments')
print(linspace_array)
print()

py_repeat = np.array([1, 2, 3] * 3)
np_repeat = np.repeat([1, 2, 3], 3)
print('Use repeat to repeat a series, sorted by value.')
print(np_repeat)
print('Contrast with Python [1, 2, 3] * 3')
print(py_repeat)
print()

print()

# Multi-dimensional Arrays
print("Multi-dimensional Arrays:")
print()

multidimensional_1 = np.array([list_reference_conversion, list_constant_conversion, [7, 8, 9]])
print(multidimensional_1)
print(multidimensional_1.shape)
print()

multidimensional_2 = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(multidimensional_2)
print(multidimensional_2.shape)
print()

jagged = np.array([[1, 2, 3, 4], [5, 6, 7]])
print(jagged)
print(jagged.shape)
print()

reshape = np.reshape(range_array, (3, 5))
print('Use reshape to convert array dimensions.')
print('The resulting array must have the same size (# indices) as the original.')
print(reshape)
print()

resize = np.resize(range_array, (2, 3))
print('Use resize to change the size or shape of the array, truncating or repeating as necessary')
print(resize)
resize = np.resize(linspace_array, 12)
print(resize)
print()

ones = np.ones((3, 2))
zeros = np.zeros((2, 3))
eye = np.eye(5)
diag = np.diag(linspace_array)
print('Create or convert 2D arrays with np.ones, np.zeros, np.eye, np.diag')
print(ones, zeros, eye, diag, sep='\n' * 2)
print()

ones = np.ones((2, 3), int)
zeros = np.zeros((2, 3), int)
vstack = np.vstack((ones, zeros))
hstack = np.hstack((ones, zeros))
print('Stack arrays vertically or horizontally with vstack and hstack.')
print(vstack)
print()
print(hstack)
print()

print()

# Array Operations
print('Array Operations:')
print()

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr3 = np.array([0., 0.5, 1., 1.5])
arr4 = np.array(['a', 'b', 'c'])

print('Unlike sequences, math operations are performed on each element of an array')
print('[1, 2, 3] * 2 =', [1, 2, 3] * 2)
print('[1 2 3] * 2 =', arr1 * 2)
print()
print('[1 2 3] + 2 =', arr1 + 2)
print('[1 2 3] ** 2 =', arr1**2)
print()

print('Arrays can be added, subtracted together, multiplied or divided')
print('[1 2 3] + [4 5 6] =', arr1 + arr2)
print('[1 2 3] * [4 5 6] =', arr1 * arr2)
print()

print('Dot product')
print('[1 2 3] • [4 5 6] =', np.dot(arr1, arr2))
print()

print('T method transposes rows and columns')
print(multidimensional_2)
print(multidimensional_2.shape)
print()
print(multidimensional_2.T)
print(multidimensional_2.T.shape)
print()

print('dtype returns array data type')
print('[1 2 3] :', arr1.dtype)
print('[0. 0.5 1. 1.5] :', arr3.dtype)
print('[\'a\' \'b\' \'c\'] : ', arr4.dtype)
print()

print('astype casts array to new datatype')
print('[1 2 3] as float :', arr1.astype('f'))
print('[0. 0.5 1. 1.5] as int :', arr3.astype('i'))
print()

print('Math functions on [0 2 4 6 … 24 26 28]')
print('sum:', np.sum(range_array))
print('min:', np.min(range_array))
print('max:', np.max(range_array))
print('mean:', np.mean(range_array))
print('median:', np.median(range_array))
print('std dev:', np.std(range_array))
print('index of min:', np.argmin(range_array))
print('index of max:', np.argmax(range_array))
print()

print()

# Indexing and Slicing
print('Indexing and Slicing:')
print()

print('Can index and slice like regular Python sequences')
print(range_array)
print('range_array[4]:', range_array[4])
print('range_array[-4]:', range_array[-4])
print('range_array[6:10]:', range_array[6:10])
print('range_array[-4:]:', range_array[-4:])
print()

table = np.arange(36)
table.resize(6, 6)
print(table)
print()
print('Specific index:')
print('table[2,2]:', table[2,2])
print()

print('Range starting at index (does not wrap across rows)')
print('table[3,3 : 6]:', table[3,3 : 6])
print('table[3,3 : 4]:', table[3,3 : 4])
print('table[3,3 : 9]:', table[3,3 : 9])
print('table[3,3:]:', table[3,3:])
print()

print('2D slices (rows, columns)')
print('table[:2, :-1]:', table[:2, :-1], sep='\n')
print()
print('table[-1, ::2]:', table[-1, ::2], sep='\n')
print()

print('Conditional indexing and assignment')
print('table[table > 20]:', table[table > 20])
print()
table[table > 20] = 0
print('table[table > 20] = 0:')
print(table)
print()

print()

# Copying Data
print('Copying Data:')
print()

table_copy = table[:3, :3]
print('table_copy = table[:3, :3]', table, table_copy, sep='\n' * 2)
print()

print('Copies made by assignment (or assignment of slices!) are references:')
print('changes to the copy are reflected in the original!')
table_copy[:] = 0
print('table_copy[:] = 0', table_copy, table, sep='\n' * 2)
print()

print('Using the copy function of numpy will return a new, standalone array object')
np_table_copy = table.copy()
print('np_table_copy = table.copy()', table, np_table_copy, sep='\n' * 2)
print()
np_table_copy[:] = 0
print('np_table_copy[:] = 0', np_table_copy, table, sep='\n' * 2)

print()

# Iterating Over Arrays
print('Iterating Over Arrays')
print()

iter_table = np.random.randint(0, 10, (4,3))
print(iter_table)
print()

print('Iterate with foreach, either by row or index')

for row in iter_table:
    print(row)

print()

for i in range(len(iter_table)):
    print(iter_table[i])

print()

print('Use enumerate to iterate over row indices and values')

for i, row in enumerate(iter_table):
    print('row', i, ':', row)

print()

iter_table_sq = iter_table ** 2
print('Use zip to iterate over two tables simultaneously')

for i, j in zip(iter_table, iter_table_sq):
    print('{} + {} = {}'.format(i, j, i+j))

