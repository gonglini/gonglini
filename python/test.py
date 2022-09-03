import youtube_dl
import pafy
import cv2
import numpy as np
import keyboard



url = 'https://www.youtube.com/watch?v=G2wySVKCkA0'
video = pafy.new(url)
best = video.getbest(preftype = 'mp4')

cap = cv2.VideoCapture(best.url)

ym_per_pix = 30 / 720
xm_per_pix = 3.7 / 720

frame_size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out1 = cv2.VideoWriter('C:\\Users\\bit\\Desktop\\opencv_youtube.mp4', fourcc, 20.0, frame_size)

def wrapping(image):
    (h, w) = (image.shape[0], image.shape[1])

    source = np.float32([[w // 2 - 30, h * 0.53], [w // 2 + 60, h * 0.53], [w * 0.3, h], [w, h]])
    destination = np.float32([[0, 0], [w-350, 0], [400, h], [w-150, h]])
    transform_matrix = cv2.getPerspectiveTransform(source, destination)
    minv = cv2.getPerspectiveTransform(destination, source)
    _image = cv2.warpPerspective(image, transform_matrix, (w, h))

    return _image, minv
    
def color_filter(image):
    hls = cv2.cvtColor(image, cv2.COLOR_BGR2HLS)

    lower = np.array([20, 150, 20])
    upper = np.array([255, 255, 255])

    yellow_lower = np.array([0, 85, 81])
    yellow_upper = np.array([190, 255, 255])

    yellow_mask = cv2.inRange(hls, yellow_lower, yellow_upper)
    white_mask = cv2.inRange(hls, lower, upper)
    mask = cv2.bitwise_or(yellow_mask, white_mask)
    masked = cv2.bitwise_and(image, image, mask = mask)

    return masked
    
while True:
    retval, image = cap.read()
    if not retval:
        break
        
    wrapped_image, minverse = wrapping(image)
    cv2.imshow('video', image)
    cv2.imshow('wrapped', wrapped_image)

    #w_f_image = color_filter(image)
    #cv2.imshow('w_f_img', w_f_image)

    key = cv2.waitKey(35)
    if key == 27:
        break

  


    


if cap.isOpened():
    cap.release()
cv2.destroyAllWindows()
    
    

    
