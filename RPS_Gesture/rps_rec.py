import cv2
import cvzone
import time
import random

from cvzone.HandTrackingModule import HandDetector

cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)

detector = HandDetector(maxHands=1)

timer = 0
stateResult = False
startGame = False
initialTime = 0
scores = [0,0]

while True:
    imgBG = cv2.imread("resources/layout.jpg")
    success, img = cap.read()
    
    imgScaled = cv2.resize(img,(0,0),None,0.392,0.392)
    imgScaled = imgScaled[:,75:525]
    
    hands, img = detector.findHands(imgScaled)
    
    if startGame:
        if not stateResult:
            timer = time.time() - initialTime
            cv2.putText(imgBG,str(int(timer)),(260,200),cv2.FONT_HERSHEY_PLAIN,4,(255,0,255),4)
            if timer>3:
                stateResult = True
                timer = 0        
        
                if hands:
                    playerMove = None
                    hand = hands[0]
                    fingers = detector.fingersUp(hand)   
                    if fingers == [1,1,1,1,1]:
                        playerMove = 'paper'
                    if fingers == [0,0,0,0,0]:
                        playerMove = 'rock'
                    if fingers == [0,1,1,0,0]:
                        playerMove = 'scissor'
                    
                    choices = ["paper.png", "rock.png", "scissor.png"]
                    random_img = random.choice(choices)
                    imgAI = cv2.imread(f"resources/{random_img}", cv2.IMREAD_UNCHANGED)
                    
                    if imgAI is None:
                        print(f"Error: Could not load image resources/{random_img}")
                        continue
                    
                    imgBG = cvzone.overlayPNG(imgBG, imgAI, (45, 110))

                    
                    #player wins
                    if (playerMove == 'paper' and random_img == 'rock.png') or\
                       (playerMove == 'rock' and random_img == 'scissor.png') or\
                       (playerMove == 'scissor' and random_img == 'paper.png'):
                        scores[1]+=1
                           
                    #AI wins
                    if (playerMove == 'rock' and random_img == 'paper.png') or\
                       (playerMove == 'scissor' and random_img == 'rock.png') or\
                       (playerMove == 'paper' and random_img == 'scissor.png'):
                        scores[0]+=1
                    
                    
                    print(f"Player: {playerMove}, AI: {random_img[:-4]}")
         
    imgBG[103:291,352:528] = imgScaled
    
    if stateResult:
        imgBG = cvzone.overlayPNG(imgBG, imgAI, (45, 110))
    
    cv2.putText(imgBG,str(scores[0]),(177,97),cv2.FONT_HERSHEY_PLAIN,2,(255,255,255),2)
    cv2.putText(imgBG,str(scores[1]),(492,97),cv2.FONT_HERSHEY_PLAIN,2,(255,255,255),2)
    
    
    #cv2.imshow("Image",img)
    cv2.imshow("layout",imgBG)
    #cv2.imshow("scaled", imgScaled)
    key = cv2.waitKey(1)
    if key == ord('s'):
        startGame = True
        initialTime = time.time()
        stateResult = False
