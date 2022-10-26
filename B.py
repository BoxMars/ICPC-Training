n=int(input())

flag=True

while flag:
    sn=list(str(n))
    s=0
    for i in sn:
        s+=int(i)
    if n%s!=0:
        n+=1
    else:
        flag=False
print(n)