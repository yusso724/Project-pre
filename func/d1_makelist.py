import math

# Need to input RAW DATA!!!
def MakeList(filename):
    print("test")
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

    ff = open(infile,"r")
    FILE_LIST = []
    for line in ff:
        FILE_LIST.append(line.split())
    ff.close()
    return FILE_LIST


def main():
    inputfile = "/Users/leejunho/Desktop/git/python3Env/group_study/project_pre/data_txt/BEIJING_Aqi/Aqi_Beijing_day.txt"
    con_list = MakeList(inputfile)
    print(con_list)

if __name__=="__main__":
    main()






