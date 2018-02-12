n=input()
s=raw_input()
s=map(int,s.split())
##print s
n1=len(s)
t=[[0 for j in range(n+1) ]for i in range(n1)]
for i in range(n1):
    for j in range(n+1):
        if j==0:
            t[i][j]=1
        elif j<s[i]:
            t[i][j]=t[i-1][j]
        else:
            t[i][j]=t[i][j-s[i]]+t[i-1][j]
for i in t:
    print i
 
