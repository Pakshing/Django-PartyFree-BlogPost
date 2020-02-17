from celery import shared_task
from time import sleep
from twilio.rest import Client
import os
from twilio.twiml.voice_response import Play, VoiceResponse

account_sid = os.environ.get('TWILIO_ID')
auth_token = os.environ.get('TWILIO_TOKEN')

client = Client(account_sid, auth_token)
CallFrom = "+14083177234"

@shared_task
def sleepy(waitTime,userPhoneNo):
    print('DONE')
    sleep(waitTime*60)
    call = client.calls.create(
                    url='https://handler.twilio.com/twiml/EHd724fff58517eddb16e547bde6ad371e',
                    to="+1" + str(userPhoneNo),
                    from_=CallFrom
                )
    print(call.sid)
    return None
