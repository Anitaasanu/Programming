s1="amazon"
s2="mazona"
print ((s1[2:]+s1[:2])==s2) or ((s1[-2:]+s1[:-2])==s2)
s1=list(s1)
s2=list(s2)
n1=len(s1)
n2=len(s2)

def rotate(s1,s2):
    t=s1[0]
    if s1==s2:
        print s1
        return True
    else:
        print s1
        for i in range(n1):
            if i+1==n1:
                s1[i]=t
            else:
                s1[i]=s1[i+1]
        return rotate(s1,s2)
            
print rotate(s1,s2)
    
