s = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
n=len(s)
def min_jump(s,l,n):
    count=0
    if l==n:
        return 0
    jumps=[float('inf')]*n
    jumps[0]=0
    for i in xrange(n):
        for j in xrange(i+1,i+s[i]+1):
            if j >= n:
                break
            jumps[j]=min(jumps[j],jumps[i]+1)
    for i in jumps:
        print i
l=0
print min_jump(s,l,n)
