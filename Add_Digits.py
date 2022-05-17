def disum(n):
    sum=0
    while(n!=0):
        rem=n%10
        sum+=rem
        n=n//10
    return(sum)    
    
num=int(input())
sum1=0
sum2=0
sum3=0
sum4=0
sum5=0
sum1=disum(num)
sum2=disum(sum1)
sum3=disum(sum2)
sum4=disum(sum3)
sum5=disum(sum4)
print(sum5)