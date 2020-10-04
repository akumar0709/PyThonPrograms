import cv2

# 0 is id for our webcam
cap = cv2.VideoCapture("http://{Your:IP:ADDRESS}:8080/video")

# set is used to set size  3 = width 4 = height 10 = set briteness 
cap.set(3,640)
cap.set(4,480)
cap.set(10,100)
while True:
    # read() returns bool and img a
    success,img= cap.read()

    # To detect Edges canny image = all black with with white borders.
    # TO convert to Gray Scale 
    imggrey = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    # Functions to show image output
    cv2.imshow("MyImage",img)
    # press q from keyboard to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
          break