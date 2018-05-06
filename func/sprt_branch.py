import sys

from d0_makelist import *
from d0_makelist_column import *

def show_branch(filename1):
    if(filename1[0]=="/"):
        filename1 = filename1
    elif((filename1[0]=="C")&(filename1[1]==":")):
        filename1 = filename1
    else:
        filename1 = os.getcwd() + "/" + filename1   # get the path included filename
    loca1=len(filename1)
    for i in range (1,len(filename1)+1):       # find the "/" location
        if(filename1[-i] == "/"):
            loca1 = i-1
            break
    FILENAME1 = filename1.replace(filename1[:-loca1],"")   # this is the shorten filename
    filename1_No_Txt = FILENAME1.replace(".txt","")
    infile1 = filename1
    print(infile1)

    RawList = MakeList(infile1)
    RawList_c = MakeList_column(infile1)

#    for j in RawList[0]:
#        print(j,"",end="")

#    print("")

    #print("Please input branch name you want to extract")
    Branch  = input()
    List_c = []
    if Branch in RawList[0]:
        for q in range(len(RawList_c)):
            if Branch == RawList_c[q][0]:
                List_c = RawList_c[q]
    else:
        return show_branch(infile1)

    print(List_c)

    FN = infile1.replace(".txt", "_picked.txt")
    Of = open(FN, "w+")
    for i in range(len(List_c)):
        Of.write(str(List_c[i]))
        Of.write("\n")
        if i == len(List_c) - 1:
            break
    Of.close()
    return FN

def main():
    infile = "../data_txt/BEIJING_Aqi/Aqi_Beijing_Holi.txt"
    outfile = show_branch(infile)
    print(outfile)

if __name__=="__main__":
    main()
#show_branch("../data_txt/BEIJING_Aqi/Aqi_Beijing.txt")
