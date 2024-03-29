import os, requests

from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import View, generic

from accounts.models import User
from accounts.forms import AccountForm


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
        token = {"token": user_info.json()}
        request.session['user'] = token

        return redirect(f"http://localhost:8000/accounts/signup")


class AccountSignupView(View):
    def get(self, request, **kwargs):
        session = request.session.get('user')

        # 여기서 세션이 없다면 회원가입 차단하는 로직 추가 즉 처음 로그인 한다면 kakao_login 으로 이동
        if session is None:
            return redirect('kakao_login')

        form = AccountForm()
        form.fields['kakao_nickname'].initial = session['token']['kakao_account']['profile']['nickname']

        # user = User.objects.get(kakao_nickname=session['token']['kakao_account']['profile']['nickname'])
        # 카카오 로그인 시 [필수] 와 [선택] 선택의 경우 사용자가 선택하지 않으면 이메일을 따로 입력하던가 해야될 듯?
        # 아니면 카카오스토리 프로필 URL 의 경우에는 중복이 될 수 없으므로 이것으로 처리해도 될 듯
        ## 추가적으로 카카오로 아이디가 회원가입이 되어 있으면 redirect 해서 로그인을 자동으로 수행하도록

        context = {
            "session": session,
            "form": form
        }

        return render(request, 'signup.html', context=context)
    def post(self, request, **kwargs):
        form = AccountForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('signin')

        context = {
            "form": form
        }

        return render(request, 'signin.html', context=context)


class AccountSigninView(View):
    def get(self, request, **kwargs):
        # 카카오 로그인이 되어 있으면 자동으로 화면을 옮겨 로그인
        session = request.session.get('user')  # token = {"token": user_info.json()}
        print(f'AccountSigninView, {session}', flush=True)

        return render(request, 'signin.html', context=session)


class AccountSignoutView(View):
    def get(self, request, **kwargs):
        session = request.session.get('user')
        print(f'AccountSignoutView, {session}', flush=True)
        url = 'https://kapi.kakao.com/v1/user/logout'
        header = {
            'Authorization': f'bearer {session}'
        }

        response = requests.post(url, headers=header)
        result = response.json()

        if result.get('id'):
            del request.session['user']
            return render(request, 'index.html')

        return render(request, 'index.html')
