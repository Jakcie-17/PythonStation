# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 16:23:14 2024

@author: 17
"""

total = 0
for i in range(2,21):
    
    if i % 2 == 0:
        print(i,end=",")
        
    if i % 5 == 0:
        total += i
        
print()
print("5的倍數和:",total)