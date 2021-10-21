import json
from json.encoder import JSONEncoder
from django.contrib.auth.backends import UserModel
from django.shortcuts import render
from rest_framework import permissions
from rest_framework.permissions import AllowAny
from rest_framework import viewsets
from .serializers import UserSerializers
from .models import CustomUser
from django.http import JsonResponse
from django.contrib.auth import get_user_model, login, logout
from django.views.decorators.csrf import csrf_exempt
import re
import random

def genrate_session(length=10):
    return ''.join(random.SystemRandom().choice([chr(i) for i in range(97, 123)] + [str(i) for i in range(10)]) for _ in range(length))

@csrf_exempt
def signin(request):
    if not request.method == "POST":
        return JsonResponse({'error': 'Send Post request only'})

    username = request.POST['email']
    password = request.POST['password']

    # if not re.match("([\w\.\-_]+)?\w+@+(\.\w+){1,}", username):
    #     return JsonResponse({'error': 'Email is not valid'})
    
    if len(password) < 3:
        return JsonResponse({'error': 'Password is too small'})

    UserModel = get_user_model()

    try:
        user = UserModel.objects.get(email=username)
        if user.check_password(password):
            usr_dict = UserModel.objects.filter(email=username).values().first()
            usr_dict.pop('password')

            if user.session_token != '0':
                user.session_token == '0'
                user.save()
                return JsonResponse({'error': 'previous token session exists'})
            token = genrate_session()
            user.session_token = token
            user.save()
            login(request, user)
            return JsonResponse({'token': token, 'usr_dict': usr_dict})
        else:
            return JsonResponse({'error': 'Invalid Password'})
    except UserModel.DoesNotExist:
          return JsonResponse({'error': 'Invalid Email'})


def signout(request, id):
    logout(request)

    UserModel = get_user_model()

    try:
        user = UserModel.objects.get(pk=id)
        user.session_token = "0"
        user.save()
    except UserModel.DoesNotExist:
        return JsonResponse({'error':'Invalid id'})
    
    return JsonResponse({'success':'Logout Success'})

class UserViewsets(viewsets.ModelViewSet):
    permission_classes_by_action = {'create': [AllowAny]}
    queryset = CustomUser.objects.all().order_by('id')
    serializer_class = UserSerializers

    def get_permissions(self):
        try:
            return [permissions() for permissions in self.permission_classes_by_action[self.action]]
        except KeyError:
            return [permissions() for permissions in self.permission_classes]