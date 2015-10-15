from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def incoming(request):
    return render(request, "recording/record.html")

@csrf_exempt
def recordingComplete(request):
    Recording record
    record.recordingURL=request.POST['recordingURL']
    record.incomingNumber=request.POST['From']
    record.callerName=request.POST['CallerName']
    record.callStatus=request.POST['CallStatus']
    record.callSID=request.POST['CallSid']
    record.duration=request.POST['RecordingDuration']
    record.save()
