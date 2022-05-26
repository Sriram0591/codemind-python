a,b,c=map(int,input().split())
i=a
count=0
while(i>=a):
    temp=i
    if(temp%c==0):
        count+=1
    i+=1
    if(i>b):
        break
print(count)    
    
