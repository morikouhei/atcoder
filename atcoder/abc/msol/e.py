import sys
input = sys.stdin.readline
def main():
    n = int(input())
    l = [list(map(int,input().split())) for i in range(n)]

    xcal = [[0]*n for i in range(1<<n)]
    ycal = [[0]*n for i in range(1<<n)]

    for i in range(1<<n):
        for j in range(n):
            xcal[i][j] = abs(l[j][0])
            ycal[i][j] = abs(l[j][1])
            for k in range(n):
                if (i>>k) & 1:
                    xcal[i][j] = min(xcal[i][j],abs(l[j][0]-l[k][0]))
                    ycal[i][j] = min(ycal[i][j],abs(l[j][1]-l[k][1]))
            xcal[i][j] *= l[j][2]
            ycal[i][j] *= l[j][2]
    ans = [float("INF")]*(n+1)

    for i in range(1<<n):
        count = 0
        for j in range(n):
            if i >> j & 1:
                count += 1
        j = i
        while j >= 0:
            j &= i
            cost = 0
            for k in range(n):
                if not (i>>k & 1):
                    cost += min(xcal[j][k],ycal[i-j][k])
                if cost > ans[count]:
                    break
            ans[count] = min(ans[count],cost)
            j -= 1

    for i in ans:
        print(i)
if __name__ == "__main__":
    main()