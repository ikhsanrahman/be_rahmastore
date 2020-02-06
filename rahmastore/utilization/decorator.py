from functools import wraps
# from django.http import HttpRequest
from rest_framework.response import Response

from .auth_helper import Auth

# def user_token_required(request):
#     data, status = Auth.get_logged_in_user(request)
#     token = data.get('data')
#     if not token:
#         return data, status
#     return True

def user_token_required(f):
    @wraps(f)
    def decorated(request, *args, **kwargs):
        data, status = Auth.get_logged_in_user(args[0])
        token = data.get('data')
        if not token:
            return Response(data, status)

        return f(request, *args, **kwargs)

    return decorated

def buyer_token_required(f):
    @wraps(f)
    def decorated(request, *args, **kwargs):

        data, status = Auth.get_logged_in_buyer(args[0])
        token = data.get('data')

        if not token:
            return Response(data, status)

        return f(request, *args, **kwargs)

    return decorated
