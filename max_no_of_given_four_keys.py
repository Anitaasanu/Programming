n=input("enter the number:")
def find_optimal(n):
    if n<7:
        return n
    maximum = 0
    b=n-3
    while(b>0):
        current=(n-b-1)*find_optimal(b)
        if current>maximum:
            maximum = current
        b-=1
    return maximum
print find_optimal(n)
