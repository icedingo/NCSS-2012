import csv,sys
f=['firstname','lastname','email','street','town','state']
z=raw_input().split(',')
for b in csv.DictReader(open('addresses.csv'),f):
 for q in z:
	s=q.split('=')
	if b[s[0]]!=s[1]:break
 else:csv.DictWriter(sys.stdout,f).writerow(b)