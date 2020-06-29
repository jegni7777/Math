#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 15 15:00:04 2020

@author: jaegeunkim
"""
"""
This code was written for calculating the amount of money that we'll get if we finish all payment on national insurance.
"""

import numpy as np
from math import trunc
import sys

alpha = np.zeros(23) #alpha는 소득대체율에 해당하는 비례상수입니다.
for i in range(alpha.shape[0]):
    if i == 0: alpha[i] = 2.4
    elif i == 1: alpha[i] = 1.8
    elif i == 3: alpha[i] = 1.5
    else: alpha[i] = 1.5 - 0.015*(i-2)
    
beta = np.zeros(23) #beta는 B에 곱해주는 상수값입니다.
for i in range(beta.shape[0]):
    if i == 0 : beta[i] = 0.75
    else: beta[i] = 1.0
    
startY = int(input("가입시작 연도는?(1988년 이상이어야 합니다)     "))
startM = int(input("가입시작 월은?     "))
endY = int(input("가입종료 연도는?     "))
endM = int(input("가입종료 월은?     "))
A = int(input("연금수급전 3년간의 평균소득월액의 평균액은 ?     "))
B = int(input("가입자 개인의 가입기간중의 평균소득월액의 평균액은 ?     "))
P = (endY - startY)*12 + (endM-startM) #P는 전체 가입개월수입니다.
if P < 10*12: 
    print("가입기간이 10년 미만입니다. 자격미달입니다.")
    sys.exit()
    
if P >= 20*12: n = trunc( (P-20*12)/12 ) #n은 20년을 초과하거나 미달하는 가입기간 개월수입니다.
else: n = trunc( (P-20*12)/12 ) - 1

Pn = np.zeros(23)

dictP = dict() #이 딕셔너리는 연도별 가입개월수를 값으로 갖습니다. 키는 연도입니다.
if endY - startY >=2 : 
    middleY = np.arange(startY+1,endY,1)
    for x in middleY:
        dictP.update({x : 12})
    dictP.update({startY : 13-startM})
    dictP.update({endY : endM-1})
elif endY - startY ==1 :
    dictP.update({startY : 13-startM})
    dictP.update({endY : endM-1})
elif endY - startY ==0 :
    dictP.update({endY: endM - startM})
    
for i in range(23): #수열 Pn에 해당하는 개월수를 계산해서 넣어줍니다.
    for x in dictP:
        if i==0 and 1988 <= x <=1998 : Pn[i] += dictP[x]
        if i==1 and 1999 <= x <=2007 : Pn[i] += dictP[x]
        if 2<=i<=21 and x == 2008 + (i-2) : Pn[i] = dictP[x]
        if i==22 and 2028 <= x : Pn[i] += dictP[x]

S = 0 #S는 연금지급액입니다.
for i in  range(23):
    S += alpha[i]*(A + beta[i]*B)*Pn[i]/P
S *= 1 + 0.05*n
paidC9 = trunc(0.09*B*P)
paidC45 = trunc(0.045*B*P)
print("\n노령연금 예상월액은 "+str(trunc(S/12))+" 입니다.  ")
print("납부한 연금보험료는 9% 기준 "+str(trunc(0.09*B*P))+" 입니다.")
print("납부한 연금보험료는 4.5% 기준 "+str(trunc(0.045*B*P))+" 입니다.")

r = 0.015 #r은 이자율입니다.
a0 = paidC45/360
T = a0*(1+r/12)*((r/12+1)**360 - 1)/(r/12)
print(str(r*100)+"% 이자율에서 "+str(paidC9)+"을 360개월로 나눈 금액을 매월 적금에 넣었을 때 발생하는 원리금은 "
      + str(T)+"원 입니다." )