n=int(input("Enter the no of elements in set:"))
i=0
l1=[]
while i<n:
    a=int(input("enter:"))
    l1.append(a)
    i=i+1
print(l1)
l=len(l1)
i=0
j=0
while i<l-1:
    j=l1[l-1]
    while j<l-1:
        l1[j]=l1[j+1]
        j=j+1
    l1[0]=j
    i=i+1
    print(l1)
