s=[10,20,11,70,50,40,100,5]
s=list(s)
n=len(s)
k=3
l=[]
op=[]
a=s[:3]
a.sort()
print a[0]
for j in xrange(k,n):
    ind = k
    for i in range(k):  
        if s[j]<a[i]:
            ind=i
            break
    a.insert(ind,s[j])
    a.pop(0)
    print a[0]

    
