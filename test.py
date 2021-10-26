import numpy as np
from PIL import ImageGrab
from numpy.core.fromnumeric import size
import cv2
import time
from directkeys import PressKey , W , S , A , D , ReleaseKey
#countdown
for i in list(range(4))[::-1]:
    print(i+1)
    time.sleep(1)

last_time = time.time()


def process_img(original_img):
    processed_img = cv2.cvtColor(original_img , cv2.COLOR_BGR2GRAY)
    processed_img = cv2.Canny(processed_img , threshold1=200 , threshold2=300)
    return processed_img
    

#importing frames from game running in top left corner
while 1:
    screen = np.array(ImageGrab.grab(bbox=(0,40,800,640)))
    new_screen = process_img(screen)
    # printscreen_numpy = np.array(printscreen_pil.getdata() , dtype = 'uint8' ).reshape((printscreen_pil.size[1] , printscreen_pil.size[0] , 3))
    print('down')
    PressKey(W)
    
    ReleaseKey(W)
    print('up')
    print("Loop took {} seconds" , format(time.time() - last_time))
    last_time = time.time()
    cv2.imshow('window' , new_screen)
    # cv2.imshow('window' , cv2.cvtColor(np.array(screen) , cv2.COLOR_BGR2RGB))
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break


