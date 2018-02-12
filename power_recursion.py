def power(n,m):
    if(m==1):
        return n
    else:
        return n*power(n,m-1)
print power(5,3)
