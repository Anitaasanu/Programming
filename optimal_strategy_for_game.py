s=[8,15,3,7]
n=len(s)
t=[[[0 for i in xrange(2)] for j in xrange(n)] for k in range(n)]
##for i in t:
##    print i
def osg(s,n):
    for l in range(n):
        i=0
        j=l
        for i in range(n-l):
            print i,j
            if i==j:
                t[j-1][i-1][0]=s[j-1]
            else:
                if (t[i+1][j][1]+s[i])>(t[i][j-1][1]+s[j]):
                    t[i][j][0] = t[i+1][j][1]+s[i]
                    t[i][j][1] = t[i+1][j][0]
                else:
                    t[i][j][0] = t[i][j-1][1]+s[j]
                    t[i][j][1] = t[i][j-1][0]

            j+=1
        for i in t:
            print i
osg(s,n)
