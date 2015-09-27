try:
    from django.utils.encoding import force_text  # noqa
except ImportError:
    from django.utils.encoding import force_unicode as force_text  # noqa


try:
    from urllib2 import urlopen, HTTPError  # noqa
except ImportError:
    from urllib.request import urlopen, HTTPError  # noqa

# Django 1.10 removes patterns, instead it is just a list
try:
    from django.conf.urls import patterns
except ImportError:
    def patterns(prefix, *urls):
        assert prefix == ''
        return urls
