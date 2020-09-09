from django.http import JsonResponse
from django.shortcuts import HttpResponse
from api import models
import json
import base64


# Create your views here.
def login(request):
    if request.method == "POST":
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        try:
            user = models.user.objects.get(username=username)
            print(user)
            if user.password == password:
                temp = bytes(username, 'utf-8')
                user.session_id = base64.b64encode(temp)
                user.save()
                response = HttpResponse(json.dumps({'username': username, 'userid': user.userid}),
                                        content_type='application/json')
                response.status_code = 200
                response.set_cookie('session_id', user.session_id)
                return response
            else:
                response = HttpResponse(json.dumps({"error": "password is wrong"}),
                                        content_type='application/json')
                response.status_code = 401
                return response
        except:
            response = HttpResponse(json.dumps({"error": "no such a user"}),
                                          content_type='application/json')
            response.status_code = 401
            return response
    response = HttpResponse(json.dumps({"error": "require POST"}),
                            content_type='application/json')
    response.status_code = 401
    return response


def logout(request):
    if request.method == "POST":
        username = request.POST.get('username', None)
        session_id = request.COOKIES.get('session_id')
        try:
            user = models.user.objects.get(username=username)
            if user.session_id != session_id:
                response = HttpResponse(json.dumps({'error': 'session expiration'}),
                                        content_type='application/json')
                response.status_code = 401
                response.set_cookie('session_id', '')
                user.session_id = ''
                user.save()
                return response
            else:
                user.session_id = ''
                user.save()
                response = HttpResponse(json.dumps({'message': 'ok'}),
                                        content_type='application/json')
                response.status_code = 200
                response.set_cookie('session_id', '')
                return response
        except:
            response = HttpResponse(json.dumps({"error": "no such a user"}),
                                    content_type='application/json')
            response.status_code = 401
            return response
    response = HttpResponse(json.dumps({"error": "require POST"}),
                            content_type='application/json')
    response.status_code = 401
    return response


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')

    response = HttpResponse(json.dumps({"error": "require POST"}),
                            content_type='application/json')
    response.status_code = 401
    return response
