import numpy as np
import math
import sys,os
import scipy
from scipy import stats
from statsmodels.stats import weightstats
from sympy import exp,sqrt,pi,Integral
sys.path.append("/Users/leejunho/Desktop/git/python3Env/group_study/project_pre/func/")
from c1_basic_statistic import *

#Single hypothesis examination of SAMPLE_MEAN value. To see whether given "TRUE_MEAN" significantly different with sample "MEAN"
# "pvalue < alpha", say alpha = 0.05, reject H0, accept H1 within alpha level. 
# Assume under n>=30, the t distribution could be smear to gaussian, but we do Ttest to be more precised. 
def bothSide_hypothesis(filename, TRUE_MEAN=0):
    #returns : [test_statistic, pvalue, sample_SAMPLE_MEAN, TRUE_MEAN]
    
    #filename :: input filename
    #TRUE_MEAN :: The mean value to be tested, whether it is significantly different with sample mean. 

    # H0 : SAMPLE_MEAN = TRUE_MEAN
    # H1 : SAMPLE_MEAN != TRUE_MEAN
    
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

    SAMPLE_MEAN = c1_mean(infile)

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

    Ztest = weightstats.ztest(DATA_LIST, value=TRUE_MEAN ,alternative='two-sided') 
    Ttest = stats.ttest_1samp(DATA_LIST,TRUE_MEAN)
#    print(Ttest[0]); print(Ttest[1])
#    Ttest = weightstats.ttest_ind(DATA_LIST, x2=None, value=TRUE_MEAN, alternative='two-sided')
#    print(Ttest)
    List = [float("%0.6f"%(Ttest[0])), float("%0.6f"%(Ttest[1])), float("%0.6f"%(SAMPLE_MEAN)), TRUE_MEAN]
    return List


def main():
    inputfile = "gaus30.txt"
    T_test = bothSide_hypothesis(inputfile, TRUE_MEAN = 9.3)
    print(T_test)

if __name__=="__main__":
    main()



