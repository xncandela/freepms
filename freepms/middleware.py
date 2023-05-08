from django.http import HttpResponseRedirect, HttpResponseNotAllowed
from django.urls import reverse
import pytz
from django.utils import timezone
from django.conf import settings
from django.contrib.auth.models import AnonymousUser
from threading import local



USER_ATTR_NAME = getattr(settings, 'LOCAL_USER_ATTR_NAME', '_current_user')

_thread_locals = local()


def _do_set_current_user(user_fun):
    setattr(_thread_locals, USER_ATTR_NAME, user_fun.__get__(user_fun, local))


def _do_set_current_hotel(hotel):

    setattr(_thread_locals, 'Hotel', hotel.__get__(hotel, local))

def _set_current_user(user=None):
    '''
    Sets current user in local thread.
    Can be used as a hook e.g. for shell jobs (when request object is not
    available).
    '''
    _do_set_current_user(lambda self: user)


class CurrentUserMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # request.user closure; asserts laziness;
        # memorization is implemented in
        # request.user (non-data descriptor)
        _do_set_current_user(lambda self: getattr(request, 'user', None))


        setattr(_thread_locals, 'Hotel', 'prueba')

        response = self.get_response(request)
        return response


def get_current_user():
    current_user = getattr(_thread_locals, USER_ATTR_NAME, None)
    if callable(current_user):
        return current_user()
    return current_user

def get_current_authenticated_user():
    current_user = get_current_user()
    if isinstance(current_user, AnonymousUser):
        return None
    return current_user




#
#
# class CurrentHotelMiddleware(object):
#     def __init__(self, get_response):
#         self.get_response = get_response
#
#     def __call__(self, request):
#         setattr(_thread_locals, 'HOTEL', )
#         hotel = request.session.get('hotel',None)
#         return self.get_response(request)
#



class TimezoneMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        tzname = request.session.get('django_timezone')
        if tzname:
            timezone.activate(pytz.timezone(tzname))
        else:
            timezone.deactivate()
        return self.get_response(request)




class MenuMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response
        self.menu='Prueba de menu'

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_template_response(self, request, response):
        response.context_data["menu"] = self.menu
        return response