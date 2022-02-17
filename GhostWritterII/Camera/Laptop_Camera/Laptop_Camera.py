import cv2
def cameraInit(camera_num):
    return cv2.VideoCapture(camera_num)

def get_frame(cap):
    _, frame = cap.read()
    return frame,None
def release(cap):
    cap.release()

