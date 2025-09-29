from flask import Flask, render_template, Response
from ultralytics import YOLO
from cvzone.HandTrackingModule import HandDetector
import cv2
import cvzone
import math
import time
import numpy as np


app = Flask(__name__)
cap = cv2.VideoCapture(0)

cap.set(3,640)
cap.set(4,480)

model = YOLO("runs/detect/train/weights/best.pt")

classNames = ["A", "F", "L", "Y"]
offset = 20
imgSize = 640
detector = HandDetector(maxHands=1)

def gen_frames():
    while True:
        success, img = cap.read()
        if not success:
            break
        else:
            hands, img = detector.findHands(img)
            listinfo = []
            if hands:
                hand = hands[0]
                x, y, w, h = hand['bbox']

                imgWhite = np.ones((imgSize, imgSize, 3),np.uint8)*255
                try:
                    imgCrop = img[y-offset:y+h+offset,x-offset:x+w+offset]
                    

                    aspectRatio = h/w
                    if aspectRatio>1:
                        k = imgSize/h
                        wCal = math.ceil(k*w)
                        imgResize = cv2.resize(imgCrop,(wCal,imgSize))
                        wGap = math.ceil((imgSize-wCal)/2)
                        imgWhite[:,wGap:wCal+wGap] = imgResize
                    else:
                        k = imgSize/w
                        hCal = math.ceil(k*h)
                        imgResize = cv2.resize(imgCrop,(imgSize,hCal))
                        hGap = math.ceil((imgSize-hCal)/2)
                        imgWhite[hGap:hGap+hCal,:] = imgResize
                    #cv2.imshow("ImageWhite", imgWhite)
                    results = model.predict(imgWhite, stream=True)
                    for r in results:
                        boxes = r.boxes
                        for box in boxes:
                            x1, y1, x2, y2 = map(int, box.xyxy[0])
                            w,h = x2-x1, y2-y1
                            cvzone.cornerRect(img, (x1,y1,w,h))
                            conf = math.ceil((box.conf[0]*100))/100
                            cls = int(box.cls[0])
                            if classNames[cls] == 'A':
                                color = (0, 255, 0)
                            elif classNames[cls] == 'F':
                                color = (255, 102, 0)
                            elif classNames[cls] == 'L':
                                color = (255, 0, 0)
                            else:
                                color = (255, 0, 255)

                            cvzone.cornerRect(img, (x1, y1, w, h),colorC=color,colorR=color)
                            cvzone.putTextRect(img, f'{classNames[cls].upper()} {int(conf*100)}%',
                                            (max(0, x1), max(35, y1)), scale=2, thickness=4,colorR=color,
                                            colorB=color)
                except cv2.error as e:
                    cv2.putText(img, "Going out of frame", (50, 50), cv2.FONT_HERSHEY_SIMPLEX,
                                1, (0, 0, 255), 2, cv2.LINE_AA)
                    print(f"Resize failed: {e}")
            else:
                cv2.putText(img, "No hand detected", (50, 50), cv2.FONT_HERSHEY_SIMPLEX,
                            1, (0, 0, 255), 2, cv2.LINE_AA)
            ret, buffer = cv2.imencode('.jpg', img)
            img = buffer.tobytes()
            yield(b'--img\r\n'
                  b'Content-Type: image/jpeg\r\n\r\n'+img+b'\r\n')


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=img')

if __name__ == "__main__":
    app.run(debug = True)
