#作業四

import math as m
from scipy.stats import norm

# 輸入值
S0 = float(input('stock price today :')) #當期股票價格
sigma = float(input('sigma :')) #資產價格波動率
d = float(input('dividends : '))#dividends
r = 0.01*float(input('interest rate(%) :')) # interest rate
K = float(input('strike price :')) #strike price
T = int(input('到期期數(月):'))/12 #六個月到期
dt = [int(n) for n in input('請輸入股利發放時間(用空格分開) :').split()]#股利發放時間(用空格分開)

# 算出股利折現，以求新股價
D = 0
for i in dt:
	D += d*m.exp(-r*i/12)
S = S0 - D

# d1、d2
d1 = (m.log(S/K)+(r+0.5*sigma**2)*T)/(sigma*T**(0.5))
d2 = d1 - sigma*T**(0.5)
print('d1 =',d1)
print('d2 =',d2)

# 常態分布
# put、call分別價格為何

p = K*m.exp(-r*T)*norm.cdf(-d2) - S*norm.cdf(-d1)
c = S*norm.cdf(d1) - K*m.exp(-r*T)*norm.cdf(d2)
print('call price =',c)
print('put price =',p)

