n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

ans = 0
for i,j in zip(a,b):
    ans += i*j
if ans == 0:
    print("Yes")
else:
    print("No")