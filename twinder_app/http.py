import twilio

from django.http import HttpResponse


class TwilioResponse(HttpResponse):
    """
    Content Type defaulted to application/xml
    """
    def __init__(self, message=None, content_type='application/xml'):
        super(TwilioResponse, self).__init__(None, content_type)

        message = message if message else ''
        response = twilio.twiml.Response()
        response.message(message)

        self.content = response
