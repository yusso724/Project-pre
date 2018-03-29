#-*- coding: utf-8 -*-
#by minseok
#본 코드는 정규분포의 확률밀도함수를 구현한 함수입니다.
from sympy import exp, sqrt, pi, Integral, Symbol

def Normald_pdf(Mean,Variance,Pmin,Pmax):                       #평균,분산,구간1,구간2
    x = Symbol('x')
    f = exp(-(x-Mean)**2/(2*Variance**2))/(Variance*sqrt(2*pi))
    print(Integral(f, (x,Pmin,Pmax)).doit().evalf())