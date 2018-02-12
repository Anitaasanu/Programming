class node:
    def __init__(self,key):
        self.left=None
        self.right=None
        self.val=key
root=node(10)
root.left=node(20)
root.right=node(30)
root.left.left=node(40)
root.left.right=node(60)
def height_BT(root):
    if root==None:
        return 0
    else:
        l_h=height_BT(root.left)
        r_h=height_BT(root.right)
        if l_h>r_h:
            return l_h+1
        else:
            return r_h+1
            
print height_BT(root)
