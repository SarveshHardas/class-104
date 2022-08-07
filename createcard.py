import cv2

img = cv2.imread("F:\game\Python\class activity\class 104\assets\poster.jpg")
rocket = img[120:360,400:500]
img[0:240,500:600] = rocket

text_show = "I love coding at Whitehat jr."
cv2.putText(img,text_show,(20,220),fontFace=cv2.FONT_HARSHEY_COMPLEX_SMALL,fontScale = 1,color=(0,0,255))

cv2.imshow("Output",img)
cv2.waitkey(0)