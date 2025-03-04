# Problem: B - Fix the Forecast! - https://codeforces.com/gym/591928/problem/B

from collections import defaultdict

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    sorted_a = sorted(a)
    sorted_b = sorted(b)
    dicc = defaultdict(list)

    for i in range(n):
        dicc[sorted_a[i]].append(sorted_b[i])

    output = []
    for i in range(n):
        output.append(dicc[a[i]].pop())

    for i in range(n):
        print(output[i], end=" ")
    print()
