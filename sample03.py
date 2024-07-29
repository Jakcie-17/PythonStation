# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 15:50:18 2024

@author: 17
"""

water = int(input("輸入降雨量"))

if water >= 3000:
    print("大淹水")
    print("超大大豪雨")
    
elif water >= 2000:
    print("可游泳")
    print("超大豪雨")
    
elif water >= 1000:
    print("大豪雨")
    
else:
    print("下雨天")
    print("都要帶傘")