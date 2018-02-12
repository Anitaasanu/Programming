s1="sunday"
s1=list(s1)
s2="saturday"
s2=list(s2)
n1=len(s1)+1
n2=len(s2)+1
t=[[0 for i in range(n2)] for j in range(n1)]
##def insert(s1,s2,i,j):
##    s1[i]=s2[j]
for i in range(n1):
        for j in range(n2):
            print i,j
            if i==0:
                t[i][j]=j
            elif j==0:
                t[i][j]=i
            elif s1[i-1]==s2[j-1]:
                t[i][j]=t[i-1][j-1]
            else:
                t[i][j]=min(t[i-1][j-1],t[i-1][j],t[i][j-1])+1
for i in t:
    print i

