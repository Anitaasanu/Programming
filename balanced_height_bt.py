class node:
    def __init__(self,key):
        self.left=None
        self.right=None
        self.val=key
root=node(1)
root.left=node(10)
##root.right=node(39)
root.left.left=node(5)
def height(root):
    print "hello"
    if root==None:
        return 0
    else:
        l_h=height(root.left)
        r_h=height(root.right)
        if l_h>r_h:
            return l_h+1
        else:
            return r_h+1
if height==1 or height==0:
    print "Balanced Tree"
else:
    print "Not Balanced Tree"
