#! /usr/local/bin/python3

import pandas as pd
import numpy as np

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

