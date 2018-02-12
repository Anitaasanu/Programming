s=[8, 5, 10, 7, 9, 4, 15, 12, 90, 13]
k=4
n=len(s)
for i in range(n-k+1):
    print max(s[i:i+k]),
