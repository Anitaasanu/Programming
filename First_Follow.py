##v=u'\u03B5'
with open('input.txt')as f:
    lines = f.read().splitlines()
d={}
for s in lines:
    s=s.split('->')
    d[s[0]]=s[1].split('|')
f1={}
f2={}
def First(a):
    b=[]
    for i in d[a]:
        if i[0].islower():
            b.append(i[0])
        else:
            c=First(i[0])
            while 'v' in c:
                c.pop(c.index('v'))
                b+=c
                i=i[1:]
                c=First(i[0])
            b+=c
    return b
def Follow(a):
    f = []
    for k in d:
        for j in d[k]:
            if a in j:
                ind = j.index(a)
                i = j[ind+1:]
                if len(i)>0:
                    if i[0].isupper():
                        b=f1[i[0]]
                        while 'v' in b:
                            i=i[1:]
                            b.pop(b.index('v'))
                            f+=b
                            if len(i) == 0:
                                f+=f2[k]
                                break
                            if i[0].isupper():
                                b += f1[i[0]]
                            else :
                                b.append(i[0])
                        else:
                            b = b.append(i[0])
                        f+=b
                elif len(i) == 0:
                    f+=f2[k]
    return f
                
for i in d:
    f1[i]=First(i)
    print i,f1[i]

for i in d:
    f2[i]=list(set(Follow(i)))
    f2['S'] = ['$']
print i,f2[i]
