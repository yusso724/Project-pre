#Author : JUNHO LEE
#According to central limit theorem, even though distribution of population does not belongs to Gaussian, distribution of the sample mean is gaussian, if event number bigger than 30
from matplotlib import pyplot as plt
import numpy as np
import sys,os
from sympy import exp,sqrt,pi,Integral
sys.path.append("/Users/leejunho/Desktop/git/python3Env/group_study/project_pre/func/")
from c1_basic_statistic import *

# recommand to use on sample size bigger than 30, i.e. n>=30
def Fit_Sample_Gaus_histo(filename, Xaxis_Name='', SIGMA=2,exp_Mean_error=0.1, norm=0, Show=False, Show_sample=False):
    # returns [Mean-n*sigma,Mean+n*sigma,Total_Entry,Expected number to reach given sigma confidence interval, SIGMA, MEAN,sample_mean_error(std) ,exp_Mean_error]  (exp_MEAN_error :: [Mean-exp_MEAN_error ,Mean+exp_MEAN_error] within given sigma confidence interval)

    # Xaxis_Name :: put what you want for Axis name
    # norm :: 0 for normalized histogram showing. (suggest do not change this value)
    # exp_Mean_error :: expected Mean error in given SIGMA level confidence interval
    # SIGMA :: pick your sigma range to be returned
    # Show :: if True, the maximum y value of canvas would be sample_mean_distribution's Maximum value
    # Show_sample :: if True, it will print the sample distribution as well

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
    BIN_NUM = bin_num(infile);        #print(BIN_NUM)
    Mode = most_frequent_bin(infile); #print(type(Mode)); print(Mode)
    Median = c1_median(infile)
    Range = c1_data_range(infile);    #print(Range)
    Total_Entry = c1_total_ENTRY(infile); Total_Entry = int(Total_Entry); str_TE = str(Total_Entry)
    Mean = c1_mean(infile);  str_Mean = str(Mean)
    Var = c1_variance(infile);
    Std = c1_standard_deviation(infile); str_Std = str(Std)
    SSEM = c1_sample_standard_error_of_mean(infile); 
    shorten_SSEM = "%0.4f"%(SSEM)
    str_SSEM = str(shorten_SSEM)

    FROM = Range[0]; END = Range[1];  #print(BIN_NUM, FROM, END)
    Brange = (END-FROM)/BIN_NUM;
    RANGE = END-FROM
    t = np.arange(FROM-RANGE, END+RANGE, Brange) 
    gaussian = (1/(Std * np.sqrt(2 * np.pi))*np.exp(-(t-Mean)**2/(2 * Std**2)))
    sample_gaussian = (1/(SSEM * np.sqrt(2 * np.pi))*np.exp(-(t-Mean)**2/(2 * SSEM**2)))

    sample_inte = 0
    for i in range(len(sample_gaussian)):
        sample_inte = sample_inte + sample_gaussian[i]
#        print(sample_gaussian[i])
#    print(sample_inte)
    for i in range(len(sample_gaussian)):
        sample_gaussian[i] = sample_gaussian[i]/sample_inte
#        print(sample_gaussian[i])

    TJG = 0
    for i in range(len(gaussian)):
        TJG = TJG + gaussian[i]
    TJG = Total_Entry / TJG 
    for i in range(len(gaussian)):
        gaussian[i] = TJG * gaussian[i]

    str_Mean = str_Mean[:len(str_TE)+2]; #print(str_Mean)    
    str_Std = str_Std[:len(str_TE)+2]; #print(str_Std)

    X_AXIS = []
    X_WIDTH = []
    Y_VALUE = []

    f = open(infile,'r')
    BinN = 0
    for line in f:
        _,xaxis0,xaxis1, yaxis = line.split()
        X_AXIS.append(float(xaxis0) + (float(xaxis1)-float(xaxis0))/2)
        X_WIDTH.append((float(xaxis1)-float(xaxis0)))
        Y_VALUE.append(float(yaxis))
        BinN = BinN + 1
    
    WEIGHT = 1
    WEIGHT = float(Total_Entry)
    for i in range(len(gaussian)):
        gaussian[i] = gaussian[i]/Total_Entry
#            print("!!!",SCALE)
#            sample_gaussian[i] = sample_gaussian[i] / SCALE
#            print(sample_gaussian[i])
#            print(gaussian[i])

    if(norm==1):
        for i in range(len(sample_gaussian)):
            SCALE = sample_gaussian[i] / gaussian[i]
            sample_gaussian[i] = sample_gaussian[i] / SCALE *9/10
            
    MAX = 0; MAX_S = 0
    for i in range(len(gaussian)):
        if(MAX<gaussian[i]):
            MAX=gaussian[i]
        if(MAX_S<sample_gaussian[i]):
            MAX_S=sample_gaussian[i]
 

    for i in range(len(Y_VALUE)):
        Y_VALUE[i] = float(Y_VALUE[i])/WEIGHT


    plt.figure(1)
#    plt.plot(t,s2)
    plt.plot(t,gaussian)
    plt.plot(t,sample_gaussian)
    if(Show_sample==True):
        barlist = plt.bar(X_AXIS,Y_VALUE,X_WIDTH[0],fill=False)
        for i in range(len(barlist)):
            barlist[i].set_color('r')
    if(Show == False):
        plt.axis([X_AXIS[0],X_AXIS[BinN-1],0,Mode[2]*10/9/WEIGHT])
    else:
        plt.axis([X_AXIS[0],X_AXIS[BinN-1],0,MAX_S])
        MAX = MAX_S

    locs, labels = plt.xticks()
    TEXT = "Total Entry : " + str(Total_Entry) + "\n" + "POP Mean Est: " + str_Mean + "\n" + "POP Std Est: " + str_Std \
           + "\n" + "Sample Mean STD: " + str_SSEM
    if(Show == False): 
        plt.text(Range[1]-(Range[1]-Range[0])*0.05, Mode[2]*21/20/WEIGHT, TEXT, fontsize=16, ha='right', va='top', rotation=0)
    else:
        plt.text(Range[1]-(Range[1]-Range[0])*0.05, MAX_S*20/21, TEXT, fontsize=16, ha='right', va='top', rotation=0)

    one_sigma_left = "%0.3f"%(Mean-Std); one_sigma_left = str(one_sigma_left)
    one_sigma_right = "%0.3f"%(Mean+Std); one_sigma_right = str(one_sigma_right)
    two_sigma_left = "%0.3f"%(Mean-2*Std); two_sigma_left = str(two_sigma_left)
    two_sigma_right = "%0.3f"%(Mean+2*Std); two_sigma_right = str(two_sigma_right)
    plt.text(Mean-2*Std,0,"|",fontsize=8, ha='right', va='bottom', rotation=0, color='black')
    plt.text(Mean-2*Std,0,two_sigma_left,fontsize=7.5, ha='center', va='top', rotation=0, color='black')
    plt.text(Mean+2*Std,0,"|",fontsize=8, ha='right', va='bottom', rotation=0, color='black')
    plt.text(Mean+2*Std,0,two_sigma_right,fontsize=7.5, ha='center', va='top', rotation=0, color='black')
#    plt.text(Mean,0,r"$\mu \pm 2\sigma$",fontsize=20, ha='right', va='bottom', rotation=0, color='black')
 
    plt.text(Mean,0,"|",fontsize=10, ha='center', va='center', rotation=0, color='b')

    plt.text(Mean-Std,0,"|",fontsize=8, ha='right', va='bottom', rotation=0, color='black')
    plt.text(Mean-Std,0,one_sigma_left,fontsize=7.2, ha='center', va='top', rotation=0, color='black')
    plt.text(Mean+Std,0,"|",fontsize=8, ha='right', va='bottom', rotation=0, color='black')
    plt.text(Mean+Std,0,one_sigma_right,fontsize=7.2, ha='center', va='top', rotation=0, color='black')
    plt.text(Mean-Std,0,r"$\mu - \sigma$",fontsize=7, ha='right', va='bottom', rotation=0, color='black')

    sample_two_sigma_left = "%0.3f"%(Mean-2*SSEM); sample_two_sigma_left = str(sample_two_sigma_left)
    sample_two_sigma_right = "%0.3f"%(Mean+2*SSEM); sample_two_sigma_right = str(sample_two_sigma_right)
    plt.text(Mean-2*SSEM,0,"|",fontsize=13, ha='center', va='bottom', rotation=0, color='green')
    plt.text(Mean-2*SSEM,MAX/4,"$\overline{x}  - 2\sigma_x$", fontsize=18, ha='right', va='top', rotation=0, color='green')
    plt.text(Mean+2*SSEM,0,"|",fontsize=13, ha='center', va='bottom', rotation=0, color='green')
    plt.text(Mean+2*SSEM,MAX/4,"$\overline{x}  + 2\sigma_x$", fontsize=18, ha='left', va='top', rotation=0, color='green')
    plt.text(Mean-2*SSEM,0,sample_two_sigma_left,fontsize=7.5, ha='right', va='top', rotation=0, color='green')
    plt.text(Mean+2*SSEM,0,sample_two_sigma_right,fontsize=7.5, ha='left', va='top', rotation=0, color='green')

    plt.ylabel("Entry Number")
    if(Xaxis_Name == ''):
        XLABEL = filename_No_Txt.replace("_hist",'')
    else:
        XLABEL = Xaxis_Name
    plt.xlabel(XLABEL)
    plt.title(filename_No_Txt)
    SaveName = filename_No_Txt +"_Gaussian_normalized"+ ".pdf"
    plt.grid(True)
    plt.savefig(SaveName)
#    plt.show()
    plt.close('all')
    f.close()
    Ex_Num = (SIGMA*Std/exp_Mean_error)*(SIGMA*Std/exp_Mean_error)
    return_list = [float("%0.6f"%(Mean-SIGMA*SSEM)),float("%0.6f"%(Mean+SIGMA*SSEM)),Total_Entry,float("%0.3f"%(Ex_Num)),str(SIGMA)+" SIGMA",float("%0.6f"%(Mean)),float("%0.6f"%(SSEM)), exp_Mean_error]

    print("Careful!!!!")
    print("Event number better larger than 30 !!!!!")
    print("Current Event number is : ",Total_Entry)
    return return_list


def main():
    inputfile = "gaus100.txt"
#    inputfile = "/Users/leejunho/Desktop/git/python3Env/group_study/fruit_team/ROOT/Project/tranfer_test/data/soomin/LA_s/POS_NEG_PROP/execute_root/tea_0319Mon_LA_s_P_n_N_tree_cut_tea_0319Mon_LA_s_P_n_N_f_Pos_Neg_propotion_hist.txt"

#    Two_sigma_range = Fit_Sample_Gaus_histo(inputfile, ".X-axis.", SIGMA=2, Show_sample=True, Show = True)
    Two_sigma_range = Fit_Sample_Gaus_histo(inputfile,SIGMA=1.96, exp_Mean_error=0.1)
    print(Two_sigma_range)

if __name__ == "__main__":
    main()

