#! /usr/local/python3

# Instantiate objects from classes

class Person:
    department = 'School of Information'

    def __init__(self, name, location):
        self.set_name(name)
        self.set_location(location)

    def set_name(self, name):
        self.name = name

    def set_location(self, location):
        self.location = location

sample_person = Person('Mike', 'Chicago')
print(sample_person.location)
print()

# map(), Functional Programming

prices_store_1 = [10.0, 11.0, 12.34, 2.34]
prices_store_2 = [9.0, 11.1, 12.34]

# map() applies a function to each item of one or two iterables

# Two iterables may be used for comparison, for example
# Stops after the shortest iterable has been exhausted
lowest_prices = map(min, prices_store_1, prices_store_2)

# returns a map object, which must be iterated over to retrieve values
print(lowest_prices)
print()

for price in lowest_prices:
    print(price, end=' ')

print('\n')

# One iterable used to apply transformation to collection
def half(price):
    return price / 2

half_off_store_1 = map(half, prices_store_1)

for price in half_off_store_1:
    print(price, end=' ')

print('\n')

# Transformations do not need to be numerical
people = ['Dr. Christopher Brooks', 'Dr. Kevyn Collins-Thompson', 'Dr. VG Vinod Vydiswaran', 'Dr. Daniel Romero']

for person in people:
    print(person)

print()

def get_title_and_last_name(full_name_with_title):
    title = full_name_with_title.split()[0]
    last_name = full_name_with_title.split()[-1]
    return title + ' ' + last_name

last_names_with_titles = map(get_title_and_last_name, people)

for name in last_names_with_titles:
    print(name)

print()
