# Problem: Red and Blue - https://codeforces.com/contest/1469/problem/B

for _ in range(int(input())): 
    x = int(input()) 
    red = list(map(int, input().split()))
    y = int(input()) 
    blue = list(map(int, input().split()))
    red_prefix = 0
    red_max = 0
    for i in range(x):
        red_prefix += red[i]
        red_max = max(red_max, red_prefix)

    blue_prefix = 0
    blue_max = 0
    for i in range(y):
        blue_prefix += blue[i]
        blue_max = max(blue_max, blue_prefix)

    print(max(0, red_max + blue_max))
