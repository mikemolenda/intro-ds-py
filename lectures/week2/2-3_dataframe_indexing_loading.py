#! /usr/local/bin/python3

import pandas as pd

# DataFrame Indexing and Loading

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

# Some DataFrame operations, such as broadcasting and in-place operations, change the data in the original frame
pet_supplies['Location'] = None
print(pet_supplies)
print()

costs = pet_supplies['Cost']
costs += 2
print(pet_supplies)
print()

# To explicitly use a copy, call copy() on the DataFrame first
pet_supplies_discount = pet_supplies.copy()
discount = 0.2
pet_supplies_discount['Cost'] *= (1 - discount)
print(pet_supplies)
print()
print(pet_supplies_discount)
print()

# Importing from data sources
# Pandas library has methods for importing CSV, relational data, JSON, Excel, HTML tables

olympic_medals = pd.read_csv('../../data/olympics.csv')
print(olympic_medals.head())
print()

# Indicate that first column should be indexes, and second row should be column names
olympic_medals = pd.read_csv('../../data/olympics.csv', index_col=0, skiprows=1)
print(olympic_medals.head())
print()

# Change column names to be unique and more meaningful
print(olympic_medals.columns)
print()

for col in olympic_medals.columns:
    if col[:2] == '01':
        olympic_medals.rename(columns={col:'Gold' + col[4:]}, inplace=True)
    if col[:2] == '02':
        olympic_medals.rename(columns={col:'Silver' + col[4:]}, inplace=True)
    if col[:2] == '03':
        olympic_medals.rename(columns={col:'Bronze' + col[4:]}, inplace=True)
    if col[:1] == '№':
        olympic_medals.rename(columns={col:'#' + col[2:]}, inplace=True)

print(olympic_medals.head())
print()