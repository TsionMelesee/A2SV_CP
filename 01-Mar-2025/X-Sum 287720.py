# Problem: X-Sum - https://codeforces.com/problemset/problem/1676/D

def x_sum(arr):
    n, m = len(arr), len(arr[0])
    max_val = 0

    for i in range(n):
        for j in range(m):
            cnt = arr[i][j]
            x, y = i - 1, j - 1
            while x >= 0 and y >= 0:
                cnt += arr[x][y]
                x -= 1
                y -= 1

            x, y = i - 1, j + 1
            while x >= 0 and y < m:
                cnt += arr[x][y]
                x -= 1
                y += 1

            x, y = i + 1, j - 1
            while x < n and y >= 0:
                cnt += arr[x][y]
                x += 1
                y -= 1

            x, y = i + 1, j + 1
            while x < n and y < m:
                cnt += arr[x][y]
                x += 1
                y += 1

            max_val = max(max_val, cnt)

    return max_val


t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    print(x_sum(arr))
