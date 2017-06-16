#! /usr/local/bin/python3

import csv

# Convert CSV data to list of dictionaries
with open('../../data/mpg.csv') as csv_file:
    mpg = list(csv.DictReader(csv_file))

print(mpg[:3])
print(len(mpg))
print(mpg[0].keys())
print(mpg[0]['cty'])
print()

# Average MPG for all cars
avg_cty_mpg = sum(float(entry['cty']) for entry in mpg) / len(mpg)
avg_hwy_mpg = sum(float(entry['hwy']) for entry in mpg) / len(mpg)

print('Average City MPG: {:.2f}'.format(avg_cty_mpg))
print('Average Highway MPG: {:.2f}'.format(avg_hwy_mpg))
print()

# Group average city MPG by number of cylinders
cylinder_types = set(entry['cyl'] for entry in mpg)

avg_cty_mpg_by_cyl = []

for cyl_type in cylinder_types:
    sum_mpg = 0
    cyl_type_count = 0

    for entry in mpg:
        if entry['cyl'] == cyl_type:
            sum_mpg += float(entry['cty'])
            cyl_type_count += 1

    avg_cty_mpg_by_cyl.append((cyl_type, sum_mpg / cyl_type_count))

# Sort by number of cylinders, asc
avg_cty_mpg_by_cyl.sort(key=lambda avg_tuple: avg_tuple[0])

for tuple in avg_cty_mpg_by_cyl:
    print('{} cylinders: {:.2f} mpg'.format(tuple[0], tuple[1]))

print()

# Sort by average MPG, asc
avg_cty_mpg_by_cyl.sort(key=lambda avg_tuple: avg_tuple[1])

for tuple in avg_cty_mpg_by_cyl:
    print('{} cylinders: {:.2f} mpg'.format(tuple[0], tuple[1]))

print()

# Group average city MPG by vehicle class
vehicle_classes = set(entry['class'] for entry in mpg)

avg_cty_mpg_by_class = []

for vehicle_class in vehicle_classes:
    sum_cty_mpg = 0
    vc_count = 0

    for entry in mpg:
        if entry['class'] == vehicle_class:
            sum_cty_mpg += float(entry['cty'])
            vc_count += 1

    avg_cty_mpg_by_class.append((vehicle_class, sum_cty_mpg / vc_count))

# Sort by mpg, desc
avg_cty_mpg_by_class.sort(key=lambda avg_tuple: avg_tuple[1], reverse=True)

for tuple in avg_cty_mpg_by_class:
    print('{}: {:.2f} mpg'.format(tuple[0], tuple[1]))
