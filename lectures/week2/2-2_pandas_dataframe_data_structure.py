#! /usr/local/bin/python3

import pandas as pd
import numpy as np

# Create from group of Series / dictionaries (1 Series = 1 row)

purchase_1 = pd.Series({'Name': 'Chris',
                        'Item Purchased': 'Dog Food',
                        'Cost': 22.5})
purchase_2 = pd.Series({'Name': 'Kevyn',
                        'Item Purchased': 'Kitty Litter',
                        'Cost': 2.5})
purchase_3 = pd.Series({'Name': 'Vinod',
                        'Item Purchased': 'Bird Seed',
                        'Cost': 5.0})

pet_supplies = pd.DataFrame([purchase_1, purchase_2, purchase_3], index=['Store 1', 'Store 1', 'Store 2'])

print(pet_supplies)
print()

# Querying

# Unique index: Returns single row as Series
print(pet_supplies.loc['Store 2'])
print()
print(type(pet_supplies.loc['Store 2']))
print()

# Repeated index: Returns multiple rows as DataFrame
print(pet_supplies.loc['Store 1'])
print()
print(type(pet_supplies.loc['Store 1']))
print()

# Query single column, returns 1-col DataFrame
print(pet_supplies['Item Purchased'])
print()

# Query multiple columns with list of column names
# Note first argument ":" indicating that we want the full set of rows
print(pet_supplies.loc[:, ['Name', 'Cost']])
print()

# Can supply a slice to get only certain indices, by name or index (use iloc)
print(pet_supplies.loc['Store 2':, ['Name', 'Cost']])
print()
print(pet_supplies.iloc[1:, [2, 0]])
print()


# Query row / column intersection
print(pet_supplies.loc['Store 1', 'Cost'])
print()

# Query intersection with operation chaining
# This approach creates a copy of the data, instead of a view of the data
# Should generally be avoided
print(pet_supplies.loc['Store 1']['Cost'])
print()

# Transposition: swap row indices and column names
print(pet_supplies.T)
print()

# Select list of column values from transposed table
print(pet_supplies.T.loc['Cost'])
print()

# Drop rows
print(pet_supplies.drop('Store 1'))
print()

# Note that the original DataFrame itself is not affected, returns a copy instead
pet_supplies_store_1 = pet_supplies.drop('Store 2')
print(pet_supplies_store_1)
print()
print(pet_supplies)
print()

# Can update the DataFrame itself with inplace option
pet_supplies_copy = pet_supplies.copy()
pet_supplies_copy.drop('Store 1', inplace=True)
print(pet_supplies_copy)
print()

# Can use the axes option to drop a column instead (default axis=0 for row, axis=1 for column)
print(pet_supplies.drop('Name', axis=1))
print()

# Can also drop a column in place with del keyword
del pet_supplies_copy['Name']
print(pet_supplies_copy)
print()

# Add new columns by broadcast assignment
pet_supplies['Location'] = None
print(pet_supplies)
print()

# Run operation on all values of column with broadcasting
pet_supplies_discount = pet_supplies.copy()
discount = 0.2
pet_supplies_discount['Cost'] *= (1 - discount)
print(pet_supplies_discount)
print()



