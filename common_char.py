s1="geeksforgeeks"
s2="geeksquiz"
t=[]
d={}
for i in s1:
    if i not in s2:
        t.append(i)
for i in s2:
    if i not in s1:
        t.append(i)
for j in range(len(t)):
    if t[j] not in d:
        d[t[j]]=i
for i in d:
    print i
