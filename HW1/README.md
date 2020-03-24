# 作業一
>製作本金攤還試算表，本金平均攤還法是將本金平均在貸款期間償還，每期償還的本金均相同，而每期所攤還的利息卻因累積未攤還之本金逐漸減少而跟著減少，因此每期所需攤還的本利和會越來越少。    
    
* [程式碼](https://github.com/yanruchen36/Financial_Engineering/blob/master/HW1/hw1revise.py)     

## 學習歷程

* 付款公式  
  * 每月應攤還本金 = 本金÷總期數  
  
  * 每月應攤還利息 = 剩餘本金×月利率  
  
  * 每月應付金額 = 前兩項相加
          
* 介面製作  
  * 第一個視窗  
    要取得計算所需的值，本金、年利率、期數，並決定單位（萬、百分率、年）。得到值之後讓使用者按下按鈕，並讓此動作告知程式開始運算結果。  
          
  * 第二個視窗
    返回計算結果，並用表格的方式簡單明瞭。使用tkinter treeview。
    * [參考資源](https://blog.csdn.net/sinat_27382047/article/details/80161637)  
         
         
 * 互評後修改內容  
 
    * 將每月應付款金額改成整數，以方便付款  
    * 公式錯誤部分修正  
    * 新增每月應攤還本金格  
    * 變數定義寫註解說明清楚  
    
  * 尚未修正  
    * 流程圖  
    
## 使用說明 
  1. 輸入本金、期數和年利率後，按下送出。
<div align=center><img width="300" height="300" src="https://github.com/yanruchen36/Financial_Engineering-/blob/master/HW1/gui1.png"/></div>
  2. 即可得到本金攤還試算結果。  
  <div align=center><img width="300" height="300" src="https://github.com/yanruchen36/Financial_Engineering-/blob/master/HW1/gui2.png"/></div>
  3. 上下滾動查看。
  <div align=center><img width="300" height="300" src="https://github.com/yanruchen36/Financial_Engineering-/blob/master/HW1/gui3.png"/></div>  

## 流程圖    
    
  <div align=center><img width="150" height = "600"   src="https://github.com/yanruchen36/Financial_Engineering-/blob/master/HW1/Untitled%20Diagram.png"/></div>

