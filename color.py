#importing modules

import cv2   
import sys
import numpy as np


#capturing video through webcam
cap=cv2.VideoCapture('clr test.wmv')
countg=0
countb=0
countw=0
county=0
countr=0
counto=0
countp=0
countbl=0
output=open('ColorReport.txt','w')
while(1):
    _, img = cap.read()
	    
	#converting frame(img i.e BGR) to HSV (hue-saturation-value)

    hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

	#definig the range of red color
    red_lower=np.array([136,87,111],np.uint8)
    red_upper=np.array([180,255,255],np.uint8)

	#defining the Range of Blue color
    blue_lower=np.array([99,115,150],np.uint8)
    blue_upper=np.array([110,255,255],np.uint8)
	
	#defining the Range of yellow color
    yellow_lower=np.array([22,60,200],np.uint8)
    yellow_upper=np.array([60,255,255],np.uint8)
    
    green_lower=np.array([65,60,60],np.uint8)
    green_upper=np.array([80,255,255],np.uint8)
    
    orange_lower=np.array([10,100,20],np.uint8)
    orange_upper=np.array([25,255,255],np.uint8)
    brown_lower=np.array([20,100,100],np.uint8)
    brown_upper=np.array([30,255,255],np.uint8)
    
    
    #white_lower=np.array([0,0,0],np.uint8)
    #white_upper=np.array([0,0,255],np.uint8)
    
    black_lower=np.array([0,0,0],np.uint8)
    black_upper=np.array([0,0,0],np.uint8)

	#finding the range of red,blue and yellow color in the image
    red=cv2.inRange(hsv, red_lower, red_upper)
    blue=cv2.inRange(hsv,blue_lower,blue_upper)
    yellow=cv2.inRange(hsv,yellow_lower,yellow_upper)
    green=cv2.inRange(hsv,green_lower,green_upper)
    brown=cv2.inRange(hsv, brown_lower, brown_upper)
    orange=cv2.inRange(hsv,orange_lower,orange_upper)
    #white=cv2.inRange(hsv,white_lower,white_upper)
    black=cv2.inRange(hsv,black_lower,black_upper)

	
	#Morphological transformation, Dilation  	
    kernal = np.ones((5 ,5), "uint8")
    
    red=cv2.dilate(red,kernal)
    res=cv2.bitwise_and(img, img, mask = blue)
    blue=cv2.dilate(blue,kernal)
    res1=cv2.bitwise_and(img, img, mask = blue)

    yellow=cv2.dilate(yellow,kernal)
    res2=cv2.bitwise_and(img, img, mask = yellow)
    green=cv2.dilate(green,kernal)
    res3=cv2.bitwise_and(img, img, mask = green)
    
    
    brown=cv2.dilate(brown,kernal)
    res4=cv2.bitwise_and(img, img, mask = brown)

    #white=cv2.dilate(white,kernal)
    #res4=cv2.bitwise_and(img, img, mask = white)

    orange=cv2.dilate(orange,kernal)
    res5=cv2.bitwise_and(img, img, mask = orange)    
    
    black=cv2.dilate(black,kernal)
    res6=cv2.bitwise_and(img, img, mask = black)


	#Tracking the Red Color
    contours,hierarchy=cv2.findContours(red,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
	
    for pic, contour in enumerate(contours):
        
        area = cv2.contourArea(contour)
        if(area>300):
			
            x,y,w,h = cv2.boundingRect(contour)	
        
           
            img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
            cv2.putText(img,"RED color",(x,y),cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,255))
        countr+=1
	#Tracking the Blue Color
    contours,hierarchy=cv2.findContours(blue,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if(area>300):
            x,y,w,h = cv2.boundingRect(contour)	
            img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
            cv2.putText(img,"Blue color",(x,y),cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,0,0))
        countb+=1
	#Tracking the yellow Color
    contours,hierarchy=cv2.findContours(yellow,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if(area>300):
            x,y,w,h = cv2.boundingRect(contour)	
            img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
            cv2.putText(img,"yellow  color",(x,y),cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0,255,0)) 
        county+=1
    contours,hierarchy=cv2.findContours(green,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if(area>300):
            x,y,w,h = cv2.boundingRect(contour)	
        
            
            img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
            cv2.putText(img,"green  color",(x,y),cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0,0,255))
        countg+=1
        
    contours,hierarchy=cv2.findContours(orange,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if(area>3000):
            x,y,w,h = cv2.boundingRect(contour)	
            img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
            cv2.putText(img,"orange  color",(x,y),cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0,0,255))
        counto+=1
        
    contours,hierarchy=cv2.findContours(black,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if(area>300):
            x,y,w,h = cv2.boundingRect(contour)	
            img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
            cv2.putText(img,"black  color",(x,y),cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0,0,255))
        countbl+=1
        
    
        
    contours,hierarchy=cv2.findContours(brown,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if(area>300):
            x,y,w,h = cv2.boundingRect(contour)	
            img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
            cv2.putText(img,"brown  color",(x,y),cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0,0,255))
        countp+=1
            
    #contours,hierarchy=cv2.findContours(white,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    #for pic, contour in enumerate(contours):
     #   area = cv2.contourArea(contour)
      #  if(area>3000):
         #   x,y,w,h = cv2.boundingRect(contour)	
          #  img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
           # cv2.putText(img,"white color",(x,y),cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0,255,0))
        #countw+=1
    #cv2.imshow("Redcolour",red)
    cv2.imshow("Color Tracking",img)
    #cv2.imshow("red",res) 	
    if cv2.waitKey(10) & 0xFF == ord('q'):
    	cap.release()
    	cv2.destroyAllWindows()
    	break  
if countg>countr and countg>countb and countg>countw and countg>county and countg>counto and countg>countp and countg>countbl:
    print('green')
    output.write('Color with the highest occurance is GREEN')
elif countr>countg and countr>countb and countr>countw and countr>county and countr>counto and countr>countp and countr>countbl:
    print('red')
    output.write('Color with the highest occurance is RED')
elif countb>countg and countb>countr and countb>countw and countb>county and countb>counto and countb>countp and countb>countbl :
    print('blue')
    output.write('Color with the highest occurance is BLUE')
elif countw>countg and countw>countr and countw>countb and countw>county and countw>counto and countw>countp and countw>countbl:
    print('white')
    output.write('Color with the highest occurance is WHITE')
elif county>countg and county>countr and county>countb and county>countw and county>counto and county>countp and county>countbl:
    print('yellow')
    output.write('Color with the highest occurance is YELLOW')
elif counto>countg and counto>countr and counto>countb and counto>countw and counto>county and counto>countp and counto>countbl:
    print('orange')
    output.write('Color with the highest occurance is ORANGE')
else:
    print('black')
output.close()

    
    