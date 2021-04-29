x=input('Enter the string:')
list=[]
for l in x:
    list.append(l)
a=len(list)
i=0
l1=[]
l2=[]
while i<a/2:
    l1.append(list[i])
    i=i+1
i=a/2
while i>=a/2 and i<a:
    l2.append(list[i])
    i=i+1
print(l1,l2)
ans=set(l1).intersection(l2)
c=len(ans)
if c==0:
    print(-1)
else:
    print(c)
