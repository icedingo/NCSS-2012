import StringIO


class Node(object):
  def __init__(self, left, right):
    self.left = left
    self.right = right

  def __str__(self):
    out = StringIO.StringIO()
    self.pprint(out, '')
    return out.getvalue()

  def pprint(self, out, indent):
    out.write('%s(%s\n' % (indent, self.get_description()))
    for child in self.get_children():
      child.pprint(out, indent + '  ')
    out.write('%s)\n' % indent)

  def get_children(self):
    return (self.left, self.right)

  def get_description(self):
    raise NotImplementedError

  def evaluate(self, variables):
    raise NotImplementedError

#############################################################
#\_________________________________________________________/#
#|                                                         |#
#|               DO NOT COPY ABOVE THIS BOX!               |#
#|_________________________________________________________|#
#/                                                         \#
#############################################################

class AndNode(Node):
  # def __init__(self, left, right):
  #   pass  # your code here
  def get_description(self):
    return 'AND'

  def evaluate(self, variables):
    leftvar  = self.left.evaluate(variables)
    rightvar = self.right.evaluate(variables)
    return leftvar and rightvar


class OrNode(Node):
  # def __init__(self, left, right):
  #   pass  # your code here
  def get_description(self):
    return 'OR'

  def evaluate(self, variables):
    leftvar  = self.left.evaluate(variables)
    rightvar = self.right.evaluate(variables)
    return leftvar or rightvar


class NotNode(Node):
  def __init__(self, child):
    self.child = child

  def get_description(self):
    return 'NOT'

  def evaluate(self, variables):
    return not self.child.evaluate(variables)

  def get_children(self):
    return [self.child]


class VarNode(Node):
  def __init__(self, variable):
    self.variable = variable

  def get_description(self):
    return self.variable

  def evaluate(self, variables):
    return variables[self.variable]

  def pprint(self, out, indent):
    out.write('%s%s\n' % (indent, self.get_description()))

  def get_children(self):
    return []