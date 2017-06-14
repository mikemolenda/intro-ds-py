#! /usr/local/bin/python3

# String Formatter
print('String Formatter:')
print()

sales_record = sales_record = {'item': 'banana', 'price': 0.29, 'quantity': 6, 'person': 'Ape Man'}
sales_statement = '{} bought {} {}{} at ${:.2f} each, for a total of ${:.2f}'

print(sales_record)
print(sales_statement)
print()

print(sales_statement.format(sales_record['person'],
                             sales_record['quantity'],
                             sales_record['item'],
                             's' if sales_record['quantity'] > 1 else '',
                             sales_record['price'],
                             sales_record['price'] * sales_record['quantity']))


