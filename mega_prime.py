def prime(n):
    if(n==1):
        return 0
    for i in range(2,n):
        if n % i == 0:
           return 0
    return 1
n = int(input())
s = str(n)
c=0
for j in s:
    if prime(int(j)):
        c+=1
if prime(n) and c==len(s):
    print("Mega Prime")
else:
    print("Not Mega Prime")