def prime(n):
    if n==1:
        return -1
    else:
        for i in range(2,n):
            if n % i == 0:
                return -1
    return 1

a = int(input())
b = int(input())

for j in range(a,b+1):
    if prime(j)==1:
        print(j)