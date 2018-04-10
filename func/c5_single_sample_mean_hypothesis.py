import numpy as np
import math
import sys,os
import scipy
from statsmodels.stats import weightstats
from sympy import exp,sqrt,pi,Integral
sys.path.append("/Users/leejunho/Desktop/git/python3Env/group_study/project_pre/func/")
from c1_basic_statistic import *

#Single hypothesis examination of Mean value. To see whether given "test_MEAN" significantly different with sample "MEAN"
# "pvalue < alpha", say alpha = 0.05, reject H0, accept H1 within alpha level. 
def bothSide_hypothesis(filename, test_MEAN=0):
    #returns : (test_statistic, pvalue)
    
    #filename :: input filename
    #test_MEAN :: The mean value to be tested, whether it is significantly different with sample mean. 

    # H0 : Sample_Mean = test_MEAN
    # H1 : Sample_Mean != test_MEAN
    
    if(filename[0]=="/"):
        filename = filename
    else:
        filename = os.getcwd() + "/" + filename   # get the path included filename
    loca=len(filename)
    for i in range (1,len(filename)+1):       # find the "/" location
        if(filename[-i] == "/"):
            loca = i-1
            break

    FILENAME = filename.replace(filename[:-loca],"")   # this is the shorten filename
    filename_No_Txt = FILENAME.replace(".txt","")
    infile = filename

    DATA_LIST = []
    f = open(infile,'r')
    for line in f:
        _,xaxis0,xaxis1, yaxis = line.split()
        X1 = float(xaxis0); X2 = float(xaxis1); Y = int(float(yaxis))
        if Y==0:
            continue
        else:
            for i in range(Y):
                DATA_LIST.append(X1+(X2-X1)/2)
#    print(DATA_LIST)
#    print(len(DATA_LIST))
    f.close()

    Ztest = weightstats.ztest(DATA_LIST, value=test_MEAN ,alternative='two-sided') 
    return Ztest


def main():
    inputfile = "gaus100.txt"
    Z_test = bothSide_hypothesis(inputfile, test_MEAN = 10)
    print(Z_test)

if __name__=="__main__":
    main()



