# Problem: E - Minimum Subsequence - https://codeforces.com/gym/594077/problem/E

from collections import defaultdict


x =int(input())
for _ in range(x):
    a = int(input())
    arr = ((input()))
    one = []
    zero =[]
    ans = []
    temp =1
    if arr[0]=='1':
        one.append(1)
    else:
        zero.append(1)
    ans.append(1)
    for i in range(1,len(arr)):
        if arr[i]=='0':
            if len(one)>0:
                popped = one.pop()
                ans.append(popped)
                
                zero.append(popped)
            else:
                temp+=1
                ans.append(temp)
                zero.append(temp)
        elif arr[i]=='1':
            if len(zero)>0:
                popped = zero.pop()
                ans.append(popped)
                
                one.append(popped)
            else:
                temp+=1
                ans.append(temp)
                one.append(temp)
    print(temp)
    print(*ans)




        
