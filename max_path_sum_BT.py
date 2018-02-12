class node:
    def __init__(self,key):
        self.left=None
        self.right=None
        self.val=key
root=node(10)
root.left=node(2)
root.right=node(10)
root.left.left=node(20)
root.left.right=node(1)
root.right.right=node(-25)
root.right.right.right=node(4)
root.right.right.left=node(3)
m=0
def max_path_sum_BT(root,m):
    if root==None:
        return 0
    l=max_path_sum_BT(root.left,m)
    r=max_path_sum_BT(root.right,m)
    max_single=max(max(l,r)+root.val,root.val)
    max_top=max(max_single,l+r+root.val)
    m=max(m,max_top)
    return max_single
print max_path_sum_BT(root,m)
