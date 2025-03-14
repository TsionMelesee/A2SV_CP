# Problem: D - Life Across the Stars - https://codeforces.com/gym/591928/problem/D

from collections import Counter
x = int(input())
prefix = Counter()

for _ in range(x):
    l, r = map(int, input().split())
    prefix[l] += 1
    prefix[r] -= 1

prefix =  list(prefix.items())
prefix.sort()
val,max_val,year = 0,0,0

for i in range(len(prefix)):
    val += prefix[i][1]
    if val > max_val:
        max_val = val
        year = prefix[i][0]

print(year, max_val)
