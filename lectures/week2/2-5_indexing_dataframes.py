#! /usr/local/bin/python3

import pandas as pd
import numpy as np

# Indexing DataFrames

# Setting custom index
# WARNING: discards the original index! To keep the original, add a new column and then set custom index

olympic_medals = pd.read_csv('../../data/olympics.csv', index_col=0, skiprows=1)

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
print()

# Change index from country to number of medals won at summer games

# Create new column for country and assign it the values in index
olympic_medals['Country'] = olympic_medals.index

# Set index to summer golds
olympic_medals = olympic_medals.set_index('Gold')

print(olympic_medals.head())
print()
print()

# Reset index to default numbered column, and restore current index to standard column
olympic_medals = olympic_medals.reset_index()

print(olympic_medals.head())
print()
print()


# Multi-level indexing

census = pd.read_csv('../../data/census.csv')

print(census.head())
print()
print()

# Reduce data to only rows with sum level of 50
census = census[census['SUMLEV'] == 50]

# Reduce data to limited set of columns
cols_to_keep = ['STNAME',
                'CTYNAME',
                'POPESTIMATE2010',
                'POPESTIMATE2011',
                'POPESTIMATE2012',
                'POPESTIMATE2013',
                'POPESTIMATE2014',
                'POPESTIMATE2015',
                'BIRTHS2010',
                'BIRTHS2011',
                'BIRTHS2012',
                'BIRTHS2013',
                'BIRTHS2014',
                'BIRTHS2015']

census = census[cols_to_keep]

print(census.head())
print()
print()

# Set multi-level index to combo of state and county name
census = census.set_index(['STNAME', 'CTYNAME'])

print(census.head())
print()
print()

# Query multi-level indexes in order, by the level you want to query
print(census.loc['Illinois', 'Cook County'])
print()
print()

# Compare two counties
print(census.loc[[('Illinois', 'Cook County'), ('California', 'Los Angeles County')]])
print()
print()


# Re-index the purchases by store and name

purchase_1 = pd.Series({'Name': 'Chris',
                        'Item Purchased': 'Dog Food',
                        'Cost': 22.50})
purchase_2 = pd.Series({'Name': 'Kevyn',
                        'Item Purchased': 'Kitty Litter',
                        'Cost': 2.50})
purchase_3 = pd.Series({'Name': 'Vinod',
                        'Item Purchased': 'Bird Seed',
                        'Cost': 5.00})

pet_supplies = pd.DataFrame([purchase_1, purchase_2, purchase_3], index=['Store 1', 'Store 1', 'Store 2'])

pet_supplies['Location'] = pet_supplies.index
pet_supplies = pet_supplies.set_index(['Location', 'Name'])

pet_supplies = pet_supplies.append(pd.Series(data={'Cost': 3.0, 'Item Purchased': 'Cat Food'}, name=('Store 2', 'Kevyn')))
print(pet_supplies)
print()
