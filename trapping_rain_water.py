s=[3,0,0,2,0,4]
n=len(s)
t_l=[0]*n
t_r=[0]*n
for i in range(n):
    t_l[i]=max(t_l[i-1],s[i])
t_r[n-1]=s[n-1]
for i in range(n-2,-1,-1):
    t_r[i]=max(t_r[i+1],s[i])
print t_l,t_r
t=0
for i in range(n):
    t+=min(t_l[i],t_r[i])-s[i]
print t
