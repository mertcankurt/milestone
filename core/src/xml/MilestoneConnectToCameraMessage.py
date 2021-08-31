class MilestoneConnectToCameraMessage:
    def __init__(self, username, password, camera_guid, token):
        self.cam_guid = camera_guid
        self.token = token
        self.username = username
        self.password = password

    def getMessage(self):
        self.xml = "<?xml version='1.0' encoding='UTF-8'?><methodcall><requestid>1</requestid><methodname>connect</methodname>"
        self.xml = self.xml + "<username>{}</username><password>{}</password>".format(self.username, self.password)
        self.xml = self.xml + "<cameraid>{}</cameraid>".format(self.cam_guid)
        self.xml = self.xml + "<alwaysstdjpeg>yes</alwaysstdjpeg>"
        self.xml += "<transcode><allframes>yes</allframes></transcode>"
        self.xml = self.xml + "<connectparam>id={}&amp;connectiontoken={}</connectparam>".format( self.cam_guid, self.token)
        self.xml = self.xml + "</methodcall>\r\n\r\n"
        return bytes(self.xml,"utf-8")
