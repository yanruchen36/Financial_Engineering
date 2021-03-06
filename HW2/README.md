## Homework 2    

* [ytm計算程式碼](https://github.com/yanruchen36/Financial_Engineering/blob/master/HW2/hw2ytm%E8%A8%88%E7%AE%97.py)  
* [Spot Rate 計算程式碼](https://github.com/yanruchen36/Financial_Engineering/blob/master/HW2/spotrate%E8%A8%88%E7%AE%97.py) 
* [Forward Rate 計算程式碼](https://github.com/yanruchen36/Financial_Engineering/blob/master/HW2/forwardrate%E8%A8%88%E7%AE%97.py)  



# 學習歷程  

* 計算公式　　
  
  * 到期殖利率 Yield to Maturity
  <div align=center><img width="400" height="50" src="https://github.com/yanruchen36/Financial_Engineering/blob/master/HW2/ytm.PNG"/></div>　　
> PV為當期價格，F為票面價值，R是年利率，M為每年期數，N為年數乘以期數。　　
  
  
   * 即期利率 Spot rate  
   
   [參考](https://www.trignosource.com/finance/spot%20rate.html#Calculator)
   
   zero coupon bond 的到期殖利率 = 即期利率  
   > zero coupon bond 即在到期日前不給付利息，只在到期日給付說好的金額  
   
   
  
   * 遠期利率 Forward rate  
  
   [參考](https://www.trignosource.com/finance/Forward%20rate.html#Calculator)
  
  [如何由債券殖利率算出理論即期利率](http://greenhornfinancefootnote.blogspot.com/2010/06/how-to-compute-theoretical-spot-rates.html)  
  [如何由理論即期利率算出遠期利率](http://greenhornfinancefootnote.blogspot.com/2010/08/how-to-compute-forward-rates-from.html)  
  
 * 三者關係  
 
  ytm = weighted average spot rate
  
  
# 流程圖  

  * yield to maturity 
    
  ![image](https://github.com/yanruchen36/Financial_Engineering/blob/master/HW2/ytm%E6%B5%81%E7%A8%8B%E5%9C%96.png)
  
