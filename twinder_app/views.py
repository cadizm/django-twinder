from django.http import HttpResponse, Http404
from django.views.decorators.csrf import csrf_exempt

import twilio.twiml

from .http import TwilioResponse
from .utils import valid_twilio_request, send_twilio_message

from pprint import pformat

import logging
logger = logging.getLogger('twinder.' + __name__)


@csrf_exempt
def sms(request):
    """
    Responsd to a text to a twilio sms-enabled number.
    """
    if request.method != 'POST':
        logger.debug('Invalid request method: GET')
        raise Http404()

    if 'HTTP_X_TWILIO_SIGNATURE' not in request.META:
        logger.debug('HTTP_X_TWILIO_SIGNATURE missing')
        raise Http404()

    if not valid_twilio_request(request):
        logger.debug('INVALID HTTP_X_TWILIO_SIGNATURE')
        raise Http404()

    logger.debug('POST vars:\n{}'.format(pformat(dict(request.POST))))

    send_twilio_message('+11234567890', request.POST['Body'])

    return TwilioResponse('http://www.youtube.com/watch?v=C-u5WLJ9Yk4')
