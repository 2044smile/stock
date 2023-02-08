from django.urls import path

from .views import AccountKakaoView, AccountKakaoCallBackView


urlpatterns = [    
    path('kakao/', AccountKakaoView.as_view(), name="kakao_oauth_authorize"),
    path('kakao/callback/', AccountKakaoCallBackView.as_view())
]
