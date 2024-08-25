# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 11:58:17 2024

@author: Student
"""

a="Đại học Quốc gia, Khu phố 6, P. Linh Trung, Q. Thủ Đức, Tp.HCM"
a=a.replace('P. ','').replace('Q. ', '').replace('Tp. ', '')
x = a.split(',')
for i in x:
    print(i)