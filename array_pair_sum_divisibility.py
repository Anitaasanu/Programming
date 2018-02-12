s=[92,75,65,48,45]
s=list(s)
n=len(s)
m=10
d={}
for i in range(n):
    if s[i]%m not in d:
        d[s[i]%m]=1
    else:
        d[s[i]%m]+=1
a=[]
for i in d:
    print i,d[i]

f=0
if m%2 == 0 and d[m/2]%2!=0:
    f=1
    print "False"
else:
    for i in d:
        if m-i in d:
            if d[i] != d[m-i]:
                f=1
                print "False"
                break
        else:
            f=1
            print "False"
            break
    
if f==0:
    print "True"
for i in a :
    print i
