
from rest_framework.parsers       import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts             import render
from django.http                  import HttpResponse, JsonResponse
from django.core                  import serializers
from api.models                   import User
from api.serializers              import UserSerializer
import json

# Database helper functions
def getSerializedUsers():    # Get all users from database and return the serialized data
    users = User.objects.all()
    user_serializer = UserSerializer(users, many=True)
    return user_serializer.data
def createNewUser(request):  # Create a new user, get all users and return serialized data
    data = JSONParser().parse(request)
    user_serializer = UserSerializer(data=data)
    if user_serializer.is_valid():
        user_serializer.save()
        serialized_users = getSerializedUsers()
        return serialized_users
    elif not user_serializer.is_valid():
        return "Invalid Data"


# api/
@csrf_exempt
def index(request):

    # Return all data in API
    if request.method == 'GET':
        users = User.objects.all()
        user_serializer = UserSerializer(users, many=True)
        return JsonResponse(user_serializer, safe=False)

    # Return 'Method Not Allowed' status code
    else:
        response = HttpResponse("Error")
        response.status_code(405)
        return response

# api/users
@csrf_exempt
def users(request):

    # Return all users
    if request.method == 'GET':
        serialized_users = getSerializedUsers()
        return (JsonResponse(serialized_users, safe=False))

    # Add a new user and return all users (including the new user)
    elif request.method == 'POST':
        response = None
        data     = createNewUser(request)
        if not (data == "Invalid Data"):
            response = JsonResponse(data, status=406, safe=False)
        else:
            response = JsonResponse(data, status=201)
        return response



        print(JSONParser().parse(request))
        response = HttpResponse('Success')
        response.status_code = 201
        return response

# api/users/:id
@csrf_exempt
def user_details(request):
    return




        















# def index(request):
#     return HttpResponse('This is the api endpoint')

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
        content = serializers.serialize("json", User.objects.all())

        response = HttpResponse(content, content_type='application/json')

        return response


