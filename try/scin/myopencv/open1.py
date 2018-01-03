from cv2 import *

img = imread(r"C:\Users\heyulin\Desktop\07c1b01c507a1f61aa47fc6fba177498_zuizuizuizui.jpg") 
# img =cv2.imread(r'http://file.epubit.com.cn/ScreenShow/170679fc9cb8ead53c8d')
ele = getStructuringElement(MORPH_RECT,(4,4))
dstimg = erode(img,ele)
blurimg = blur(img,(4,4))
namedWindow('Image')
namedWindow('Image_erod')
namedWindow('Image_blur')
imshow('Image_erod',dstimg)
imshow('Image',img)
imshow('Image_blur',blurimg)
waitKey(0)