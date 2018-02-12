s="taabbaeat"
n =len(s)
t=[[0 for i in range(n)] for j in range(n)]

##for i in t:
##    print i
def lps(s,n):
    m_len=1
    i=0
    while i <n:
        t[i][i]=True
        i+=1
    start=0
    i =0
    while i <n-1:
        if s[i]==s[i+1]:
            t[i][i+1]=True
            start=i
            m_len=2
        i+=1
    j=3
    while j<=n:
        i=0
        k=i+j-1
        while i<(n-j+1):
            print i,k
            if t[i+1][k-1] and s[i]==s[k]:
                t[i][k]=True
                if k>m_len:
                    start=i
                    m_len=k-i+1
            k+=1
            i+=1
        j+=1
    for i in t:
        print i
    return m_len
print lps(s,n)
                
            
