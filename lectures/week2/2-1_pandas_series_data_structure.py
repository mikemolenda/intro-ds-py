#! /usr/local/bin/python3

import pandas as pd
import numpy as np

# PART 1 CREATE SERIES

# Pandas Series are collections with index, type and name
# Numpy arrays used to store data under the hood
animals = ['Tiger', 'Bear', 'Moose']
numbers = [1, 2, 3]

print(pd.Series(animals))
print()
print(pd.Series(numbers))
print()

# NoneType is handled as object in object Series, NaN in number series
animals = ['Tiger', 'Bear', None]
numbers = [1, 2, None]

print(pd.Series(animals))
print()
print(pd.Series(numbers))
print()

# Convert dictionary to Pandas Series
sports = {'Archery': 'Bhutan',
          'Golf': 'Scotland',
          'Sumo': 'Japan',
          'Taekwondo': 'South Korea'}

sports_series = pd.Series(sports)

print(sports)
print()
print(sports_series)
print()
print(sports_series.index)
print()

# Explicitly assign index values to series
animals_series = pd.Series(['Tiger', 'Bear', 'Moose'], index=['India', 'America', 'Canada'])

print(animals_series)
print()


# PART 2 QUERY SERIES


