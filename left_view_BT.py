class node:
    def __init__(self,key):
        self.left=None
        self.right=None
        self.val=key
root=node(1)
root.left=node(2)
root.right=node(3)
root.right.right=node(4)
root.left.left=node(5)
def left_view(root):
    if root==None:
        return
    else:
        print root.val
        left_view(root.left)
##        print root.val
left_view(root)
