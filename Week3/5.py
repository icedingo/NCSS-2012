import re

atom_regex     = re.compile(r'[a-z]\w*')
variable_regex = re.compile(r'[A-Z]\w*')
token_regex    = re.compile(r'\w+|\(|\)|\.|,|:-|\?-')
oldtokens      = []

def tokenise(line):
    #print token_regex.findall(line)
    return token_regex.findall(line)

def pop(tokens, legal, regex=False):
    #print 'pop!', tokens, legal, regex
    if regex:
        if tokens and legal.match(tokens[0]):
            tokens.pop(0)
            return True
    elif tokens and tokens[0] in legal:
        tokens.pop(0)
        return True
    return False

def valid(tokens):
    #print 'validating', tokens
    return query(tokens) or rule(tokens)

def query(tokens):
    #print 'query:', tokens
    return pop(tokens, '?-') and predicate(tokens) and pop(tokens, '.')

def rule(tokens):
    #print 'rule:', tokens
    return predicate(tokens) and (pop(tokens,'.') or (pop(tokens, ':-') and predicate_list(tokens) and pop(tokens, '.')))

def predicate_list(tokens):
    #print 'predicate_list:', tokens
    return predicate(tokens) and ((pop(tokens, ',') and predicate_list(tokens)) or True)

def predicate(tokens):
    #print 'predicate', tokens
    return atom(tokens) and pop(tokens, '(') and term_list(tokens) and pop(tokens, ')')

def term_list(tokens):
    #print 'term_list', tokens
    #if tokens[1] == ',':
    #    return (term(tokens) and pop(tokens, ',') and term_list(tokens))
    return term(tokens) and ((pop(tokens, ',') and term_list(tokens)) or True)
    #return term(tokens) or (term(tokens) and pop(tokens, ',') and term_list(tokens))

def term(tokens):
    #print 'term', tokens
    return atom(tokens) or variable(tokens)

def atom(tokens):
    #print 'atom', tokens
    return pop(tokens, atom_regex, True)

def variable(tokens):
    #print 'variable', tokens
    return pop(tokens, variable_regex, True)

program = open('program.plg')
i = 0

for line in program:
    i += 1
    line = line.strip()
    #print 'line:', line
    if line and not valid(tokenise(line)):
        print 'Invalid program on line %d!' % i
        break
else:
    print 'Valid program!'