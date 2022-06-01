n=int(input())
count=0
while(n):
    a,b=map(int,input().split())
    i=a
    while(i<=b):
        temp=i
        rem=temp%10
        if(rem==2 or rem==3 or rem==9):
            count+=1
        temp=temp/10
        i+=1
    print(count)
    count=0
    n-=1
