n = int(input())
badwords = input().split(" ")
t = int(input())
while t>0:
	t = t-1
	line = input()
	ans = 0
	for badword in badwords:
		listLine = line.split()
		x=0
		for l in listLine:
			if l == badword:
				x+=1
		ans+=x
	if ans == 0:
		print("You Have Done Great Job!")
	else:
		print('Please Check:',ans,' Abused Words are Found')