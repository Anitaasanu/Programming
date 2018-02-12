s="adcffaet"
s=list(s)
n=len(s)
p="onkl"
p=list(p)
m=len(p)
d={}
for i in range(m):
    if p[i] not in d:
        d[p[i]]=i
for i in d:
    print i,d[i]
f=0
for i in range(n):
    if s[i] in d:
        result=s[i]
        f=1
        break
if f==0:
    print "characters are not present"
else:
    print "Final min index character is :",result
