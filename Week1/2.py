input_file  = open('input.txt','rU')
line_number = 0
count_dict  = { 'a':3,
                'r':2,
                'd':1,
                'v':1,
                'k':1 }

for line in input_file:
    line_number += 1
    for letter in count_dict:
        if line.lower().count(letter) < count_dict[letter]:
            break
    else:
        print 'Aardvark on line', line_number