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

# Get key by index number
print(sports_series.iloc[3])

# Get key by value
print(sports_series.loc['Golf'])
print()

# Add / update
print(animals_series)
print()

animals_series.loc['China'] = 'Panda'
print(animals_series)
print()

animals_series.loc['America'] = 'Eagle'
print(animals_series)
print()

# Vectorization: aggregate operations
numbers = pd.Series([100.0, 120.0, 10.0, 3.0])
print(numbers)
print()

print(np.sum(numbers))
print()

# Faster than iteration - uses vectorization
long_series = pd.Series(np.random.randint(0, 1000, 10000))
print(long_series.head(10))
print(len(long_series))
print(np.sum(long_series))
print()

# Broadcasting: apply operation to every member of series
long_series += 111
print(long_series.head(10))
print()

# Appending series
print(sports_series)
print()

cricket_loving_countries = pd.Series(['Australia',
                                      'Barbados',
                                      'Pakistan',
                                      'England'],
                                     index = ['Cricket',
                                              'Cricket',
                                              'Cricket',
                                              'Cricket'])

sports_series = sports_series.append(cricket_loving_countries)
print(sports_series)
print()

# Series may have non-unique keys. Querying for one of these keys returns a series
print(sports_series.loc['Cricket'])
print()


