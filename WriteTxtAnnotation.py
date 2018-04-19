import cv2
import os
import numpy as np

img_dir=r"C:\Users\lli40\Desktop\DrivingData\Video\03\f2d5f586-5875-4e91-a958-aac16612975d"
txt_dir=r"C:\Users\lli40\Desktop\DrivingData\Video\03\1580473d-4bc2-4e24-b17e-69029fdf5294\Annotation"


index_list=[[]]*5
index_list[0]=[range(2059,2176),range(9810,9930),range(15554,15652),range(20505,21897)]# Marker
index_list[1]=[range(1391,1543),range(5045,5233),range(8162,8354),range(11271,11471),
               range(24078,24262)]# Touchscreen
index_list[2]=[range(3597,3965),range(8920,9279),range(12726,15119),range(16171,17087)]# Phone
index_list[3]=[range(2709,3029),range(7379,7565),range(10510,10691),range(12018,12189),range(19816,19991),
               range(23379,23551)]# Drink
index_list[4]=[range(5811,6862),range(17202,19350),range(22428,22707),range(24904,25161)]# Texting
folder = os.path.exists(txt_dir)
if not folder:
    os.makedirs(txt_dir)
txt_file=open(txt_dir+"\\"+"annotation.txt","a+")
img_count=0;
for img_file in os.listdir(img_dir):
    img_count+=1
    print(img_file)
    if "jpg" in img_file:
        no_fame=int(img_file[:-4])
        act_index=-1
        for i in range(5):
            for j in range(len(index_list[i])):
                if no_fame in list(index_list[i][j]):
                    act_index = i
    txt_file.write(img_file+"#"+str(act_index+1)+"\n")
print(img_count)
txt_file.close()


