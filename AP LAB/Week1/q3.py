n = int(input("Enter Number of Strings: "))
x=[]
for i in range(n):
	s=input("Enter String: ")
	x.append(s)
count = 0
for str in x:
	if str[0] == str[len(str)-1] and len(str)>1:
		count+=1
print('Count=',count)
for str in x:
	if len(str)%2!=0:
		print(str,end=" ")
