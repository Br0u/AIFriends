
from django.urls import path

from views.user.account.login import LoginView
from views.user.account.logout import LogoutView
from views.user.account.refresh_token import RefreshTokenView
from views.user.account.register import RegisterView
from .views.index import index

urlpatterns = [
    path('api/user/account/login', LoginView.as_view()),
    path('api/user/account/logout', LogoutView.as_view()),
    path('api/user/account/register', RegisterView.as_view()),
    path('api/user/account/refresh_token', RefreshTokenView.as_view()),

    path('', index)
]

