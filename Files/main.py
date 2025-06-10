import cv2
import mediapipe as mp
import time

# Initialize webcam feed (0 for default camera)
cap = cv2.VideoCapture(0)

# Initialize MediaPipe Hands module
mpHands = mp.solutions.hands
hands = mpHands.Hands() # Default parameters for hand detection
mpDraw = mp.solutions.drawing_utils # Utility for drawing hand landmarks

pTime = 0 # Previous time
cTime = 0 # Current time

while True:
    # Read a frame from the webcam
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # Convert BGR image to RGB as required by MediaPipe
    # Process the RGB frame to detect hands
    results = hands.process(imgRGB)
    #print(results.multi_hand_landmarks)

    # Check if any hands were detected
    if results.multi_hand_landmarks:
        # Iterate over each detected hand
        for handLms in results.multi_hand_landmarks:
            # mpDraw.draw_landmarks(img, handLms) normal just points no lines on hands
            for id, lm, in enumerate(handLms.landmark): #Iterate over each landmark in the hand
                # h, w, c = img.shape
                # print(id, lm)
                h, w, c = img.shape #Getting image dimensions
                cx, cy = int(lm.x*w), int(lm.y*h) #Convert normalized landmark coordinates to pixel values
                print(id, cx, cy)  #Print landmark ID and coordinates
                if id == 0: # Highlight landmark ID 0 (wrist) with a filled circle
                # if id == 4:
                    cv2.circle(img, (cx, cy), 15, (255, 0, 255), cv2.FILLED)
            # Draw all landmarks and connections on the hand
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS) #for lining the hands
    
     # Calculate and display the frame rate (FPS)
    cTime = time.time() #will give us current time
    fps = 1/(cTime-pTime)# Compute FPS
    pTime = cTime # Update previous time

    # cv2.putText(img, str(int(fps)), (10,70), cv2.FONT_HERSHEY_SIMPLEX, 3, (255,0,255), 3) #different Fonts
    #cv2.putText(img, str(int(fps)), (10,70), cv2.FONT_HERSHEY_PLAIN, 3, (255,0,255), 3)
    cv2.putText(img, str(int(fps)), (10,70), cv2.FONT_HERSHEY_COMPLEX_SMALL, 3, (255,0,255), 3)
    # cv2.putText(img, str(int(fps)), (10,70), cv2.FONT_HERSHEY_DUPLEX, 3, (255,0,255), 3)

    cv2.imshow("Image", img) #Show the frame in a window
    
    cv2.waitKey(1) #Wait for 1ms and continue to next frame