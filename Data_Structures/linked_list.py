class Node:
    def __init__(self,info):
        self.info=info
        self.next=None
class LList:
    def __init__(self):
        self.head=None
    def disp(self):
        temp=self.head
        while(temp!=None):
            print(temp.info,end=' ')
            temp=temp.next
h=LList()
print("Enter -1 to exit")
i=0
while i!=-1:
    i=int(input("Enter data"))
    if(i!=-1):
        if h.head==None:
            start=Node(i)
            h.head=start
            prev=start
            continue
        cur=Node(i)
        prev.next=cur
        prev=cur
print("Printing data of List:")
h.disp()
