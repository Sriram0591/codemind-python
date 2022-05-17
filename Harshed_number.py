number=int(input())
sum=0
temp=number
while(number!=0):
    
    digit=number%10
    sum+=digit
    number=number//10
if(temp%sum==0):
    print("True")
else:
    print("False")
