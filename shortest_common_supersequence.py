s1="AGGTAB"
s1=list(s1)
s2="GXTXAYB"
s2=list(s2)
n1=len(s1)
n2=len(s2)
c=[[0 for i in xrange(n1+1)]for j in xrange(n2+1)]
for i in range(n2+1):
    for j in range(n1+1):
     if(i==0 or j==0):
         c[i][j]= 0
     elif(s1[j-1]==s2[i-1]):
         c[i][j] = c[i-1][j-1]+1
     else:
         c[i][j] = max(c[i-1][j],c[i][j-1])
     l=c[n2][n1]
print(n1+n2-l)
