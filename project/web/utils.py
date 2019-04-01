import requests
import json
from social_django.models import UserSocialAuth


class Api():
    main_url = 'https://api.vk.com/method/'
    api_version = '5.92' # версия api VK



    # генерируем url
    def method(self, method, params=None):
        if not params:
            params = {}
        if not params.get('v'):
            params['v'] = self.api_version


        full_url = self.generate_url(method)
        return requests.get(full_url, params=params)

    # получение  url
    def generate_url(self, method):
        gen_url = self.main_url + method
        return gen_url

# получение id user и токена
def get_user(user_id):
    social = UserSocialAuth.objects.get(user=user_id)
    get_user_token = {
        'user_token': social.extra_data.get('access_token')
    }
    return get_user_token
