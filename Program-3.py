num = int(input("enter number"))
a=1
if num % 2 == 0:
    for i in range(1,num-1):
        print(a, end=',')
        a = a + 2
else:
    for i in range(1,num):
        print(a, end=',')
        a = a + 2
print(a)
