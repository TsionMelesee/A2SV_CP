# Problem: C - Penalty Shootout - https://codeforces.com/gym/596141/problem/C

x = int(input())
for _ in range(x):
    pen = input()
    first =0
    second = 0
    amnt = 0
    i = 0
    
    def fun(pen,first,second,i,size):
        # print(i)
        # print(pen)
        if len(pen)==0:
            return 10
        
        
        if second+int((size-i+1)/2)<first or first+int((size-i)/2)<second:
            return i
        if i%2==0 and pen[0]!='?':
            first+=int(pen[0])
            # amnt+=1
            return fun(pen[1:],first,second,i+1,size)
        elif i%2!=0 and pen[0]!='?':
            second+=int(pen[0])
            # amnt+=1
            return fun(pen[1:],first,second,i+1,size)
        else:
            return min(fun('0'+pen[1:],first,second,i,size),fun('1'+pen[1:],first,second,i,size))
    
    if len(set(pen))==1 and pen[0]=='?':
        print(6)
    elif len(set(pen))==1 and pen[0]!='?':
        print(10)
    else:
        
        print((fun(pen,first,second,i,len(pen))))
    # print(amnt)
    

        

        