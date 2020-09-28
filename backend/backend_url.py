from backend.views.index import IndexView
from backend.views.login import LoginView
from backend.views.apis import IndexAPIView
from backend.views.apis import MenuApiView
from backend.views.welcome import WelcomeView
from backend.views.captcha import CaptchaView
from backend.views.menu import MenuView
from backend.views.setting import SettingMenu

from django.urls import path

urlpatterns = [
    path('index', IndexView.as_view(), name="index"),
    path('', IndexView.as_view(), name="index"),
    path('login', LoginView.as_view(), name="login"),
    path('welcome', WelcomeView.as_view(), name="welcome"),
    path('catcha', CaptchaView.as_view(), name="captcha"),
    path('menu', MenuView.as_view(), name="menu"),
    path('setting', SettingMenu.as_view(), name="setting"),

    path('index_api', IndexAPIView.as_view()),
    path('menu_api', MenuApiView.as_view()),
]
