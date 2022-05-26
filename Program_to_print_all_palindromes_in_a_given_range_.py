a=int(input())
b=int(input())
i=a
sum=0
k=0
while(i>=a):
    temp=i
    while(temp!=0):
        rem=temp%10
        sum=sum*10+rem
        temp=temp//10
    if(sum==i):
        sum=i
        print('%d '%i,end="")    
    sum=0
    i+=1
    if(i>b):
        break
    
