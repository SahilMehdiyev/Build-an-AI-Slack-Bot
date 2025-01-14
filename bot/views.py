from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt



@csrf_exempt
def slack_event_endpoint(request):
    
    print(request.body,request.method)
    return HttpResponse('<h1>Hello world!</h1>',status=200)

