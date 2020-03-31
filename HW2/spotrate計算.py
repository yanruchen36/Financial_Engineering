"""
spot rate計算
"""
import math

d = int(input('債券存續時間 = '))
p = int(input('債券當期價格 = '))
f = int(input('債券票面價格 = '))

P = p/f
s = (P)**(-1/d) - 1
S = (-1/d)*math.log(P)

print('spot rate of interest: ', 100*round(s,4),'%')
print('spot force of interest: ',100*round(S,4),'%')

