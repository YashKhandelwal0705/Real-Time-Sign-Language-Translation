import os
import cv2

input_dir = "D:/Projects/SLT/New Dataset/Y - Copy"
floatingPoint = 6

files = [f for f in os.listdir(input_dir) if f.lower().endswith(".jpg")]
for f in files:
    img_path = os.path.join(input_dir,f)
    label_file_name = f.split(".")[0]+".txt"
    label_path = os.path.join(input_dir, label_file_name)
    img = cv2.imread(img_path)
    imgH, imgW, channel = img.shape
    label_file = open(label_path,'r')
    list_info = label_file.readline().split(" ")
    if(len(list_info)==5):
        _,x,y,w,h = list_info[0], float(list_info[1]), float(list_info[2]), float(list_info[3]), float(list_info[4])
        label_file.close()
        #To avoid values <0
        x = max(x,0)
        y = max(y,0)
        w = max(w,0)
        h = max(h,0)
        xcenter, ycenter = x+w/2, y+h/2
        xnorm, ynorm = round(xcenter/imgW,floatingPoint), round(ycenter/imgH, floatingPoint)
        wnorm, hnorm = round(w/imgW,floatingPoint), round(h/imgH, floatingPoint)

        #To avoid values >1
        xnorm=min(xnorm,1)
        ynorm=min(ynorm,1)
        hnorm=min(hnorm,1)
        wnorm=min(wnorm,1)
        list_info = list(f"{_} {xnorm} {ynorm} {wnorm} {hnorm}")
        label_file = open(label_path,'w')
        label_file.writelines(list_info)
        label_file.close()
        print(f"Normalised {label_file_name}")
