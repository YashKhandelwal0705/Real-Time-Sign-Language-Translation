import cv2
from cvzone.HandTrackingModule import HandDetector
import numpy as np
import math

cap = cv2.VideoCapture(0)
detector = HandDetector(maxHands=1)

while True:
    success, img = cap.read()
    hands, img = detector.findHands(img)
    if hands:
        hand = hands[0]
        handtype = hand['type']
        x, y, w, h = hand['bbox']
    cv2.imshow("Image",img)
    cv2.waitKey(1)

