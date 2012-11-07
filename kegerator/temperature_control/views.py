from django.http import HttpResponse

from temperature_control.models import *

import json

def temp_log(request, size):
    readings = TemperatureReading.objects.all().order_by('time')
    ret_val = []
    for i, reading in enumerate(readings):
        if(i < size):
            ret_val.append((reading.time, reading.temperature))
    return HttpResponse(json.dumps(ret_val), mimetype='application/json') 

