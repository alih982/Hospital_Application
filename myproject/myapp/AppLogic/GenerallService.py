from myapp.models import OTPRecord
import random
import sys
from ..Models import ItemModel, OtpModel
from ..models import OTPRecord


# general_service.py

from threading import local

_ctx = local()

def set_request(request):
    _ctx.request = request

def get_request():
    return getattr(_ctx, "request", None)

def post(key, default=None):
    req = get_request()
    if not req:
        raise RuntimeError("No request context found")
    return req.POST.get(key, default)

def get(key, default=None):
    req = get_request()
    if not req:
        raise RuntimeError("No request context found")
    return req.GET.get(key, default)

def with_request(view_func):
    def wrapper(request, *args, **kwargs):
        set_request(request)
        return view_func(request, *args, **kwargs)
    return wrapper

