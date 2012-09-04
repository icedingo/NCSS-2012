import csv
import sys

learning = csv.DictReader(open('data.csv','rU'))
unknown  = csv.DictReader(open('unknown.csv','rU'))
output   = csv.DictWriter(sys.stdout, fieldnames=learning.fieldnames)
check    = set(learning.fieldnames).intersection(set(unknown.fieldnames))
predict  = list(set(learning.fieldnames).difference(set(unknown.fieldnames)))[0]
learning = list(learning)
unknown  = list(unknown)


# print 'learning'
# for l in learning:
#     print l
# print

# print 'unknown'
# for u in unknown:
#     print u
# print

# print 'check, predict'
# print check, predict
# print

# print 'derpstart'
for test in unknown:
    # print 'derp'
    # print 'test!', test
    max_diff = len(check) + 1
    for line in learning:
        diff = 0
        for field in check:
            if line[field] != test[field]:
                diff += 1
        if diff < max_diff:
            max_diff = diff
            closest = line
    closest.update(test)
    output.writerow(closest)

# print 'derpfinal'