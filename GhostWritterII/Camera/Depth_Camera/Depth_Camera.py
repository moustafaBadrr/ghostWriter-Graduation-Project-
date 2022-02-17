
from Camera.Depth_Camera import realsense_depth as rs
def cameraInit(_):
    return rs.DepthCamera()

def get_frame(cap):
    ret, depth_frame, frame = cap.get_frame()
    return frame,depth_frame
def release(cap):
    cap.release()

