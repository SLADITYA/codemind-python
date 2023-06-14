def prime(n):
    if n==1:
        return -1
    for i in range(2,n):
        if n % i == 0:
            return -1
    return 1

t = int(input())
for _ in range(1,t+1):
    n = int(input())
    for j in range(n,n*2):
        if prime(j)==1:
            break
    for k in range(n,1,-1):
        if prime(k)==1:
            break
    if abs(n-k)>abs(n-j):
        print(j)
    else:
        print(k)