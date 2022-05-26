a=int(input())
i=1
count=1
while(i<=a):
    if(a%i==0):
        temp=i
        for k in range(2,(temp//2)+1):
            if(temp%k==0):
                count+=1
                break
    i+=1            
print(count)    