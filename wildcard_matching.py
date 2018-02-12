s1="baaabab"
s2="*****ba*****ab"
s1=list(s1)
s2=list(s2)
n1=len(s1)
n2=len(s2)
t=[[False for j in range(n2+1)] for i in range(n1+1)]
def isMatch(s1,s2,n1,n2):
    if n2==0:
        return n1==0
    t[0][0]=True
    for i in range(1,n2+1):
        if s2[i-1]=='*':
            t[0][i] = t[0][i-1]
    for i in range(1,n1+1):
        for j in range(1,n2+1):
            if s2[j-1]=='*':
                t[i][j]=t[i][j-1] or t[i-1][j]
            elif s2[j-1]=='?' or s1[i-1]==s2[j-1]:
                t[i][j]=t[i-1][j-1]
            elif s2[j-1]!=s1[i-1]:
                t[i][j]=False
##    for i in t:
##        print i
    return t[n1][n2]        
                 
print isMatch(s1,s2,n1,n2)
