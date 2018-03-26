from c1_basic_statistic import c1_data_range, c1_median, most_frequent_bin
from c1_basic_statistic import c1_total_ENTRY, c1_mean, c1_variance, c1_standard_deviation

Input_file = "../data_txt/root3_project.txt"

MODE = most_frequent_bin(Input_file);      print("MODE :",MODE)
DATA_RANGE = c1_data_range(Input_file);    print("DATA_RANGE :",DATA_RANGE)
MEDIAN = c1_median(Input_file);            print("MEDIAN :",MEDIAN)
Total_ENTRY = c1_total_ENTRY(Input_file);  print("Total_ENTRY :",Total_ENTRY)
MEAN = c1_mean(Input_file);                print("MEAN :",MEAN)
VARIANCE = c1_variance(Input_file);        print("VARIANCE :",VARIANCE)
STD = c1_standard_deviation(Input_file);   print("STD :",STD)


