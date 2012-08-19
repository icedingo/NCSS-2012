size = int(raw_input('Enter size: '))

spiral = [['|' for i in xrange(size)] for i in xrange(size)]

for i in xrange(size):
    spiral[i][size-1-i] = '\\'

    direction = -1 if i > size-1-i else 1
    for j in xrange(i,size-1-i,direction):
        spiral[i][j] = '-'
    if 1 <= i < size/2 + size % 2:
        spiral[i][i-1] = '/'
    elif size/2 - 1 + size % 2 < i:
        spiral[i][i] = '/'



print '\n'.join(map(' '.join,spiral))