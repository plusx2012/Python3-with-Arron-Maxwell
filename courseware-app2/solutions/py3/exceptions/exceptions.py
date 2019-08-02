'''

>>> colors = ['Brick Red', 'Fern Green',
...    'Deep Sky Blue', 'Cadmium Orange']

Implement get_index_or_default() by catching an exception.

>>> get_index_or_default(colors, 0, 'Burgundy')
'Brick Red'
>>> get_index_or_default(colors, 10, 'Burgundy')
'Burgundy'
>>> get_index_or_default(colors, -1, 'Bright Pink')
'Cadmium Orange'
>>> get_index_or_default(colors, 5, 'Bright Pink')
'Bright Pink'


Now implement a function to parse a string into first and last name:

>>> parsed = parse_name('John Smith')
>>> type(parsed)
<class 'dict'>
>>> parsed['first']
'John'
>>> parsed['last']
'Smith'

>>> parsed = parse_name('Melissa Jones')
>>> parsed['first']
'Melissa'
>>> parsed['last']
'Jones'

>>> parse_name('John Wayne Smith')
Traceback (most recent call last):
...
ValueError: Cannot split name: John Wayne Smith

>>> parse_name('Bob')
Traceback (most recent call last):
...
ValueError: Cannot split name: Bob


And another function to parse a USA-style phone number.

>>> parts = parse_phone_number('415-555-1212')
>>> type(parts)
<class 'dict'>
>>> parts['area']
'415'
>>> parts['exchange']
'555'
>>> parts['last4']
'1212'


>>> parts = parse_phone_number('303-777-1234')
>>> parts['area']
'303'
>>> parts['exchange']
'777'
>>> parts['last4']
'1234'

>>> parse_phone_number('415-555-12345')
Traceback (most recent call last):
...
ValueError: Invalid format: 415-555-12345

>>> parse_phone_number('41-555-1234')
Traceback (most recent call last):
...
ValueError: Invalid format: 41-555-1234

>>> parse_phone_number('415-55-1234')
Traceback (most recent call last):
...
ValueError: Invalid format: 415-55-1234

>>> parse_phone_number('415-555')
Traceback (most recent call last):
...
ValueError: Invalid format: 415-555

'''

# Write your code here:


def get_index_or_default(mapping, key, default):
    try:
        return mapping[key]
    except IndexError:
        return default

def parse_name(full_name):
    parts = full_name.split()
    if len(parts) != 2:
        raise ValueError('Cannot split name: ' + full_name)
    return {
        'first': parts[0],
        'last': parts[1],
        }

def parse_phone_number(full_number):
    fields = full_number.split('-')
    if len(fields) == 3:
        area, exchange, last4 = fields
        if len(area) == 3 and len(exchange) == 3 and len(last4) == 4:
            return {
                'area': area,
                'exchange': exchange,
                'last4': last4,
                }
    raise ValueError('Invalid format: ' + full_number)


# Do not edit any code below this line!

if __name__ == '__main__':
    import doctest
    count, _ = doctest.testmod()
    if count == 0:
        print('*** ALL TESTS PASS ***\nGive someone a HIGH FIVE!')

# Copyright 2015-2018 Aaron Maxwell. All rights reserved.
