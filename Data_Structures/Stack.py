class Stack:
    l=list()
    def push(self,n):
        self.l.append(n)
    def pop(self):
        if(len(self.l)>0):return self.l.pop()
        return -1
    def disp(self):
        print(self.l)
