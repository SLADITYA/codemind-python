def prime(n):
    if n==1:
        return -1
    else:
        for i in range(2,n):
            if n % i == 0:
                return -1
    return 1

a = int(input())
cnt=0
for j in range(1,a+1):
    if prime(j)==-1 and a%j==0:
        cnt+=1
print(cnt)