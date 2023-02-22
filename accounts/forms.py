from django import forms


class AccountForm(forms.Form):
    email = forms.EmailField(
        max_length=255,
    )
    kakao_nickname = forms.CharField(
        max_length=32
    )
    stock_code_1 = forms.CharField(
        max_length=8
    )
    stock_code_2 = forms.CharField(
        max_length=8
    )
    stock_code_3 = forms.CharField(
        max_length=8
    )