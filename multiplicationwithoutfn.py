def mult(a,b):
    if(b==0):
        return 0
    elif(b>0):
        return a+mult(a,b-1)
    else:
        return -mult(a,-b)
print mult(-22,-8)
