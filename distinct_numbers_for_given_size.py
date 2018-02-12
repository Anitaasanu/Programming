s=[1,2,1,3,4,2,3]
k=4
n=len(s)
d={}
cnt=0
for i in range(n-k):
    for j in range(k):
        if s[i] not in d:
            d[s[i]]=1
        else:
            d[s[i]]+=1
    print cnt
    del d[s[n-i]]
    
    
