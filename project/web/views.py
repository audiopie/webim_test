import requests
import json

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout
from django.views import View

from social_django.models import UserSocialAuth
from .utils import Api, get_user


class Index(View):
    get_user_token = {}

    def get(self, request):
        api = Api()
        user_id = request.user.id
        if user_id is not None:
            get_user_token = get_user(user_id)
            friends_request = api.method('friends.get',  {'access_token': get_user_token.get('user_token'), 'count': 5})
            show_friends = friends_request.json()
            args = {
                'show_friends': show_friends,
                }
            return render(request, 'base.html', args)
        else:
            return render(request, 'base.html')


class Logout(View):
    def get(self, request):
        logout(request)
        return redirect('index')
