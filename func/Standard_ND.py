#-*- coding: utf-8 -*-
#by minseok
#본 코드는 표준정규분포표 함수입니다.
from sympy import exp,sqrt,pi,Integral,Symbol

def Standard_nd(Z_value):                                                     #표준정규분포에서 분산은 1, 평균은 0입니다.
    x = Symbol('x')
    Z = x
    f = exp(-(Z)**2/2)/(sqrt(2*pi))
    return "%0.4f"%float(Integral(f,(Z,0,Z_value)))

def Standard_nd_interval(Z_value1,Z_value2):                                  #표준정규분포 특정구간 확률입니다.
    if(Z_value1*Z_value2 > 0):                                                #두 Z값이 같은 부호
        if(Z_value1 > Z_value2):
            min,max = Z_value2,Z_value1
        else:                                                                 #Z_value2가 큰 경우와 두 값이 같은 경우를 포함합니다.
            min,max = Z_value1,Z_value2
        return "%0.4f"%(float(Standard_nd(max)) - float(Standard_nd(min)))

    if(Z_value1*Z_value2 < 0):                                                #두 Z값이 다른 부호
        if (Z_value1 > Z_value2):
            plus,minus = Z_value1,Z_value2
        else:                                                                 #위와 같습니다.
            plus,minus = Z_value2,Z_value1
        return "%0.4f"%(float(Standard_nd(plus)) + float(Standard_nd(minus)))

    if(Z_value1*Z_value2 == 0):                                               #어느 한쪽이 0이거나 둘다 0
        if(Z_value1 == 0):                                                    #Z_value1이 0인 경우, 0~Z_value2이므로 표준정규분포 함수를 사용합니다.
            return Standard_nd(Z_value2)
        else:                                                                 #Z_value2가 0이거나 둘다 0
            return Standard_nd(Z_value1)
