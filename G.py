_case = int(input())

for case in range(_case):
    s = list(map(int, input().split()))
    s1 = list(map(int, input().split()))
    s2 = list(map(int, input().split()))
    l1 = [0 for _ in range(s[0]**2+1)]
    for i in range(len(s1)):
        l1[s1[i]]=i+1
    same_part=[]
    for i in s2:
        if l1[i]>0:
            same_part.append(l1[i])
    dp=[0 for i in range(len(same_part))]
    dp[0]=1
    m=0
    print(same_part)
    for i in range(1,len(same_part)):
        for j in range(i):
            if same_part[i]>same_part[j]:
                dp[i]=max(dp[i],dp[j]+1)
                m=max(m,dp[i])
    print("Case {}: {}".format(case+1,m))


