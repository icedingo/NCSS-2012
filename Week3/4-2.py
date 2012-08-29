tree = input('Enter tree: ')

def max_depth(tree, level=0):
    maxdepth = level
    if len(tree[1]) == 0:
        return level
    for subtree in tree[1]:
        maxdepth = max(maxdepth, max_depth(subtree, level + 1))
    return maxdepth

#print max_depth(tree)

def max_length(tree):
    if len(tree[1]) == 0:
        return len(tree[0]) + 2
    length = 0
    for subtree in tree[1]:
        length += max_length(subtree)
    return max(length, len(tree[0]) + 2)

#print max_length(tree)

def ready_to_print(tree, m_depth, depth=0, levels=[]):
    length = max_length(tree)
    levels[depth] += '[' + tree[0].ljust(length-2, '_') + ']'
    for subtree in tree[1]:
        ready_to_print(subtree, m_depth, depth+1, levels)
    if depth < m_depth - 1:
        for d in xrange(depth+1,m_depth):
            levels[d] = levels[d].ljust(len(levels[depth]),'.')
    return levels

m_depth = max_depth(tree) + 1
levels = ['']*(m_depth)
#print levels

for line in ready_to_print(tree, m_depth, levels=levels):
    print line

#("supercalifragilisticexpialidocious",(("a",(("b",(("candy",(("childrenlikeplaying",()),)),)),("onomatopoeia",()),)),("d",(("egg",(("f",()),)),)),))
