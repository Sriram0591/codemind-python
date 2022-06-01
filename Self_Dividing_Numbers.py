def digc(n):
    c=0
    while(n):
        c+=1
        n=n//10
    return c
    
def self(num):
    temp=num
    a=0
    while(num):
        rem=num%10
        if(rem==0):
            break
        if(temp%rem==0):
            a+=1
        num=num//10
    return a    
    
l=int(input())
u=int(input())
i=l
while(i<=u):
    if(self(i)==digc(i)):
        print('%d '%i,end='')
    i+=1    