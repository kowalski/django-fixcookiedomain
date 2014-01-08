django-fixcookiedomain
======================

Django middleware setting the session of csrf cookie domains to the request host. This is to play nice with f... MSIE

Sets settings.SESSION_COOKIE_DOMAIN and settings.CSRF_COOKIE_DOMAIN
to the host requested. All the browsers but IE would consider a cookie
without domain specified to like this, howether IE is *special*.

=============
Configuration
=============

Simply add the 'fixcookiedomain.middleware.Middleware' to the MIDDLEWARE_CLASSES
in your settings.py. Be sure to put it before 'django.contrib.sessions.middleware.SessionMiddleware' in the chain.
