class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)

s="{()}[]{"
s=list(s)
n=len(s)
s1=Stack()
def matchingcharacter(c1,c2):
##    print c1,c2
    if c1=='[' and c2==']':
         s1.pop()
         return True
    elif c1=='{' and c2=='}':
         s1.pop()
         return True
    elif c1=='(' and c2==')':
         s1.pop()
         return True
    else :
         return False
    
def paranthesischecking(s,n):
    for i in xrange(n):
        if s[i]=='[' or s[i]=='{' or s[i]=='(':
            s1.push(s[i])
        elif s[i]==']' or s[i]=='}' or s[i]==')':
            if s1.isEmpty():
                return False
            elif(not matchingcharacter(s1.peek(),s[i])):
                return False
    if s1.isEmpty():
          return True
    else:
         return False
 
if paranthesischecking(s,n):
    print "string is balanced"
else:
    print "string is not balanced"
