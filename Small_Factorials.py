n=int(input())
pro=1
i=1
while(n!=0):
    a=int(input())
    for i in range(1,a+1):
        pro=pro*i
    print(pro)
    pro=1
    n-=1