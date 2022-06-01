def factorial(num):
    i=1
    fact=1
    while(i<=num):
        fact=fact*i
        i+=1
    return fact    

n=int(input())
temp=n
sum=0
while(n!=0):
    rem=n%10
    sum+=factorial(rem)
    n=n//10
if(temp==sum):
    print('The number %d is a strong number'%temp)
else:
    print('The number %d is not a strong number'%temp)