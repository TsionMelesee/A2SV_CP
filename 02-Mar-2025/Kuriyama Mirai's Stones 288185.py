# Problem: Kuriyama Mirai's Stones - https://codeforces.com/contest/433/problem/B

x = int(input())
arr = list(map(int,input().split()))
y  =int(input())
prefix = [0]*x
prefix[0]=arr[0]
for i in range(1,len(arr)):
    prefix[i]=prefix[i-1]+arr[i]
arr.sort()
for i in range(1,len(arr)):
    arr[i]=arr[i-1]+arr[i]



for i in range(y):
    a,b,c = map(int,input().split())
    if a == 1:
        if b-2<0:
            print(prefix[c-1])
        else:
            print(prefix[c-1]-prefix[b-2])
    else:
        if b-2<0:
            print(arr[c-1])
        else:


            print(arr[c-1]-arr[b-2])
