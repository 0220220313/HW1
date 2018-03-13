# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd



train_dat = pd.read_csv("training_data.csv" ,header=None)
train_dat = pd.read_csv("testing_data.csv" ,header=None )
train = train_dat.values

k=0
price=0

def ave(a,b):
    total=0
    for x in range (a-b,a):
        total=total+train[x,3]
    return total/b;   
n=0
m=0
macd=np.zeros((len(train),1))
def EMA (a,b):
    return (ave(a-2,b)*(b-1)+train[a-1,3]*2)/(b+1);
def DIF (a,n,m):
    return EMA(a,n)-EMA(a,m); 
def MACD(a,x,n,m):
    macd[a]=(macd[a-1]*(x-1)+DIF(a,n,m)*2)/(x+1) 
    return macd[a]
def buy(a):
    if 0>DIF(a,15,30)> MACD(a,15,15,30) and 0>MACD(a-1,15,15,30)>DIF(a-1,15,30)  and k<1:
        return 1;
    return 0;
def sell(a):
    if DIF(a-1,15,30)> MACD(a-1,15,15,30)>0 and  MACD(a,15,15,30)>DIF(a,15,30)>0 and k>-1:
        return 1;
    return 0;
test=np.zeros((len(train)-1,1))

for x in range(0,16):
       test[x]=0
       macd[x]=0
for x in range (16, len(train)):
    
    
    if buy(x):
                 k=k+1
                 price=price-train[x,0]
                 test[x-1]=1  
    elif sell(x):
                 k=k-1
                 price=price+train[x,0]
                 test[x-1]=-1    
    else:
        test[x-1]=0
#print(price,k)
price=0
P=0
hold=0
for x in range(0,len(train)-1):
    if test[x]==1:
        hold+=1
        P-=train[x+1,0]
    elif test[x]==-1:
        hold-=1
        P+=train[x+1,0]
#print(P,hold)
np.savetxt("output.csv",test,fmt="%d")





if __name__ == '__main__':
    # You should not modify this part.
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('--training',
                       default='training_data.csv',
                       help='input training data file name')
    parser.add_argument('--testing',
                        default='testing_data.csv',
                        help='input testing data file name')
    parser.add_argument('--output',
                        default='output.csv',
                        help='output file name')
    args = parser.parse_args()
