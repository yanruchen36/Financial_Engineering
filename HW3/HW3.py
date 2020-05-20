# 作業三

# 輸入值
'''
S0 = 160 #今天股價
K = 150 # strike price
u = 1.5 #上升
d = 0.5 #下降
n = 3 # 到期期數
r = 0.18232 # 複利的無風險利率
'''

S0 = float(input('stock price today = ')) #今天股價
K = float(input('strike pirce = ')) # strike price
u = float(input('u = ')) #上升
d = float(input('d = ')) #下降
n = int(input('n = ')) # 到期期數
r = 0.01*float(input('r(%) = ')) # 複利的無風險利率


import math
R = math.exp(r) # 真正的獲利

y = (R-d)/(u-d) # risk neutral probability

import numpy as np
# 製作陣列
c = np.array([None]*(n+1))
p = np.array([None]*(n+1))

#先計算出未來n期選擇權價值
for i in range(n+1):
	c[i] = max(0, S0*u**(n-i)*d**i - K)
	p[i] = max(0, K - S0*u**(n-i)*d**i)


"""
遞迴法例子 階層
def factorial(z):
    if z == 0 or z == 1:
        return 1
    else:
        return z*factorial(z - 1)
"""
#往回推選擇權價格
def price(u,d,Type):
	
	if u == n:
		return Type[d]
	else:
		return (y*price(u+1,d,Type)+(1-y)*price(u+1,d+1,Type))/R

C = round(price(0,0,c),4)
P = round(price(0,0,p),4)

print('call price =',C)
print('put price =',P)



"""
		suu(cuu = 0/suu-x)
	su
s		sud(cuu = 0/sud-x)
	sd
		sdd(cuu = 0/sdd-x)

先推所有股價的現貨價格
再推選擇權價格 往前推
往前推選擇權價格是:
cu = (pcuu + (1-p)cud) /R
cd = (pcud + (1-p)cdd) /R
"""