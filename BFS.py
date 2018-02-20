edges=[[1,2,24],[1,4,20],[1,3,3],[3,4,12]]
d={}
for i in range(len(edges)):
    if edges[i][0] not in d:
        d[edges[i][0]]=[edges[i][1]]
    else:
        d[edges[i][0]]+=[edges[i][1]]
    if edges[i][1] not in d:
        d[edges[i][1]]=[edges[i][0]]
    else:
        d[edges[i][1]]+=[edges[i][0]]
    for i in range(1,5):
        if i not in d:
            d[i]=[]
print d
visited=[False]*4
def lot(d,a):
    s=[]
    q=a
    visited[q-1]=True
    s.append(q)
    while True:
        q=s.pop(0)
        print q
        for i in d[q]:
            if not visited[i-1]:
                s.append(i)
                visited[i-1]=True
        if len(s)==0:
            break
        
    
lot(d,1)
