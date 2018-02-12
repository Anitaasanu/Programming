s="geeksf"
s=list(s)
n=len(s)+1
t=[[0 for i in range(n)] for j in range(n)]
for i in range(n):
    for j in range(n):
##        print i,j
        if i==0 or j==0:
            t[i][j]=0
        elif s[j-1]==s[i-1]:
            t[i][j]=1
        else:
            if. 
for i in t:
        print i
