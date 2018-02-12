class node:
    def __init__(self,data):
        self.left=None
        self.right=None
        self.h=0
        self.val=data
##d={}
root = node(1)
root.left        = node(2)
root.right       = node(3)
root.left.left  = node(7)
root.left.right = node(6)
root.right.left  = node(5)
root.right.right = node(4)
##cnt=0
q=[]
queue = []
def vertical_view(root,cnt):
    if root==None:
        return
    else:
        root.h=cnt
        print root.val,root.h
       
        if(cnt%2==0):
            vertical_view(root.left,cnt+1)
            vertical_view(root.right,cnt+1)
        else:
            vertical_view(root.right,cnt+1)
            vertical_view(root.left,cnt+1)
def level_order(root):
    cnt=0
    queue.append(root)
    while len(queue)!=0:
        n = queue[0]
        print (n.val)
        if(cnt%2==0):
            if n.left!= None:
                queue.append(n.left)
            if n.right!= None:
                queue.append(n.right)
        else:
            if n.right!= None:
                queue.append(n.right)
            if n.left!= None:
                queue.append(n.left)
        cnt+=1
        queue.pop(0)

##vertical_view(root,cnt)
level_order(root)
##q=sorted(q,key=lambda x:x[1])
##count =[]
##for i in q:
##    print i 
    
        
