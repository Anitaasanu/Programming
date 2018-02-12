from operator import itemgetter, attrgetter, methodcaller
arr = [[0 for j in xrange(3)] for i in xrange(4)]
arr = [(3, 5, 20), (1, 2, 50), (6, 19, 100), (2, 100, 200)];
n = len(arr)
m = len(arr[0])
finish=[]
start=[]
profit =[]
table=[]
def calprofit(s,f,p):
    for i in xrange(n):
        if(i==0):
            total=p[0]
        else:
            if f[i-1]<=s[i]:
                total+=p[i]
            else:
                s
        table[i]=total
def lastNon(arr,i):
    for j in xrange(i-1,-1,-1):
        if arr[j][1]<=arr[i][0]:
            return j
    return -1
def scheduling(arr,n,m):
    arr = sorted(arr,key=itemgetter(1))
    table = [0 for i in xrange(n)]
##    result=calprofit(start,finish,profit)
            
    ##    result = final(start,finish,profit)
    table[0] = arr[0][2]
    for i in xrange(1,n):
        incl = arr[i][2]
        l = lastNon(arr,i)
        if l!=-1:
            incl += table[l]
        table[i] = max(incl,table[i-1])
    print table
    return table[n-1]

print scheduling(arr,n,m)
    
   
