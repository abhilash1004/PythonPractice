import random

n = int(input("Enter n: "))
d = {}
sum = 0
str = ''
c=0
for i in range(n):
	s = input("Enter Value: ")
	p = random.randrange(0,100)
	d[p] = s
	#sum += d[s]
	x=1
	try:
		y= int(s)
	except:
		x=0
	if x==1:
		sum += int(s)
		c+=1
	else:
		str += s
print(d)
if c!=0:
	print("Average = ",(sum/c))
else:
	print("Average = 0")
print(str)
v = input("Enter Value to find in dictionary: ")
x=0
for key in d:
	if d[key] == v:
		print("Founded ",v ," and its key = ",key)
		x=1
if x==0:
	print("Not Founded")
	
for key in d:
	for ch in d[key]:
		if ch.isdigit() or ch.isupper() or ch.islower():
			continue
		print(d[key], end=" ")
		break 