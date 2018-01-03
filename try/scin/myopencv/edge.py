from cv2 import *

img = imread(r"C:\Users\heyulin\Desktop\07c1b01c507a1f61aa47fc6fba177498_zuizuizuizui.jpg") 

gray = cvtColor(img,COLOR_BGRA2BGR)
blur_gray = blur(gray,(8,8))
can_gray = Canny(blur_gray,3,9,3)
imshow('ssg',can_gray)
waitKey(0)