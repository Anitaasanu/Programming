n = 4
m = 4
mat= [[1, 2, 3, 4 ],[ 2, 2, 3, 4 ],[ 3, 2, 3, 4 ],[ 4, 5, 6, 7 ] ]
for i in mat:
    print i
table=[[1 for i in xrange(m)] for j in xrange(n)]
##print tab
##print mat 
def lis(mat,n,m):
    for i in xrange(n):
        for j in xrange(m):
            if i==0 and mat[i][j]-mat[i][j-1]==1:
                table[i][j]=1+table[i][j-1]
            else:
                if j==0 and mat[i][j]-mat[i-1][j]==1:
                    table[i][j]=1+table[i-1][j]
                else:
                    if mat[i][j]-mat[i-1][j]==1 and mat[i][j]-mat[i][j-1]==1:
                        table[i][j]=1+max(table[i-1][j],table[i][j-1])
                    else:
                        if mat[i][j]-mat[i-1][j]==1:
                            table[i][j]=1+table[i-1][j]
                        if mat[i][j]-mat[i][j-1]==1:
                            table[i][j]=1+table[i][j-1]
                            
            
lis(mat,n,m)
for i in table:
    print i
