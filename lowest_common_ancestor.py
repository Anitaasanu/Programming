class node:
    def __init__(self,key):
        self.right=None
        self.left=None
        self.val=key
root=node(20)
root.left=node(8)
root.right=node(22)
root.left.left=node(4)
root.left.right=node(12)
root.left.right.left=node(10)
root.left.right.right=node(14)
n1=input("enter the value for n1:")
n2=input("enter the value for n2:")
def lcm(root,n1,n2):
    if root==None:
        return
    else:
        print "hello"
        if (n1<root.val and n2>root.val) or (n2<root.val and n1>root.val):
            return root.val
        elif (root.val<n1 and root.val<n2):
            return lcm(root.right,n1,n2)
        elif (root.val>n1 and root.val>n2):
            return lcm(root.left,n1,n2)
        else:
            if root.val == n1 :
                return n1
            elif root.val == n2:
                return n2
            
print lcm(root,n1,n2)
