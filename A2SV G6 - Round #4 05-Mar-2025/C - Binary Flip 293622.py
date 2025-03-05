# Problem: C - Binary Flip - https://codeforces.com/gym/590053/problem/C

x = int(input())
for _ in range(x):
    n = int(input())
    a = list(input())
    b = list(input())
    
    prefix = [int(a[0])]
    for i in range(1, n):
        prefix.append(prefix[-1] + int(a[i]))
    
    flips = 0
    flag = True
    
    for i in range(n - 1, -1, -1):
        if flips % 2 == 0 and a[i] != b[i]:
            if (i + 1) != prefix[i] * 2:
                flag = False
                break
            flips += 1
        elif flips % 2 != 0 and a[i] == b[i]:
            if (i + 1) != prefix[i] * 2:
                flag = False
                break
            flips += 1
    
    print("YES" if flag else "NO")
