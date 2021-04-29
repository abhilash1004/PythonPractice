def dig(num):
	s = 0
	while(num!=0):
		r = num%10
		num = (num//10)
		s = s+r
	return s


t = int(input())
while t>0:
	t-=1
	m = int(input())
	num = [0] * (m * 10);
	#print(num)
	size = 0
	for itr in range(m):
		templine = input()
		templist = templine.split(" ")
		#print(templist)
		temp = int(templist[0])
		temp2 = int(templist[1])
		for i in range(temp):
			num[size] = temp2
			size = size+1
	#print(size)
	mul = 1
	n=0
	#print(num)
	while size>0:
		n += mul*num[size-1]
		#print(n)
		size = size-1
		mul *= 10
	#print('n=',n)
	ans = 0
	s =0
	for i in range(1,n+1):
		#print(i)
		s += i
		ans += dig(i)
		#print(dig(i))
	print(ans,'=>',end="")
	while ans//10!=0:
		ans = dig(ans)
	print(ans)
	#print('s=',s)
