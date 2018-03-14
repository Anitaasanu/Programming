a=int(input().strip())
if a==0:
    print (0)
while a>0:
    n=int(input())
    t=map(int,input().strip().split())
    t=list(t)
    c = []
    d = {}
    if n==0:
        print (0)
    for i in t:
        d[i]=True
    for i in range(len(t)):
        if t[i]==0:
            continue
        elif -t[i] in d:
            c.append(abs(-t[i]))
    c=list(set(c))
    c.sort()
    for i in c:
        print (-i,i,end=' ')
    
    if len(c)==0:
        print(0)
    else:
        print ()
    
    a-=1

    
