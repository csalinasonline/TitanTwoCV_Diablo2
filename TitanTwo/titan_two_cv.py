import os
import cv2

class GCVWorker:
    def __init__(self, width, height):
        os.chdir(os.path.dirname(__file__))
        self.gcvdata = bytearray([0x00])
    
    def __del__(self):
        del self.gcvdata
    
    def process(self, frame):
		position = (10,50)
		cv2.putText(
		frame, #numpy array on which text is written
		"Test", #text
		position, #position at which writing has to start
		cv2.FONT_HERSHEY_SIMPLEX, #font family
		1, #font size
		(209, 80, 0, 255), #font color
		3) #font stroke
        return (frame, None)
