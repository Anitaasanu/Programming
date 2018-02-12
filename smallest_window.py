s = "this is a test string"
s=list(s)
p="tist"
d={}
n=len(s)
m=len(p)
for i in range(m):
    d[p[i]]=0
##print d
cnt=0
window=float('inf')
prev=-444
for i in range(n):
    if s[i] in d:
        c=s[i]
        if d[s[i]]==0:
            cnt+=1
        prev=d[s[i]]
        d[s[i]]=i
        if cnt==m:
            val=max(d.values())-min(d.values())
            if window<val:
                d[s[i]] = prev
            else:
                window = val
mini = min(d.values())
maxi = max(d.values())
for i in range(mini,maxi+1):
    print s[i],
