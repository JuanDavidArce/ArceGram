"""ArceGram views"""
#Django
from django.http import HttpResponse
import json

#Utilities
from datetime import datetime

def hello_world(request):  #this kind of functions are named as views
    """Return a greeting."""
    now=datetime.now().strftime('%b %dth , %Y - %H: %M hrs')
    return HttpResponse("Oh, hi! current server time is {now}".format(now=now))

def sort_integers(request):
    """Return a JSON response with sorted integers"""
    numbers= request.GET['numbers']
    numbers= list(map(int,numbers.split(',')))
    sorted_ints =sorted(numbers)
    data={
        'status':'ok',
        'numbers': sorted_ints,
        'message': 'Integers sorted successfully'
    }
    return HttpResponse(json.dumps(data,indent=4),
    content_type='application/json'
    )

def say_hi(request,name,age):
    """Return a gereeting"""

    if age<12:
        message='Sorry {},you are not allowed here'.format(name)
    else:
        message='Hello , {} ! Welcome to ArceGram'.format(name)
    return HttpResponse(message)
