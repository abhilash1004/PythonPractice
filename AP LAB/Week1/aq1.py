n=int(input("Enter n: "))
m=int(input("Enter m: "))
x = [0]*(m+1)

if m>1:
	x[1]=x[0]=1
	i = 2
	while i**2 <=m:
		#print(i,end=" ")
		if x[i]!=0:
			i+=1
			continue
		j=2
		while(1):
			a = i * j
			if a>m:
				break
			x[a] = 1
			j+=1
		i+=1
print("The Prime Numbers in Range ",n," to ",m,':')
i=n
while i<=m:
	if x[i]==0:
		print(i,end=" ")
	i+=1

