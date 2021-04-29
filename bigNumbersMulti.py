#Write a multiplication that takes two numbers that probably near 10^200 and perform multiplication of two numbers

#Input:

#First line of program will contain number of test case
#Each test case contains two Big number


#Output:

#For each test case print multiplication of two numbers

#Sample Input 1:
#1
#7234234234324234324232323423423432432423423423
#20

#Sample Output 1:
#144684684686484686484646468468468648648468468460


t = int(input())
while t>0:
	t -=1
	n1 = int(input())
	n2 = int(input())
		print(n1*n2)