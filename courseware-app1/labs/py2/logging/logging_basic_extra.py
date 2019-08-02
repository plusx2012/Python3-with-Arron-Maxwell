'''_

This is the file your logger will log to:
>>> LOGFILE
'logging-basic-extra.txt'

To make this lab pass, in the code section, you need to do the
following:

1) Invoke logging.basicConfig() with the correct arguments.
   (Hint: set level, format and filename.)
2) Define the log_announcements() function.


Let's first test the log level threshold. 
>>> logging.debug('debug message')
>>> logging.info('info message')
>>> logging.warning('warning message')
>>> logging.error('error message')
>>> logging.critical('critical message')

The log file ought to have records only of WARNING or greater.  We'll use
the print_log() function (defined for you below) to check the log file
contents:

>>> print_log()
[WARNING] warning message
[ERROR] error message
[CRITICAL] critical message


Next, define the log_announcements() function. This one's a bit
tricky. The argument it takes is a template string:

>>> log_announcements("I'm learning %s")

Check that it adds some new records:

>>> print_log()
[WARNING] warning message
[ERROR] error message
[CRITICAL] critical message
[CRITICAL] I'm learning Python
[WARNING] I'm getting good at it!
[CRITICAL] I'm learning logging
[WARNING] I'm going to be great at it!

Hint: log_announcements() will invoke logging functions several
times. Some will use the template string, and some won't.

'''

from __future__ import print_function

LOGFILE = 'logging-basic-extra.txt'

def print_log():
    "Prints out what's written to the log file so far."
    print(open(LOGFILE).read(), end="")

# This "with" line resets the log file to be empty,
# each time you run the test:
with open(LOGFILE, 'w'): pass
    
# Write your code here:



# Do not edit any code below this line!

if __name__ == '__main__':
    import doctest
    count, _ = doctest.testmod()
    if count == 0:
        print('*** ALL TESTS PASS ***\nGive someone a HIGH FIVE!')

# Copyright 2015-2018 Aaron Maxwell. All rights reserved.
