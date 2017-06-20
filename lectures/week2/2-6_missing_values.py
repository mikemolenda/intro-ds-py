#! /usr/local/bin/python3

import pandas as pd
import numpy as np

# Handling missing values

player_log = pd.read_csv('../../data/log.csv')

print(player_log)
print()

# Use fillna('ffill') to forward-fill NaN values from previous occupied row - be sure to index/sort first!
player_log.set_index(['time', 'user'], inplace=True)

# One column only
fill_paused = player_log.copy()
fill_paused['paused'].fillna(method='ffill', inplace=True)

print(fill_paused)
print()

# All columns
player_log.fillna(method='ffill', inplace=True)

print(player_log)
print()
