n = int(input("Enter Number of rows: "))
x=0
for i in range(1,n+1):
	for j in range(i):
		x+=1
		print(x,end=" ")
	print()

