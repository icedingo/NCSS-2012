import re
import string

atom_regex     = re.compile(r'[a-z]\w*')
variable_regex = re.compile(r'[A-Z]\w*')
token_regex    = re.compile(r'\w+|\(|\)|\.|,|:-|\?-')

class Fact(object):
    def __init__(self,line):
        line = line.strip().split('(')
        self.name = line[0].strip()
        self.data   = [ atom.strip('). ') for atom in line[1].split(',') ]
        self.length = len(self.data)

    def satisfies(self, query, orig_vars={}):

        fact = self
        var_dict = orig_vars.copy()
        for i in xrange(query.length):
            testing_term = query.data[i]
            if variable([testing_term]):
                if testing_term not in var_dict:
                    var_dict[testing_term] = fact.data[i]
                elif var_dict[testing_term] != fact.data[i]:
                    return False
            elif atom([testing_term]):
                if testing_term != fact.data[i]:
                    return False

        return var_dict

class Rule(object):
    def __init__(self,line):
        self.name       = line.split('(')[0].strip()
        self.subqueries = line.split(':-')[1]
        self.data       = line.split(':-')[0]
        self.data       = map(string.strip,self.data[self.data.index('(')+1:self.data.rindex(')')].split(','))
        self.length     = len(self.data)
        self.querylist  = []
        tquery = []
        for part in self.subqueries.split(','):
            tquery.append(part)
            if ')' in part:
                self.querylist.append(Query(','.join(tquery)))
                tquery = []
        
    def solve(self, rules_list, orig_vars={}):

        i = 0
        gens = []
        var_list = [orig_vars.copy()]
        while True:
            if len(gens) <= i:
                gens.append(self.querylist[i].solve(rules_list, var_list[-1]))

            result = gens[i].next()
            if result is not False:

                i += 1
                tvars = result.copy()
                tvars.update(var_list[-1])
                var_list.append(tvars)
                if i == len(self.querylist):

                    yield self.onlyown(var_list[-1])
                    i -= 1
                    var_list.pop()
            else:
                i -= 1
                if i < 0:
                    break
                var_list.pop()
                gens.pop()

        yield False

    def onlyown(self, var_dict):

        own = {}
        for i in self.data:
            two = var_dict[i]
            own[i] = var_dict[i]
        return own

class Query(object):
    def __init__(self,line):
        line        = line.strip().split('(')
        self.name   = line[0].strip('?- ')
        self.data   = [ atom.strip('). ') for atom in line[1].split(',') ]
        self.length = len(self.data)

    def solve(self, rules_list, orig_vars={}):

        for rule in rules_list:
            if rule.name != self.name or rule.length != self.length:
                continue
            var_dict = {} #orig_vars.copy()
            if isinstance(rule, Rule):
                for i in xrange(self.length):

                    cur = self.data[i]
                    if atom([rule.data[i]]):
                        continue
                    if atom([cur]):
                        var_dict[rule.data[i]] = cur

                    elif variable([cur]):

                        if cur in orig_vars:

                            var_dict[rule.data[i]] = orig_vars[cur]

                result = rule.solve(rules_list, var_dict)
                for r in result:
                    if r is not False:
                        r = self.convert(rule, r)

                        yield r
            if isinstance(rule, Fact):
                for k in self.data:
                    if k in orig_vars:
                        var_dict[k] = orig_vars[k]
                result = rule.satisfies(self, var_dict)
                if result is not False:  #ie. it is a dict of vars

                    result = self.convert(rule,result)

                    yield result
        else:
            yield False

    def convert(self, rule, var_dict):
        own_vars = {}
        l = len(self.data)
        for i in xrange(l):
            cur = rule.data[i]
            if variable([cur]):
                if variable([self.data[i]]):
                    own_vars[self.data[i]] = var_dict[cur]
            if atom([cur]):
                if variable([self.data[i]]):
                    own_vars[self.data[i]] = cur
        return own_vars

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

rules_list   = []
queries_list = []

out = []
for line in program:
    tokens = tokenise(line)
    if rule(tokens[:]):
        if ':-' in line:
            rules_list.append(Rule(line))
        else:
            rules_list.append(Fact(line))
    elif query(tokens[:]):
        resgen = Query(line).solve(rules_list)
        for res in resgen:
            if res is not False:

                if not res:
                    out.append('yes')
                else:
                    var_keys = sorted(res.keys())
                    for key in var_keys:
                        out.append(key + ' = ' + res[key])

                break

        else:
            out.append('no')

for line in out:
    print line
