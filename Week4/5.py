import re

atom_regex     = re.compile(r'[a-z]\w*')
variable_regex = re.compile(r'[A-Z]\w*')
token_regex    = re.compile(r'\w+|\(|\)|\.|,|:-|\?-')

class Rule:
    def __init__(self,line):
        line = line.strip().split('(')
        self.name = line[0].strip()
        self.data = [ atom.strip('). ') for atom in line[1].split(',') ]
        self.length = len(self.data)

class Query:
    def __init__(self,line):
        line = line.strip().split('(')
        self.name = line[0].strip('?- ')
        self.data = [ atom.strip('). ') for atom in line[1].split(',') ]
        self.length = len(self.data)

    def check_against(self, rule):
        if self.name != rule.name:
            return False
        if self.length != rule.length:
            return False
        var_dict = {}
        for i in xrange(self.length):
            current = self.data[i]
            if variable([current]):
                if current not in var_dict:
                    var_dict[current] = rule.data[i]
                elif var_dict[current] != rule.data[i]:
                    return False
            elif atom([current]):
                if current != rule.data[i]:
                    return False
        if not var_dict:
            output = 'yes'
        else:
            output = []
            var_keys = sorted(var_dict.keys())
            for key in var_keys:
                output.append(key + ' = ' + var_dict[key])
            output = '\n'.join(output)
        return (True, output)

def tokenise(line):
    return token_regex.findall(line)

def pop(tokens, legal, regex=False):
    if regex:
        if tokens and legal.match(tokens[0]):
            tokens.pop(0)
            return True
    elif tokens and tokens[0] in legal:
        tokens.pop(0)
        return True
    return False

def valid(tokens):
    return query(tokens) or rule(tokens)

def query(tokens):
    return pop(tokens, '?-') and predicate(tokens) and pop(tokens, '.')

def rule(tokens):
    return predicate(tokens) and (pop(tokens,'.') or (pop(tokens, ':-') and predicate_list(tokens) and pop(tokens, '.')))

def predicate_list(tokens):
    return predicate(tokens) and ((pop(tokens, ',') and predicate_list(tokens)) or True)

def predicate(tokens):
    return atom(tokens) and pop(tokens, '(') and term_list(tokens) and pop(tokens, ')')

def term_list(tokens):
    return term(tokens) and ((pop(tokens, ',') and term_list(tokens)) or True)

def term(tokens):
    return atom(tokens) or variable(tokens)

def atom(tokens):
    return pop(tokens, atom_regex, True)

def variable(tokens):
    return pop(tokens, variable_regex, True)

program = open('program.plg')

rules_list = []

for line in program:
    tokens = tokenise(line)
    if rule(tokens[:]):
        rules_list.append(Rule(line))
    elif query(tokens[:]):
        q = Query(line)
        for r in rules_list:
            result = q.check_against(r)
            if result:
                break
        else:
            print 'no'
            continue
        print result[1]