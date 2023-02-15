from django.urls import path

from .views import AccountKakaoView, AccountKakaoCallBackView


urlpatterns = [    
    path('kakao/', AccountKakaoView.as_view(), name="kakao_login"),
    path('kakao/callback/', AccountKakaoCallBackView.as_view(), name="kakao_callback")
]
