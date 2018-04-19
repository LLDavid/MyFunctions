import xlrd
import os
import pandas as pd
import csv
import math
# xls path
xls_dir=r"C:\Users\lli40\Desktop\DrivingData\Video\04"
xls_name=r"e56d_CodingII.xls"
xls_path=xls_dir+"\\"+xls_name
# txt path
txt_dir=r"C:\Users\lli40\Desktop\DrivingData\Video\04"
txt_name=r"e56d_CodingII.txt"
txt_path=txt_dir+"\\"+txt_name
# img_dir
img_dir=r"C:\Users\lli40\Desktop\DrivingData\Video\04\014d387c-5afc-462e-a5d7-7681e31da417"
# read xls file
data=pd.read_table(xls_path)
data=data.values.tolist()
# open folder
folder = os.path.exists(txt_dir)
if not folder:
    os.makedirs(txt_dir)
txt_file=open(txt_path,"a+")
img_count=0;
#
for i in range(len(data)):
    if len(data[i])<4:
        del len[i]

for img_file in os.listdir(img_dir):
    img_count+=1
    if "jpg" in img_file:
        no_fame = int(img_file[:-4])
        act_index = -1
        action="Driving"
        print(img_file)
        for i in range(len(data)):
            j=i+1
            if i<len(data)-1:
                if math.isnan(data[i+1][2]):
                        j=j+1
                if math.isnan(data[i][2]) :
                    i=i-1
                if (int(data[i][2])<=no_fame) & (int(data[j][2])>=no_fame) & (data[i][0]==data[j][0]):
                    action=data[i][0]
                    print(action)
                    break
            else:
                break
        txt_file.write(img_file + "#" + str(action) + "\n")
        print(img_file + "#" + str(action))
print(img_count)
txt_file.close()