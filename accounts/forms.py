from django import forms

from accounts.models import User

class AccountForm(forms.Form):
    email = forms.EmailField(label="Email address", max_length=255)
    kakao_nickname = forms.CharField(label="Kakao Nickname", max_length=32)
    password = forms.CharField(label="Password", widget=forms.PasswordInput())
    stock_code_1 = forms.CharField(label="주식종목 코드를 적어주세요", max_length=8)
    stock_code_2 = forms.CharField(label="주식종목 코드를 적어주세요", max_length=8)
    stock_code_3 = forms.CharField(label="주식종목 코드를 적어주세요", max_length=8)

    class Meta:
        model = User
