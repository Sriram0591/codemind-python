def reverse(n):
   sum=0
   while(n!=0):
       rem=n%10
       sum=sum*10+rem
       n=n//10
   return(sum)

num=int(input())
sqr=num*num
rev=reverse(num)
sqr1=rev*rev 
ans=reverse(sqr1)
if(ans==sqr):
	print("True")
else:
	print("False")