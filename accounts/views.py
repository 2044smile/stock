import os, requests

from django.shortcuts import redirect, HttpResponse
from django.views import View
from django.http.response import JsonResponse


class AccountKakaoView(View):
    def get(self, request):
        KAKAO_API = "https://kauth.kakao.com/oauth/authorize?response_type=code"
        CLIENT_ID = os.environ.get('KAKAO_REST_API_KEY')
        REDIRECT_URI = os.environ.get('KAKAO_REDIRECT_URI')
        
        return redirect(f"{KAKAO_API}&client_id={CLIENT_ID}&redirect_uri={REDIRECT_URI}")


class AccountKakaoCallBackView(View):
    def get(self, request):
        data = {
            "grant_type": "authorization_code",
            "client_id": os.environ.get('KAKAO_REST_API_KEY'),
            "redirection_uri": f"{os.environ.get('ADDRESS')}/accounts/kakao",
            "code": request.GET.get('code')
        }

        token_response = requests.post("https://kauth.kakao.com/oauth/token", data=data)

        access_token = token_response.json().get('access_token')

        user_info = requests.get("https://kapi.kakao.com/v2/user/me", headers={"Authorization": f"Bearer {access_token}"})
        
        dic = {"token": user_info.json()}

        return JsonResponse(dic, json_dumps_params={'ensure_ascii': False})
