edges = [[1,2],[0,1],[2,3],[0,2]]
d={}
for i in edges:
    if i[0] not in d:
        d[i[0]]=[i[1]]
    else:
        d[i[0]]+=[i[1]]
    for i in xrange(4):
        if i not in d:
            d[i] = []
repeat=[]
visited=[False]*4
s = []
def recursive_dfs(i,d):
    global s
    visited[i-1]=True
    s.append(i)
    a=d[i]    
    for b in a:
        if not visited[b-1]:
            recursive_dfs(b,d)
##        elif b in s:
##                print b

recursive_dfs(0,d)
print s
