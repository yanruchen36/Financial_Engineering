"""計算過程和結果輸出
"""

def calculate():
	p = 10000*int(p_entry.get())
	t = int(t_entry.get())
	r = 0.01*int(r_entry.get())

	times = t*12
	totalpayment = 0
	pp = p/times # 每月應還本金
	
	clist = []
	interestlist = []
	totalclist = []
	plist = []
	principallist = []
	
	for i in range(times):

		cp = p*r/12#每月應付利息金額
		c = pp + cp
		p -= pp
		clist.append(round(c))
		interestlist.append(round(cp,3))
		plist.append(round(p,3))
		principallist.append(round(pp,3))
	
	# 顯示新視窗和結果

	window2 = tk.Tk()
	window2.title("本金攤還試算表結果")
	tree = ttk.Treeview(window2, show = "headings")
	tree["columns"] = ("month","payment","interest","principal", "remaining principal")
	tree.column("month", width = 50)
	tree.column("payment", width = 100)
	tree.column("interest", width = 100)
	tree.column("principal", width = 100)
	tree.column("remaining principal", width = 160)
	
	# 顯示表頭
	tree.heading("month",text="month")  
	tree.heading("payment",text="payment")
	tree.heading("interest",text="interest")
	tree.heading("principal",text="principal")
	tree.heading("remaining principal",text="remaining principal")

	# 插入數據
	t = int(t_entry.get())
	times = 12*t
	for i in range(times):
		tree.insert("",i,values=((i+1),clist[i],interestlist[i], principallist[i], plist[i])) 

	tree.pack()
	window2.mainloop()




"""製作介面
"""

import tkinter as tk
from tkinter import ttk

window = tk.Tk() # 最初畫面
window.title("本金攤還試算")
window.geometry("400x300")
window.configure(background = "white")

header_label = tk.Label(window, text = "本金攤還試算")

# 以下為 p_frame 群組
p_frame = tk.Frame(window)
# 向上對齊父元件
p_frame.pack(side=tk.TOP)
p_label = tk.Label(p_frame, text = "本金（萬）")
p_label.pack(side=tk.LEFT)
p_entry = tk.Entry(p_frame)
p_entry.pack(side=tk.LEFT)

# 以下為 t_frame 群組
t_frame = tk.Frame(window)
t_frame.pack(side=tk.TOP)
t_label = tk.Label(t_frame, text = "期數（年）")
t_label.pack(side=tk.LEFT)
t_entry = tk.Entry(t_frame)
t_entry.pack(side=tk.LEFT)

# 以下為 r_frame 群組
r_frame = tk.Frame(window)
r_frame.pack(side=tk.TOP)
r_label = tk.Label(r_frame, text = "利率（%）")
r_label.pack(side=tk.LEFT)
r_entry = tk.Entry(r_frame)
r_entry.pack(side=tk.LEFT)

result_label = tk.Label(window)
result_label.pack()

calculate_btn = tk.Button(window, text = "送出", command = calculate)
calculate_btn.pack()


window.mainloop()



"""	def _init_(self):
		tk.Frame._init_(self)
		self.creatwidgets()

	def creatwidgets(self):
		self.btn = tk.Button(self, text = "送出", command = self.clickbtn)
	
	def clickbtn(self):
		self.close()"""