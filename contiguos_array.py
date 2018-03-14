a=int(input().strip())
while a>0:
    n=int(input())
    t=map(int,input().strip().split())
    t=list(t)
    #print (t[0])
    t.sort()
    cnt=1
    for i in range(len(t)):
        #print (t[i])
        if t[i]-t[i-1]==1 or t[i]-t[i-1]==0:
            cnt+=1
    if cnt==len(t):
        print ("Yes")
    else:
        print("No")
    a-=1
