m = int(input("Enter m: "))
n=int(input("Enter n: "))
mat = []
d1,d2 = {},{}
print("Enter Rows of Matrix: ")
for i in range(m):
	print(">",end="")
	row = list(map(int,input().split()))
	mat.append(row)
	for ele in row:
		if ele!=0:
			d1[ele] = d1.get(ele,0) + 1
print("Enter Rows of Matrix 2: ")
for i in range(m):
	print(">",end="")
	row = list(map(int,input().split()))
	mat.append(row)
	for ele in row:
		if ele!=0:
			d2[ele] = d2.get(ele,0) + 1


