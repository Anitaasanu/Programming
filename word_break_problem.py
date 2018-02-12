d=[ "mobile","samsung","sam","man","mango","icecream","and","go","i","like","ice","cream"]
s="ilikesamsung"
a=[]
b=[]
n1=len(s)
n2=len(d)
def wbp(s,d,l,n1):
    i=0
    while(i<n1):
        print i
        for j in range(l,n2):
            if s[i:j+1]in d:
                a.append(s[i:j+1])
                break
        i=j+1
    print a
##                return wbp(s,d,j+1,n1)
##            
##            return (s,d,i,n1)
    
l=0                
wbp(s,d,l,n1)
         
