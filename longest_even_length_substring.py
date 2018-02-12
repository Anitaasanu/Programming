s ="123123"
s = [int(i) for i in list(s)]
n =len(s)
def longest_even_length_substring(s,n):
    maxlength=0
    for i in xrange(n):
       for j in xrange(i+1,n):
            l=j-i+1
            leftsum=0
            rightsum=0
            for k in xrange(l/2):
                leftsum+=int(s[i+k])
                rightsum+=int(s[i+k+l/2])
                if(leftsum==rightsum):
                    maxlength=l
            j=j+2
    return maxlength
            
print longest_even_length_substring(s,n)
