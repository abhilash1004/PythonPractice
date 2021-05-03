line = input("Enter the line:\n")
words = line.split(" ")
d = {}
for word in words:
	d[word]=d.get(word,0)+1
sum = 0
for key in d:
	sum += d[key]
print("Total No of Words: ",sum)
