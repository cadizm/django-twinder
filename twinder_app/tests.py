from mock import patch

from django.conf import settings
from django.core.urlresolvers import reverse
from django.test import TestCase, Client

import logging
logger = logging.getLogger('twinder.' + __name__)


class SmsTestCase(TestCase):
    def setUp(self):
        self.assertFalse(settings.TWILIO_LIVE)
        self.client = Client()

    def tearDown(self):
        pass

    def test_sms_get_404(self):
        response = self.client.get(reverse('sms-view'))
        self.assertEqual(404, response.status_code)

    def test_sms_missing_signature(self):
        response = self.client.post(reverse('sms-view'))
        self.assertEqual(404, response.status_code)

    @patch('twinder_app.views.valid_twilio_request', return_value=False)
    def test_sms_bad_signature(self, mock_valid_twilio_request):
        extra = {
            'HTTP_X_TWILIO_SIGNATURE': 'invalid signature',
        }
        response = self.client.post(reverse('sms-view'), **extra)
        self.assertEqual(404, response.status_code)

    @patch('twinder_app.views.send_twilio_message')
    @patch('twinder_app.views.valid_twilio_request', return_value=True)
    def test_sms_valid(self,
            mock_valid_twilio_request,
            mock_send_twilio_message):
        data = {
            'Body': 'I am the text body',
        }
        extra = {
            'HTTP_X_TWILIO_SIGNATURE': 'HpS7PBa1Agvt4OtO+wZp75IuQa0=',
        }
        response = self.client.post(reverse('sms-view'), data, **extra)

        self.assertEqual(1, mock_send_twilio_message.call_count)
        self.assertEqual(200, response.status_code)
