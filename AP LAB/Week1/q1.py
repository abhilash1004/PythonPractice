x=input("ENter 1st List of Numbers")
y=input("Enter 2nd List of Numbers")
l1,l2=list(map(int,x.split(" "))),list(map(int,y.split(" ")))
ol=[]
el=[]
for i in l1:
	if i%2!=0:
		ol.append(i)
for i in l2:
	if i%2==0:
		el.append(i)
print("Odd list: ",ol,"\nEven List: ",el)