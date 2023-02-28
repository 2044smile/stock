from django import forms
from django.contrib.auth.forms import UserCreationForm

from accounts.models import User

class AccountForm(UserCreationForm):
    email = forms.EmailField(
        label="Email address", 
        max_length=255,
        error_messages={
            'required': "You must write an email"
        })
    kakao_nickname = forms.CharField(label="Kakao Nickname", max_length=32)
    # password = forms.CharField(
    #     label="Password", 
    #     widget=forms.PasswordInput(),
    #     error_messages={
    #         'required': "You must write a password"
    #     })
    stock_code_1 = forms.CharField(
        label="주식종목 코드를 적어주세요", 
        max_length=8,
        error_messages={
            'required': "You must write a stcok code"
        })
    stock_code_2 = forms.CharField(
        label="주식종목 코드를 적어주세요", 
        max_length=8,
        error_messages={
            'required': "You must write a stcok code"
        })
    stock_code_3 = forms.CharField(
        label="주식종목 코드를 적어주세요", 
        max_length=8,
        error_messages={
            'required': "You must write a stcok code"
        })

    class Meta:
        model = User
        fields = ('email', 'kakao_nickname', 'password1', 'password2', 'stock_code_1', 'stock_code_2', 'stock_code_3', )
