s=[3, 4, 1, 9, 56, 7, 9, 12]
m=5
n=len(s)
s.sort()
for i in s:
    print i,
diff=float('inf')
for i in range(n-m): 
    diff=min(s[m+i-1]-s[i],diff)
print diff
