#! /usr/local/bin/python3

import pandas as pd
import numpy as np

# Querying DataFrames

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

# Boolean masking: Method used to efficiently return views from DataFrames.
# Boolean mask overlaid on top of DF, cells aligned with True cells in mask returned, cells aligned with False are not.

print(olympic_medals['Gold'] > 0)
print()

# Mask applied to dataset using where()
olympic_gold = olympic_medals.where(olympic_medals['Gold'] > 0)

print(olympic_gold)
print()

# Drop NaN results
olympic_gold = olympic_gold.dropna()

print(olympic_gold)
print()

# Alternate syntax, automatically filters out NaN rows
olympic_gold = olympic_medals[olympic_medals['Gold'] > 0]

print(olympic_gold)
print()

# Can chain masks,
# e.g. countries who won gold in summer OR winter:
olympic_gold_s_w = olympic_medals[ (olympic_medals['Gold'] > 0) | (olympic_medals['Gold.1'] > 0) ]

print(olympic_gold_s_w)
print()

# e.g. countries who won in winter, but never summer:
olympic_gold_w = olympic_medals[ (olympic_medals['Gold.1'] > 0) & (olympic_medals['Gold'] == 0) ]

print(olympic_gold_w)
print()

# Note that the expressions on either side of the boolean operators are encased in parentheses

# Query all names who purchased products worth more than $3.00
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

expensive_pet_supplies = pet_supplies[pet_supplies['Cost'] > 3.0]

print(expensive_pet_supplies)
print()
