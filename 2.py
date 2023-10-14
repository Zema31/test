import cv2

img = cv2.imread('images/cat5.jpg')
#img = cv2.resize(img, (img.shape[1]//3, img.shape[0]//3))

low_red = (17,50,110)
high_red = (101,140,180)
only_cat = cv2.inRange(img, low_red, high_red)

cat_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV) #Преобразуем в HSV
cat_color_low = (7,40,60) #Данный цвет это темный ненасыщенный красный, близкий к бордовому
cat_color_high = (18,255,200) #Данный цвет это светлый насыщенный оранджевый
only_cat_hsv = cv2.inRange(cat_hsv, cat_color_low, cat_color_high)

moments = cv2.moments(only_cat_hsv, 1) # получим моменты
x_moment = moments['m01']
y_moment = moments['m10']
area = moments['m00']
x = int(x_moment / area) # Получим координаты x,y кота
y = int(y_moment / area) # и выведем текст на изображение
cv2.putText(img, "Cat!", (x,y), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2)

cv2.imshow('cat_found', img)
cv2.imshow('cat_color_hsv', only_cat_hsv)
cv2.imshow('only car', only_cat)
cv2.waitKey(0)