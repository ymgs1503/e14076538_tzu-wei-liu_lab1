#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random
def gogo(num, bin_str='', coin=''):  #轉成二進位、硬幣型式
    count=0
    for count in range(9):     #共九個硬幣，做九次
        decimal = num
        state_num = num % 2   #看最右邊位數是0或1
        num = num // 2  #每次把數字除2右移
        binary = 0
        binary += state_num*(10**count)  #計算二進位
        bin_str = str(state_num)+bin_str  #將二進位用str表示
        if state_num == 0:                 #判斷硬幣狀態
            coin = 'H' + coin
        else:
            coin = 'T' + coin
    return bin_str, coin          #回傳二進位、硬幣型式


class Nine_coins:
    def __init__(self, num):   #初始化參數
        self.number = num
        binary=0
        self.coin=''
        self.bin_str=''
        self.bin_str, self.coin = gogo(self.number, self.bin_str, self.coin)  #將數字轉成二進位及硬幣型式並回傳
       
    def __repr__(self):    #印出硬幣狀態
        return("Nine_Coins: "+ self.coin)
    
    def __str__(self):     #修改print印出的東西
        return f"binary: {self.bin_str} and decimal: {self.number}"
    
    def toss(self):        #重新投擲
        self.number = random.randint(0,511)     #產稱隨機0~511範圍的變數
        self.bin_str, self.coin = gogo(self.number,'','')    #將新數字轉成二進位及硬幣型式並回傳

