n = int(input())
a = 0
b = 1
lst=[0,1]
for i in range(1,n//2):
    c = a+b
    a = b
    b = c
    lst.append(c)
if n in lst:
    print("True")
else:
    print("False")