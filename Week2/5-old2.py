import re

f = open('numbers.txt')

landline_base = r'[0-9]{4}[- ]?[0-9]{4}'
mobile_base   = r'[0-9]{3}[- ]?[0-9]{3}'

landline     = re.compile(r'(?:\s|^)(?:(?:\(0[0-35-9]\) )|(?:0[0-35-9][- ]?))?' + landline_base + r'\b')
landline_int = re.compile(r'(?:\s|^)\+61[- ]?[0-35-9][- ]?' + landline_base + r'\b')
mobile       = re.compile(r'(?:\s|^)04[0-9]{2}[- ]?' + mobile_base + r'\b')
mobile_int   = re.compile(r'(?:\s|^)\+61[- ]?4[- ]?[0-9]{3}[- ]?' + mobile_base + r'\b')

numbers = []

for line in f:
    landline_nums     = landline.findall(line)
    landline_int_nums = landline_int.findall(line)
    mobile_nums       = mobile.findall(line)
    mobile_int_nums   = mobile_int.findall(line)

    # for num in landline_nums:
    #     num = num.strip()
    #     if '-' in num:
    #         pass
    numbers += landline_nums
    numbers += landline_int_nums
    numbers += mobile_nums
    numbers += mobile_int_nums

for num in numbers:
    print num.strip()

