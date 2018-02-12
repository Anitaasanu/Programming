a={10,22,9,33,21,50,41,60,80}
a=list(a)
n=len(a)
cnt =[1]*n

for i in xrange(1,n):
    for j in xrange(0,i):
        if a[i]>a[j] and cnt[i]<cnt[j]+1:
           cnt[i]=cnt[j]+1
    print cnt
