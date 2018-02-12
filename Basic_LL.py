class node:
    def __init__(self,data):
        self.val=data
        self.next=None
class Linked_list:
    def __init__(self):
        self.head=None
    def push(self,new_data):
        new_node=node(new_data)
        new_node.next=self.head
        self.head=new_node
