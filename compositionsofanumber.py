m=3
arr=[]
def compositions(n,i):
    
    if(n==0):
        print array(arr,i)
    else:
        j=1
        for j in xrange(m):
            arr.append(j)
            compositions(n-j,i+1)
            j+=1
def array(a,size):
    i=0
    for i in xrange(size):
        print a[i]
        print "\n"
print compositions(5,0)
