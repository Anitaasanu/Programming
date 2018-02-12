class node :
    def __init__(self,key):
        self.val=key
        self.left=None
        self.right=None
root=node(1)
root.left = node(2)
root.right = node(3)
root.left.left = node(4)
root.left.right=node(5)
root.right.left=node(6)

def DFS_tree(root):
    s=[]
    p=[]
    q = root
    while True:
        s.append(q.val)
        l=q.left
        r=q.right
        if l!=None:
            p.append(l)
        if r!=None:
            p.append(r)
        if len(p)==0:
            break
        print p
        q = p.pop()
    return s
    
print DFS_tree(root)    
