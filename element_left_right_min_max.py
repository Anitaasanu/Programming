s=[4,2,1,3,5,7]
n=len(s)


def findelement(s,n):
    r_min=float('inf')
    l_max=0
    for i in range(1,n):
        l_max=max(l_max,s[i-1])
    for i in range(n-1,0,-1):
        if s[i]>l_max and r_min>s[i]:
            return i
        r_min=min(r_min,s[i])
    return -1
print findelement(s,n)
    
