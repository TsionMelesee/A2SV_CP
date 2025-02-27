# Problem: B - Jo's Adventure - https://codeforces.com/gym/590053/problem/B

length,query = map(int,input().split())
arr = list(map(int,input().split()))

prefix_one = [0]*(length)
for i in range(1,length):
    if arr[i-1]>arr[i]:
        prefix_one[i]=arr[i-1]-arr[i]
    else:
        prefix_one[i]=0
for i in range(1,length):
    prefix_one[i]=prefix_one[i-1]+prefix_one[i]
# print(prefix_one)

prefix_two =  [0]*(length)
for i in range(length-2,-1,-1):
    if arr[i + 1] > arr[i]:
        prefix_two[i]=arr[i + 1]-arr[i]
    else:
        prefix_two[i] = 0
for i in range(length - 2, -1, -1):
    prefix_two[i] += prefix_two[i + 1]
    
for _ in range(query):
    left,right = map(int,input().split())
    if left<right:
        print(prefix_one[right - 1] - (prefix_one[left - 1] if left>1 else 0)) 
    else:
        print(prefix_two[right - 1] -( prefix_two[left - 1]if left>1 else 0))