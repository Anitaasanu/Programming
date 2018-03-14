a=int(input().strip())
if a==0:
    print (0)
while a>0:
    n=int(input())
    t=map(int,input().strip().split())
    t=list(t)
    ma=max(t)
    c=list(t)
    b=[]
    for i in range(n-2,-1,-1):
        if t[i]>t[i+1]:
            continue
        else:
            t[i],t[i+1]=t[i+1],t[i+1]
    
    m=c[0]
    b=[m]
    for i in range(n-1):
        if m<c[i+1]:
            m=c[i+1]
        b.append(m)
    m = []
    if t[0] == b[0]:
        m.append(t[0])
    for i in range(1,n):
        if t[i] > b[i]:
            m.append(t[i])
            
    from collections import OrderedDict
    t = list(OrderedDict.fromkeys(t))
    m = list(OrderedDict.fromkeys(m))
    for i in t:
        print (i,end= " ")
    print ()
    for i in m:
        if c.count(i)>1:
            m.remove(i)
    if m==[]:
        print (-1)
    else:
        for i in m:
            print (i,end= " ")
        print ()
    a-=1
