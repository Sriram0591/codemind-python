n=int(input())
sum=0
sqr=n*n
while(sqr!=0):
    rem=sqr%10
    sum +=rem
    sqr//=10

if(sum==n):
    print("Neon Number")
else:
    print("Not Neon Number")