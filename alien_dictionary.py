d=["caa", "aaa", "aab"]
g={}
s=[]
t=1
def make_graph(g,w1,w2):
    for i in range(len(w1)):
        if w1[i]!=w2[i]:
            g[w1[i]]+=[w2[i]]
            break
def topological(e,v):
    global t
    v[e]=True
    for i in g[e]:
        if not v[i]:
            topological(i,v)
    s.append([e,t])
    t+=1
for i in d:
    for j in i:
        if j not in g:
            g[j]=[]
for i in range(len(d)):
    if i+1<len(d):
        make_graph(g,d[i],d[i+1])
v={}
for i in g:
    if i not in v:
        v[i]=False
for i in g:
    if not v[i]:
        topological(i,v)
s.sort(key=lambda x:x[1],reverse=True)
print(s)
