s=[2, 5, 2, 6, -1, 9999999, 5, 8, 8, 8]
d={}
for i in range(len(s)):
    if s[i] not in d:
        d[s[i]]=1
    else:
        d[s[i]]+=1
s1=[]
for i in d:
    s1.append([i,d[i]])
s1.sort(key=lambda x:x[1],reverse=True)
print s1
