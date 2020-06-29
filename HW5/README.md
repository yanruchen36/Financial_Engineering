# 作業五  
## 作業內容  
1. 透過 Monte Carlo method  
2. 對 Hull White Model 模擬 Short Rate  
3. 將 Short Rate 帶入 Geometric Brownian Motion，r 換成 r(t) 模擬股價  
4. 自訂選擇權履約價，對每一條 path 計算出到期日時的 PayOff  
5. 對所有 Path 的 PayOff 進行期望值計算，並折現回 t=0 的時間點  
6. 計算出 Call Price & Put Price  

## 程式碼  

## 學習歷程  
* Monte Carlo method   
  蒙地卡羅方法（英語：Monte Carlo method），也稱統計類比方法，是1940年代中期由於科學技術的發展和電腦的發明，而提出的一種以機率統計理論為指導的數值計算方法。是指使用亂數（或更常見的偽亂數）來解決很多計算問題的方法。    
* Hull White Model  
是利率模型的一種。此模型中、為了把未來利率的變動變換成數學上較簡潔的Lattice model，將利率當作百慕達選擇權（選擇權存續期間中設定複數個期間，在這些期間可以執行的選擇權），以此便能將利率的變動價值以選擇權模評價型來評價。    
![image](https://github.com/yanruchen36/Financial_Engineering/blob/master/HW5/hull_white.PNG)  

* Geometric Brownian Motion     
幾何布朗運動（英語：geometric Brownian motion, GBM），也叫做指數布朗運動（英語：exponential Brownian motion）是連續時間情況下的隨機過程，其中隨機變量的對數遵循布朗運動，[1]也稱維納過程。幾何布朗運動在金融數學中有所應用，用來在布萊克-舒爾斯定價模型中模仿股票價格。    
