_case=int(input())
for case in range(_case):
    l=int(input())
    maze=[]
    r=1
    for i in range(l):
        if r==1:
            maze =maze+list(map(int, input().split()))
        else:
            maze =maze+list(map(int, input().split()))[::-1]
        r*=-1
    h=0
    for i in range(1,len(maze)):
        if maze[i]<maze[i-1]:
            h+=1
        if maze[i]>maze[i-1]:
            h-=1
    if h<0:
        maze=maze[::-1]
    res=""
    for i in maze:
        res+="{} ".format(i)
    res=res[:-1]
    print(res)



