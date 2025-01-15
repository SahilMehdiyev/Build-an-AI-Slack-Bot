import requests
import json
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
import helpers

SLACK_BOT_OAUTH_TOKEN = helpers.config(
    'SLACK_BOT_OAUTH_TOKEN',
    default=None,
    cast=str
)


def send_message(message,channel_id):
    url = "https://slack.com/api/chat.postMessage"
    headers = {
        "Content-Type": "application/json: charset=utf-8",
        "Authorization": f"Bearer {SLACK_BOT_OAUTH_TOKEN}",
        "Accept": "application/json"
    }

    data = {
        "channel": f'{channel_id}',
        "text": message
    }
    return requests.post(url,json=data,headers=headers)
    

@csrf_exempt
@require_POST
def slack_event_endpoint(request):
    json_data = {}
    try:
        json_data = json.loads(request.body.decode('utf-8'))
    except Exception as e:
        return HttpResponse('Invalid JSON', status=400)
    
    data_type = json_data.get('type')
    allowed_data_type = [
        'url_verification',
        'event_callback'
    ]
    if data_type not in allowed_data_type:
        return HttpResponse('Not Allowed', status=400)
    
    if data_type == 'url_verification':
        challenge = json_data.get('challenge')  
        if challenge is None:
            return HttpResponse('Not Allowed', status=400)
        return HttpResponse(challenge, status=200)
    
    if data_type == 'event_callback':
        event = json_data.get('event') or {}
        msg_text = event.get('text')
        # user_id = event.get('user_id')
        channel_id = event.get('channel_id')
        r = send_message(msg_text,channel_id=channel_id)
        return HttpResponse("Success", status=r.status_code)
    return HttpResponse("Success", status=200)

