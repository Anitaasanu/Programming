class node:
    def __init__(self,key):
        self.left=None
        self.right=None
        self.val=key
root1=node(1)
root1.left=node(2)
root1.right=node(3)
##root1.right.left=node(4)
##root1.right.right=node(5)
root1.left.left=node(4)
root1.left.right=node(5)
root2=node(1)
root2.left=node(4)
root2.right=node(2)
root2.right.left=node(7)
root2.right.right=node(6)
root2.left.left=node(5)
root2.left.right=node(4)
def identical(r1,r2):
    if r1==None and r2==None:
        return True
    elif r1!=None and r2!=None:
        if r1.val==r2.val:
            if identical(r1.left,r2.right):
                if identical(r1.right,r2.left):
                    return True
    else :
        return False
        
print identical(root1,root2)
