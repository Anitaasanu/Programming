mat=[[0,1,1,0,1],[1,1,0,1,0],[0,1,1,1,0],[1,1,1,1,1],[0,0,0,0,0]]
for i in mat:
    print i
n=5
t=[[0 for i in range(n)] for j in range(n)]
def msssm(mat,n):
    for i in range(n):
        for j in range(n):
            if mat[i][j]==1:
                t[i][j]=min(t[i-1][j],t[i][j-1],t[i-1][j-1])+1
    return t
t = msssm(mat,n)
for i in t:
    print i
##t = mat[:]
##for i in range(n):
##        for j in range(n):
##            if i == 0 or j ==0:
##                continue
##            elif mat[i][j]==1 and mat[i-1][j] == 1 and mat[i][j-1]==1:
##                t[i][j] = t[i-1][j-1]+1
##print "Answer"
##for i in t:
##    print i
##for i in mat:
##    print i
##by Deepakoda                
