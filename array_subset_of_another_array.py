s1=[11, 1, 13, 21, 3, 7]
s2=[11,3,7,1,13,21,22,32]
s1=list(s1)
s2=list(s2)
n1=len(s1)
n2=len(s2)
d={}
def subset(s1,s2,n1,n2):
    f=0
    if n1>n2:
        for i in range(n1):
            d[s1[i]]=i
        for i in range(n2):
            if s2[i] not in d:
                f=1
                return False
        return True
    else:
        for i in range(n2):
            d[s2[i]]=i
        for i in range(n1):
            if s1[i] not in d:
                f=1
                return False
        return True
        
            
print subset(s1,s2,n1,n2)
