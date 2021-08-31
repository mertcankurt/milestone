class MilestoneGetAlarmListMessage:
    def __init__(self, center_time, time_span, num_alarms):
        self.center_time = center_time
        self.time_span = time_span
        self.num_alarms = num_alarms

    def getMessage(self):
        self.xml = "<?xml version='1.0' encoding='UTF-8'?><methodcall><requestid>1</requestid><methodname>alarms</methodname>"
        self.xml = self.xml + "<centertime>{}</centertime>".format(self.center_time)
        self.xml = self.xml + "<numalarms>{}</numalarms>".format(self.num_alarms)
        self.xml = self.xml + "<timespan>{}</timespan></methodcall>\r\n\r\n".format(self.time_span)
        return bytes(self.xml, "utf-8")
