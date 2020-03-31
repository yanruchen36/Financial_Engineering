"""作業二
計算市場債券報價中的ytm、spot rate、forward rate
以及建立forward rate對照表"""

# 首先取得所需值
while True:
	try:
		p = int(input('債券當期價格(元)=')) # 債券當前價格
		f = int(input('債券票面價值(元)=')) # 債券票面價值
		c = 0.01*int(input('債券票面利率(％)=')) # 債券票面利率
		n = int(input('債券到期年數(年)=')) # 到期年數
		m = int(input('每年付息次數(annully=1,semiannually=2,quarterly=4)=')) # 付息次數
		
		n = n*m
		c = c/m
		C = c*f
		
		for i in range(1,10000):

			r = i/100 #換成百分率
			F = f/((1+0.01*r)**n) #本金和
			TC = 0 #利息和

			for j in range(1,n+1):
				TC += C/((1+0.01*r)**j)
	
			pv = TC + F #present value

			d = pv - p # 因為r越大的話pv會慢慢變小
			if d <= 0:
				ytm = r
				break
		print('ytm=',r,'%')
		break
	except ValueError:
		print('格式錯誤，請重新輸入。')
	