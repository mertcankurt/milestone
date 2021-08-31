from src.videoprocess.LiveVideoHeaderParser import *
import cv2
import numpy as np

def process_Video(clientTCP, liveVideoFrameQueue, maxBufferSize):
    while True:
        frame = bytearray()
        frameSize = 0
        img = clientTCP.recv(maxBufferSize)
        milestoneImageMessageStartIndex = img.find(b"Image")
        imageLen = len(img)
        if(milestoneImageMessageStartIndex != -1):
            imageHeaderEndIndex = img.index(b"\r\n\r\n\xff\xd8") + 4
            imageHeader = ParseLiveVideoHeader(img[milestoneImageMessageStartIndex:imageHeaderEndIndex])
            imageBufferSize = int(imageHeader["content-length"])
            # print("IMAGE SIZE: " + str(imageBufferSize))
            frame += (img[imageHeaderEndIndex:])
            frameSize = imageBufferSize
            frameSize -= len(img[imageHeaderEndIndex:])
            while(frameSize != 0):
                img = clientTCP.recv(maxBufferSize)
                if(frameSize >= len(img)):
                    frame += img
                    frameSize -= len(img)
                else:
                    frame += img[:frameSize]
                    frameSize -= len(img[:frameSize])
                    # print("FRAME SIZE: " + str(len(frame)))
                    liveVideoFrameQueue.put(frame)
        # else:
            # print("WE MIGHT HAVE A PROBLEM")
            # milestoneStatusStartIndex = img.find(b"<")
            # milestoneImageStartIndex = img.find(b"\xff\xd8")
            # imageEndIndex = img.find(b"\xff\xd9")
            # print("ImageStartIndex: " + str(milestoneImageStartIndex))
            # print("ImageEndIndex: " + str(milestoneImageStartIndex))


def imshow_threaded(img_queue, cv_flag):
    print("================================= inside the imshow thread")
    while True:
        img = img_queue.get()
        inp = np.asarray(img, dtype=np.uint8)
        i0 = cv2.imdecode(inp, cv2.IMREAD_UNCHANGED)
        cv2.imshow('Decoded with OPENCV', i0)
        if (cv2.waitKey(1) & 0xFF == ord('q')) and cv_flag:
            print("CLOSING THE IMSHOW")
            cv2.destroyAllWindows()
            break

    cv2.destroyAllWindows()
    

    

    
