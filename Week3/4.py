tree = input('Enter tree: ')

def max_length_depth(tree, depth=0, max_depth=0):
    print depth
    max_depth = max(depth,max_depth)
    depth += 1
    print tree[0], '-', tree[1]
    if len(tree[1]) == 0:
        return (len(tree[0]) + 2, depth)
    length = 0
    for subtree in tree[1]:
        length_depth = max_length_depth(subtree, depth, max_depth)
        length += length_depth[0]
        max_depth = max(max_depth, length_depth[1])
        print tree[0], length
    return (max(length,len(tree[0])+2), max_depth)

max_length, max_depth = max_length_depth(tree)

levels = ['']*max_depth

def populate_levels(tree, levels, max_depth, level=0):
    max_length = max_length_depth(tree)[0]
    print 'LEVEL', level
    levels[level] += '[' + tree[0].ljust(max_length, '_') + ']'
    if level >= max_depth:
        return
    populate_levels(tree[1], levels, level+1)

populate_levels(tree, levels, max_depth)
print levels