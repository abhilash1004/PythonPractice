

if __name__ == '__main__':
    n = int(input())
    x=input()
    l=x.split(",")
l.sort(reverse=True)
j=0
while j<n-1:
    if l[j]==l[j+1]:
        j=j+1
        continue
    print(l[j+1])
    break
print(l)
list = ["geeks", "for", "geeks"]
for index in range(len(list)):
    print(list[index])
    print(index)
    print('HI')
print('Finished')
