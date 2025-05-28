import cv2
from cvzone.HandTrackingModule import HandDetector
import numpy as np
import math

cap = cv2.VideoCapture(0)
detector = HandDetector(maxHands=1)

offset = 20
imgSize = 640
counter = 1722
folder = r"D:\Projects\SLT\New Dataset\Y"
class_id = 3

while True:
    success, img = cap.read()
    hands, img = detector.findHands(img)
    listinfo = []
    if hands:
        hand = hands[0]
        x, y, w, h = hand['bbox']

        imgWhite = np.ones((imgSize, imgSize, 3),np.uint8)*255
        imgCrop = img[y-offset:y+h+offset,x-offset:x+w+offset]
        

        aspectRatio = h/w
        if aspectRatio>1:
            k = imgSize/h
            wCal = math.ceil(k*w)
            imgResize = cv2.resize(imgCrop,(wCal,imgSize))
            wGap = math.ceil((imgSize-wCal)/2)
            imgWhite[:,wGap:wCal+wGap] = imgResize
            xWhite, yWhite, wWhite, hWhite = wGap, 0, wCal, imgSize
        else:
            k = imgSize/w
            hCal = math.ceil(k*h)
            imgResize = cv2.resize(imgCrop,(imgSize,hCal))
            hGap = math.ceil((imgSize-hCal)/2)
            imgWhite[hGap:hGap+hCal,:] = imgResize
            xWhite, yWhite, wWhite, hWhite = 0, hGap, imgSize, hCal
        listinfo.append(f"{class_id} {xWhite} {yWhite} {wWhite} {hWhite}")
        cv2.imshow("ImageCrop", imgCrop)
        cv2.imshow("ImageWhite",imgWhite)
    cv2.imshow("Image",img)
    key = cv2.waitKey(1)
    
    if key == ord("m"):
        counter+=1
        cv2.imwrite(f"{folder}/Y{counter}.jpg",imgWhite)
        if listinfo:
            with open(f"{folder}/Y{counter}.txt",'w') as label_file:
                label_file.writelines(listinfo)
        print(f"Image and Lebel File Y{counter} saved successfully")


