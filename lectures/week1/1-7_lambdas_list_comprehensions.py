#! /usr/local/bin/python3

people = ['Dr. Christopher Brooks', 'Dr. Kevyn Collins-Thompson', 'Dr. VG Vinod Vydiswaran', 'Dr. Daniel Romero']

def get_title_and_last_name(full_name_with_title):
    title = full_name_with_title.split()[0]
    last_name = full_name_with_title.split()[-1]
    return title + ' ' + last_name

last_names_with_titles = map(get_title_and_last_name, people)

for name in last_names_with_titles:
    print(name)

print()


# Lambdas are anonymous functions that are simultaneously declared and used
# Passing the predefined function get_title_and_last_name above can be bypassed by declaring it in the args for map()
last_names_with_titles_lambda = map(lambda person : person.split()[0] + ' ' + person.split()[-1], people)

for name in last_names_with_titles_lambda:
    print(name)

print()


# List comprehensions are an abbreviated syntax for creating collections
# Expressions can be used in the definition of a collection to specify its contents

traditional = []

for num in range(1, 10):
    if (num % 2 == 0):
        traditional.append(num)

print(traditional)

list_comp = [num for num in range(1, 10) if num % 2 ==0]
print(list_comp)
print()

# Expressions can be simple, or compound
times_table = [i * j for j in range(1, 10) for i in range(10)]
print(times_table)
print()


# Print all possible user IDs that can be created from two lowecase letters followed by two digits
lowercase = 'abcdefghijklmnopqrstuvwxyz'
digits = '0123456789'

possible_user_ids = [a1 + a2 + d1 + d2 for a1 in lowercase for a2 in lowercase for d1 in digits for d2 in digits]
print(possible_user_ids)
print()
