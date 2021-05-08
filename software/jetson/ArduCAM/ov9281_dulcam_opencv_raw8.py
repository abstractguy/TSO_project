import numpy as np
import cv2
import time
def fourcc(a, b, c, d):
    return ord(a) | (ord(b) << 8) | (ord(c) << 16) | (ord(d) << 24)

def pixelformat(string):
    if len(string) != 3 and len(string) != 4:
        msg = "{} is not a pixel format".format(string)
        raise argparse.ArgumentTypeError(msg)
    if len(string) == 3:
        return fourcc(string[0], string[1], string[2], ' ')
    else:
        return fourcc(string[0], string[1], string[2], string[3])
cap = cv2.VideoCapture(0,cv2.CAP_V4L2)
cap.set(cv2.CAP_PROP_FOURCC, pixelformat("GREY"))
cap.set(cv2.CAP_PROP_CONVERT_RGB,0)
now = time.time()
frame_num=0
while(True):
    if time.time() - now > 1:
        now = time.time()
        print(frame_num)
        frame_num=0
    else:
        frame_num = frame_num+1
    # Capture frame-by-frame
    ret, frame = cap.read()
    # Display the resulting frame
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
