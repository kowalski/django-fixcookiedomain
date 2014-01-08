from django.conf import settings

from utils import make_tls_property


to_monkeypatch = settings.__dict__['_wrapped'].__class__
SESSION_COOKIE_DOMAIN = make_tls_property()
to_monkeypatch.SESSION_COOKIE_DOMAIN = SESSION_COOKIE_DOMAIN
CSRF_COOKIE_DOMAIN = make_tls_property()
to_monkeypatch.CSRF_COOKIE_DOMAIN = CSRF_COOKIE_DOMAIN


class Middleware(object):
    '''
    Sets settings.SESSION_COOKIE_DOMAIN and settings.CSRF_COOKIE_DOMAIN
    to the host requested. All the browsers but IE would consider a cookie
    without domain specified to like this, howether IE is *special*.

    Be sure to put this middleware *before*
    django.contrib.sessions.middleware.SessionMiddleware in the
    MIDDLEWARE_CALSSES list.
    '''

    def process_request(self, request):
        host = request.get_host()
        if ':' in host:
            host, port = host.split(':')
        host = host.lower()

        SESSION_COOKIE_DOMAIN.value = host
        CSRF_COOKIE_DOMAIN.value = host
