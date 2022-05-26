def reverse(n):
    sum=0
    while(n!=0):
        rem=n%10
        sum=sum*10+rem
        n=n//10
    return(sum)
    
    
n=int(input())
while(n!=0):
    a=int(input())
    p=reverse(a)
    if(p==a):
        print("True")
    else:
        print("False")
    n-=1
    