import os
import pascal_voc_writer as pvw
import numpy as np
import cv2


img_dir=r"C:\Users\28399\Desktop\Data\Drive\Viva\HandDetection\detectiondata\train\pos"
txt_dir=r"C:\Users\28399\Desktop\Data\Drive\Viva\HandDetection\detectiondata\train\posGt"
output_dir=r"C:\Users\28399\Desktop\Data\Drive\Viva\HandDetection\detectiondata\train\XML"
for file in os.listdir(txt_dir):
    file_name=os.path.splitext(file)[0]
    img_file_path=img_dir+"\\"+file_name+".png"
    txt_file_path=txt_dir+"\\"+file_name+".txt"
    f_file=open(txt_file_path,'r')
    line_no=1
    for each_line in f_file:
        if line_no==2:
            content=each_line.split(' ',11)
            # print(content[1:5])
            # Get Bounding Box
            x_min=int(content[1])
            y_min=int(content[2])
            x_max=x_min+int(content[3])
            y_max=y_min+int(content[4])
            img=cv2.imread(img_file_path)
            sp = img.shape
            # print(x_max,y_max)
            # Writer(path, width, height)
            writer = pvw.Writer(img_file_path, sp[1], sp[0])
            # ::addObject(name, xmin, ymin, xmax, ymax)
            writer.addObject('Hand', x_min, y_min, x_max, y_max)
            # ::save(path)
            writer.save(output_dir+"\\"+file_name+".xml")
        line_no+=1





