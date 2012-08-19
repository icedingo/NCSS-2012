import re

f = open('numbers.txt')

landline = r'(?:(?:(?:\+61[- ]?\d[- ]?)|(?:0\d[- ]?)|(?:\(0\d\)[- ]))?(?:\d{4}[- ]?\d{4}))'
mobile   = r'(?:(?:\+61[- ]?\d|\(?0\d\)?)[- ]?(?:\d[- ]?){7}\d)'

find_ALL_the_numbers = re.compile(r'(?<!\d)(?:' + landline + r'|' + mobile + r')(?!\d)')

numbers = []
for line in f:
    numbers += find_ALL_the_numbers.findall(line)

for num in numbers:
    print num