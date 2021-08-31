import queue
import threading
from src.videoprocess.LiveVideoProcessing import *
import time
from src.videoprocess.flaskvideoserver import *
from src.xml.MilestoneConnectToCameraMessage import MilestoneConnectToCameraMessage
from src.xml.MilestoneGetAlarmListMessage import MilestoneGetAlarmListMessage
from src.xml.MilestoneGetLiveVideoMessage import MilestoneGetLiveVideoMessage
from src.xml.MilestoneStopVideoMessage import MilestoneStopVideoMessage

def sendConnectToCameraMessage(username, password, camera_GUID_List, loginToken, clientTCP):
    #Connect to a Camera
    image_msg = MilestoneConnectToCameraMessage(username, password, camera_GUID_List[0], loginToken)
    imageServer_connect = image_msg.getMessage()
    # print("[INFO] Connection Request:", imageServer_connect)
    # print()
    clientTCP.send(imageServer_connect)
    data = clientTCP.recv(4096).decode("utf-8")
    print("[INFO] Connection Response:", data)

def sendGetAlarmListMessage(clientTCP):
    # get alarms list
    alarmList = MilestoneGetAlarmListMessage(round(time.time()*1000), 86400000, 16)
    alarmListMessage = alarmList.getMessage()
    # print("[INFO] Alarm List Request message:", alarmListMessage)
    # print()
    clientTCP.send(alarmListMessage)
    alarmListResponse = clientTCP.recv(1024*8).decode("utf-8")
    print("[INFO] Alarm List Response Recieved...")
    # print("Alarm List:", alarmListResponse)
    # print()

def sendGetLiveVideoMessage(clientTCP, maxBufferSize):
    # Getting Live Video From ImageServer
    live = MilestoneGetLiveVideoMessage()
    getLiveVideoMessage = live.getMessage()
    print("[INFO] Live Video Request:", getLiveVideoMessage)
    clientTCP.send(getLiveVideoMessage)

    liveVideoFrameQueue = queue.Queue()

    # threading.Thread(target=imshow_threaded, args=[liveVideoFrameQueue,True]).start()
    threading.Thread(target=process_Video, args=[clientTCP, liveVideoFrameQueue, maxBufferSize]).start()

    app = FlaskVideoServer(liveVideoFrameQueue).getFlaskApp()
    app.run(host='localhost',port=9000 , threaded=True, debug=False)

