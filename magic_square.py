n = 3
s = [[0 for i in xrange(n)]for x in xrange(n)]

def valid_side(m,s,i):
    if sum(s[i]) <= m:
        return True
    else:
        return False
def com_sum(m,s,i):
    if sum(s[i]) == m:
        return True
    else:
        return False

def find():
    d = [0]
    for i in xrange(n):
        if s[0][i] == 0:
            d.append(i)
            return d
        
def make_magic(s,n):
    m = n*(n^2+1)/2
    [r,c] = find()
    j = 1
    while(j<=n*n):
        for i in xrange(n):
            s[r][i] = j
            j+=1
        print s[0]
        if not(com_sum(m,s,0)):
            make_magic(s,n)
        else:
            break

make_magic(s,n)
        
            
        
            
        
        
    
