num = int(input("Enter Number: "))
sum = 0
n = num
while n!=0:
	r = n%10
	n = n//10
	sum += (r**3)
if sum == num:
	print("Armstrong")
else:
	print("Not Armstrong") 