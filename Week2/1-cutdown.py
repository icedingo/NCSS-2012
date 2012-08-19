import re
for w in open('words.txt'):
 if re.match('(?i)[tm]((?![aeiou]{2}).)*y$',w):print w[:-1]