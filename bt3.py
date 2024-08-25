# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 07:07:10 2024

@author: TruongThiThanhUyen
"""
N= int(input('nhap N:'))
if N>=10 and N<=99:
    a=N//10
    b=N%10
    print('tổng các chữ số của N:',a+b)
