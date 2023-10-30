# 2 hand working code(with video release)
import cv2
from cvzone.HandTrackingModule import HandDetector
from pyautogui import press
from time import sleep

detector = HandDetector(maxHands=2, detectionCon=0.7)

video = cv2.VideoCapture(0)

while True:
    video = cv2.VideoCapture(0)
    ret, img = video.read()
    video.release()
    img = cv2.flip(img, 1)
    hand = detector.findHands(img, draw=False)
    if len(hand)==2:
        lmlist = hand[0]
        lmlist1=hand[1]
        if lmlist['type']=='Left':
            fingerup2=detector.fingersUp(lmlist)
            fingerup1=detector.fingersUp(lmlist1)
        else:
            fingerup2=detector.fingersUp(lmlist1)
            fingerup1=detector.fingersUp(lmlist)
        
       

        if lmlist:
            fingerup=fingerup2+fingerup1
#             print(fingerup)
            
        
            match fingerup:
             
                case [0, 1, 0, 0, 0, 0, 0, 0, 0, 0]: 
                    press('1')
                    cv2.waitKey(200)
                    
                case [0, 1, 1, 0, 0, 0, 0, 0, 0, 0]:
                    press('2')
                    cv2.waitKey(200)
                case [0, 1, 1, 1, 0, 0, 0, 0, 0, 0]:
                    press('3')
                    cv2.waitKey(200)
                case [0, 1, 1, 1, 1, 0, 0, 0, 0, 0]:
                    press('4')
                    cv2.waitKey(200)
                case [1, 1, 1, 1, 1, 0, 0, 0, 0, 0]:
                    press('5')
                    cv2.waitKey(200)
                case [1, 1, 1, 1, 1, 0, 1, 0, 0, 0]:
                    press('6')
                    cv2.waitKey(200)
                case [1, 1, 1, 1, 1, 0, 1, 1, 0, 0]:
                    press('7')
                    cv2.waitKey(200)
                case [1, 1, 1, 1, 1, 0, 1, 1, 1, 0]:
                    press('8')
                    cv2.waitKey(200)
                case [1, 1, 1, 1, 1, 0, 1, 1, 1, 1]:
                    press('9')
                    cv2.waitKey(200)
                case [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]:
                    press('0')
                    cv2.waitKey(200)
                case [0, 0, 0, 0, 0, 0, 1, 1, 0, 0]:
                    break
                   
        

          
video.release()
cv2.destroyAllWindows()
