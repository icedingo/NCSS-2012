f = open('input.txt','rU')
n = 0
d = {'a':3,
'r':2,
'd':1,
'v':1,
'k':1}
for line in f:
 n += 1
 for letter in d:
  if line.lower().count(letter) < d[letter]:
   break
 else:
  print 'Aardvark on line', n