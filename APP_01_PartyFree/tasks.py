from celery import shared_task
from time import sleep
from twilio.rest import Client
from twilio.twiml.voice_response import Play, VoiceResponse
account_sid = 'AC94a0517d20fc9a6ad2eee9d5423791b7'
auth_token = 'c135b809899593c0b8317a57ce5b9a0b'
client = Client(account_sid, auth_token)
CallFrom = "+19167961080"


@shared_task
def sleepy(waitTime,userPhoneNo):
    print('DONE')
    sleep(waitTime*60)
    call = client.calls.create(
                    url='https://handler.twilio.com/twiml/EH1f4472badc0e04c79cc0f48f19ebc86e',
                    to="+1" + str(userPhoneNo),
                    from_=CallFrom
                )
    print(call.sid)
    return None
