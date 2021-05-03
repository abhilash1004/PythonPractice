x = ['1','2','3','4','5','6','7','8','9','0','A','B','C','D','E','F']
str=input("Enter the string: ")
p=1
for i in str:
	if i not in x:
		p=0
if p==1:
	print("Hexa Decimal")
else:
	print("Not Hexa Decimal")