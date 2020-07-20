import re

nameRegex = re.compile(r'''
(0[1-9]|1[0-9]|2[0-9]|3[0-1])\/ # day
(0[1-9]|1[1-2])\/ # month
(1[\d][\d][\d]|2[\d][\d][\d]) # year
''', re.VERBOSE)

match = nameRegex.findall('26/03/2222')


day, month, year = match[0]
