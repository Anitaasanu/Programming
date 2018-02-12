def rearrange(s, n):
    i = -1
    for j in xrange(n):
        if (s[j] < 0):
            i += 1
            s[i], s[j] = s[j], s[i]
    pos=i+1
    neg=0
    while (pos < n and neg < pos and s[neg] < 0):
        s[neg], s[pos] = s[pos], s[neg]
        pos += 1
        neg += 2  
s = [-1, 2, -3, 4, 5, 6, -7, 8, 9]
n = len(s)
rearrange(s, n)
print s
