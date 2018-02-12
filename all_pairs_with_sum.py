s1=[1, 2, 4, 5, 7]
s2=[5, 6, 3, 4, 8]
s1=list(s1)
s2=list(s2)
n1=len(s1)
n2=len(s2)
m=9
d={}
for i in range(n1):
    d[s1[i]]=i
##print d
for i in range(n2):
    if abs(m-s2[i]) in d:
        print m-s2[i],s2[i]

