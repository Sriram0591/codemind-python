import math
x,y,m=map(int,(input().split()))
power=(math.pow(x,y))
ans=power%m
print('%d'%ans)