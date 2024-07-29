# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 16:39:50 2024

@author: 17
"""

import random


guess = 0
count = 1
minValue = 1
maxValue = 100
ans = random.randint(minValue, maxValue)
#題目 當 count >5 就要離開,在判斷是否是猜對了

while ans != guess and count <= 5:
    guess = int(input("請輸入"+str(minValue)+"~"+str(maxValue)+"的整數:"))
    
    if guess >= minValue and guess <= maxValue:
        
        if guess > ans:
            maxValue = guess
            print(minValue,"至",maxValue)
        elif guess < ans:
            minValue = guess
            print(minValue,"至",maxValue)
        count += 1
    else:
        print("請輸入",minValue,"至",maxValue)
        
        
if ans == guess:
    
    print("猜對了")

else:
    print(ans)
    print("猜錯了,次數已滿")