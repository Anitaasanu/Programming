s=[3, 34, 3, 12, 5, 3]
a=9
n=len(s)
d={}
def subset_sum_problem(s,n,a):
    for i in range(n):
        if (a-s[i])>0:
            if s[i] not in d:
                d[s[i]]=a-s[i]
    print d
    
    for i in d:
        
        if d[i] in d:
            return True
        
            
    
print subset_sum_problem(s,n,a)
