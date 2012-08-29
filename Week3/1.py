tree = input('Enter tree: ')

def is_strict(tree):
    if len(tree[1]) == 0:
        return True
    elif len(tree[1]) == 3:
        for subtree in tree[1]:
            if not is_strict(subtree):
                break
        else:
            return True
    else:
        return False

if is_strict(tree):
    print 'Strict'
else:
    print 'Non-strict'
