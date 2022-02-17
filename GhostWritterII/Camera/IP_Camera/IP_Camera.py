import cv2
def cameraInit(ip):
    return cv2.VideoCapture(ip)

def get_frame(cap):
    _, frame = cap.read()
    return frame,None
def release(cap):
    cap.release()
