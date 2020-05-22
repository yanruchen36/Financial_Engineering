# Homework 3

## 作業說明

> A non-dividend-paying stock is selling for $160.    
  u = 1.5; d = 0.5; r = 18.232% per period    
  Hence p = (R − d)/(u − d) = 0.7.     
  Consider a European call on this stock with X = 150 and n = 3.    
  What is the call/put value? Or what is the PV of the expected payoff at expiration? (by backward induction).   

## 程式碼  
* [HW3](https://github.com/yanruchen36/Financial_Engineering/blob/master/HW3/HW3.py)

## 學習歷程  
* 二項期權定價模型 BOPM  

    [參考](https://wiki.mbalib.com/zh-tw/%E4%BA%8C%E9%A1%B9%E6%9C%9F%E6%9D%83%E5%AE%9A%E4%BB%B7%E6%A8%A1%E5%9E%8B)  
    
* 逆向歸納法 backward induction   
一開始有當期資產價格，利用BOPM求出到期的股價、期權價格後，從最後一個階段開始分析，逐步向前歸納出當期期權價格。  
    [參考](https://wiki.mbalib.com/zh-tw/%E9%80%86%E5%90%91%E5%BD%92%E7%BA%B3%E6%B3%95)
  
