s="aabebcdd"
n=len(s)+1
t=[[ 0 for i in range(n)] for j in range(n)]
for i in t:
    print i
for i in xrange(1,n):
    for j in xrange(1,n):
        if s[i-1]==s[j-1] and j!=i:
            t[i][j]=1+t[i-1][j-1]
        else:
            t[i][j]=max(t[i-1][j],t[i][j-1])
for i in t :
    print i
