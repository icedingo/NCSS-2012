occurrences = {}
line = raw_input('Enter line: ')
while line != '':
 for word in line.split():
  if word not in occurrences:
   occurrences[word] = 0
  occurrences[word] += 1
 line = raw_input('Enter line: ')

counts = occurrences.items()
counts.sort()
for word, count in counts:
  print word, count