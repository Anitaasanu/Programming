s="geeksforgeeks"
s=list(s)
n=len(s)
mat = [[0 for a in xrange(n)]for j in xrange(n)]
def lps(s,n):
    for a in xrange(n):
        j=a
        i=0
        while(j<n and i<n-1):
            print i,j
            if(i==j):
                mat[i][j]=1
            elif(s[i]==s[j]):
                mat[i][j]=mat[i+1][j-1]+2
            else:
                mat[i][j]=max(mat[i][j-1],mat[i+1][j])
            j+=1
            i+=1
lps(s,n)
for j in mat:
    print j
