# HW1
---
＃ ave(a,b)
def ave(a,b):
    total=0
    for x in range (a-b,a):
        total=total+train[x,3]
    return total/b;   
為第a-b天到第a天的收盤價平均值

＃ EMA（a,b)
類似ave function但越近的收盤價，權重越重

# DIF
  將兩個不同天數的平均相減，在此程式中使用15天的EMA與30天的EMA做相減，當數值大於0則有漲的趨勢，反之則跌

# MACD
  將DIF做平均，越靠近的DIF權重越大
  
# 概念
  若DIF、 MACD與DIF-MACD皆小於0，代表為空頭市場，亦即預測走向為跌，而DIF-MACD由負數轉正數時代表此股票有一定的機率要開始漲了，
  是買進的訊號，若手上的股票小於1，便買進。

  反之若三者皆大於0便是多頭市場，代表預測走向為漲，而DIF-MACD由正轉負時，便有一定機率開始下跌，若手上有持股，便在此時賣出




  
