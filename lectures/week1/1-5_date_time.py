#! /usr/local/bin/python3

import datetime as dt
import time as tm

# Get UNIX Epoch time
print(tm.time())
print()

# Get current time as timestamp (Y, M, D, h, m, s, μs)
timestamp = dt.datetime.fromtimestamp(tm.time())
print(timestamp)
print()

# Get timestamp attributes
print(timestamp.year)
print((timestamp.year, timestamp.month, timestamp.day))

dt_format = '{}/{}/{} {}:{}:{}'
print(dt_format.format(timestamp.day,
                 timestamp.month,
                 timestamp.year,
                 timestamp.hour,
                 timestamp.minute,
                 timestamp.second))

print()

# Timedelta calculations
delta = dt.timedelta(days=183)
today = dt.date.today()
six_months_from_now = today + delta
print(six_months_from_now)
print(today > today - delta)
print()