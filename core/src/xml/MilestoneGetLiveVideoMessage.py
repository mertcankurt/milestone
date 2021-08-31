#for optional fields this class can be modified
class MilestoneGetLiveVideoMessage:
    def __init__(self,width=0, height=0,compressionRate = 75, framerate = "full"):
        self.width = width
        self.height = height
        self.compressionRate = compressionRate
        self.framerate = framerate
    def getMessage(self):
        self.xml = "<?xml version='1.0' encoding='UTF-8'?><methodcall><requestid>1</requestid><methodname>live</methodname>"
        self.xml = self.xml + "<compressionrate>{}</compressionrate>".format(self.compressionRate)
        self.xml = self.xml + "<sendinitialimage>yes</sendinitialimage>"
        self.xml += "<attributes framerate='{}' />".format(self.framerate)
        if(self.width!=0 and self.height!=0):
            self.xml = self.xml + "<adaptivestreaming><resolution><widthhint>{}<widthhint/><heighthint>{}<heighthint/></resolution></adaptivestreaming>".format(self.width, self.height)
        self.xml = self.xml + "</methodcall>\r\n\r\n"
        return bytes(self.xml, "utf-8")
