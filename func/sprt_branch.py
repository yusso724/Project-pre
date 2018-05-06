import sys

from d0_makelist import *
from d0_makelist_column import *

def show_branch(filename):
    RawList = MakeList(filename)
    RawList_c = MakeList_column(filename)

    for j in RawList[0]:
        print(j,"",end="")

    print("")

    #print("Please input branch name you want to extract")
    Branch  = input()
    List_c = []
    if Branch in RawList[0]:
        for q in range(len(RawList_c)):
            if Branch == RawList_c[q][0]:
                List_c = RawList_c[q]
    else:
        return show_branch(filename)

    print(List_c)

    FN = filename.replace(".txt", "C.txt")
    Of = open(FN, "w+")
    for i in range(len(List_c)):
        Of.write(str(List_c[i]))
        Of.write("\n")
        if i == len(List_c) - 1:
            break
    Of.close()
    return FN

show_branch("../data_txt/BEIJING_Aqi/Aqi_Beijing.txt")