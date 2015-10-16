from django.db import models

class Recording(models.Model):
    recordingURL = models.TextField()
    duration=models.IntegerField()
    incomingNumber=models.TextField()
    callerName=models.TextField()
    callStatus=models.TextField()
    callSID=models.TextField()
    timestamp=models.DateTimeField(auto_now_add=True)

    def __repr__(self):
        return "recording by %s, %d seconds at %s, saved at %s" % (self.callerName, self.duration, str(self.timestamp), self.recordingURL)

    __str__=__repr__
