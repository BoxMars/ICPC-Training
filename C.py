input()
s = list(map(int,input().split()))
cost = 0
for i in range(1, len(s)):
    if s[i] < s[i - 1]:
        cost += s[i - 1] - s[i]
        s[i] = s[i - 1]
print(cost)
