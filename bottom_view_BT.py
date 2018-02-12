class node:
    def __init__(self,key):
        self.left=None
        self.right=None
        self.hd=0
        self.bv = 0
        self.val=key
d={}
root=node(20)
root.left=node(8)
root.right=node(22)
root.right.right=node(25)
root.left.left=node(5)
root.left.right=node(10)
root.left.left.right=node(9)
root.left.left.left=node(7)
root.left.right.right=node(3)
count = 0
def in_order(root,count):
    prev=root
    if root ==None:
        return
    else:
        in_order(root.left,count-1)
        root.hd = count
        print root.val,root.hd
        d[root.val] = root.hd
        in_order(root.right,count+1)
queue =[]
q=[]
l = []
def level_order(root):
    queue.append(root)
    while len(queue)!=0:
        n = queue[0]
        q.append(n.val)
        if n.left!= None:
            queue.append(n.left)
        if n.right!= None:
            queue.append(n.right)
        queue.pop(0)
def bottom_view(d,q):
    for i in q:
        l.append([i,d[i]])
    d={}
    for i in l:
        d[i[1]] =i[0]
    v = [i for i in d]
    v.sort()
    for i in v:
        print d[i]
in_order(root,count)
level_order(root)
print d
bottom_view(d,q)

    
