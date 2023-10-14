import cv2

video = cv2.VideoCapture('videos/pizza.mp4')

while True:
    suc, img = video.read()
    img = cv2.resize(img, (img.shape[1]//3, img.shape[0]//3))
    cv2.imshow('pizza', img)
    cv2.waitKey(30)

