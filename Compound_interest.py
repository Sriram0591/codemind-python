import math
p,r,t=map(float,input().split())
ci=math.pow((1+r/100.00),t)
ans=p*ci
print('%.2f'%ans)