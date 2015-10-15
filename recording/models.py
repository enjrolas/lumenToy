from django.db import models

class Recording(models.Model):
    recordingURL = models.TextField()
    duration=models.IntegerField()
    incomingNumber=models.TextField()
    callerName=models.TextField()
    callStatus=models.TextField()
    callSID=models.TextField()
    timestamp=models.DateTimeField(auto_now_add=True)

