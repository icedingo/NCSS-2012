import re

class word:
    def __init__(self, word_string):
        self.word_string = word_string.strip()
        temp_split       = self.word_string.split('|')
        self.word        = temp_split[0]
        self.POS         = temp_split[1]
        self.label       = temp_split[2]
        label_split      = self.label.split('-')
        self.label_type  = label_split[0]
        if len(label_split) > 1:
            self.category = label_split[1]
        else:
            self.category = None        

    def __str__(self):
        return self.word_string

    def __repr__(self):
        return self.word + ': ' + self.POS + ', ' + self.label

inputtxt = open('input.txt')
ne_regex = re.compile('[^| ]+\|[^| ]+\|(?:[IB]-[^| ]+|O)')

named_entities = []

for line in inputtxt:
    worded = [ word(x) for x in ne_regex.findall(line) ]
    #print map(repr,worded)
    temp_ent = []
    for w in worded:
        if w.label_type == 'O':
            if temp_ent:
                named_entities.append(' '.join(map(str,temp_ent)))
                temp_ent = []
            continue
        elif w.label_type == 'B':
            if temp_ent:
                named_entities.append(' '.join(map(str,temp_ent)))
                temp_ent = []
            temp_ent.append(w)
        elif w.label_type == 'I':
            if temp_ent:
                prev_word = temp_ent[-1]
                if w.category != prev_word.category:
                    named_entities.append(' '.join(map(str,temp_ent)))
                    temp_ent = []
            temp_ent.append(w)
    if temp_ent:
        named_entities.append(' '.join(map(str,temp_ent)))

for ne in named_entities:
    print ne