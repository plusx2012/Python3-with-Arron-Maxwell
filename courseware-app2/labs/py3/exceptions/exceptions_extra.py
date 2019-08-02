'''

In Python, you can define your own exceptions. To do this, start with
a built-in base class called Exception:

>>> raise Exception("An Error")
Traceback (most recent call last):
...
Exception: An Error

You can subclass this to create your own type:

>>> class MyException(Exception):
...     pass

Then you can raise and catch it, just like any other exception:

>>> raise MyException("My Very Own Error")
Traceback (most recent call last):
...
MyException: My Very Own Error

You can add useful methods, even a custom constructor:

>>> class ErrorCodeException(Exception):
...     def __init__(self, message, code):
...         self.message = message
...         self.code = code
...     def describe(self):
...         return "[{}] {}".format(self.code, self.message)
...
>>> try:
...     raise ErrorCodeException("Alien Invasion Detected", 42)
... except ErrorCodeException as err:
...     print(err.describe())
...
[42] Alien Invasion Detected


It's important to think about how the exception will be represented in
stack traces and logs, so you can quickly understand the error - and
how to fix it. Here's what it looks like by default:

>>> raise ErrorCodeException("Out of coffee", 99)
Traceback (most recent call last):
...
ErrorCodeException: ('Out of coffee', 99)

You can customize this by adding a special method called __str__():

>>> class ErrorCodeException(Exception):
...     def __init__(self, message, code):
...         self.message = message
...         self.code = code
...     def describe(self):
...         return "[{}] {}".format(self.code, self.message)
...     def __str__(self):
...         return self.describe()
...
>>> raise ErrorCodeException("Out of coffee", 99)
Traceback (most recent call last):
...
ErrorCodeException: [99] Out of coffee

See how the last line is different? The more complex and unusual your
exception type's state, the more likely defining __str__() will be
helpful.

Another thing you can do with exceptions: define a hierarchy of
specialized types. Your base class inherits from Exception, and you
can then create other exceptions which subclass from that one:

>>> class CookingException(Exception):
...     'Base error class for robotic chef'
...
>>> class BakingError(CookingException):
...     'Signals a problem when baking'
...
>>> class FryingError(CookingException):
...     'Using a frying pan'
...
>>> class BurntFoodStuckToGrillError(FryingError):
...     'This will be hard to clean'
...
>>> class FoodOnFireError(FryingError):
...     'Not good! Flames!'

This lets you catch a wider net in your except: blocks. You can create
a try/except which will catch the base exception type, which also
catches its derived classes:

>>> try:
...     raise BurntFoodStuckToGrillError('eggs')
... except CookingException:
...     print('Breakfast will be late')
...
Breakfast will be late


And when you have multiple except blocks, each can catch a different,
broad category of exception type:

>>> try:
...     raise FoodOnFireError('steak')
... except BakingError:
...     print('Check the oven please')
... except FryingError:
...     print('Check the grill right away')
...
Check the grill right away


Now it's your turn. Create some exceptions for file-reading errors,
which are sub-types of a common base exception:

>>> read_corrupt_image('secrets.jpg')
Traceback (most recent call last):
...
CorruptImageException: secrets.jpg

>>> read_truncated_file('data.xls')
Traceback (most recent call last):
...
EarlyEndOfFileException: data.xls

>>> try:
...     read_truncated_file('data.xls')
... except FileReadException as file_error:
...     print('Bad file: ' + file_error.path)
...
Bad file: data.xls

>>> try:
...     read_corrupt_image('secrets.jpg')
... except FileReadException as file_error:
...     print('Bad file: ' + file_error.path)
...
Bad file: secrets.jpg


Next, create a different hierachy - this time with some methods.
Write a function called send_money(), which - when needed - can raise
a range of different exceptions, sharing common superclasses.  To work
properly, your send_money() will use the global variables ACCOUNTS and
CURRENCIES (already defined for you, below.)

>>> send_money("Jim", "Bob", 14.5, "USD")
Successfully transferred $14.50 from Jim to Bob
>>> send_money("Bob", "Alice", 21.25, "USD")
Successfully transferred $21.25 from Bob to Alice

>>> send_money("Jim", "Tim", 42.75, "EUR")
Traceback (most recent call last):
...
MissingRecipientError: $42.75: Jim -> Tim

>>> send_money("Jim", "Tim", 14.5, "XYZ")
Traceback (most recent call last):
...
UnknownCurrencyError: UnknownCurrencyError("XYZ")

>>> send_money("Stacy", "Alice", 1000, "CAN")
Traceback (most recent call last):
...
InsufficientFundsError: $1000.00: Stacy -> Alice

>>> try:
...     send_money("Jim", "Tim", 42.75, "EUR")
... except MoneyTransferError as err:
...     print(err.describe_transfer())
...
Jim attempted to send $42.75 to Tim

>>> try:
...     send_money("Stacy", "Alice", 1000, "CAN")
... except MoneyTransferError as err:
...     print(err.describe_transfer())
...
Stacy attempted to send $1000.00 to Alice

>>> try:
...     send_money("Jim", "Tim", 14.5, "XYZ")
... except MoneyTransferError as err:
...     print(err.describe_transfer()) # HINT: skipped!
... except TransactionError as err:
...     print('WARNING: Transaction error: ' + str(err))
...
WARNING: Transaction error: UnknownCurrencyError("XYZ")

'''

# These globals will be used by the send_money() function you write.
ACCOUNTS = {
    # name: amount in account
    'Jim': 20,
    'Stacy': 17,
    'Bob': 11,
    'Alice': 21,
}
# Add your country's currency to this list!
CURRENCIES = {'USD', 'CAN', 'EUR'}

# Write your code here:




# Do not edit any code below this line!

if __name__ == '__main__':
    import doctest
    count, _ = doctest.testmod()
    if count == 0:
        print('*** ALL TESTS PASS ***\nGive someone a HIGH FIVE!')

# Copyright 2015-2018 Aaron Maxwell. All rights reserved.
