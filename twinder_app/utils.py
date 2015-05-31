"""
Twilio request validation and sms messaging

For reference
    https://twilio-python.readthedocs.org/en/latest/usage/validation.html
    http://www.twilio.com/docs/security

To make request validation fancier, put in django middleware.
"""
from twilio.rest import TwilioRestClient
from twilio.util import RequestValidator
from twilio import TwilioException, TwilioRestException, TwimlException

from django.conf import settings

import logging
logger = logging.getLogger('twinder.' + __name__)


class TwilioRequestValidator(object):
    def __init__(self):
        self.validator = RequestValidator(settings.TWILIO_AUTH_TOKEN)
        self.callback_url = settings.TWILIO_CALLBACK_URL

    def validate(self, request):
        if not settings.TWILIO_LIVE:
            return True

        return self.validator.validate(
                settings.TWILIO_CALLBACK_URL,
                request.POST,
                request.META['HTTP_X_TWILIO_SIGNATURE'],
                )

valid_twilio_request = TwilioRequestValidator().validate


class TwilioMessager(object):
    def __init__(self):
        self.client = TwilioRestClient(
                settings.TWILIO_ACCOUNT_SID,
                settings.TWILIO_AUTH_TOKEN
                )

    def send_message(self, to, message):
        try:
            message = self.client.messages.create(
                    to=to,
                    from_=settings.TWILIO_SMS_NUMBER,
                    body=message,
                    )
        except TwilioRestException:
            logger.exception('TwilioRestException')
        except TwilioException:
            logger.exception('TwilioException')

        logger.debug('Created twilio message\n\t{}\n\t{}'.format(
                message.sid, message.body))

send_twilio_message = TwilioMessager().send_message
