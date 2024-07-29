# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 15:45:06 2024

@author: 17
"""

account = input("帳號:")
pwd = input("密碼:")

if account == "lcc" and pwd == "good":
    print("登入成功")
    print("待辦事項如下")
    
else:
    print("帳密錯誤")
    print("執行完畢")