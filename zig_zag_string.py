s="PAYPALISHIRING"
s=list(s)
n=len(s)
l=3
t=[]
for i in range(n):
    j=2*l-3
    if i==0:
        t.append(s[i])
    else:
        if(j<=n and j>=0):
            t.append(s[j])
    l-=1
print t
