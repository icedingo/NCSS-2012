import re

textsub = re.compile(r'[^a-zA-Z]')

encodekey = raw_input('Enter key: ')
cleartext = raw_input('Enter text: ')
cleartext = textsub.sub('',cleartext)

if cleartext != '':
    order = [ x[0] for x in sorted(list(enumerate(encodekey)),key=lambda x:x[1]) ]

    keylength = len(encodekey)
    encodetable = [ cleartext[i:i+keylength] for i in xrange(0,len(cleartext),keylength) ]

    currentalpha = (-len(encodetable[-1]))%26
    for i in xrange(len(encodetable[-1]), keylength):
        encodetable[-1] += chr(ord('a') + (currentalpha+i)%26)

    ciphertext = ''
    for i in order:
        for line in encodetable:
            ciphertext += line[i]
else:
    ciphertext = ''
    
print ciphertext