class node:
    def __init__(self,key):
        self.left=None
        self.right=None
        self.val=key
root=node(1)
root.left=node(2)
root.right=node(10)
root.left.left=node(20)
root.left.right=node(1)
root.left.right.left=node(5)
root.left.right.right=node(6)
root.right.right=node(-25)
root.right.right.right=node(4)
root.right.right.left=node(3)
root.right.right.right.left=node(4)
root.right.right.right.left.left=node(10)
root.right.right.right.left.right=node(20)
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
def diameter_BT(root):
    if root==None:
        return 0
    l_h=height_BT(root.left)
    r_h=height_BT(root.right)
    l_d=diameter_BT(root.left)
    r_d=diameter_BT(root.right)
    return max(l_h+r_h+1,max(l_d,r_d))
print diameter_BT(root)
    
