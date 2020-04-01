"""
forward rate
"""
import math

t = int(input('債券原始到期時間(年): '))
r = int(input('債券存續時間(年): '))

print('請輸入',t,'年期零息債券價格')
pt = int(input('債券價格:'))
print('請輸入',t+r,'年期零息債券價格')
ptr = int(input('債券價格:'))

f1 = (pt/ptr)**(1/r) - 1
f2 = (1/r)*math.log(pt/ptr)

print(r,'year forward rate of interest beginning',t,'years from now on: ',round(100*f1,2),'%')
print(r,'year forward force of interest beginning',t,'years from now on: ',round(100*f2,2),'%')