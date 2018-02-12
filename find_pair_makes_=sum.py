s1=[5, 7, 4, 6]
s2=[1,2,3,8]
s1=list(s1)
s2=list(s2)
n1=len(s1)
n2=len(s2)
d={}
def find_pair(s1,s2):
    sum1= sum(s1)
    sum2= sum(s2)
    if sum2>sum1:
        diff=(sum2-sum1)/2
        for i in range(n2):
            d[s2[i]]=i
        for i in range(n1): 
            if s1[i]+diff in d:
                v1=s1[i]
                v2=s1[i]+diff
    else:
        diff=(sum1-sum2)/2
        for i in range(n1):
            d[s1[i]]=i
        for i in range(n2): 
            if s2[i]+diff in d:
                v1=s2[i]
                v2=s2[i]+diff
        
    return [v1,v2]
    
print find_pair(s1,s2)
