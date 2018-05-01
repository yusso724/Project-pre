import sys
import os
import matplotlib.pyplot as plt

def man_py_scatter(filename):
    sys.path.append("../../func")
    from d0_makelist_column import MakeList_column

    if (filename[0] == "/"):
        filename = filename
    elif ((filename[0] == "C") & (filename[1] == ":")):
        filename = filename
    else:
        filename = os.getcwd() + "/" + filename  # get the path included filename
    loca = len(filename)
    for i in range(1, len(filename) + 1):  # find the "/" location
        if (filename[-i] == "/"):
            loca = i - 1
            break

    FILENAME = filename.replace(filename[:-loca], "")  # this is the shorten filename
    filename_No_Txt = FILENAME.replace(".txt", "")
    infile = filename

    list_c = MakeList_column(infile)
#date_list = list_c.pop(0)
#print(len(list_c))

    x = len(list_c)
    size = 150/len(list_c[0])
#print(len(list_c[0]),len(list_c[1]),len(list_c[2]))
    for i in range(1,x):
        y_list_int = []
        y_list = []
        y_list = list_c[i]
   #     print(list_c)
 #   print(y_list)
   # print(i)
    #print(y_list)
        y_label =  y_list[0]

        x_len = len(list_c)
        for k in range(1,len(y_list)):
      #  print(k)
            y_list_int.append(float(y_list[k]))

    #print(len(y_list_int))
        for j in range(i,x_len):
            x_list_int = []
            x_list = []
            x_list = list_c[j]
            x_label = x_list[0]
            for k in range(1,len(x_list)):
                x_list_int.append(float(x_list[k]))
            plt.scatter(x_list_int, y_list_int, s=size, c='black', marker='o', alpha=0.5, label='C1')
            plt.title(y_label+'_'+'basic scatter plot ')
            plt.xlabel(x_label)
            plt.ylabel(y_label)
            plt.savefig(x_label+'_'+y_label+'.pdf')
            plt.close('all')
  #      x_list_int.clear()
   #     x_list.clear()
   # y_list_int.clear()
   # y_list.clear()
def main():
    file1 = "Aqi_Beijing_Holi.txt"
    man_py_scatter(file1)
#print("over!",i,j,x,x_len)

'''
aqi = list_c[1]
list_c.pop(0)
print(list_c)
aqi.pop(0)
#print(aqi)

'''



if __name__=="__main__":
    main()

#range는 최소에서 0.05 최고에서 0.05