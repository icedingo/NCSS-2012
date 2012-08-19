import re

f = open('numbers.txt')

homephone = re.compile(r'(?:(?:(?:(?:\W|^)\+61|\b0)[1-35-9])[- ]?|\b)(?:[0-9]){4}[- ]?(?:[0-9]){4}\b')
mobile = re.compile(r'(?:(?:(?:\W|^)\+61|\b0)4)(?:[0-9]){2}[- ]?(?:[0-9]){3}[- ]?(?:[0-9]){3}\b')
#international

numbers = []

for line in f:
    numbers += homephone.findall(line)
    numbers += mobile.findall(line)


for n in numbers:
    n = n.strip()
    if ' ' in n and '-' in n:
        continue
    print n