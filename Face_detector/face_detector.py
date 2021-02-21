import cv2

face_cascader = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

img = cv2.imread("news.jpg")

faces = face_cascader.detectMultiScale(img, scaleFactor=1.1,minNeighbors=5)

for x,y,w,h in faces:
    img_rectangle = cv2.rectangle(img, (x,y),(x+w, y+h), (0,255,0), 3)

cv2.imshow("Example", img)
cv2.waitKey(0)
cv2.destroyAllWindows()