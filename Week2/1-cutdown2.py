import re
for w in open('words.txt'):
 if re.search(r'(?i)^[tm][aeiou]?([^aeiou][aeiou]?)*y$',w): print w[:-1]