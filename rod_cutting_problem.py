length=[1,2,3,4,5,6,7,8]
price=[3,5,8,9,10,17,17,20]
n=len(length)+1
m=len(price)+1
table=[0 for i in range(n)]
def rcp(l,p,n,m):
    for i in range(1,n):
         val=-1
         for j in range(i):
            table[i]=max(val,p[j]+table[i-j-1])
            val=table[i]
         print table
            
rcp(length,price,n,m)            
