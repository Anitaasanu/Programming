s=[-2,-3,4,-1,-2,-3,5,1]
n = len(s)
max_sum=0
a=0
for i in xrange(n):
    a+=s[i]
    if a>0:
        if max_sum<a:
            max_sum=a
    else :
        a=0
print max_sum
