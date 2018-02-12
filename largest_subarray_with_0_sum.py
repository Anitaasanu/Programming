s=[15,-2,2,-8,1,7,10,23]
s=list(s)
n=len(s)

def largest_sbarr(s,n):
    d={}
    sum_s=0
    max_len=0
    for i in range(n):
        sum_s+=s[i]
        if s[i]==0 and max_len==0:
            max_len=1
        if sum_s==0:
            max_len=i+1
        if sum_s in d:
            max_len=max(max_len,i-d[sum_s])
        else:
            d[sum_s]=i
    for i in d:
        print i,d[i]
    return max_len
print largest_sbarr(s,n)
