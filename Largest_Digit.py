num=int(input())
large=0
rem=0
while(num>0):
    rem=num%10
    if(rem>large):
       large=rem
    num=num//10

print("%d"%large)