# from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    print(request.COOKIES)
    oldval = request.COOKIES.get('view_count', 1)
    resp = HttpResponse('view count=' + str(oldval))

    # for autograder
    resp.set_cookie('dj4e_cookie', '5a2c8a18', max_age=1000)

    if oldval:
        resp.set_cookie('view_count', int(oldval) + 1)  # No expired date - until browser closes
    else:
        resp.set_cookie('view_count', 1)
    resp.set_cookie('zap', 42, max_age=1000)  # seconds until expire
    return resp
    # return HttpResponse("this is where to implement the session")