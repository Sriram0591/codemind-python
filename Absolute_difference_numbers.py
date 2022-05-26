def reverse(n):
    sum=0
    while(n!=0):
        rem=n%10
        sum=sum*10+rem
        n=n//10
    return(sum)    

n,lim=map(int,input().split())
temp=reverse(n)
count=0
dig=0
while(n!=0):
    rem=n%10
    count+=1
    dig=(dig*10)+rem
    n=n//10
    if(count==lim):
        break

count1=0
dig1=0
while(temp!=0):
    rem1=temp%10
    count1+=1
    dig1=dig1*10+rem1
    temp=temp//10
    if(count1==lim):
        break

rev1=dig1
rev=reverse(dig)
if(rev>rev1):
    print(rev-rev1)
else:
    print(rev1-rev)
    