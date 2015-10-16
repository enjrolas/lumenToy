from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from recording.models import Recording
import logging
import sys
log=logging.getLogger(__name__)

@csrf_exempt
def incoming(request):
    return render(request, "recording/record.html", { 'request' : request })

def listRecordings(request):
    allRecordings=Recording.objects.all().order_by("-timestamp")
    return render(request, "recording/list.html", {'recordings' : allRecordings})

@csrf_exempt
def recordingComplete(request):
    log.debug("POST request:")
    log.debug(request.POST)
    url=request.POST.get('RecordingUrl')
    log.debug(url)
    caller=request.POST.get('Caller')
    log.debug(caller)
    name=request.POST.get('CallerName')
    log.debug(name)
    status=request.POST.get('CallStatus')
    log.debug(status)
    sid=request.POST.get('CallSid')
    log.debug(sid)
    duration=int(request.POST.get('Duration'))
    log.debug(duration)
    record=Recording(
        recordingURL=url,
        incomingNumber=caller,
        callerName=name,
        callStatus=status,
        callSID=sid,
        duration=duration,
        )
    try:
        log.debug("saving the recording to the db")
        record.save()
    except Exception:
        log.debug("trouble saving it")
        log.debug(Exception)
        log.debug(sys.exc_info())
    try:
        log.debug("here's your recording: ")
        log.debug(record)
    except Exception:
        log.debug("trouble printing it")
        log.debug(Exception)
    log.debug("saved recording")
    return HttpResponse("ok")

