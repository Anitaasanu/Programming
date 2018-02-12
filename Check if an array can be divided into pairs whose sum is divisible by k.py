d ={}
a = [9, 7, 3]
k = 6
n=len(a)
s=[]
for i in range(n):
    if a[i]%k not in d:
        d[a[i]%k] = 1
    else:
        d[a[i]%k]+=1
print d
cnt=True
for i in d:
    if k-i in d:
       if d[i]!=d[k-i]:
           cnt = False
           break
    else:
        cnt = False
        break
print cnt
