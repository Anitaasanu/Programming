class node:
    def __init__(self,data):
        self.left=None
        self.right=None
        self.h=0
        self.val=data
##d={}
root = node(1)
root.left = node(2)
root.right = node(3)
root.left.left = node(4)
root.left.right = node(5)
root.right.left = node(6)
root.right.right = node(7)
root.right.left.right = node(8)
root.right.right.right = node(9)
cnt=0
q=[]
def vertical_view(root,cnt):
    if root==None:
        return
    else:
        root.h=cnt
        print root.val,root.h
        q.append([root.val,root.h])
        vertical_view(root.left,cnt-1)
        vertical_view(root.right,cnt+1)
vertical_view(root,cnt)
print sorted(q,key=lambda x: x[1])
