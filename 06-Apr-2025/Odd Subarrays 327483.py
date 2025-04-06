# Problem: Odd Subarrays - https://codeforces.com/problemset/problem/1686/B

x = int(input())

for _ in range(x):
    n = int(input())
    arr = list(map(int, input().split()))
    cnt = 0
    diff = []

    for i in range(1, n):
        diff.append(arr[i] - arr[i - 1])

    seen = {}
    for i in range(len(diff)):
        if diff[i] < 0 and (i - 1) not in seen:
            seen[i] = True 
            cnt += 1

    print(cnt)
