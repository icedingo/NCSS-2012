x=int(input())
s=[['|']*x for j in' '*x]
for i in range(x):
 s[i][x-1-i]='\\'
 d=-1 if i>x-1-i else 1
 for j in xrange(i,x-1-i,d):s[i][j]='-'
 if 1<=i<x/2+x%2:s[i][i-1]='/'
 elif x/2-1+x%2<i:s[i][i]='/'
print'\n'.join(map(' '.join,s))
