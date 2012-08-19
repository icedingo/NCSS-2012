num = int(raw_input('Enter number: '))

luckynumbers = range(1,num+1)

crossout = 2
current = 0

while crossout <= len(luckynumbers):
    start = len(luckynumbers) - len(luckynumbers)%crossout - 1
#    print crossout, len(luckynumbers), start
#    print luckynumbers
    for i in xrange(start,0,-crossout):
        luckynumbers.pop(i)
    current += 1
    crossout = luckynumbers[current]

print luckynumbers[-1]