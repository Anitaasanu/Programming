d={}
s="ABDEFGABEF"
s=list(s)
n=len(s)
start=0
cur_len = 1
max_len = 1
for i in range(n):
    if s[i] not in d:
        d[s[i]]= i
    else:
        start = d[s[i]]
        d[s[i]] = i
for s[i]in d:
   print d[s[i]]
##print start
##i=d[s[i]]
##while(i>=0):
##    if s[i]
    
