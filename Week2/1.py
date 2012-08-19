import re

f = open('words.txt')

#regexone = re.compile(r'^[tm].*?y$',re.I)
regexone = re.compile(r'^[tm][aeiou]?([^aeiou][aeiou]?)*y$',re.I)
#regextwo = re.compile(r'[aeiou]{2}',re.I)


for word in f:
    w = word.strip()
    if regexone.search(w) is not None:# and regextwo.search(w) is None:
        print w