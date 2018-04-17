import os
import cv2
import numpy as np


img_dir=r"C:\Users\28399\Desktop\Data\Drive\Viva\HandTracking\Train\test_positive\0000"
video_dir=r"C:\Users\28399\Desktop\Data\Drive\Viva\HandTracking\Train\Video\\"
video_name=r"train01.mp4"
(width,height)=(640,480)
video_path=video_dir+video_name
videoWriter = cv2.VideoWriter(video_path, cv2.VideoWriter_fourcc(*'MP4s'), 24, (width,height))
for file in os.listdir(img_dir):
    img_path=os.path.join(img_dir, file)
    img=np.resize(cv2.imread(img_path),(height,width,3))
    videoWriter.write(img)
videoWriter.release()