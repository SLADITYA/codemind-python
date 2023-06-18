def prime(n):
    for i in range(2,n):
        if n % i == 0:
            return -1
    return 1
def pal(n):
    s = str(n)
    p = "".join(reversed(s))
    if s == p:
        return 1
    return -1
a = int(input())
for j in range(a+1,a**8):
    if prime(j)==1 and pal(j)==1:
        print(j)
        break