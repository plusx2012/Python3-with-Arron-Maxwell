'''

In this lab, you'll work with some types in the collections
module. Specifically, the namedtuple, defaultdict, and OrderedDict
types.

Reference:

https://docs.python.org/3/library/collections

First, create a Car named tuple.

>>> johns_car = Car('Kia', 'Rio', 2014)
>>> jessicas_car = Car('Mazda', 'CX-5', 2016)

>>> type(jessicas_car)
<class '__main__.Car'>

>>> johns_car[0]
'Kia'
>>> johns_car[2]
2014
>>> johns_car.model
'Rio'

>>> jessicas_car.make
'Mazda'
>>> jessicas_car.model
'CX-5'
>>> jessicas_car.year
2016
>>> jessicas_car.year == jessicas_car[2]
True


Now, work with defaultdict. Write the functions below to create and
return the appropriate kind of defaultdict.

>>> quantities = dict_default_float()
>>> type(quantities)
<class 'collections.defaultdict'>
>>> quantities['wood']
0.0
>>> quantities['coal'] += 120
>>> quantities['steel'] = 10
>>> sorted(quantities.items())
[('coal', 120.0), ('steel', 10), ('wood', 0.0)]


>>> percentages = dict_default_100()
>>> type(percentages)
<class 'collections.defaultdict'>
>>> percentages['total']
100
>>> sorted(percentages.keys())
['total']
>>> percentages['rent'] = 22
>>> percentages['rent']
22
>>> sorted(percentages.items())
[('rent', 22), ('total', 100)]


Let's combine named tuples and default dictionaries.

>>> points = dict_default_london()
>>> type(points)
<class 'collections.defaultdict'>
>>> points['Berlin'] = Location(52.520008, 13.404954)
>>> points['Berlin'][0]
52.520008
>>> points['Berlin'][1]
13.404954
>>> london = points['London']
>>> london.latitude
51.50853
>>> london.longitude
-0.076132
>>> sorted(points.items())
[('Berlin', Location(latitude=52.520008, longitude=13.404954)), ('London', Location(latitude=51.50853, longitude=-0.076132))]


Finally, work with OrderedDict. Write the functions below to create
and operate on ordered dictionaries.

>>> applicants = build_queue('John', 'manager', 'Cindy', 'doctor', 'Tim', 'programmer')
>>> for name, job in applicants.items():
...     print('{} is applying for {}'.format(name, job))
...
John is applying for manager
Cindy is applying for doctor
Tim is applying for programmer

>>> applicants['Jane'] = 'manager'
>>> applicants
OrderedDict([('John', 'manager'), ('Cindy', 'doctor'), ('Tim', 'programmer'), ('Jane', 'manager')])

>>> fetch_first(applicants)
('John', 'manager')
>>> applicants
OrderedDict([('Cindy', 'doctor'), ('Tim', 'programmer'), ('Jane', 'manager')])

>>> fetch_last(applicants)
('Jane', 'manager')
>>> applicants
OrderedDict([('Cindy', 'doctor'), ('Tim', 'programmer')])

'''

# Write your code here:



# Do not edit any code below this line!

if __name__ == '__main__':
    import doctest
    count, _ = doctest.testmod()
    if count == 0:
        print('*** ALL TESTS PASS ***\nGive someone a HIGH FIVE!')

# Copyright 2015-2018 Aaron Maxwell. All rights reserved.
