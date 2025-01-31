import cv2
import os
from os.path import isfile, join
import matplotlib.pyplot as plt


#oncelikle indirdigimiz veri setindeki resimleri video halina getirelim.


pathIn = r"img1"
pathOut = "MOT17-13-SDP.mp4"

files = [f for f in os.listdir(pathIn) if isfile(join(pathIn,f))]

# img = cv2.imread(pathIn + "\\"+files[44])
# img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# plt.imshow(img)


#simdi resimlerimizi videoya cevirme kismina geldik.
fps = 25
#videomuzun fps degeri zaten aldigimiz kaynak sitede yaziyordu
size = (1920,1080)
#videomuzun botuyu da kaynak sitemizde yaziyor.
out = cv2.VideoWriter(pathOut, cv2.VideoWriter_fourcc(*"MP4V"), fps, size, True)

for i in files:
    print(i)
    
    filename = pathIn + "\\" + i
    
    img = cv2.imread(filename)
    
    out.write(img)

out.release()





























































