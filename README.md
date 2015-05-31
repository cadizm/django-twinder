Overview
========

If you have a twilio number and want to receive sms's and responsd to them
programmatically, here's an example django app to do just that via a twilio
callback.

Incoming requests are first validated as described [here](https://www.twilio.com/docs/security)

Feel free to modify for your needs.


Building
========

    python setup.py build sdist


Installation
============

    pip install django-twinder-0.1.0.tar.gz


Django Settings
===============

     INSTALLED_APPS += (
         'twinder_app',
     )

    # Logger namespace:
    logger = logging.getLogger('twinder.' + __name__)

    # Twilio settings variables

    TWILIO_LIVE = False

    if TWILIO_LIVE:
        TWILIO_ACCOUNT_SID = 'my live account sid'
        TWILIO_AUTH_TOKEN = 'my live auth token'
        TWILIO_SMS_NUMBER = '+11234567890'
    else:
        TWILIO_ACCOUNT_SID = 'my test account sid'
        TWILIO_AUTH_TOKEN = 'my test auth token'
        TWILIO_SMS_NUMBER = '+15005550006'

    TWILIO_CALLBACK_URL = 'http://foo.com/bar/'


Django urlconf
==============

    urlpatterns += patterns('',
        url(r'^bar/', include('twinder_app.urls')),
    )


Testing
=======

Standalone app

    python setup.py test

In django

    python manage.py test django-twinder
