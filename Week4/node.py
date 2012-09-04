class Node(object):
  def __init__(self, label):
    """Initialise a node with a given label"""
    self.label    = label
    self.children = []
    self.parent   = None
    self.root     = self

  def __str__(self):
    return self.pprint()

  def add_child(self, child):
    """
    Add a child node to the current node.
    * raises ValueError if child is None
    * raises TypeError if child is not a Node object
    * raises ValueError if child is already a child of the current node
    * raises ValueError if child already has its parent set
    """
    if child is None:
      raise ValueError("Child is None")
    if not isinstance(child, Node):
      raise TypeError("Child is not a Node object")
    if child in self.children:
      raise ValueError("Child already child of current node")
    if child.get_parent() is not None:
      raise ValueError("Child already has parent")
    child.parent = self
    self.children.append(child)

  def get_count(self):
    """Returns how many nodes are in the tree"""
    return sum(child.get_count() for child in self.children) + 1

  def get_height(self):
    """Returns the height of the tree"""
    if not self.children:
      return 1
    return max(child.get_height() for child in self.children) + 1

  def get_label(self):
    """Returns the label of the current node"""
    return self.label

  def get_parent(self):
    """Returns the parent of the current node. Returns None if node does not have a parent"""
    return self.parent

  def has_ancestor(self, node):
    """Returns whether or not the current node has 'node' as an ancestor"""
    if self.parent is not None:
      return True if self.parent == node else self.parent.has_ancestor(node)
    return False

  def has_descendant(self, node):
    """Returns whether or not the current node has 'node' as a descendant"""
    if node in self.children:
      return True
    for child in self.children:
      if child.has_descendant(node):
        return True
    else:
      return False

  def pprint(self):
    """Returns a string containing the nested 2-tuple representation of the tree"""
    return '("%s", (%s))' % (self.label, ', '.join(child.pprint() for child in self.children))
