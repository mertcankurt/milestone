def sendLoginTokenMessage(client):
    #Logging in and getting login token from SOAP ServerCommandService 
    loginTokenMessage = client.service["Login"]("BE07504F-B330-4475-9AE4-1A7FF10BD486")
    loginToken = loginTokenMessage["Token"]
    print("Received Login TOKEN = " + loginToken)
    print()
    return loginToken

def sendGetConfigurationMessage(client, loginToken):
    #Getting Camera List from SOAP ServerCommandService 
    getConfigurationMessage = client.service["GetConfiguration"](loginToken)
    camera_GUID_List = getConfigurationMessage["CameraGroups"]["CameraGroupInfo"][0]["Cameras"]["guid"]
    print("Avaliable Camera Guids:", camera_GUID_List)
    print()
    return camera_GUID_List