n=4
op=0
cl=0
s=[]
def paranthesis_print(n,op,cl):
    if cl==n:
        print ''.join(s)
        return
    else:
        if op>cl:
            s.append(')')
            paranthesis_print(n,op,cl+1)
            s.pop()
        if op<n:
            s.append('(')
            paranthesis_print(n,op+1,cl)
            s.pop()
paranthesis_print(n,op,cl)
