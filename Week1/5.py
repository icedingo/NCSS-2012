bilingual = open('bilingual.txt','rU')
english = {}
german = {}

for pair in bilingual:
    psplit = pair.split()
    e = psplit[0]
    g = psplit[1]
    english[e] = g
    german[g] = e

orig = raw_input('Enter English: ')
togerman = []
for word in orig.split():
    if word in english:
        togerman.append(english[word])
    else:
        togerman.append(word)

backtoenglish = []
for word in togerman:
    if word in german:
        backtoenglish.append(german[word])
    else:
        backtoenglish.append(word)

print 'German:', ' '.join(togerman)
print 'English:', ' '.join(backtoenglish)