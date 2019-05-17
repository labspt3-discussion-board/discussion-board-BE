from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.core import serializers
from api.models import User
import json

def index(request):
    return HttpResponse('This is the api endpoint')


@csrf_exempt # UNSAFE MUST FIND ALTERNATIVE
def createUser(request):
    if request.method == 'POST':

        data_string = request.body.decode('utf-8')
        data_json = json.loads(data_string)
        
        # print(data_json['username'])


        newUser = User(username=data_json['username'])
        newUser.save()

        print(serializers.serialize("json", User.objects.all()))

        

        content = serializers.serialize("json", User.objects.all())

        response = HttpResponse(content, content_type='application/json')

        return response
    elif request.method =='GET':
        return HttpResponse('no')


