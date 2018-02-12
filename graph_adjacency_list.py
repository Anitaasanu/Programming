edges = [[1,2],[0,1],[0,2],[2,3],[3,3]]
d={}
for i in edges:
    if i[0] not in d:
        d[i[0]]=[i[1]]
    else:
        d[i[0]].append(i[1])
    if i[1] not in d:
        d[i[1]]=[i[0]]
    else:
        d[i[1]].append(i[0])
for i in d:
    d[i]=list(set(d[i]))       
print d
