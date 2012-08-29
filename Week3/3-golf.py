a,b=map(int,raw_input().split())
r=range
l=len
n=r(3,b+1,2)
c=l(n)
for i in r(c/2):
 if not n[i]:continue
 j=n[i]
 n[i+j::j]=(0,)*((c-i-1)/j)
n=[2]+[x for x in n if x]
e=0
for i in r(l(n)-1):
 if n[i]<a:continue
 d=n[i+1]-n[i]
 if d>e:e,k=d,i
print n[k],n[k+1]