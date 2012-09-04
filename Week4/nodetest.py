from node import Node

# Tree 1
n0 = Node('n0')
n1 = Node('n1')
n2 = Node('n2')
n3 = Node('n3')
n4 = Node('n4')
n5 = Node('n5')
n6 = Node('n6')
n7 = Node('n7')
n8 = Node('n8')
n9 = Node('n9')
n10 = Node('n10')
n11 = Node('n11')

n0.add_child(n1)
n1.add_child(n2)
n1.add_child(n3)
n2.add_child(n4)
n3.add_child(n5)
n4.add_child(n6)
n6.add_child(n7)
n2.add_child(n8)
n8.add_child(n9)
n9.add_child(n10)
n10.add_child(n11)

print '---Heights'
print 'n0', n0.get_height()
print 'n2', n2.get_height()
print 'n4', n4.get_height()
print 'n11', n11.get_height()
print

print '---Counts'
print 'n0', n0.get_count()
print 'n1', n1.get_count()
print 'n2', n2.get_count()
print 'n7', n7.get_count()
print

print '---pprint'
print 'n0', n0.pprint()
print 'n2', n2.pprint()
print 'n9', n9.pprint()
print 'n5', n5.pprint()
print

print '---descendants'
print 'n0,n11', n0.has_descendant(n11)
print 'n1,n0', n1.has_descendant(n0)
print 'n4,n8', n4.has_descendant(n8)
print 'n6,n7', n6.has_descendant(n7)
print

print '---ancestors'
print 'n0,n2', n0.has_ancestor(n2)
print 'n7,n8', n7.has_ancestor(n8)
print 'n7,n2', n7.has_ancestor(n2)
print 'n5,n0', n5.has_ancestor(n0)
print

print '---labels'
print 'n0', n0.get_label()
print 'n2', n2.get_label()
print 'n8', n8.get_label()
print 'n11', n11.get_label()
print

# Example
k0 = Node('n0')
k1 = Node('n1')
k2 = Node('n2')
k3 = Node('n3')
k4 = Node('n4')

k0.add_child(k1)
print k0.pprint()
k0.add_child(k2)
print k0.pprint()
k1.add_child(k3)
print k0.pprint()
print k1.pprint()

print '---EXAMPLE---'
print k0.get_height()
print k1.get_count()
print k0.pprint()
print k0.has_descendant(k3)
print k2.has_descendant(k3)
print k3.has_ancestor(k4)
print

print '---ERROR!---'
#k2.add_child(None)
#k4.add_child('win')
#k1.add_child(k3)
#k4.add_child(k2)
print 'Not checking errors.'
