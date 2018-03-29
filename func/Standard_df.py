#-*- coding: utf-8 -*-
#by minseok
#본 코드는 표준정규분포표 함수입니다.
from sympy import exp,sqrt,pi,Integral,Symbol

def Standard_nd(Z_value):                                           #표준정규분포에서 분산은 1, 평균은 0입니다.
    x = Symbol('x')
    Z = x
    f = exp(-(Z)**2/2)/(sqrt(2*pi))
    print("%0.4f"%float(Integral(f,(Z,0,Z_value))))
