from django.urls import path

from .views import AccountKakaoView, AccountKakaoCallBackView, AccountSignupView


urlpatterns = [    
    path('kakao/', AccountKakaoView.as_view(), name="kakao_login"),
    path('kakao/callback/', AccountKakaoCallBackView.as_view(), name="kakao_callback"),

    path('signup/', AccountSignupView.as_view(), name="signin")
]
