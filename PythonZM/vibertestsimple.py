from flask import Flask, request, Response
from viberbot import Api
from viberbot.api.bot_configuration import BotConfiguration
from viberbot.api.messages.text_message import TextMessage
from viberbot.api.viber_requests import (
    ViberConversationStartedRequest,
    ViberFailedRequest,
    ViberMessageRequest,
    ViberSubscribedRequest,
    ViberUnsubscribedRequest,
)
import logging

app = Flask(__name__)
viber = Api(
    BotConfiguration(
        name='BluePhoenix',
        avatar='https://gravatar.com/avatar/082ba7a1f8be1f459b38f9d991c20df2?s=400&d=robohash&r=x',
        auth_token='524e6ea27c67d19c-7ecb89e869996967-8ca1582092aa8173'
    )
)

@app.route('/', methods=['POST'])
def incoming():
    app.logger.debug(f"Received request. Post data: {request.get_data()}")

    if not viber.verify_signature(request.get_data(), request.headers.get('X-Viber-Content-Signature')):
        return Response(status=403)

    viber_request = viber.parse_request(request.get_data())

    if isinstance(viber_request, ViberMessageRequest):
        message = viber_request.message
        viber.send_messages(viber_request.sender.id, [message])
    elif isinstance(viber_request, ViberSubscribedRequest):
        viber.send_messages(viber_request.get_user.id, [TextMessage(text="Thanks for subscribing!")])
    elif isinstance(viber_request, ViberFailedRequest):
        app.logger.warn(f"Client failed receiving message. Failure: {viber_request}")

    return Response(status=200)

if __name__ == "__main__":
    context = ('d:\\server.crt', 'd:\\server.key')
    app.run(host='0.0.0.0', port=443, debug=True, ssl_context=context)
