def uidcheck(word):
    flag=[0,0,0,0,1]
    if len(word)==10:
        flag[0]=1
    x=0
    y=0
    for ch in word:
        if ch.isupper():
            x=x+1
        if ch.isdigit():
            y=y+1
        if ch.isdigit() or ch.isupper() or ch.islower():
            continue
            flag[4]=0
    if x>=2:
        flag[1]=1
    if y>=3:
        flag[2]=1
    count={}
    for ch in word:
        count[ch]=count.get(ch,0)+1
    p=len(count)
    if p==10:
        flag[3]=1
    if sum(flag)==5:
        return 1
    else:
        return 0


t=int(input())
l=[]
for s in range(0,t):
    x=input()
    l.append(x)
v=len(l)
for i in range(0,v):
    a=uidcheck(l[i])
    if a==1:
        print("Valid")
    else:
        print("Invalid")
