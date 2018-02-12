s=[10,22,9,33,21,50,41,60,80]
s=list(s)
n=len(s)
c=[1]*n
def lis(s,n):
    for i in xrange(n):
        for j in xrange(i):
            if(s[i]>s[j]):
                c[i]=max(c[i],c[j]+1)
    print c
lis(s,n)
