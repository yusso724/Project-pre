import sys
sys.path.append("/home/soomin/Desktop/group_study/Project-pre/func")

from d0_makelist_column import MakeList_column

#infile1 = "test1.txt"
#infile2 = "test2.txt"

def ROW_COL(infile1, infile2):
    COL_LIST1 = MakeList_column(infile1)
    COL_LIST2 = MakeList_column(infile2)
    COL_LIST1.append(COL_LIST2[1])
    COL_LIST3=COL_LIST1

    print(COL_LIST3)

    COL_LIST4=[]

    for k in range(len(COL_LIST3[0])):
        gg=[]
        for m in range(len(COL_LIST3)):
            gg.append(COL_LIST3[m][k])

        COL_LIST4.append(gg)
    print(COL_LIST4)


    Of = open("test_out.txt","w+")
    for i in range(len(COL_LIST4)):
        for j in range(len(COL_LIST4[i])):
            Of.write("%s" %COL_LIST4[i][j])
            if(j!=len(COL_LIST4[i])-1):
                Of.write(" ")
            if(j==len(COL_LIST4[i])-1):
                Of.write("\n")
    Of.close()
    return Of


def main():
    INFILE1 = "test1.txt"
    INFILE2 = "test2.txt"
    ROW_COL(INFILE1, INFILE2)


if __name__=="__main__":
    main()


