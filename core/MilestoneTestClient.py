from requests.sessions import Session
from zeep import Client
from zeep import transports
from zeep import cache
from zeep.transports import Transport
from zeep import Settings
from zeep.wsdl.definitions import Service
from zeep.cache import SqliteCache
from requests.auth import HTTPBasicAuth
from zeep.wsse.username import UsernameToken
import socket
from XMLManager import *
from SOAPManager import *
from LiveVideoProcessing import *
    
clientTCP = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
maxBufferSize = 8*1024

def main():
    IP = "192.168.1.34"
    PORT = 7563
    username = "aselsan"
    password = "Abc12345."

    SOAPENDPOINTURL = "https://"+ IP +"/ManagementServer/ServerCommandService.svc?wsdl"

    session = Session()
    session.verify = False
    session.auth = HTTPBasicAuth(username, password)
    settings = Settings(strict=False, xml_huge_tree=True)
    transport = Transport(session=session, timeout=50, cache = SqliteCache())
    client = Client(SOAPENDPOINTURL, settings=settings, transport=transport)

    loginToken = sendLoginTokenMessage(client)

    camera_GUID_List = sendGetConfigurationMessage(client, loginToken)

    clientTCP.connect((IP, PORT))

    sendConnectToCameraMessage(username, password, camera_GUID_List, loginToken, clientTCP)

    sendGetAlarmListMessage(clientTCP)

    sendGetLiveVideoMessage(clientTCP, maxBufferSize)

main()


