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

def No_leaf_node(root):
    if root==None:
        return 0
    if root.left==None or root.right==None:
        return 1
    else:
        return No_leaf_node(root.left)+No_leaf_node(root.right)
    
print No_leaf_node(root)
