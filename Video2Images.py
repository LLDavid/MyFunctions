import cv2
import numpy as np
import os

video_dir=r"C:\Users\28399\Desktop\Data\Drive\sub01"
video_name=r"138e6236-2ec2-4ac4-a36d-dc9c5e0e9a73.mp4"
video_path=video_dir+"\\"+video_name
image_dir=video_dir+"\\"+video_name[:-4]
folder = os.path.exists(image_dir)
if not folder:
    os.makedirs(image_dir)
cap = cv2.VideoCapture(video_path)
# cap.set(1,start_frame)
print(cap.isOpened())
fps = cap.get(5)
(width, height) = (int(cap.get(3)),int(cap.get(4)))
# (width, height)=(720,480)
print(fps)
now_frame=0
success = True
while success:
    now_frame += 1
    image = cap.read()
    if now_frame % 5 ==0:
        print("the " + str(now_frame) + "th frame\n")
        image_np = np.array(image[1]).astype(np.uint8)
        w_output=cv2.imwrite(image_dir+"\\"+str(now_frame)+".jpg",image_np)
        if not w_output:
            print("imwrite failed\n")
            break
cap.release()
