from Data_Structures import Stack
from Data_Structures import Queue
s=Stack()
q=Queue()
print("Executing stack")
for i in range(3):
    num=int(input("Enter Into Stack"))
    s.push(num)
for i in range(3):
    print(s.disp())
    print(s.pop())

print("Executing queue")

for i in range(3):
    num=int(input("Enter Into queue"))
    q.push(num)
for i in range(3):
    print(q.disp())
    print(q.pop())
