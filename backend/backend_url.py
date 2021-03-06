from backend.views.index import IndexView
from backend.views.index import RegView
from backend.views.index import LogoutView
from backend.views.index import ChangeView
from backend.views.login import LoginView
from backend.views.apis import IndexAPIView
from backend.views.apis import MenuApiView
from backend.views.apis import UserApiView
from backend.views.welcome import WelcomeView
from backend.views.captcha import CaptchaView
from backend.views.menu import MenuView
from backend.views.user import UserView
from backend.views.user import AddUserView
from backend.views.table import TableView
from backend.views.setting import SettingMenu

from django.urls import path

urlpatterns = [
    path('index', IndexView.as_view(), name="index"),
    path('', IndexView.as_view(), name="index"),
    path('login', LoginView.as_view(), name="login"),
    path('logout', LogoutView.as_view(), name="logout"),
    path('welcome', WelcomeView.as_view(), name="welcome"),
    path('catcha', CaptchaView.as_view(), name="captcha"),
    path('menu', MenuView.as_view(), name="menu"),
    path('setting', SettingMenu.as_view(), name="setting"),
    path('table', TableView.as_view(), name="table"),
    path('change', ChangeView.as_view(), name="change"),
    path('user', UserView.as_view(), name="user"),
    path('add', AddUserView.as_view(), name="add"),

    path('index_api', IndexAPIView.as_view(), name="api_index"),
    path('menu_api', MenuApiView.as_view(), name="api_menu"),
    path('user_api', UserApiView.as_view(), name="api_user"),

    path('reg', RegView.as_view(), name="reg"),
]
