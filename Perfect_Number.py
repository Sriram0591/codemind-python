n=int(input())
sum=0
temp1=n
i=1
while(i<n):
    temp=i
    if(temp1%temp==0):
        sum+=temp
    i+=1    
    
if(sum==n):
    print("True")
else:
    print("False")