n=int(input())
pro=1
sum=0
while(n!=0):
    rem=n%10
    sum+=rem
    pro=pro*rem
    n=n//10
if(pro==sum):
    print("Spy Number")
else:
    print("Not Spy Number")