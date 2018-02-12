s=[1,9,3,10,4,20,2]
s=list(s)
n=len(s)
d={}
for i in range(n):
    d[s[i]]=i
##print d
m =0
for i in range(n):
    if s[i]-1 not in d:
        a=s[i]
        c = 0
        while(a in d):
            print a
            a+=1
            m = max(m,c+1)
            c+=1
print m
