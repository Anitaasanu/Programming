class node:
    def __init__(self,key):
         self.left=None
         self.right=None
         self.nextright=None
         self.val=key
root=node(10)
root.left=node(8)
root.right=node(2)
root.left.left=node(3)
##root.left.right=node(5)
##root.right.left=node(6)
root.right.right=node(90)
queue=[]
q=[]
q1=[]
q2=[]
def level_order(root):
##    print "Hello"
    queue.append(root)
    while len(queue)!=0:
        n=queue[0]
        q.append(n.val)
        if n.left!=None:
            q1.append(n.left.val)
            queue.append(n.left)
        if n.right!=None:
            q2.append(n.right.val)
            queue.append(n.right)
        queue.pop(0)
def con_nodes_slevel(q1,q2):
    for i in range(len(q2)):
        print "The next Right element of :",q1[i],"is",q2[i]
level_order(root)
con_nodes_slevel(q1,q2)
for i in q:
    print i
